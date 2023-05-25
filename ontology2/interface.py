import os
from uuid import uuid4
from owlready2 import *

from ontology2.ontology_scheme import construct
from config import ONTOLOGIES


JAVA_EXE="/usr/lib/jvm/java-17-openjdk/bin/java"


class Property:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class Ontology:
    def __init__(self, name='default', website='Not defined', ontology=None):
        self.name = name

        onto_path.append(f"{os.path.abspath(ONTOLOGIES)}")

        if ontology:
            self.raw_onto = ontology
        else:
            self.raw_onto = get_ontology(f"http://privacy-ontology.com/{name}.owl")
            construct(self.raw_onto)

        self.policy = self.individual('PrivacyPolicy', evidence=None, properties=[Property('policyWebsite', website)])

    @staticmethod
    def reason():
        sync_reasoner(infer_property_values=True)

    def save(self):
        self.raw_onto.save()

    @staticmethod
    def gen_name(u, c):
        return f'{u}:{c}'

    def individual(self, entity, evidence='Not defined', binds=None, properties=None):
        cls_ = getattr(self.raw_onto, entity)
        uuid = uuid4().hex[:23].lower()
        individual = cls_(self.gen_name(uuid, cls_.__name__))
        individual.uuid = uuid

        if properties:
            for p in properties:
                setattr(individual, p.key, p.value)

        return self.bind(self.evidence(individual, evidence), binds)

    @staticmethod
    def evidence(individual, text="Not defined"):
        individual.evidence = text
        return individual

    @staticmethod
    def property(key, value):
        return Property(key, value)
    
    def bind(self, individual, binds=None):
        self.autolink(individual)

        if binds:
            for p in binds:
                try:
                    getattr(individual, p.key).append(p.value)
                except AttributeError:
                    setattr(individual, p.key, p.value) 

        return individual
    
    def autolink(self, individual):
        data_ = getattr(self.raw_onto, 'Data')
        activity_ = getattr(self.raw_onto, 'Activity')
        agent_ = getattr(self.raw_onto, 'Agent')

        if isinstance(individual, data_):
            self.bind(self.policy, binds=[Property('considers_data', individual)])

        if isinstance(individual, activity_):
            self.bind(self.policy, binds=[Property('considers_activity', individual)])

        if isinstance(individual, agent_):
            self.bind(self.policy, binds=[Property('considers_agent', individual)])

        return individual
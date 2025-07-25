from uuid import uuid4
from owlready2 import *

from env import env
from ontology.ontology_scheme import construct


JAVA_EXE = env()['java']
ONTO_IRI = env()['iri']


class Property:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class Ontology:
    def __init__(self, path='./', name='default', 
                 website='Not defined', ontology=None, create_root_policy=True):
        self.name = name

        onto_path.append(path)

        if ontology:
            self.raw_onto = ontology
        else:
            self.raw_onto = get_ontology(f"http://{ONTO_IRI}/{name}.owl")
            construct(self.raw_onto)

        if create_root_policy:
            self.policy = self.individual(
                'PrivacyPolicy', 
                evidence=None, 
                properties=[Property('policyWebsite', website)])

    def new_policy(self, website):
        self.policy = self.individual(
            'PrivacyPolicy', 
            evidence=None, 
            properties=[Property('policyWebsite', website)])

    @staticmethod
    def reason():
        sync_reasoner(infer_property_values=True)

    def save(self):
        self.raw_onto.save()

    @staticmethod
    def gen_name(u, c):
        return f'{c}.{u}'

    def individual(self, entity, evidence='Not defined', binds=None, properties=None):
        cls_ = getattr(self.raw_onto, entity)
        uuid = uuid4().hex[:23].lower()
        individual = cls_(self.gen_name(uuid, cls_.__name__))
        individual.uuid = uuid

        activity_ = getattr(self.raw_onto, 'Activity')
        if isinstance(individual, activity_):
            individual.does = True

        if properties:
            for p in properties:
                if p:
                    setattr(individual, p.key, p.value)

        return self.bind(self.evidence(individual, evidence), binds)

    @staticmethod
    def evidence(individual, text="Not defined"):
        individual.evidence = text
        return individual

    @staticmethod
    def property(key, value):
        return Property(key, value)
    
    @staticmethod
    def destroy(entity):
        if entity:
            destroy_entity(entity)

    def bind(self, individual, binds=None):
        self.autolink(individual)

        if binds:
            for p in binds:
                if p.value:
                    try:
                        setattr(individual, p.key, p.value)
                    except ValueError:
                        getattr(individual, p.key).append(p.value)

        return individual
    
    def autolink(self, individual):
        data_ = getattr(self.raw_onto, 'Data')
        activity_ = getattr(self.raw_onto, 'Activity')
        agent_ = getattr(self.raw_onto, 'Agent')

        if isinstance(individual, data_):
            self.bind(self.policy, binds=[Property('considers', individual)])

        if isinstance(individual, activity_):
            self.bind(self.policy, binds=[Property('considers', individual)])

        if isinstance(individual, agent_):
            self.bind(self.policy, binds=[Property('considers', individual)])

        return individual
    
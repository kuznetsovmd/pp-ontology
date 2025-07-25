from ontology.interface import Ontology


def build(**kwargs):
    Ontology(**kwargs).save()

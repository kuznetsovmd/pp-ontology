from ontology2.ontology.interface import Ontology


def process_onto_blank():
    # Blank ontology
    Ontology("blank").save()

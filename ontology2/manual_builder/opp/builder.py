from ontology2.ontology.interface import Ontology

from ontology2.manual_builder.opp.reader import read
from ontology2.manual_builder.opp.reasoner import reason
from ontology2.manual_builder.opp.processor import process


def process_opp():

    policies = read()

    onto = Ontology("summary", create_root_policy=False)
    for p in policies:
        process(onto, p)
    onto.save()
    
    for i, p in enumerate(policies, start=1):
        onto = Ontology(i)
        process(onto, p)
        onto.save()

    reason(policies)

from pprint import pprint

import owlready2
from ontology import construct_ontology, finish
from opp.processor import process_opp
from opp.reader import read_opp
from standalone_policies.amazon_web_services import process_aws
from standalone_policies.google_cloud import process_google_cloud
from standalone_policies.threeplususa import process_3plususa
from standalone_policies.caresense import process_caresense
from standalone_policies.dario import process_dario
from standalone_policies.zepp import process_zepp
from standalone_policies.renpho import process_renpho


def main():
    """
    Constructing ontology
        onto = construct_ontology()

    Making individuals
        i1 = onto.PrivacyPolicy()
        i2 = onto.Data()
        i3 = onto.DataProtectionOfficer()

    DataProperty assertion
        i4 = onto.Evidence()
        i4.evidenceContent = "text"

    ObjectProperty assertion
        i2.hasEvidence = [i4]
        i1.considersData.append(i2)

    Finishing work
        finish(onto)

    SPARQL example
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX onto: <file:///home/user/Source/repos/ontology/resources/iot-ontology-summary.owl#>
        SELECT ?subject ?object ?content
        WHERE { ?subject onto:hasEvidence ?object .
                ?object onto:evidenceContent ?content }
    """

    owlready2.JAVA_EXE="/usr/lib/jvm/java-17-openjdk/bin/java"

    # # Ontology containing whole dataset

    # onto = construct_ontology("blank")
    # finish(onto)

    # onto = construct_ontology("summary")
    # policies = read_opp()
    
    # for p in policies:
    #     process_opp(onto, p)
    # finish(onto, reason=False)
    
    # # Ontologies containing policies by 1
    # for p in policies:
    #     o = construct_ontology()
    #     process_opp(o, p)
    #     finish(o, reason=False)

    # o = construct_ontology("3plususa")
    # process_3plususa(o)
    # finish(o, reason=False)

    # o = construct_ontology("aws")
    # process_aws(o)
    # finish(o, reason=False)

    # o = construct_ontology("google-cloud")
    # process_google_cloud(o)
    # finish(o, reason=False)

    o = construct_ontology("caresense")
    process_caresense(o)
    finish(o)

    o = construct_ontology("dario")
    process_dario(o)
    finish(o)

    o = construct_ontology("zepp")
    process_zepp(o)
    finish(o)

    o = construct_ontology("renpho")
    process_renpho(o)
    finish(o)


if __name__ == '__main__':
    main()

#!/usr/bin/env python

# from ontology2.interface import Ontology as Ontology2
# from ontology.ontology import Ontology
# from experiments.opp.processor import process_opp
# from experiments.opp.reader import read_opp
# from experiments.cloud_computing_policies.amazon_web_services import process_aws
# from experiments.cloud_computing_policies.google_cloud import process_google_cloud
# from experiments.cloud_computing_policies.threeplususa import process_3plususa
from experiments.healthcare_policies2.caresense import process_caresense
from experiments.healthcare_policies2.renpho import process_renpho
from experiments.healthcare_policies2.zepp import process_zepp
# from experiments.onto2_examples import process_onto2_test


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

    OR throught new Ontology class
        o = Ontology("blank")
        o.individual(
            'Activity',
            'some evidence',
            [
                o.connection(
                    'appliesToData',
                    o.individual(
                        'Data', 
                        'some evidence'
                        [o.individual('User', 'some evidence')])
                )
            ]
        )

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


    # Ontology containing whole dataset
    # Ontology2("blank_v2").save()

    # onto = Ontology("summary")
    # policies = read_opp()
    
    # for p in policies:
    #     process_opp(onto.raw_onto, p)
    # onto.write(reason=False)
    
    # # Ontologies containing policies by 1
    # for i, p in enumerate(policies, start=1):
    #     onto = Ontology(i)
    #     process_opp(onto.raw_onto, p)
    #     onto.write(reason=False)

    # onto = Ontology("3plususa")
    # process_3plususa(onto.raw_onto)
    # onto.write(reason=False)

    # onto = Ontology("aws")
    # process_aws(onto.raw_onto)
    # onto.write(reason=False)

    # onto = Ontology("google-cloud")
    # process_google_cloud(onto.raw_onto)
    # onto.write(reason=False)

    process_caresense()
    process_renpho()
    process_zepp()

    # process_onto2_test()


if __name__ == '__main__':
    main()

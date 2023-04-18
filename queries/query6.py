import csv
from pprint import pprint

from owlready2 import *

from config import ONTOLOGIES, QUERIES


def main():
    """
    What are the causes for policy change in the OPP data set?
    """
    onto_path.append(ONTOLOGIES)
    onto = get_ontology(
        f"http://test.org/iot-ontology-summary.owl").load()

    with onto:
        res = list(default_world.sparql("""
            
            PREFIX onto: <http://test.org/iot-ontology-summary.owl#>
            
            SELECT DISTINCT ?class ?cause ?id ?website 
            # SELECT ?class (COUNT(?class) as ?c)
            # SELECT( COUNT( DISTINCT ?id ) AS ?c ) 
            WHERE {
                {
                    ?activity  a                      onto:PolicyChangeActivity.
                    ?activity  onto:hasPolicyChangeCause ?cause                .
                    ?class     rdfs:subClassOf           onto:PolicyChangeCause.
                    ?cause     a                         ?class                .
                    ?policy    onto:considersActivity    ?activity             .
                    ?policy    onto:policyId             ?id                   .
                    ?policy    onto:policyWebsite        ?website              .
                } UNION {
                    ?activity  a                      onto:PolicyChangeActivity.
                    ?activity  onto:hasPolicyChangeCause ?cause                .
                    ?class     rdfs:subClassOf           onto:Cause            .
                    ?cause     a                         ?class                .
                    ?policy    onto:considersActivity    ?activity             .
                    ?policy    onto:policyId             ?id                   .
                    ?policy    onto:policyWebsite        ?website              .
                }
            } # GROUP BY ?class
            
        """))

        pprint(res)

        with open(f"{QUERIES}/query6.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(res)


if __name__ == '__main__':
    main()

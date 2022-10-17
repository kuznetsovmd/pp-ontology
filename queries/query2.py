import csv
from pprint import pprint

from owlready2 import *

from config import ontologies, queries


def main():
    """
    * What notification mechanisms are used to notify?
    """
    onto_path.append(ontologies)
    onto = get_ontology(
        f"http://test.org/iot-ontology-summary.owl").load()

    with onto:
        res = list(default_world.sparql("""
            
            PREFIX onto: <http://test.org/iot-ontology-summary.owl#>
            
            SELECT DISTINCT ?class ?mechanism ?id ?website 
            # SELECT ?class (COUNT(?class) as ?c)
            WHERE {
                {
                    ?activity  a                      onto:PolicyChangeActivity .
                    ?activity  onto:hasMechanism      ?mechanism                .
                    ?class     rdfs:subClassOf        onto:NotificationMechanism.
                    ?mechanism a                      ?class                    .
                    ?policy    onto:considersActivity ?activity                 .
                    ?policy    onto:policyId          ?id                       .
                    ?policy    onto:policyWebsite     ?website                  .
                } UNION {
                    ?activity  a                      onto:PolicyChangeActivity .
                    ?activity  onto:hasMechanism      ?mechanism                .
                    ?class     rdfs:subClassOf        onto:Mechanism            .
                    ?mechanism a                      ?class                    .
                    ?policy    onto:considersActivity ?activity                 .
                    ?policy    onto:policyId          ?id                       .
                    ?policy    onto:policyWebsite     ?website                  .
                }
            } # GROUP BY ?class
            
        """))

        pprint(res)

        with open(f"{queries}/query2.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(res)


if __name__ == '__main__':
    main()

import csv
from pprint import pprint

from owlready2 import *

from config import ONTOLOGIES, QUERIES


def main():
    """
    * How many privacy policies use general notice as notification mechanism in case of their change?
    """
    onto_path.append(ONTOLOGIES)
    onto = get_ontology(
        f"http://test.org/iot-ontology-summary.owl").load()

    with onto:
        res = list(default_world.sparql("""
            
            PREFIX onto: <http://test.org/iot-ontology-summary.owl#>
            
            SELECT( COUNT( DISTINCT( ?id ) ) as ?amount )
            WHERE {
                ?mechanism a                      onto:OnWebsitePage         .
                ?activity  onto:hasMechanism      ?mechanism                 .
                ?policy    onto:considersActivity ?activity                  .
                ?policy    onto:policyId          ?id                        .
            }
            
        """))

        pprint(res)

        with open(f"{QUERIES}/query3.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(res)


if __name__ == '__main__':
    main()

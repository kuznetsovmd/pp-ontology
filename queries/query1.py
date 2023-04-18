import csv
from pprint import pprint

from owlready2 import *

from config import ONTOLOGIES, QUERIES


def main():
    """
    * How many privacy policies include information about notification mechanisms used to inform end users about policy change?
    """
    onto_path.append(ONTOLOGIES)
    onto = get_ontology(
        f"http://test.org/iot-ontology-summary.owl").load()

    with onto:
        res = list(default_world.sparql("""
            
            PREFIX onto: <http://test.org/iot-ontology-summary.owl#>
            
            SELECT( COUNT( DISTINCT( ?id ) ) AS ?c )
            WHERE {
                ?activity  a                      onto:PolicyChangeActivity .
                ?activity  onto:hasMechanism      ?mechanism                .
                ?policy    onto:considersActivity ?activity                 .
                ?policy    onto:policyId          ?id                       .
            }
            
        """))

        pprint(res)

        with open(f"{QUERIES}/query1.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(res)


if __name__ == '__main__':
    main()

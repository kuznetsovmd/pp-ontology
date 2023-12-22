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
        f"http://test.org/first-annotation.owl").load()

    with onto:
        res = list(default_world.sparql("""
            
            PREFIX onto: <http://test.org/first-annotation.owl#>
            
            SELECT ( ?c AS ?class ) ( COUNT( DISTINCT( ?i ) ) AS ?count )
            WHERE {
                ?i  a  ?c
            }
            GROUP BY ?c
        """))

        pprint(res)

        with open(f"{QUERIES}/query1.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(res)


if __name__ == '__main__':
    main()

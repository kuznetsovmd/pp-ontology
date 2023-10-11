import csv
from pprint import pprint

from owlready2 import *

from config import ONTOLOGIES, QUERIES


def main():
    """
    * What are the possible causes for policy change in particular privacy policy?
    """
    onto_path.append(ONTOLOGIES)
    onto = get_ontology(
        f"http://test.org/iot-ontology-summary.owl").load()

    with onto:
        res = list(default_world.sparql("""
            
            PREFIX onto: <http://test.org/iot-ontology-summary.owl#>
            
            SELECT DISTINCT ?class
            WHERE {
                ?policy   a                         onto:PrivacyPolicy        .
                ?policy   onto:policyId             635                       .
                ?policy   onto:considersActivity    ?activity                 .
                ?activity a                         onto:PolicyChangeActivity .
                ?activity onto:hasPolicyChangeCause ?cause                    .
                ?cause    a                         ?class                    .
                ?class    rdfs:subClassOf           onto:PolicyChangeCause    .
            }
            
        """))

        pprint(res)

        with open(f"{QUERIES}/query7.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(res)


if __name__ == '__main__':
    main()

import csv
from pprint import pprint

from owlready2 import *

from config import ONTOLOGIES, QUERIES


def main():
    """
    * What are the evidences which contain the personal notifications about privacy policy change?
    """
    onto_path.append(ONTOLOGIES)
    onto = get_ontology(
        f"http://test.org/iot-ontology-summary.owl").load()

    with onto:
        res = list(default_world.sparql("""
            
            PREFIX onto: <http://test.org/iot-ontology-summary.owl#>
            
            SELECT DISTINCT ?id ?website ?content
            WHERE {
                ?class     rdfs:subClassOf        onto:NotificationMechanism .
                ?activity  onto:hasMechanism      ?mechanism                 .
                ?activity  a                      onto:PolicyChangeActivity  .
                ?policy    onto:considersActivity ?activity                  .
                ?policy    onto:policyId          ?id                        .
                ?policy    onto:policyWebsite     ?website                   .
                ?mechanism onto:hasEvidence       ?evidence                  .
                ?evidence  onto:evidenceContent   ?content                   .
            }
            
        """))

        pprint(res)

        with open(f"{QUERIES}/query4.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows(res)


if __name__ == '__main__':
    main()

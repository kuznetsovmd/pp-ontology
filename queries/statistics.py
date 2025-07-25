from owlready2 import *


def run(ontologies):
    """
    * How many privacy policies include information about notification mechanisms used to inform end users about policy change?
    """
    onto_path.extend(ontologies)
    onto = get_ontology(f"http://privacy-ontology.org/annotations-summary.owl").load()

    with onto:
        res = list(default_world.sparql("""
            
            PREFIX onto: <http://privacy-ontology.org/annotations-summary.owl#>
            
            SELECT ( ?c AS ?class ) ( COUNT( DISTINCT( ?i ) ) AS ?count )
            WHERE {
                ?i  a  ?c
            } GROUP BY ?c
                                        
        """))

    return __name__, res

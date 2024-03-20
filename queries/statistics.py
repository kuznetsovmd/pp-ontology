from owlready2 import *

from config import ONTOLOGIES


def run():
    """
    * How many privacy policies include information about notification mechanisms used to inform end users about policy change?
    """
    onto_path.append(ONTOLOGIES)
    onto = get_ontology(f"http://test.org/annotations.owl").load()

    with onto:
        res = list(default_world.sparql("""
            
            PREFIX onto: <http://test.org/annotations.owl#>
            
            SELECT ( ?c AS ?class ) ( COUNT( DISTINCT( ?i ) ) AS ?count )
            WHERE {
                ?i  a  ?c
            } GROUP BY ?c
                                        
        """))

    return __name__, res

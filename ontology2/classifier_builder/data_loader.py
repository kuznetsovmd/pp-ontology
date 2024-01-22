from pprint import pprint

from owlready2 import *

from ontology2.queries.query1 import run


def load():
    res = run()
    pprint(res)

from pprint import pprint

from ontology2.queries.statistics import run


def load():
    res = run()
    pprint(res)

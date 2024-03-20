from tqdm import tqdm

from ontology.interface import Ontology

from .reader import read
from .reasoner import reason
from .processor import process


def build(path, name, dataset, structure, tqdm_conf, **kwargs):
    policies = read(dataset)

    onto = Ontology(path=path, name=f'{name}-summary', create_root_policy=False)
    for p in tqdm(policies, desc='OPP summary', **tqdm_conf):
        process(onto, p)
    onto.save()
    
    for i, p in enumerate(tqdm(policies, desc='OPP each', **tqdm_conf), start=1):
        onto = Ontology(path=path, name=f'{name}-{i}')
        process(onto, p)
        onto.save()
    
    reason(policies, structure)

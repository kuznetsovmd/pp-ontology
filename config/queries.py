import os
from queries.statistics import run as run_statistics

def config(resources, tqdm_conf, **kwargs):

    path = f'{resources}/queries'
    os.makedirs(path, exist_ok=True)

    return {
        'tqdm_conf': tqdm_conf,
        'ontologies': [
            f'{resources}/ontologies/manual',
            f'{resources}/ontologies/opp',
            f'{resources}/ontologies/annotations',
        ],
        'path': path,
        'queries': [
            run_statistics,
        ],
    }

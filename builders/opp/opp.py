import os


def config(resources, opp, tqdm_conf, **kwargs):

    ontologies = f'{resources}/ontologies/opp'
    os.makedirs(ontologies, exist_ok=True)

    return {
        'tqdm_conf': tqdm_conf,
        'dataset': opp,
        'structure': f'{resources}/opp_structure.json',
        'path': ontologies,
        'name': 'opp',
    }

import os


def config_annotated(resources, annotations, tqdm_conf, **kwargs):

    ontologies = f'{resources}/ontologies/annotated'
    os.makedirs(ontologies, exist_ok=True)

    return {
        'tqdm_conf': tqdm_conf,
        'annotations': annotations,
        'path': ontologies,
        'name': 'annotations',
    }


def config_classified(resources, annotations, tqdm_conf, **kwargs):

    ontologies = f'{resources}/ontologies/classified'
    os.makedirs(ontologies, exist_ok=True)

    return {
        'tqdm_conf': tqdm_conf,
        'annotations': f'{resources}/classified',
        'path': ontologies,
        'name': 'classified',
    }

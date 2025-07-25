import os


def env():

    resources = 'resources'
    os.makedirs(resources, exist_ok=True)

    return {
        'use_cuda': True,
        'iri': 'privacy-ontology.org',
        'resources': resources,
        'annotations': '/mnt/Source/kuznetsovmd/__datasets/annotations',
        'opp': '/mnt/Source/kuznetsovmd/__datasets/opp',
        'russian_pp': '/mnt/Source/kuznetsovmd/__datasets/ru',
        'java': '/usr/lib/jvm/java-17-openjdk/bin/java',
        'tqdm_conf': {
            'ncols': 80,
            'ascii': False,
        },
    }

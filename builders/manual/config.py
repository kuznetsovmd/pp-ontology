import os

from builders.manual.cloud_computing.amazon_web_services import build as process_aws
from builders.manual.cloud_computing.google_cloud import build as process_google_cloud
from builders.manual.cloud_computing.threeplususa import build as process_3plususa
from builders.manual.cloud_computing.hpe import build as process_hpe
from builders.manual.cloud_computing.yandex import build as process_yandex
from builders.manual.healthcare.caresense import build as process_caresense
from builders.manual.healthcare.renpho import build as process_renpho
from builders.manual.healthcare.zepp import build as process_zepp
from builders.manual.example import build as process_onto_examples
from builders.manual.blank import build as process_onto_blank


def config(resources, tqdm_conf, **kwargs):

    ontologies = f'{resources}/ontologies/manual'
    os.makedirs(ontologies, exist_ok=True)

    return {
        'tqdm_conf': tqdm_conf,
        'builders': [
            {'func': process_onto_blank, 'args': dict(path=ontologies, name='blank')},
            {'func': process_onto_examples, 'args': dict(path=ontologies, name='examples')},
            {'func': process_3plususa, 'args': dict(path=ontologies, name='3plususa')},
            {'func': process_aws, 'args': dict(path=ontologies, name='aws')},
            {'func': process_google_cloud, 'args': dict(path=ontologies, name='google-cloud')},
            {'func': process_hpe, 'args': dict(path=ontologies, name='hpe')},
            {'func': process_yandex, 'args': dict(path=ontologies, name='yandex')},
            {'func': process_caresense, 'args': dict(path=ontologies, name='caresense')},
            {'func': process_renpho, 'args': dict(path=ontologies, name='renpho')},
            {'func': process_zepp, 'args': dict(path=ontologies, name='zepp')},
        ]
    }

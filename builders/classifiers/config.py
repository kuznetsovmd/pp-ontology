import os

import torch
from torch import device as get_device
from torch.cuda import current_device, is_available

from transformers import AutoTokenizer

from builders.classifiers.model import Linear2BERT, Linear3BERT, LinearBERT


def select_device(use_cuda):
    d = current_device() if is_available() and use_cuda else get_device('cpu')
    print(f'Torch version: {torch.__version__}')
    try:
        print(f'Using: {torch.cuda.get_device_name(d)}')
    except ValueError:
        print(f'Using: CPU')
    return d


def config(resources, annotations, russian_pp, use_cuda, tqdm_conf, **kwargs):

    device = select_device(use_cuda)

    fpcollection = f'{resources}/models/fp_collection'
    os.makedirs(fpcollection, exist_ok=True)

    bert_model = 'DeepPavlov/rubert-base-cased'
    bert_tokenizer = AutoTokenizer.from_pretrained(bert_model)

    return [
        {
            'ontology_class': 'FPCollection',
            'annotations_path': annotations,
            'descriptor_path': f'{russian_pp}/json/plain.json',
            'policies_path': f'{russian_pp}/output_policies',
            'output_path': f'{resources}/classified',
            'sequence_len': 512,
            'split': .5,
            'n_epochs': 200,
            'padding': 10,
            'density': 0.01,
            'bert_tokenizer': bert_tokenizer,
            'tqdm_conf': tqdm_conf,
            'model_conf': {
                'name': 'bert-FPCollection',
                'version': 0,
                'path': fpcollection,
                'pretrained': False,
                'device': device,
                'module': Linear2BERT,
                'module_parameters': {
                    'bert_model': bert_model,
                    'bert_size': 768,
                    'hidden_size': 1024,
                    'dropout': .01, 
                    'device': device,
                },
                'optimizer': torch.optim.AdamW,
                'optimizer_parameters': {
                    'lr':  5e-5,
                    'eps': 1e-8,
                    'betas': (0.9, 0.999),
                },
                'criterion': torch.nn.BCELoss,
                'criterion_parameters': {},
            },
        },
    ]

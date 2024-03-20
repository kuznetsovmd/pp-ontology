import os

import torch
from torch import device
from torch.cuda import current_device, is_available

from transformers import AutoModel
from transformers import AutoTokenizer

from builders.classifiers.model import Linear3BERT


def print_info(device):
    print(f'Torch version: {torch.__version__}')
    try:
        print(f'Using: {torch.cuda.get_device_name(device)}')
    except ValueError:
        print(f'Using: CPU')


def config(resources, annotations, russian_pp, use_cuda, tqdm_conf, **kwargs):

    dev = current_device() if is_available() and use_cuda else device('cpu')
    print_info(dev)

    fpcollection = f'{resources}/models/fp_collection'
    os.makedirs(fpcollection, exist_ok=True)

    output_path = f'{resources}/classified'
    os.makedirs(output_path, exist_ok=True)

    bert_model = AutoModel.from_pretrained('ai-forever/ruBert-large')
    bert_tokenizer = AutoTokenizer.from_pretrained('ai-forever/ruBert-large')

    return [
        {
            'ontology_class': 'FPCollection',
            'annotations_path': annotations,
            'descriptor_path': f'{russian_pp}/output.json',
            'policies_path': f'{russian_pp}/output_policies',
            'output_path': output_path,
            'sequence_len': 512,
            'split': .8,
            'n_epochs': 500,
            'padding': 10,
            'density': .3,
            'bert_tokenizer': bert_tokenizer,
            'tqdm_conf': tqdm_conf,
            'model_conf': {
                'name': 'bert-FPCollection',
                'version': 16,
                'path': fpcollection,
                'pretrained': True,
                'device': dev,
                'bert_model': bert_model,
                'module': Linear3BERT,
                'module_parameters': {
                    'input_size': 1024,
                    'hidden_size': 1024,
                    'dropout': .01, 
                    'device': dev,
                },
                'optimizer': torch.optim.AdamW,
                'optimizer_parameters': {
                    'lr':  1e-4,
                    'eps': 1e-9,
                    'betas': (0.9, 0.98),
                },
                'criterion': torch.nn.CrossEntropyLoss,
                'criterion_parameters': {
                    'label_smoothing': .05,
                },
            },
        },
    ]

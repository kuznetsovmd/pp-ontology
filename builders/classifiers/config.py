import os

import torch
from torch import device as get_device
from torch.cuda import current_device, is_available

from transformers import AutoModel
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

    bert_model = AutoModel.from_pretrained('ai-forever/ruBert-large')
    bert_tokenizer = AutoTokenizer.from_pretrained('ai-forever/ruBert-large')
    # special_tokens_dict = {'additional_special_tokens': ['\n',' ']}
    # bert_tokenizer.add_special_tokens(special_tokens_dict)
    # bert_model.resize_token_embeddings(len(bert_tokenizer))

    return [
        {
            'ontology_class': 'FPCollection',
            'annotations_path': annotations,
            'descriptor_path': f'{russian_pp}/json/plain.json',
            'policies_path': f'{russian_pp}/plain_policies',
            'output_path': f'{resources}/classified',
            'sequence_len': 512,
            'split': .8,
            'n_epochs': 200,
            'padding': 10,
            'density': .2,
            'bert_tokenizer': bert_tokenizer,
            'tqdm_conf': tqdm_conf,
            'model_conf': {
                'name': 'bert-FPCollection',
                'version': 50,
                'path': fpcollection,
                'pretrained': True,
                'device': device,
                'bert_model': bert_model,
                'module': Linear2BERT,
                'module_parameters': {
                    'input_size': 1024,
                    'hidden_size': 2048,
                    'dropout': .05, 
                    'device': device,
                },
                'optimizer': torch.optim.AdamW,
                'optimizer_parameters': {
                    'lr':  1e-4,
                    'eps': 1e-9,
                    'betas': (0.9, 0.95),
                },
                'criterion': torch.nn.CrossEntropyLoss,
                'criterion_parameters': {
                    'label_smoothing': .05,
                },
            },
        },
    ]

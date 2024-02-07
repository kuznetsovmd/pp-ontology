import math
import time
import torch
import torch.nn as nn
from tqdm import tqdm

from config import *
from ontology2.classifier_builder.model import build_model, save_model

from ontology2.classifier_builder.transformer import Transformer
from ontology2.classifier_builder.device import *
from ontology2.classifier_builder.data import LabeledDataset, PredictionDataset, TrainDataset, get_defaults


def print_info():
    print(f'Torch version: {torch.__version__}')
    try:
        print(f'Using: {torch.cuda.get_device_name(DEVICE)}')
    except ValueError:
        print(f'Using: CPU')


def print_stats(epoch, n_epochs, start, stats):
        print(f'R: epoch={epoch} [{epoch * 100 // n_epochs}%] time=[{time_since(start)}] '
                f'T loss={stats["t_loss"]:.3f}, '
                f'T accuracy={stats["t_accuracy"]:.3f}\n')


def time_since(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)


def build_classified(train, labeled, eval):
    '''
    TODO:
    1. Check more about nopeak mask
    2. Rework training, so model see full sequence on generation
    3. Use cached hidden state
    '''

    print_info()

    defaults = get_defaults()
    dataset1 = TrainDataset(**defaults).load().split()
    dataset2 = LabeledDataset(**defaults).load().split()

    defaults['train'] = True
    dataset3 = PredictionDataset(**defaults)
    dataset3.load()

    parameters = {
        'module': Transformer,
        'module_parameters': {
            'src_vocab_size': dataset2.vocab.size, 
            'tgt_vocab_size': dataset2.vocab.size, 
            'max_seq_length': dataset2.sequence_len, 
            'd_model': 1024, 
            'num_heads': 8, 
            'num_layers': 6,
            'dropout': .1, 
            'd_ff': 2048, 
            'nopeak': True,
            'device': DEVICE,
        },
        'optimizer': torch.optim.Adam,
        'optimizer_parameters': {
            'lr':  1e-5,
            'eps': 1e-9,
            'betas': (0.9, 0.95),
        },
        'criterion': nn.CrossEntropyLoss,
        'criterion_parameters': {
            'weight': torch.tensor([
                *[0.0 for _ in range(dataset2.vocab.n_spec_tokens)],
                *[1.0 for _ in range(dataset2.vocab.n_spec_tokens, dataset2.vocab.size)]
            ], device=DEVICE)
        },
        'sep': dataset2.vocab.w2i('[sep]'),
        'ignore_index': tuple(range(dataset2.vocab.n_spec_tokens)),
        'name': 'transformer',
        'version': '.1',
    }

    if train: 
        transformer = build_model(**parameters)
        transformer = train_llm(transformer, dataset1, 1000)
        save_model(transformer, f'{RESOURCES}/models/transformer')
        transformer = build_model(f'{RESOURCES}/models/transformer', **parameters)
        annotate(transformer, dataset3)
    elif labeled: 
        transformer = build_model(f'{RESOURCES}/models/transformer', **parameters)
        transformer = train_annotate(transformer, dataset2, 1000)
        save_model(transformer, f'{RESOURCES}/models/transformer1')
        transformer = build_model(f'{RESOURCES}/models/transformer1', **parameters)
        annotate(transformer, dataset3)
    elif eval: 
        transformer = build_model(f'{RESOURCES}/models/transformer', **parameters)
        annotate(transformer, dataset3)


def train_llm(transformer, dataset, n_epochs):
    start = time.time()
    try:
        transformer.module.train()
        for epoch in range(n_epochs):
            dataset.shuffle()
            for s in tqdm(dataset.train, ncols=80):
                transformer.train(s, s)

            print_stats(epoch, n_epochs, start, transformer.stats())
    except KeyboardInterrupt:
        pass
    return transformer


def train_annotate(transformer, dataset, n_epochs):
    start = time.time()
    try:
        for epoch in range(n_epochs):
            # dataset.shuffle()
            transformer.module.train()
            for (s, t) in tqdm(dataset.train, ncols=80):
                transformer.train(s, t)

            transformer.module.eval()
            for (s, t) in tqdm(dataset.validation, ncols=80):
                transformer.test(s, t)

            print_stats(epoch, n_epochs, start, transformer.stats())
    except KeyboardInterrupt:
        pass
    return transformer


def annotate(transformer, dataset):
    for (s, t, txt) in dataset.get():
        print(txt, end='\n')

        transformer.module.eval()
        sentence = transformer.predict(s, t)
        print(' '.join(dataset.vocab.decode(sentence)), end='\n\n')

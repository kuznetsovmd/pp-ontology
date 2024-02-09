import math
import sys
import time
import torch
import torch.nn as nn
from tqdm import tqdm

from config import *
from ontology2.classifier_builder.model import build_model, save_model

from ontology2.classifier_builder.transformer import Transformer
from ontology2.classifier_builder.device import *
from ontology2.classifier_builder.data import Tokenizer, Vocabulary, \
    PredictionDataset, TrainDataset, dataset_defaults, tokenizer_defaults, vocabulary_defaults


def print_info():
    print(f'Torch version: {torch.__version__}')
    try:
        print(f'Using: {torch.cuda.get_device_name(DEVICE)}')
    except ValueError:
        print(f'Using: CPU')


def print_stats(epoch, n_epochs, start, stats):
        print(f'R: epoch={epoch} [{epoch * 100 // n_epochs}%] time=[{time_since(start)}] '
              f'T loss={stats["t_loss"]:.3f}, T accuracy={stats["t_accuracy"]:.3f} '
              f'V loss={stats["v_loss"]:.3f}, V accuracy={stats["v_accuracy"]:.3f}\n')


def time_since(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)


def unwrap_words(texts, tokenizer):
    return [t for text in texts for t in tokenizer[text]]


def build_classified(train, labeled, eval):

    print_info()

    tokenizer = Tokenizer(**tokenizer_defaults())

    with open(f'{RESOURCES}/example_texts_unlabeled.txt', 'r') as f:
        source_texts = f.read().split('\n')

    with open(f'{RESOURCES}/example_texts_labeled.txt', 'r') as f:
        target_texts = f.read().split('\n')

    vocab = Vocabulary(**vocabulary_defaults())
    vocab.new_ws(unwrap_words(source_texts, tokenizer))
    vocab.new_ws(unwrap_words(target_texts, tokenizer))
    print(f'{vocab.size=}')

    ds_defaults = dataset_defaults()
    ds_defaults['vocabulary'] = vocab
    ds_defaults['tokenizer'] = tokenizer

    t_ds1 = TrainDataset(**ds_defaults).prepare(source_texts[:40], source_texts[:40])
    v_ds1 = TrainDataset(**ds_defaults).prepare(source_texts[40:], source_texts[40:])
    t_ds2 = TrainDataset(**ds_defaults).prepare(target_texts[:15], target_texts[:15])
    v_ds2 = TrainDataset(**ds_defaults).prepare(target_texts[15:20], target_texts[15:20])

    ds_defaults['train'] = False
    p_ds1 = PredictionDataset(**ds_defaults).prepare(source_texts)

    parameters = {
        'module': Transformer,
        'module_parameters': {
            'src_vocab_size': vocab.size, 
            'tgt_vocab_size': vocab.size, 
            'max_seq_length': ds_defaults['sequence_len'], 
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
                *[0.0 for _ in range(vocab.n_spec_tokens)],
                *[1.0 for _ in range(vocab.size - vocab.n_spec_tokens)]
            ], device=DEVICE)
        },
        'sep': vocab.w2i('[sep]'),
        'ignore_index': tuple(range(vocab.n_spec_tokens)),
        'name': 'transformer',
        'version': '.1',
    }

    if train: 
        transformer = build_model(**parameters)
        transformer = train_llm(transformer, t_ds1, v_ds1, 1000)
        save_model(transformer, f'{RESOURCES}/models/transformer')
        transformer = build_model(f'{RESOURCES}/models/transformer', **parameters)
        annotate(transformer, p_ds1)
    elif labeled: 
        transformer = build_model(f'{RESOURCES}/models/transformer', **parameters)
        transformer = train_annotate(transformer, t_ds2, v_ds2, 1000)
        save_model(transformer, f'{RESOURCES}/models/transformer1')
        transformer = build_model(f'{RESOURCES}/models/transformer1', **parameters)
        annotate(transformer, p_ds1)
    elif eval: 
        transformer = build_model(f'{RESOURCES}/models/transformer', **parameters)
        annotate(transformer, p_ds1)


def train_llm(transformer, t_ds, v_ds, n_epochs):
    start = time.time()
    try:
        for epoch in range(n_epochs):
            transformer.module.train()
            for (s, t) in tqdm(t_ds, ncols=80):
                transformer.train(s, t)

            transformer.module.eval()
            for (s, t) in tqdm(v_ds, ncols=80):
                transformer.test(s, t)

            print_stats(epoch, n_epochs, start, transformer.stats())
    except KeyboardInterrupt:
        pass
    return transformer


def train_annotate(transformer, t_ds, v_ds, n_epochs):
    start = time.time()
    try:
        for epoch in range(n_epochs):
            transformer.module.train()
            for (s, t) in tqdm(t_ds, ncols=80):
                transformer.train(s, t)

            transformer.module.eval()
            for (s, t) in tqdm(v_ds, ncols=80):
                transformer.test(s, t)

            print_stats(epoch, n_epochs, start, transformer.stats())
    except KeyboardInterrupt:
        pass
    return transformer


def annotate(transformer, dataset):
    for (s, t, txt) in dataset:
        print(txt, end='\n')

        transformer.module.eval()
        sentence = transformer.predict(s, t)
        print(' '.join(dataset.vocab.decode(sentence)), end='\n\n')

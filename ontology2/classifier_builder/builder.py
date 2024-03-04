import json
import math
import re
import sys
import time
import torch
from tqdm import tqdm

from config import *
from ontology2.classifier_builder.model import build_model, model_defaults, save_model

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


def restore_annotations():

    with open(f'/mnt/Source/kuznetsovmd/__datasets/012190650e118175fe2f538504434c7c.json', 'r') as f:
        annotations = json.load(f)

    with open(f'/mnt/Source/kuznetsovmd/__datasets/ru/output.json', 'r') as f:
        policies = {a['policy_hash']: a for a in json.load(f)}

    annotations = [a for a in annotations if a['selection_class'] == 'PersonalData']
    hashes = set([a['policy_hash'] for a in annotations])
    files = [p['output_policy'] for i, p in policies.items() if i in hashes]

    texts1 = []
    for p in files:
        with open(f'/mnt/Source/kuznetsovmd/__datasets/ru/output_policies/{p}', 'r') as f:
            texts1.extend(f.read().split('\n\n\n'))

    texts2 = []
    for h in hashes:
        p = policies[h]

        with open(f'/mnt/Source/kuznetsovmd/__datasets/ru/output_policies/{p["output_policy"]}', 'r') as f:
            selection_pieces = [(a['starts_on'], a['ends_on']) for a in annotations if a['policy_hash'] == h]

            text = f.read()
            tail = 0
            annotated_text = ''
            for (s, e) in selection_pieces:
                annotated_text = f'{annotated_text}{text[int(tail):int(s)]}'
                annotated_text = f'{annotated_text}[!a]{text[int(s):int(e)]}[a]'
                tail = int(e)
            annotated_text = f'{annotated_text}{text[int(tail):]}'

            texts2.extend(annotated_text.split('\n\n\n'))

    return texts1, texts2


def build_classified(train, labeled, eval):

    texts1, texts2 = restore_annotations()
    print(texts2)

    print_info()

    vocab = Vocabulary(**vocabulary_defaults())

    tokenizer = Tokenizer(**tokenizer_defaults())
    vocab.new_ws(unwrap_words(texts1, tokenizer))
    vocab.new_ws(unwrap_words(texts2, tokenizer))

    print(f'{vocab.size=}')

    ds_defaults = dataset_defaults()
    ds_defaults['vocabulary'] = vocab
    ds_defaults['tokenizer'] = tokenizer

    t_ds1 = TrainDataset(**ds_defaults).prepare(texts1)
    v_ds1 = TrainDataset(**ds_defaults)
    t_ds2 = TrainDataset(**ds_defaults).prepare(texts2[:-20])
    v_ds2 = TrainDataset(**ds_defaults).prepare(texts2[-20:])

    t_defaults = tokenizer_defaults()
    t_defaults['train'] = True
    ds_defaults['tokenizer'] = Tokenizer(**t_defaults)
    p_ds1 = PredictionDataset(**ds_defaults).prepare(texts1)
    
    m_defaults = model_defaults()

    if train: 
        transformer = build_model(**m_defaults)
        transformer = train_llm(transformer, t_ds1, v_ds1, 1000)
        save_model(transformer, f'{RESOURCES}/models/transformer')
        transformer = build_model(f'{RESOURCES}/models/transformer', **m_defaults)
        annotate(transformer, p_ds1)

    elif labeled: 
        transformer = build_model(f'{RESOURCES}/models/transformer', **m_defaults)
        transformer = train_annotate(transformer, t_ds2, v_ds2, 1000)
        save_model(transformer, f'{RESOURCES}/models/transformer1')
        transformer = build_model(f'{RESOURCES}/models/transformer1', **m_defaults)
        annotate(transformer, p_ds1)

    elif eval: 
        transformer = build_model(f'{RESOURCES}/models/transformer1', **m_defaults)
        annotate(transformer, p_ds1)


def train_llm(transformer, t_ds, v_ds, n_epochs):
    start = time.time()
    try:
        for epoch in range(n_epochs):
            transformer.module.train()
            for (s, t) in tqdm(t_ds.shuffle(), ncols=80):
                transformer.train(s, t)

            transformer.module.eval()
            for (s, t) in tqdm(v_ds.shuffle(), ncols=80):
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
            for (s, t) in tqdm(t_ds.shuffle(), ncols=80):
                transformer.train(s, t)

            transformer.module.eval()
            for (s, t) in tqdm(v_ds.shuffle(), ncols=80):
                transformer.test(s, t)

            print_stats(epoch, n_epochs, start, transformer.stats())
    except KeyboardInterrupt:
        pass
    return transformer


def annotate(transformer, dataset):
    sentences = []
    with open(f'{RESOURCES}/predictions.txt', 'w') as f:
        for (s, t, txt) in dataset:

            print(f'ORIGINAL {"="*80}\n{txt}', end='\n', file=f)

            transformer.module.eval()
            output = transformer.predict(s, t)
            sentence = " ".join(dataset.vocab.decode(output))
            sentences.append(sentence)
            print(f'PREDICTED {"="*80}\n{sentence}', end='\n\n', file=f)
            print(re.findall(r'\[!a\].*\[a\]', sentence), end='\n\n', file=f)

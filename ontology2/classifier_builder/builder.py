import math
import sys
import time
import torch
import torch.nn as nn

from config import *
from ontology2.classifier_builder.model import build_model, save_model

from ontology2.classifier_builder.transformer import Transformer
from ontology2.classifier_builder.fetch_device import *
from ontology2.classifier_builder.text import Batcher, Tokenizer, Vocabulary, VocabularyData


def print_info():
    print(f'Torch version: {torch.__version__}')
    try:
        print(f'Using: {torch.cuda.get_device_name(DEVICE)}')
    except ValueError:
        print(f'Using: CPU')


def time_since(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)


def build_params(vocab, pretrained=True):
    return {
        'module': Transformer,
        'module_parameters': {
            'src_vocab_size': vocab.size, 
            'tgt_vocab_size': vocab.size, 
            'max_seq_length': MAX_SEQ_LEN, 
            'temperature': .5,
            'd_model': 512, 
            'num_heads': 8, 
            'num_layers': 6, 
            'dropout': .1, 
            'd_ff': 1024, 
            'device': DEVICE,
        },
        'optimizer': torch.optim.Adam,
        'optimizer_parameters': {
            'lr':  1e-5,
            'eps': 1e-9,
            'betas': (0.9, 0.98),
        },
        'criterion': nn.CrossEntropyLoss,
        'criterion_parameters': {
            'weight': torch.tensor([
                *[0.0 for _ in range(vocab.n_spec_tokens)],
                *[1.0 for _ in range(vocab.n_spec_tokens, vocab.size)]
            ], device=DEVICE)
        },
        'batcher': Batcher(
            MAX_SEQ_LEN, 
            BATCH_LEN,
            vocab.w2i('[pad]'), 
            vocab.w2i('[cls]'), 
            vocab.w2i('[sep]'), 
            vocab.w2i('[sot]')),
        'pretrained': pretrained,
        'path': f'{RESOURCES}/models/transformer',
    }


def unlabeled_train():

    vocab_data = VocabularyData(['[pad]', '[cls]', '[sep]', '[sot]'], ['[eot]', '[start]', '[end]'])
    vocab = Vocabulary(vocab_data)
    tokenizer = Tokenizer('[sot]', '[eot]')

    with open(f'{RESOURCES}/example_texts_unlabeled.txt', 'r') as f:
        texts = f.read().split('\n\n')

    vocab.new_ws(tokenizer.tokenize(texts[2]))

    transformer = build_model(**build_params(vocab, pretrained=False))

    n_epochs = 100
    start = time.time()
    try:
        for epoch in range(n_epochs):
            transformer.module.train()
            transformer.train(vocab.encode(tokenizer.tokenize(texts[2])), 
                              vocab.encode(tokenizer.tokenize(texts[2])))

            transformer.module.eval()
            transformer.test(vocab.encode(tokenizer.tokenize(texts[2])), 
                             vocab.encode(tokenizer.tokenize(texts[2])))
            transformer.epoch()
            save_model(transformer)

            print(f'R: epoch={epoch} [{epoch * 100 // n_epochs}%] time=[{time_since(start)}] '
                  f'T loss={transformer.train_losses[-1]:.3f} V loss={transformer.validation_losses[-1]:.3f}, '
                  f'T accuracy={transformer.train_accuracies[-1]:.3f} V accuracy={transformer.validation_accuracies[-1]:.3f}\n')
    except KeyboardInterrupt:
        pass


def labeled_train():

    vocab_data = VocabularyData(['[pad]'], ['[cls]', '[sep]', '[sot]', '[eot]', '[start]', '[end]'])
    vocab = Vocabulary(vocab_data)
    tokenizer = Tokenizer('[sot]', '[eot]')

    with open(f'{RESOURCES}/example_texts_unlabeled.txt', 'r') as f:
        texts = f.read().split('\n\n')

    with open(f'{RESOURCES}/example_texts_labeled.txt', 'r') as f:
        texts_labeled = f.read().split('\n\n')

    vocab.new_ws(tokenizer.tokenize(texts[2]))
    vocab.new_ws(tokenizer.tokenize(texts_labeled[2]))

    transformer = build_model(**build_params(vocab, pretrained=False))

    n_epochs = 100
    start = time.time()
    try:
        for epoch in range(n_epochs):
            transformer.module.train()
            transformer.train(vocab.encode(tokenizer.tokenize(texts[2])), 
                              vocab.encode(tokenizer.tokenize(texts_labeled[2])))

            transformer.module.eval()
            transformer.test(vocab.encode(tokenizer.tokenize(texts[2])), 
                             vocab.encode(tokenizer.tokenize(texts_labeled[2])))
            transformer.epoch()
            save_model(transformer)

            print(f'R: epoch={epoch} [{epoch * 100 // n_epochs}%] time=[{time_since(start)}] '
                  f'T loss={transformer.train_losses[-1]:.3f} V loss={transformer.validation_losses[-1]:.3f}, '
                  f'T accuracy={transformer.train_accuracies[-1]:.3f} V accuracy={transformer.validation_accuracies[-1]:.3f}\n')
    except KeyboardInterrupt:
        pass


def eval():
    vocab_data = VocabularyData(['[pad]', '[cls]', '[sep]', '[sot]'], ['[eot]', '[start]', '[end]'])
    vocab = Vocabulary(vocab_data)
    tokenizer = Tokenizer('[sot]', '[eot]', train=False)

    with open(f'{RESOURCES}/example_texts_unlabeled.txt', 'r') as f:
        texts = f.read().split('\n\n')

    with open(f'{RESOURCES}/example_texts_labeled.txt', 'r') as f:
        texts_labeled = f.read().split('\n\n')

    vocab.new_ws(tokenizer.tokenize(texts_labeled[2]))

    transformer = build_model(**build_params(vocab))

    transformer.module.eval()
    sentence = transformer.predict(vocab.encode(tokenizer.tokenize(texts[2])), vocab.w2i('[eot]'))
    print(' '.join(vocab.decode(sentence)))

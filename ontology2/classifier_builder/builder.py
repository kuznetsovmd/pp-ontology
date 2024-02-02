import math
import time
from numpy import source
import torch
import torch.nn as nn

from config import *
from ontology2.classifier_builder.model import build_model, save_model

from ontology2.classifier_builder.transformer import Transformer
from ontology2.classifier_builder.device import *
from ontology2.classifier_builder.data import Batcher, Tokenizer, Vocabulary


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


def unwrap_words(texts, tokenizer):
    return [t for text in texts for t in tokenizer.tokenize(text)]


def build_classified(train, labeled, eval):

    MAX_SEQ_LEN = 10
    BATCH_LEN = 8

    print_info()

    vocab = Vocabulary(['[pad]', '[sot]', '[cls]'], ['[sep]', '[eot]', '[start]', '[end]', '[unk]'])
    tokenizer = Tokenizer('[sot]', '[eot]', '[cls]', '[sep]', '[pad]', MAX_SEQ_LEN)
    batcher = Batcher(MAX_SEQ_LEN, BATCH_LEN, vocab.w2i('[pad]'), vocab.w2i('[cls]'), vocab.w2i('[sep]'), vocab.w2i('[sot]'))

    with open(f'{RESOURCES}/example_texts_unlabeled.txt', 'r') as f:
        texts = f.read().split('\n\n')

    with open(f'{RESOURCES}/example_texts_labeled.txt', 'r') as f:
        texts_labeled = f.read().split('\n\n')

    vocab.new_ws(unwrap_words(texts, tokenizer))
    vocab.new_ws(unwrap_words(texts_labeled, tokenizer))

    parameters = {
        'module': Transformer,
        'module_parameters': {
            'src_vocab_size': vocab.size, 
            'tgt_vocab_size': vocab.size, 
            'max_seq_length': MAX_SEQ_LEN, 
            'd_model': 1024, 
            'num_heads': 8, 
            'num_layers': 6,
            'dropout': .1, 
            'd_ff': 2048, 
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
                *[1.0 for _ in range(vocab.n_spec_tokens, vocab.size)]
            ], device=DEVICE)
        },
        'name': 'transformer',
        'version': '.1',
    }

    if train: 
        transformer = build_model(**parameters)
        # transformer = build_model(f'{RESOURCES}/models/transformer', **parameters)
        transformer = unlabeled_train(transformer, vocab, tokenizer, batcher, texts, 1000)
        save_model(transformer, f'{RESOURCES}/models/transformer')
    if labeled: 
        transformer = build_model(f'{RESOURCES}/models/transformer', **parameters)
        transformer = labeled_train(transformer, vocab, tokenizer, batcher, texts, texts_labeled, 1000)
        save_model(transformer, f'{RESOURCES}/models/transformer1')
    if eval: 
        tokenizer = Tokenizer('[sot]', '[eot]', '[cls]', '[sep]', '[pad]', MAX_SEQ_LEN, train=True)
        transformer = build_model(f'{RESOURCES}/models/transformer', **parameters)
        annotate(transformer, vocab, tokenizer, batcher, texts)


def unlabeled_train(transformer, vocab, tokenizer, batcher, texts, n_epochs):

    encoded = [vocab.encode(tokenizer.tokenize(t)) for t in texts[0:2]]
    encoded_val = [vocab.encode(tokenizer.tokenize(t)) for t in [texts[2]]]

    source = batcher.unlabeled(encoded)
    source_val = batcher.unlabeled(encoded_val)
    print(source)

    start = time.time()
    try:
        for epoch in range(n_epochs):
            transformer.module.train()
            transformer.train_unsupervised(source)

            transformer.module.eval()
            transformer.test(source_val, source_val)

            print(f'R: epoch={epoch} [{epoch * 100 // n_epochs}%] time=[{time_since(start)}] '
                  f'T loss={transformer.train_losses[-1]:.3f} V loss={transformer.validation_losses[-1]:.3f}, '
                  f'T accuracy={transformer.train_accuracies[-1]:.3f} V accuracy={transformer.validation_accuracies[-1]:.3f}\n')
    except KeyboardInterrupt:
        pass
    return transformer


def labeled_train(transformer, vocab, tokenizer, batcher, texts, texts_labeled, n_epochs):

    encoded = [vocab.encode(tokenizer.tokenize(t)) for t in [texts[2], texts_labeled[2]]]
    encoded_val = [vocab.encode(tokenizer.tokenize(t)) for t in [texts[8], texts_labeled[8]]]
    source, target = batcher.labeled([encoded[0]], [encoded[1]])
    source_val, target_val = batcher.labeled([encoded_val[0]], [encoded_val[1]])

    start = time.time()
    try:
        for epoch in range(n_epochs):
            transformer.module.train()
            transformer.train_supervised(source, target)

            transformer.module.eval()
            transformer.test(source_val, target_val)

            print(f'R: epoch={epoch} [{epoch * 100 // n_epochs}%] time=[{time_since(start)}] '
                  f'T loss={transformer.train_losses[-1]:.3f} V loss={transformer.validation_losses[-1]:.3f}, '
                  f'T accuracy={transformer.train_accuracies[-1]:.3f} V accuracy={transformer.validation_accuracies[-1]:.3f}\n')
    except KeyboardInterrupt:
        pass
    return transformer


def annotate(transformer, vocab, tokenizer, batcher, texts):

    print(tokenizer.tokenize(texts[0]), end='\n\n')
    print(texts[0], end='\n\n')

    transformer.module.eval()
    source, target = batcher.eval(vocab.encode(tokenizer.tokenize(texts[0])))
    sentence = transformer.predict(source, target, vocab.w2i('[cls]'), vocab.w2i('[sep]'), vocab.w2i('[eot]'))
    print(' '.join(vocab.decode(sentence)), end='\n\n')

    print(tokenizer.tokenize(texts[0]), end='\n\n')
    print(texts[1], end='\n\n')

    source, target = batcher.eval(vocab.encode(tokenizer.tokenize(texts[1])))
    sentence = transformer.predict(source, target, vocab.w2i('[cls]'), vocab.w2i('[sep]'), vocab.w2i('[eot]'))
    print(' '.join(vocab.decode(sentence)), end='\n\n')

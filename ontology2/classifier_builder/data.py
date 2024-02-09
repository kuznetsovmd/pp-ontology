import random
import sys
import numpy as np


def vocabulary_defaults():
    return {
        'sequence_len': 48,
        'spec_tokens': ['[pad]', '[cls]'],
        'init_tokens': ['[sep]', '[unk]', '[!a]', '[a]'],
    }


def tokenizer_defaults():
    return {
        'sequence_len': 48,
        'train': True,
        'cls': '[cls]',
        'sep': '[sep]', 
        'pad': '[pad]',
    }


def dataset_defaults():
    return {
        'sequence_len': 48,
        'batch_len': 16,
        'cls': '[cls]',
        'sep': '[sep]',
        'pad': '[pad]',
        'source_mask': ['[!a]', '[a]'],
        'target_mask': [],
        'vocabulary': None,
        'tokenizer': None,
    }


class Vocabulary:
    def __init__(self, **kwargs):
        self.spec_tokens = kwargs['spec_tokens']
        self.init_tokens = kwargs['init_tokens']
        self.index2word = {i: t for i, t in enumerate((*self.spec_tokens, *self.init_tokens))}
        self.word2index = {t: i for i, t in enumerate((*self.spec_tokens, *self.init_tokens))}

    def new_w(self, word):
        if word not in self.word2index:
            current_size = self.size
            self.word2index[word] = current_size
            self.index2word[current_size] = word
            
    def new_ws(self, words):
        for w in words:
            self.new_w(w)

    def i2w(self, index):
        try:
            return self.index2word[index]
        except KeyError:
            return '[unk]'

    def w2i(self, word):
        try:
            return self.word2index[word]
        except KeyError:
            return self.w2i('[unk]')

    def encode(self, words):
        return np.array([self.w2i(w) for w in words])

    def decode(self, indices):
        return np.array([self.i2w(i) for i in indices])
    
    @property
    def size(self):
        return len(self.word2index)
    
    @property
    def n_spec_tokens(self):
        return len(self.spec_tokens)
    
    @property
    def n_init_tokens(self):
        return len(self.init_tokens)

    
class Tokenizer:
    def __init__(self, **kwargs):
        self.sequence_len = kwargs['sequence_len'] - 1
        self.train = kwargs['train']
        self.pad = kwargs['pad']
        self.cls = kwargs['cls']
        self.sep = kwargs['sep']

    def __getitem__(self, tokens):
        tokens = tokens.lower().split(' ')
        if not self.train:
            return tokens
        tokens = [self.cls, *tokens]
        tokenized = []
        for i, t in enumerate(tokens, start=1):
            tokenized.append(t)
            if i % self.sequence_len == 0:
                tokenized.append(self.sep)
        if tokenized[-1] != self.sep:
            tokenized.append(self.sep)
        return tokenized

class TrainDataset:
    def __init__(self, **kwargs):
        self.sequence_len = kwargs['sequence_len']
        self.batch_len = kwargs['batch_len']

        self.tokenizer = kwargs['tokenizer']
        self.vocab = kwargs['vocabulary']

        self.pad = self.vocab.w2i(kwargs['pad'])
        self.cls = self.vocab.w2i(kwargs['cls'])
        self.sep = self.vocab.w2i(kwargs['sep'])

        self.target_mask = self.vocab.encode(kwargs['target_mask'])
        self.source_mask = self.vocab.encode(kwargs['source_mask'])

        self.source_texts = []
        self.target_texts = []

    def prepare(self, source_texts, target_texts=None):
        self.source_texts = source_texts
        self.target_texts = target_texts if target_texts else self.source_texts

        s_encoded = [self.vocab.encode(self.tokenizer[t]) for t in self.source_texts]
        t_encoded = [self.vocab.encode(self.tokenizer[t]) for t in self.target_texts]

        targets = [self.__target(e) for e in t_encoded]
        sources = [self.__source(t, e) for t, e in zip(targets, s_encoded)]

        sources = self.__mask_tokens(np.vstack(sources), self.source_mask)
        targets = self.__mask_tokens(np.vstack(targets), self.target_mask)

        sources = self.__split_batches(sources)
        targets = self.__split_batches(targets)

        self.samples = list(zip(sources, targets))
        return self

    def __source(self, target, encoded):
        data = np.array(encoded, dtype=np.longlong)

        n_tail = len(data) % self.sequence_len
        if n_tail:
            n_extra_pads = self.sequence_len - n_tail
            data = np.append(data, np.full((n_extra_pads,), self.pad))
        data = data.reshape(-1, self.sequence_len)

        lengths = []
        l = 0
        for t in target:
            l += 1
            if t[-1] == 2:
                lengths.append(l)
                l = 0
        lengths[-1] += l

        batch = np.ndarray((0, self.sequence_len), dtype=np.int64)
        for i, l in enumerate(lengths):
            v = np.resize(np.array(data[i]), (l, self.sequence_len))
            batch = np.vstack((batch, *v))

        return batch
    
    def __target(self, encoded):
        data = np.array(encoded, dtype=np.longlong)
        data = np.append(data, np.full((self.sequence_len - 1,), self.pad))
        window = np.full((self.sequence_len,), self.pad)
        
        batch = np.ndarray((0, self.sequence_len))
        for token in data:
            window = np.delete(window, 0)
            window = np.append(window, token)
            batch = np.vstack((batch, window.copy()))

        return  batch
    
    def __mask_tokens(self, batch, tokens):
        
        for i, b in enumerate(batch):
            pos = np.where(np.isin(b, tokens))[0]
            for p in pos:
                batch[i, p] = 0

        # for i, b in enumerate(batch):
        #     pos = np.where(np.isin(b, tokens))[0]
        #     batch[i, :] = np.append(np.delete(b, pos), np.full((len(pos),), self.pad))

        return batch
    
    def __split_batches(self, data):
        return np.split(data, np.arange(self.batch_len, len(data), self.batch_len))

    def __getitem__(self, i):
        return self.samples[i]

    def __len__(self):
        return len(self.samples)


class PredictionDataset(TrainDataset):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def prepare(self, source_texts, target_texts=None):
        self.source_texts = source_texts

        encoded = [self.vocab.encode(self.tokenizer[t]) for t in self.source_texts]
        sources = [self.__source(e) for e in encoded]
        targets = [self.__target(e) for e in encoded]
        
        self.samples = list(zip(sources, targets, self.source_texts))
        return self

    def __source(self, encoded):
        data = np.array(encoded, dtype=np.longlong)

        n_tail = len(data) % self.sequence_len
        if n_tail > 0:
            n_extra_pads = self.sequence_len - n_tail
            data = np.append(data, np.full((n_extra_pads,), self.pad))

        return data.reshape(-1, self.sequence_len)

    def __target(self, encoded):
        n_parts = len(encoded) // self.sequence_len
        n_tail = len(encoded) % self.sequence_len
        if n_tail:
            n_parts += 1

        target = np.ndarray((n_parts, self.sequence_len), dtype=np.longlong)
        target[:1, :] = np.hstack(([self.pad] * (self.sequence_len - 1), [self.cls]))
        target[1:, :] = np.hstack(([self.pad] * (self.sequence_len - 1), [self.sep]))

        return target

import random
import re
import numpy as np


def vocabulary_defaults():
    return {
        'sequence_len': 64,
        'spec_tokens': ['[pad]', '[sot]', '[sep]'],
        'init_tokens': ['[eot]', '[unk]', '[!a]', '[a]'],
    }


def tokenizer_defaults():
    return {
        'sequence_len': 64,
        'train': True,
        'pad': '[pad]',
        'sot': '[sot]',
        'sep': '[sep]',
        'eot': '[eot]',
    }


def dataset_defaults():
    return {
        'sequence_len': 64,
        'batch_len': 16,
        'pad': '[pad]',
        'sot': '[sot]',
        'eot': '[eot]',
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
        self.sot = kwargs['sot']
        self.sep = kwargs['sep']
        self.eot = kwargs['eot']
        self.ignored_tokens = ['[!a]', '[a]']

        self.punctuation = re.compile(rf"\[!?[a-zа-я]\]|[{''.join(kwargs['punctuation'])}]")
        self.reduce_spaces = re.compile(r'(?<!^)\s+(?!$)')
        self.trim_spaces = re.compile(r'(^\s)|(\s$)')

    def divide_chunks(self, l, n):
        start, length = 0, 0
        for i, t in enumerate(l, start=1):

            if t not in self.ignored_tokens:
                length += 1

            if length >= n:
                yield l[start:i]
                length, start = 0, i
        
        last = l[start:]
        if last: yield last

    def __getitem__(self, tokens):
        text = self.punctuation.sub(' \g<0> ', tokens)
        text = self.reduce_spaces.sub(' ', text)
        text = self.trim_spaces.sub('', text)
        text = text.lower().split(' ')
    
        if not self.train:
            return [self.sot, *text]
    
        text = [*text, self.eot]
        text = list(self.divide_chunks(text, self.sequence_len))

        tokenized = [[self.sot, *(text[0])], *[[self.sep, *t] for t in text[1:]]]

        return [t for text in tokenized for t in text]
    

class TrainDataset:
    def __init__(self, **kwargs):
        self.sequence_len = kwargs['sequence_len']
        self.batch_len = kwargs['batch_len']

        self.tokenizer = kwargs['tokenizer']
        self.vocab = kwargs['vocabulary']

        self.pad = self.vocab.w2i(kwargs['pad'])
        self.sot = self.vocab.w2i(kwargs['sot'])

        self.target_mask = self.vocab.encode(kwargs['target_mask'])
        self.source_mask = self.vocab.encode(kwargs['source_mask'])

        self.texts = []
        self.samples = []
    
    def shuffle(self):
        random.shuffle(self.samples)
        return self

    def prepare(self, texts):
        self.texts = texts

        encoded = [self.vocab.encode(self.tokenizer[t]) for t in self.texts]

        targets = [self.__target(e) for e in encoded]
        sources = [self.__source(e) for e in encoded]

        sources = [self.__mask_tokens(s, self.source_mask) for s in sources]
        targets = [self.__mask_tokens(t, self.target_mask) for t in targets]

        sources = self.__split_batches(np.vstack(sources))
        targets = self.__split_batches(np.vstack(targets))

        self.samples = list(zip(sources, targets))

        return self

    def __source(self, encoded):
        data = np.array(encoded, dtype=np.int64)

        n_full = len(data) // self.sequence_len
        n_tail = len(data) % self.sequence_len
        lengths = [self.sequence_len] * n_full

        if n_tail > 0:
            lengths.append(n_tail)
            n_extra_pads = self.sequence_len - n_tail
            data = np.append(data, np.full((n_extra_pads,), self.pad))
        data = data.reshape(-1, self.sequence_len)

        batch = np.ndarray((0, self.sequence_len), dtype=np.int64)
        for i, l in enumerate(lengths):
            v = np.resize(np.array(data[i]), (l, self.sequence_len))
            batch = np.vstack((batch, *v))

        return batch
    
    def __target(self, encoded):
        data = np.array(encoded, dtype=np.int64)
        window = np.full((self.sequence_len,), self.pad)
        
        batch = np.ndarray((0, self.sequence_len), dtype=np.int64)
        for token in data:
            window = np.delete(window, 0)
            window = np.append(window, token)
            batch = np.vstack((batch, window.copy()))

        return  batch
    
    def __mask_tokens(self, batch, tokens):
        for i, b in enumerate(batch):
            pos = np.where(np.isin(b, tokens))[0]
            batch[i, :] = np.append(np.delete(b, pos), np.full((len(pos),), self.pad))

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

    def prepare(self, texts):
        self.texts = texts

        encoded = [self.vocab.encode(self.tokenizer[t]) for t in self.texts]
        sources = [self.__source(e) for e in encoded]
        targets = [self.__target()] * len(sources)
        
        self.samples = list(zip(sources, targets, self.texts))
        return self

    def __source(self, encoded):
        data = np.array(encoded, dtype=np.longlong)

        n_tail = len(data) % self.sequence_len
        if n_tail > 0:
            n_extra_pads = self.sequence_len - n_tail
            data = np.append(data, np.full((n_extra_pads,), self.pad))

        return data.reshape(-1, self.sequence_len)

    def __target(self):
        target = np.hstack(([self.pad] * (self.sequence_len - 1), [self.sot]))
        return target.reshape(1, -1)

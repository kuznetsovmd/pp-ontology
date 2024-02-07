import random
import sys
import numpy as np

from config import RESOURCES


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
        self.sequence_len = kwargs['sequence_len']
        self.train = kwargs['train']
        self.pad = kwargs['pad']
        self.cls = kwargs['cls']
        self.sep = kwargs['sep']

    def tokenize(self, tokens):
        tokens = tokens.lower().split(' ')
        if not self.train:
            return tokens
        tokens = [tokens[i:i + self.sequence_len] for i in range(0, len(tokens), self.sequence_len)]
        chunked = [[*t, self.sep] for t in tokens]
        return [chunk for t in [[self.cls], *chunked] for chunk in t]


class TrainDataset:
    def __init__(self, **kwargs):
        self.source_data_path = kwargs['source_data_path']
        self.sequence_len = kwargs['sequence_len']
        self.batch_len = kwargs['batch_len']
        self.split_sep = kwargs['split_sep']
        self.dtype = kwargs['dtype']

        self.vocab = Vocabulary(**kwargs)
        self.tokenizer = Tokenizer(**kwargs)

        self.pad = self.vocab.w2i(kwargs['pad'])
        self.cls = self.vocab.w2i(kwargs['cls'])
        self.sep = self.vocab.w2i(kwargs['sep'])

        self.texts = []
        self.train = []
        self.validate = []

    @staticmethod
    def unwrap_words(texts, tokenizer):
        return [t for text in texts for t in tokenizer.tokenize(text)]
    
    def shuffle(self):
        random.shuffle(self.train)
        random.shuffle(self.validate)

    def load(self):
        with open(self.source_data_path, 'r') as f:
            self.texts = f.read().split('\n')[:10]
        self.vocab.new_ws(self.unwrap_words(self.texts, self.tokenizer))
        return self

    def split(self):
        encoded = [self.vocab.encode(self.tokenizer.tokenize(t)) for t in self.texts]
        source = [self.source(e) for e in encoded]
        target = [self.target(e) for e in encoded]


        print(f'{source=}')
        print(f'{target=}')
        print(f'{source.shape=} {target.shape}')

        sys.exit(0)

        samples_len = len(target)
        val_cnt = int(samples_len * (1 - self.split_sep))
        v_sources = target[val_cnt:]
        t_sources = target[:samples_len - val_cnt]

        self.train = self.split_batches(np.vstack(t_sources))
        self.validate = self.split_batches(np.vstack(v_sources))
        return self
    
    def source():

        

        return batch

    def target(self, encoded):
        data = np.array(encoded, dtype=self.dtype)
        extra_pads = np.full((self.sequence_len - 2,), self.pad, dtype=self.dtype)
        data = np.append(data, extra_pads)
        
        batch = np.ndarray((0, self.sequence_len), dtype=self.dtype)
        window = np.full((self.sequence_len,), self.pad)
        
        window = np.delete(window, 0)
        window = np.append(window, data[0])
        for token in data[1:]:
            window = np.delete(window, 0)
            window = np.append(window, token)
            batch = np.vstack((batch, window.copy()))

        print(f'{batch}')
        return batch
    
    def split_batches(self, data):
        return np.split(data, np.arange(self.batch_len, len(data), self.batch_len))



class LabeledDataset(TrainDataset):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.target_data_path = kwargs['target_data_path']
        self.target_texts = []

    def load(self):
        super().load()
        with open(self.target_data_path, 'r') as f:
            self.target_texts = f.read().split('\n')
        self.vocab.new_ws(self.unwrap_words(self.target_texts, self.tokenizer))
        return self

    def split(self):
        encoded_sources = [self.vocab.encode(self.tokenizer.tokenize(t)) for t in self.texts]
        encoded_targets = [self.vocab.encode(self.tokenizer.tokenize(t)) for t in self.target_texts]

        sources = [self.target(e, align=True) for e in encoded_sources]
        targets = [self.target(e, align=False) for e in encoded_targets]

        assert self.texts != len(self.target_texts), f'{len(self.texts)=}, {len(self.target_texts)=}'
        sources_len = len(sources)

        val_cnt = int(sources_len * (1 - self.split_sep))
        v_sources = sources[val_cnt:]
        t_sources = sources[:sources_len - val_cnt]
        v_targets = targets[val_cnt:]
        t_targets = targets[:sources_len - val_cnt]

        self.train = list(zip(self.split_batches(np.vstack(t_sources)), self.split_batches(np.vstack(t_targets))))
        self.validate = list(zip(self.split_batches(np.vstack(v_sources)), self.split_batches(np.vstack(v_targets))))
        return self

    def target(self, encoded, align=False):
        batch = super().target(encoded)

        if not align:
            return batch

        for i, b in enumerate(batch):
            pos = np.where((b == 6) | (b == 7) | (b == 1))[0]
            b, c = np.delete(b, pos), len(pos)
            if c > 1:
                replaced = np.append(np.full((c - 1,), self.pad), np.full((1,), self.cls))
                batch[i, :] = np.append(replaced, b)

        return batch


class PredictionDataset(TrainDataset):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def load(self):
        super().load()

    def get(self):
        encoded = [self.vocab.encode(self.tokenizer.tokenize(t)) for t in self.texts]
        sources = [self.target(e) for e in encoded]
        targets = [self.empty_target(e) for e in encoded]
        return list(zip(sources, targets, self.texts))

    def target(self, encoded):
        data = np.array(encoded, dtype=self.dtype)
        
        n_extra_pads = self.sequence_len - len(data) % self.sequence_len
        data = np.append(data, np.full((n_extra_pads,), self.pad))
        batch = data.reshape(-1, self.sequence_len)

        return batch

    def empty_target(self, encoded):
        n_parts = len(encoded) // self.sequence_len

        target = np.full((self.sequence_len - 1,), self.pad, dtype=self.dtype)
        target = np.hstack((target, [self.cls]))

        for _ in range(n_parts):
            target_i = np.full((self.sequence_len - 1,), self.pad, dtype=self.dtype)
            target = np.hstack((target, target_i, [self.sep]))

        return target.reshape(-1, self.sequence_len)


def get_defaults():
    return {
        'sequence_len': 64,
        'batch_len': 16,
        'dtype': np.uint8,
        'cls': '[cls]',
        'sep': '[sep]', 
        'pad': '[pad]',
        'train': True,
        'split_sep': 1,
        'source_data_path': f'{RESOURCES}/example_texts_unlabeled.txt',
        'target_data_path': f'{RESOURCES}/example_texts_labeled.txt',
        'spec_tokens': ['[pad]', '[cls]'],
        'init_tokens': ['[sep]', '[unk]', '[!a]', '[a]']
    }

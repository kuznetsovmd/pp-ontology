import numpy as np


class VocabularyData:
    def __init__(self, spec_tokens=()):
        self.spec_tokens = spec_tokens
        self.index2word = {i: t for i, t in enumerate(self.spec_tokens)}
        self.word2index = {t: i for i, t in enumerate(self.spec_tokens)}


class Vocabulary:
    def __init__(self, vocabulary_data):
        self.vocabulary_data = vocabulary_data

    def new_w(self, word):
        if word not in self.vocabulary_data.word2index:
            size = self.size
            self.vocabulary_data.word2index[word] = size
            self.vocabulary_data.index2word[size] = word
            
    def new_ws(self, words):
        for w in words:
            self.new_w(w)

    def i2w(self, index):
        return self.vocabulary_data.index2word[index]

    def w2i(self, word):
        return self.vocabulary_data.word2index[word]

    def __getitem__(self, words):
        return np.array([self.w2i(w) for w in words])

    def decode(self, indices):
        return np.array([self.i2w(i) for i in indices])
    
    @property
    def size(self):
        return len(self.vocabulary_data.word2index)
    
    @property
    def n_spec_tokens(self):
        return len(self.vocabulary_data.spec_tokens)

    
class Tokenizer:
    def __init__(self, sot, eot, train=True):
        self.train = train
        self.sot = sot
        self.eot = eot

    def __getitem__(self, key):
        return [self.sot, *key.lower().split(' '), self.eot] if self.train else key.lower().split(' ')

    
class Batcher:
    def __init__(self, sequence_len,  pad, cls, sep, train=True, batch_size=100, device='cpu'):
        self.sequence_len = sequence_len
        self.batch_size = batch_size
        self.device = device
        self.train = train
        self.pad = pad
        self.sep = sep
        self.cls = cls

    def __getitem__(self, tokenized):
        data = np.array(tokenized, dtype=int)
        
        if not self.train:
            sequence_len = self.sequence_len
            n_extra_pads = self.sequence_len - len(data) % self.sequence_len
            data = np.append(np.full((n_extra_pads,), self.pad), data)
            return data.reshape(-1, sequence_len)

        sequence_len = self.sequence_len - 2
        batches = np.ndarray((0, sequence_len), dtype=int)
        window = np.full((sequence_len,), self.pad),
        data = np.append(data, np.full((sequence_len,), self.pad))
        
        for token in data:
            window = np.delete(window, 0)
            window = np.append(window, token)
            batches = np.vstack((batches, window.copy()))

        n_batches = len(batches)
        left = np.reshape([self.cls for _ in range(n_batches)], (-1, 1))
        right = np.reshape([*[self.sep for _ in range(n_batches - 1)], self.pad], (-1, 1))
        return np.split(np.concatenate((left, batches, right), axis=1), np.arange(self.batch_size,len(batches),self.batch_size))


def initial_target(sequence_len, pad, sot):
    return np.append(np.full((sequence_len - 1,), pad, dtype=int), np.full((1,), sot, dtype=int)).reshape(-1, sequence_len)

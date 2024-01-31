import numpy as np


class VocabularyData:
    def __init__(self, spec_tokens=(), initial_tokens=()):
        self.spec_tokens = spec_tokens
        self.initial_tokens = initial_tokens
        self.index2word = {i: t for i, t in enumerate((*spec_tokens, *initial_tokens))}
        self.word2index = {t: i for i, t in enumerate((*spec_tokens, *initial_tokens))}


class Vocabulary:
    def __init__(self, vocabulary_data):
        self.vocabulary_data = vocabulary_data

    def new_w(self, word):
        if word not in self.vocabulary_data.word2index:
            current_size = self.size
            self.vocabulary_data.word2index[word] = current_size
            self.vocabulary_data.index2word[current_size] = word
            
    def new_ws(self, words):
        for w in words:
            self.new_w(w)

    def i2w(self, index):
        return self.vocabulary_data.index2word[index]

    def w2i(self, word):
        return self.vocabulary_data.word2index[word]

    def encode(self, words):
        return np.array([self.w2i(w) for w in words])

    def decode(self, indices):
        return np.array([self.i2w(i) for i in indices])
    
    @property
    def size(self):
        return len(self.vocabulary_data.word2index)
    
    @property
    def n_spec_tokens(self):
        return len(self.vocabulary_data.spec_tokens)
    
    @property
    def n_initial_tokens(self):
        return len(self.vocabulary_data.initial_tokens)

    
class Tokenizer:
    def __init__(self, sot, eot, train=True):
        self.train = train
        self.sot = sot
        self.eot = eot

    def tokenize(self, key):
        return [self.sot, *key.lower().split(' '), self.eot] if self.train else key.lower().split(' ')

    
class Batcher:
    def __init__(self, sequence_len, batch_size, pad, cls, sep, sot, dtype=int, device='cpu'):
        self.sequence_len = sequence_len
        self.batch_size = batch_size
        self.device = device
        self.dtype = dtype
        self.pad = pad
        self.sot = sot
        self.sep = sep
        self.cls = cls

    def pack(self, tokenized1, tokenized2=None):
        if tokenized2 is not None:
            return self.split(*self.align(self.pack_train(tokenized1), self.pack_train(tokenized2)))
        else:
            return self.pack_eval(tokenized1), self.empty_target()

    def empty_target(self):
        start = np.full((self.sequence_len - 1,), self.pad, dtype=self.dtype)
        end = np.full((1,), self.sot, dtype=self.dtype)
        return np.append(start, end).reshape(-1, self.sequence_len)

    def pack_eval(self, tokenized):
        data = np.array(tokenized, dtype=self.dtype)

        sequence_len = self.sequence_len
        n_extra_pads = self.sequence_len - len(data) % self.sequence_len
        data = np.append(np.full((n_extra_pads,), self.pad), data)
        return data.reshape(-1, sequence_len)

    def pack_train(self, tokenized):
        data = np.array(tokenized, dtype=self.dtype)

        sequence_len = self.sequence_len - 2
        batches = np.ndarray((0, sequence_len), dtype=self.dtype)
        window = np.full((sequence_len,), self.pad),
        data = np.append(data, np.full((sequence_len - 1,), self.pad))
        
        for token in data:
            window = np.delete(window, 0)
            window = np.append(window, token)
            batches = np.vstack((batches, window.copy()))

        n_batches = len(batches)
        left = np.reshape([self.cls for _ in range(n_batches)], (-1, 1))
        right = np.reshape([*[self.sep for _ in range(n_batches - 1)], self.pad], (-1, 1))
        return np.concatenate((left, batches, right), axis=1)

    def align(self, s, t):
        diff = len(s) - len(t)
        if diff == 0:
            return s, t
        
        abs_diff = abs(diff)

        filler_start = np.full((abs_diff - 1, 1), self.cls)
        filler_center = np.full((abs_diff - 1, self.sequence_len - 2), self.pad)
        filler_end = np.full((abs_diff - 1, 1), self.sep)
        filler = np.hstack((filler_start, filler_center, filler_end))

        last_start = np.full((1, 1), 1)
        last_end  = np.full((1, self.sequence_len - 1), 0)
        last = np.hstack((last_start, last_end))

        if diff < 0:
            s = np.vstack((s, filler, last))
        else:
            t = np.vstack((t, filler, last))
        return s, t
    
    def split(self, s, t):
        s_splits = np.split(s, np.arange(self.batch_size, len(s), self.batch_size))
        t_splits = np.split(t, np.arange(self.batch_size, len(t), self.batch_size))
        return s_splits, t_splits

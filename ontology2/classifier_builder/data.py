import numpy as np


class Vocabulary:
    def __init__(self, spec_tokens=(), initial_tokens=()):
        self.spec_tokens = spec_tokens
        self.initial_tokens = initial_tokens
        self.index2word = {i: t for i, t in enumerate((*spec_tokens, *initial_tokens))}
        self.word2index = {t: i for i, t in enumerate((*spec_tokens, *initial_tokens))}

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
    def n_initial_tokens(self):
        return len(self.initial_tokens)

    
class Tokenizer:
    def __init__(self, sot, eot, cls, sep, pad, sequence_len, train=True):
        self.sequence_len = sequence_len - 2
        self.train = train
        self.sot = sot
        self.eot = eot
        self.cls = cls
        self.sep = sep
        self.pad = pad

    def tokenize(self, tokens):
        tokens = tokens.lower().split(' ')
        if not self.train:
            return tokens
        tokens = [self.sot, *tokens, self.eot]
        tokens = [tokens[i:i + self.sequence_len] for i in range(0, len(tokens), self.sequence_len)]
        chunked = [[self.cls, *t, self.sep] for t in tokens[:-1]]
        chunked.append([self.cls, *tokens[-1]])
        return [chunk for t in chunked for chunk in t]
    
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

    def unlabeled(self, encoded):
        s = np.vstack(tuple(self.for_train(e) for e in encoded))
        return self.split(s)

    def labeled(self, encoded1, encoded2):
        s = np.vstack(tuple(self.for_train(e) for e in encoded1))
        t = np.vstack(tuple(self.for_train(e) for e in encoded2))
        s, t = self.align(s, t)
        return self.split(s), self.split(t)

    def eval(self, encoded):
        source = self.for_eval(encoded)
        return source, self.empty_target(source)

    def empty_target(self, source):
        n_batches = source.shape[0]
        target = np.full((self.sequence_len - 2,), self.pad, dtype=self.dtype)
        target = np.hstack((target, [self.cls, self.sot]))
        for _ in range(n_batches - 1):
            target_i = np.full((self.sequence_len - 1,), self.pad, dtype=self.dtype)
            target = np.hstack((target, target_i, [self.cls]))
        return target.reshape(-1, self.sequence_len)

    def for_eval(self, tokenized):
        data = np.array(tokenized, dtype=self.dtype)
        
        sequence_len = self.sequence_len
        n_extra_pads = sequence_len - len(data) % sequence_len
        data = np.append(np.full((n_extra_pads,), self.pad), data)
        batches = data.reshape(-1, sequence_len)
        
        return batches

    def for_train(self, tokenized):
        data = np.array(tokenized, dtype=self.dtype)

        sequence_len = self.sequence_len
        batches = np.ndarray((0, sequence_len), dtype=self.dtype)
        window = np.full((sequence_len - 1,), self.pad)
        window = np.append(window, data[:1])
        data = np.append(data, np.full((sequence_len - 1,), self.pad))
        
        for token in data[1:]:
            window = np.delete(window, 0)
            window = np.append(window, token)
            batches = np.vstack((batches, window.copy()))
            
        return batches

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
    
    def split(self, batch):
        return np.split(batch, np.arange(self.batch_size, len(batch), self.batch_size))

import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm

from config import *

from ontology2.classifier_builder.transformer import Transformer
from ontology2.classifier_builder.docs import *
from ontology2.classifier_builder.fetch_device import *
from ontology2.classifier_builder.data_pipeline import Batcher, Tokenizer, Vocabulary, VocabularyData, initial_target


def print_info():
    print(f'Torch version: {torch.__version__}')
    try:
        print(f'Using: {torch.cuda.get_device_name(DEVICE)}')
    except ValueError:
        print(f'Using: CPU')


def unlabeled_train():
    """
    Have the following issues:
    1. Two or more word occurances cuts text between them
    2. Use gready search, make beam or other sampling
    3. Check if masking properly
    4. Temperature
    """

    torch.set_printoptions(threshold=10_000)

    d_model = 1024                 # Embedding size
    num_heads = 32                 # Threads
    num_layers = 6                 # Layers
    d_ff = 2048                    # FC
    max_seq_length = 168           # --
    dropout = .1                   # --
    batch_size = 32
    temperature = .5

    vd = VocabularyData(spec_tokens=['[PAD]', '[CLS]', '[SEP]', '[SOT]', '[EOT]'])
    vocab = Vocabulary(vd)
    tokenizer = Tokenizer('[SOT]', '[EOT]')

    with open(f'{RESOURCES}/example_texts.txt', 'r') as f:
        texts = f.read().split('\n\n')

    tokens = [w for tx in texts[:1] for w in tokenizer[tx]]
    # tokens = t[texts[0]]
    # print(f'{tokens=}')
    vocab.new_ws(tokens)
    # print(f'{v.size=}')

    batcher = Batcher(max_seq_length, vocab.w2i('[PAD]'), vocab.w2i('[CLS]'), vocab.w2i('[SEP]'), train=True, batch_size=batch_size)
    # print(f'{b[tokens]=}')

    transformer = Transformer(vocab.size, vocab.size, d_model, num_heads, num_layers, 
                              d_ff, max_seq_length, dropout, temperature, device=DEVICE)

    src_data = batcher[vocab[tokens]]
    tgt_data = src_data

    # print(f'{texts[0]=}')
    # print(f'{t[texts[0]]=}')
    # print(f'{b[t[texts[0]]]=}')
    # print(f'{src_data=}')

    criterion = nn.CrossEntropyLoss(weight=torch.tensor([
        *[0.0 for _ in range(4)],
        *[1.0 for _ in range(4, vocab.size)]
    ], device=DEVICE))

    optimizer = optim.Adam(transformer.parameters(), lr=0.0001, eps=1e-9)
    transformer.train()

    try:
        for epoch in range(1000):
            for s, tokenizer in tqdm(zip(src_data, tgt_data), ncols=80, ascii=True):
                optimizer.zero_grad()
                s_gpu = torch.tensor(s, device=DEVICE)
                t_gpu = torch.tensor(tokenizer, device=DEVICE)
                output = transformer(s_gpu, t_gpu[:, :-1])
                loss = criterion(output.contiguous().view(-1, vocab.size), t_gpu[:, 1:].contiguous().view(-1))
                loss.backward()
                optimizer.step()
            print(f"Epoch: {epoch+1}, Loss: {loss.item()}")
    except KeyboardInterrupt:
        pass

    transformer.eval()

    tokenizer = Tokenizer('[SOT]', '[EOT]', train=False)
    batcher = Batcher(max_seq_length, vocab.w2i('[PAD]'), vocab.w2i('[CLS]'), vocab.w2i('[SEP]'), train=False)

    source = torch.tensor(batcher[vocab[tokenizer[texts[0]]]], device=DEVICE)
    # print(f'{source=}')

    target = torch.tensor(initial_target(max_seq_length, vocab.w2i('[PAD]'), vocab.w2i('[SOT]')), device=DEVICE)
    # print(f'{target=}')

    sentence = []
    with torch.no_grad():
        for _ in range(600):
            predicted_vec = transformer(source, target).contiguous().view(-1, vocab.size)[-1]
            predicted_word = torch.argmax(predicted_vec).unsqueeze(0).unsqueeze(1)
            sentence.append(predicted_word.item())
            if sentence[-1] == vocab.w2i('[EOT]'):
                break
            target = torch.cat((target[:, 1:], predicted_word), 1)    

    print(' '.join(vocab.decode(sentence)))


def labeled_train():
    print('Labeled train is not implemented!')


def eval():
    print('Eval is not implemented!')

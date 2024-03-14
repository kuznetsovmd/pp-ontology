import math
import time
import torch

from tqdm import tqdm
from transformers import AutoTokenizer

from config import RESOURCES
from ontology2.classifier_builder.dataset import preprocess

from ontology2.classifier_builder.device import DEVICE
from ontology2.classifier_builder.dataset import postprocess
from ontology2.classifier_builder.wrapper import build_model, model_defaults, save_model


def time_since(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)


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


def build_classified(train_model, eval_model):

    print_info()

    tokenizer = AutoTokenizer.from_pretrained("ai-forever/ruBert-base")
    ds = preprocess(tokenizer)

    train_len = int(len(ds) * .8)
    t_ds = ds[:train_len]
    v_ds = ds[train_len:]
    
    m_defaults = model_defaults()
    m_defaults['name'] = 'bert_rnn_fpc'

    if train_model: 
        model = build_model(**m_defaults)
        model = train(model, t_ds, v_ds, 500)
        outputs = annotate(model, ds)

        with open(f'{RESOURCES}/outputs.txt', 'w') as f:
            print(''.join([f'{p["predicted"]}' for o in outputs for p in o]), file=f)

        with open(f'{RESOURCES}/targets.txt', 'w') as f:
            print(''.join([f'{p}' for c in ds for p in c['target_ids']]), file=f)

        outputs = postprocess(ds, outputs)

        with open(f'{RESOURCES}/excerpts.txt', 'w') as f:
            for chunk in outputs:
                selections = [chunk['input_ids'][i] for i in chunk['indices']]
                print(tokenizer.decode(selections), end=f'\n\n{"="*80}\n\n', file=f)

    if eval_model: 
        model = build_model(path=f'{RESOURCES}/models', **m_defaults)


def train(model, t_ds, v_ds, n_epochs):
    start = time.time()
    try:
        for epoch in range(n_epochs):
            for s in tqdm(t_ds, ncols=80):
                model.train(s)
            for s in tqdm(v_ds, ncols=80):
                model.test(s)
            print_stats(epoch, n_epochs, start, model.stats())
            model.version = epoch
            save_model(model, f'{RESOURCES}/models')
    except KeyboardInterrupt:
        pass
    return model


def annotate(model, ds):
    return [model.predict(s) for s in ds]
     

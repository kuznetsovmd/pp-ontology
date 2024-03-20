import json
import math
import time
import torch

from tqdm import tqdm
from transformers import AutoTokenizer

from config import RESOURCES

from ontology2.classifier_builder.device import DEVICE
from ontology2.classifier_builder.dataset import preprocess, postprocess
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
    
    with open(f'/mnt/Source/kuznetsovmd/__datasets/ru/output.json', 'r') as f:
        policies = {p['policy_hash']: p for p in json.load(f)}

    with open(f'/mnt/Source/kuznetsovmd/__datasets/012190650e118175fe2f538504434c7c.json', 'r') as f:
        annotations = json.load(f)
        annotations = [a for a in annotations if a['selection_class'] == 'FPCollection']
        hashes = sorted(set([a['policy_hash'] for a in annotations]))

    texts = {}
    for h in hashes:
        with open(f'/mnt/Source/kuznetsovmd/__datasets/ru/output_policies/{policies[h]["output_policy"]}', 'r') as f:
            texts[h] = f.read().lower()

    tokenizer = AutoTokenizer.from_pretrained("ai-forever/ruBert-large")
    ds = preprocess(tokenizer, texts, annotations)

    train_len = int(len(ds) * .9)
    t_ds = ds[:train_len]
    v_ds = ds[train_len:]
    
    m_defaults = model_defaults()
    if train_model: 
        model = build_model(**m_defaults)
        model = train(model, t_ds, v_ds, 500)
        outputs = annotate(model, ds)
        outputs = postprocess(ds, outputs, 5, .3)

    if eval_model: 
        m_defaults['name'] = 'bert'
        m_defaults['version'] = 97
        model = build_model(path=f'{RESOURCES}/models', **m_defaults)
        model.bert.resize_token_embeddings(len(tokenizer))
        print(f'Name: {model.name}, Version: {model.version}')
        outputs = annotate(model, ds)
        outputs = postprocess(ds, outputs, 5, .3)

    with open(f'{RESOURCES}/targets.txt', 'w') as f:
        print(''.join([f'{o}' for c in ds for o in c['target_ids']]), file=f)

    with open(f'{RESOURCES}/outputs.txt', 'w') as f:
        print(''.join([f'{p}' for o in outputs for p in o["predicted"]]), file=f)
        
    new_annotations = [{
        'author': 'classifier',
        'policy_hash': 'dummy',
        'selection_class': 'Dummy',
        'start': c[0]-1,
        'end': c[1]+1,
        'selected_text': ''.join([f'{d}' for d in texts[o['hash']][c[0]:c[1]]])
    } for o in outputs for c in o['coords']]

    with open(f'{RESOURCES}/annotations.json', 'w') as f:
        json.dump(new_annotations, f, indent=4, ensure_ascii=False)



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

import json
from pprint import pprint

from config import RESOURCES


def divide_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def make_samples(samples):
    for i, s in enumerate(samples):
        t = [[.0] * 2 for _ in enumerate(s['target_ids'])]
        for j, k in enumerate(s['target_ids']):
            t[j][k] = 1.0
        samples[i]['targets'] = t
    return samples


def split_samples(samples, chunk_len):
    splitted = []
    for i, s in enumerate(samples):
        for ii, am, om, ti, ts in zip(divide_chunks(s['input_ids'], chunk_len), 
                                      divide_chunks(s['attention_mask'], chunk_len), 
                                      divide_chunks(s['offset_mapping'], chunk_len), 
                                      divide_chunks(s['target_ids'], chunk_len), 
                                      divide_chunks(s['targets'], chunk_len)):
            splitted.append({
                'sample_id': i,
                'input_ids': [101, *ii, 102],
                'attention_mask': [1, *am, 1],
                'offset_mapping': [(0, 0), *om, (0, 0)],
                'target_ids': [0, *ti, 0],
                'targets': [(1.0, 0.0), *ts, (1.0, 0.0)]
            })
    return splitted


def tokenize_targets(tokenizer, text, selections):

    tokenizer_defaults = {
        'add_special_tokens': False,
        'return_token_type_ids': False,
        'return_offsets_mapping': True,
    }

    item = tokenizer.encode_plus(text, **tokenizer_defaults)
    item['target_ids'] = []

    # annotated = ''
    p = 0
    for (s, e) in selections:

        if p > s:
            continue

        # annotated = f'{annotated}{txt[p:s]}'
        pre = len(tokenizer.encode_plus(text[p:s], **tokenizer_defaults)['input_ids'])
        item['target_ids'].extend([0] * pre)

        # annotated = f'{annotated}{txt[s:e]}'
        sel = len(tokenizer.encode_plus(text[s:e], **tokenizer_defaults)['input_ids'])
        item['target_ids'].extend([1] * sel)
        
        p = e

    # annotated = f'{annotated}{txt[p:]}'
    post = len(tokenizer.encode_plus(text[p:], **tokenizer_defaults)['input_ids'])
    item['target_ids'].extend([0] * post)

    # for i, (a, t) in enumerate(zip(annotated, txt)):
    #     if a != t:
    #         print(f'ORIGINAL {"=" * 100}')
    #         print(i, len(txt), txt[i-50:i+50])
    #         print(f'ANNOTATED {"=" * 100}')
    #         print(i, len(annotated), annotated[i-50:i+50])

    assert len(item['input_ids']) == len(item['target_ids']), 'lengths of source and target are not equal!'

    return item


def preprocess(tokenizer):

    with open(f'/mnt/Source/kuznetsovmd/__datasets/012190650e118175fe2f538504434c7c.json', 'r') as f:
        annotations = json.load(f)

    with open(f'/mnt/Source/kuznetsovmd/__datasets/ru/output.json', 'r') as f:
        policies = {a['policy_hash']: a for a in json.load(f)}

    annotations = [a for a in annotations if a['selection_class'] == 'FPCollection']
    hashes = set([a['policy_hash'] for a in annotations])

    samples = []
    for h in hashes:
        p = policies[h]

        with open(f'/mnt/Source/kuznetsovmd/__datasets/ru/output_policies/{p["output_policy"]}', 'r') as f:
            text = f.read().lower()
        
        selections = [(int(a['starts_on']), int(a['ends_on'])) for a in annotations if a['policy_hash'] == h]
        samples.append(tokenize_targets(tokenizer, text, selections))

    samples = make_samples(samples)
    samples = split_samples(samples, 510)

    return samples


def postprocess(dataset, outputs):
    for i, (d, o) in enumerate(zip(dataset, outputs)):
        dataset[i]['indices'] = [i for i, p in enumerate(o) if p['predicted'] == 1]
        dataset[i]['coords'] = [d['offset_mapping'][i] for i in d['indices']]
    return dataset

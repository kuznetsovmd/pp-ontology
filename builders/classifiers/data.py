import json
from utils.fsys import files


def read_data(descriptor, policies, annotations, ontology_class):
    with open(descriptor, 'r') as f:
        policies_map = {p['policy_hash']: p for p in json.load(f)}

    fs = files(annotations, r'.*\.json')
    
    annotations_list = []
    for file in fs:
        with open(file, 'r') as f:
            annotations_list.extend(json.load(f))

    annotations_list = [a for a in annotations_list if a['selection_class'] == ontology_class]

    hashes = sorted(set([a['policy_hash'] for a in annotations_list]))
    annotations_map = {}
    for h in hashes:
        annotations_map[h] = []
        for a in annotations_list:
            if a['policy_hash'] == h:
                annotations_map[h].append(a)

    texts_map = {}
    for h in hashes:
        with open(f'{policies}/{policies_map[h]["plain_policy"]}', 'r') as f:
            texts_map[h] = f.read().lower()

    return {
        'annotations': annotations_map, 
        'texts': texts_map,
    }


def split_data(data, split):
    train_len = int(len(data) * split)
    return {
        'train': data[:train_len],
        'validation': data[train_len:],
    }


def split(array, n):
    for i in range(0, len(array), n):
        yield array[i:i + n]


def split_samples(samples, chunk_len):
    splitted = []
    for s in samples:
        splits = \
            split(s['input_ids'], chunk_len), \
            split(s['attention_mask'], chunk_len), \
            split(s['offset_mapping'], chunk_len), \
            split(s['target_ids'], chunk_len)
        for ii, am, om, ti in zip(*splits):
            splitted.append({
                'hash': s['hash'],
                'input_ids': [101, *ii, 102],
                'attention_mask': [1, *am, 1],
                'offset_mapping': [(0, 0), *om, (0, 0)],
                'target_ids': [0, *ti, 0],
            })
    return splitted


def tokenize_targets(tokenizer, tokenizer_defaults, hash, text, selections):
    item = tokenizer.encode_plus(text, **tokenizer_defaults)
    item['hash'] = hash
    item['target_ids'] = []
    p = 0
    for (s, e) in selections:
        if p > s:
            continue
        pre = len(tokenizer.encode_plus(text[p:s], **tokenizer_defaults)['input_ids'])
        item['target_ids'].extend([0] * pre)
        sel = len(tokenizer.encode_plus(text[s:e], **tokenizer_defaults)['input_ids'])
        item['target_ids'].extend([1] * sel)
        p = e
    post = len(tokenizer.encode_plus(text[p:], **tokenizer_defaults)['input_ids'])
    item['target_ids'].extend([0] * post)
    if len(item['input_ids']) != len(item['target_ids']):
        raise Exception(f'lengths of source and target are not equal!')
    return item


def preprocess(tokenizer, texts, annotations, sequence_len):
    tokenizer_defaults = {
        'add_special_tokens': False,
        'return_token_type_ids': False,
        'return_offsets_mapping': True,
    }

    samples = []
    for hash, text in texts.items():
        selections = [a for a in annotations[hash]]
        selections = [(int(a['starts_on']), int(a['ends_on'])) for a in selections]
        samples.append(tokenize_targets(tokenizer, tokenizer_defaults, hash, text, selections))

    return split_samples(samples, sequence_len - 2)


def postprocess(dataset, outputs, padding, threshold):
    dataset['predicted'], dataset['coords'] = get_coords(outputs, dataset['offset_mapping'], padding, threshold)
    return dataset


def add_pad(array, pad_item):
    return [pad_item, *array, pad_item]


def merge(array, padding, threshold):
    merged = []
    for i, _ in enumerate(array):
        if sum([*array[i-padding:i], *array[i+1:i+1+padding]]) / 2 / padding > threshold:
            merged.append(1)
            continue
        merged.append(array[i])
    return merged


def boundries(array, coords):
    boundries = []
    start = 0
    for i, d in enumerate(array):
        if d and not start:
            start = coords[i][0]
        if not d and start:
            boundries.append((start, coords[i-1][1]))
            start = 0
    return boundries


def get_coords(data, coords, padding, threshold):
    merged = merge(data, padding, threshold)
    return merged, boundries(add_pad(merged, 0), add_pad(coords, (0, 0)))

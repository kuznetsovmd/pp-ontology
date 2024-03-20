import json
import time

from tqdm import tqdm

from builders.classifiers.utils import print_stats

from .data import preprocess, postprocess, read_data, split_data
from .wrapper import build_model, save_model


def train_classifier(ontology_class, annotations_path, 
                  descriptor_path, policies_path, sequence_len, split, 
                  n_epochs, bert_tokenizer, tqdm_conf, 
                  model_conf, **kwargs):
    
    annotations_map, texts_map = read_data(**{
        'descriptor': descriptor_path,
        'policies': policies_path,
        'annotations': annotations_path,
        'ontology_class': ontology_class,
    }).values()

    ds = preprocess(**{
        'tokenizer': bert_tokenizer,
        'texts': texts_map,
        'annotations': annotations_map,
        'sequence_len': sequence_len,
    })

    t_ds, v_ds = split_data(**{
        'data': ds,
        'split': split,
    }).values()
    
    model = build_model(**model_conf)
    start = time.time()
    try:
        for epoch in range(model.version, n_epochs):
            for s in tqdm(t_ds, **tqdm_conf):
                model.train(s)
            for s in tqdm(v_ds, **tqdm_conf):
                model.test(s)
            print_stats(epoch, n_epochs, start, model.stats())
            model.version = epoch
            save_model(model, model.path)
    except KeyboardInterrupt:
        pass


def eval_classifier(ontology_class, annotations_path, 
                  descriptor_path, policies_path, output_path, sequence_len, 
                  padding, density, bert_tokenizer,  
                  model_conf, tqdm_conf, **kwargs):
    
    annotations_map, texts_map = read_data(**{
        'descriptor': descriptor_path,
        'policies': policies_path,
        'annotations': annotations_path,
        'ontology_class': ontology_class,
    }).values()

    ds = preprocess(**{
        'tokenizer': bert_tokenizer,
        'texts': texts_map,
        'annotations': annotations_map,
        'sequence_len': sequence_len,
    })

    print(f'Model: {model_conf["name"]}, Version: {model_conf["version"]}')
    model = build_model(**model_conf)
    outputs = postprocess(ds, [model.predict(s) for s in tqdm(ds, **tqdm_conf)], padding, density)

    with open(f'{output_path}/targets{model.name}.{model.version}.txt', 'w') as f:
        print(''.join([f'{o}' for c in ds for o in c['target_ids']]), file=f)

    with open(f'{output_path}/outputs{model.name}.{model.version}.txt', 'w') as f:
        print(''.join([f'{p}' for o in outputs for p in o["predicted"]]), file=f)
        
    output = [{
        'policy_hash': o['hash'],
        'starts_on': c[0]-1,
        'ends_on': c[1]+1,
        'selection_class': ontology_class,
        'selection_content': ''.join([f'{d}' for d in texts_map[o['hash']][c[0]:c[1]]])
    } for o in outputs for c in o['coords']]

    with open(f'{output_path}/annotations{model.name}.{model.version}.json', 'w') as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

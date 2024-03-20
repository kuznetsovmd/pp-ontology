from tqdm import tqdm


def build(builders, tqdm_conf, **kwargs):
    for b in tqdm(builders, desc='Builders', **tqdm_conf):
        b['func'](**b['args'])

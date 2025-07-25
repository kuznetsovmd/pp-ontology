import csv

from tqdm import tqdm


def save_query(path, out, res):
    with open(f"{path}/{out}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(res)


def exec(path, ontologies, queries, tqdm_conf, **kwargs):
    for q in tqdm(queries, desc='Queries', **tqdm_conf):
        save_query(path, *q(ontologies))

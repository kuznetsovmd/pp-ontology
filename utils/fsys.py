import csv
import re
from os import walk
from os.path import join

from config import QUERIES


def files(path, pattern):
    fs = []
    for (dir_path, _, file_names) in walk(path):
        fs.extend([join(dir_path, f) for f in file_names if re.match(pattern, f) is not None])
    return fs


def save_query(out, res):
    with open(f"{QUERIES}/{out}.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(res)

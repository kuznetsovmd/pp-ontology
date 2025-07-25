import re
from os import walk
from os.path import join


def files(path, pattern):
    fs = []
    for (dir_path, _, file_names) in walk(path):
        fs.extend([join(dir_path, f) for f in file_names if re.match(pattern, f) is not None])
    return fs
    
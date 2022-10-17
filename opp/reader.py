import csv
import json
import os
import re

from config import datasets
from tools.fsys import files
from tools.text import remove_strong, remove_br, remove_li, remove_ul, \
    remove_spec_chars, remove_spaces, remove_newlines


def clear_segment(text):
    segment_text = remove_strong(text)
    segment_text = remove_br(segment_text)
    segment_text = remove_li(segment_text)
    segment_text = remove_ul(segment_text)
    segment_text = remove_spec_chars(segment_text)
    segment_text = remove_spaces(segment_text)
    segment_text = remove_newlines(segment_text)
    segment_text = remove_spaces(segment_text)
    segment_text = segment_text.strip()
    return segment_text


def construct_annotations(reader, segments):
    return [
        {
            "category": row[5].strip(),
            "segment_text": segments[int(row[4])].strip(),
            "attributes": json.loads(row[6])
        }
        for row in reader
    ]


def construct_data(sanitized, annotated):
    id1 = re.match(r"^.*/(\d+)_.*$", sanitized).group(1)
    id2 = re.match(r"^.*/(\d+)_.*$", annotated).group(1)
    if id1 != id2:
        raise Exception(f"Ids of a files couple are not equal! {id1} != {id2}")

    name = re.match(r"^.*\d+_(.*)\.csv$", annotated).group(1)

    with open(sanitized) as f:
        segments_texts = [clear_segment(s) for s in f.read().split("|||")]

    with open(annotated, mode="r") as f:
        reader = csv.reader(f)
        annotations_records = construct_annotations(reader, segments_texts)

    return {
        "id": id1,
        "name": name,
        "annotations": annotations_records
    }


def read_opp():
    sanitized = files(os.path.join(datasets, "OPP-115/sanitized_policies"), r"(\d+)_.*")
    annotations = files(os.path.join(datasets, "OPP-115/consolidation/threshold-0.75"
                                               "-overlap-similarity"), r"(\d+)_.*")

    sanitized.sort()
    annotations.sort()

    couples = list(zip(sanitized, annotations))

    return [construct_data(*c) for c in couples]

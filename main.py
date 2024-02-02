#!/usr/bin/env python
import argparse
import sys

from tqdm import tqdm

from utils.fsys import save_query
from ontology2.queries.statistics import run as run1

from ontology2.classifier_builder.builder import build_classified
from ontology2.annotations_builder.builder import build_annotated
from ontology2.manual_builder.cloud_computing_policies.amazon_web_services import process_aws
from ontology2.manual_builder.cloud_computing_policies.google_cloud import process_google_cloud
from ontology2.manual_builder.cloud_computing_policies.threeplususa import process_3plususa
from ontology2.manual_builder.cloud_computing_policies.hpe import process_hpe
from ontology2.manual_builder.cloud_computing_policies.yandex import process_yandex
from ontology2.manual_builder.healthcare_policies.caresense import process_caresense
from ontology2.manual_builder.healthcare_policies.renpho import process_renpho
from ontology2.manual_builder.healthcare_policies.zepp import process_zepp
from ontology2.manual_builder.onto2_examples import process_onto_examples
from ontology2.manual_builder.onto2_blank import process_onto_blank
from ontology2.manual_builder.opp.builder import process_opp


def build_manual():
    (p() for p in tqdm([
        process_onto_blank,
        process_onto_examples,

        process_3plususa,
        process_aws,
        process_google_cloud,
        process_hpe,
        process_yandex,

        process_caresense,
        process_renpho,
        process_zepp,

        process_opp,
    ], desc='Builders', ncols=80, ascii=True))


def run_quries():
    (save_query(*q()) for q in tqdm([
        run1,
    ], desc='Queries', ncols=80, ascii=True))


def main(args):
    if args.cmd == 'manual':
        build_manual()
    if args.cmd == 'annotations':
        build_annotated()
    if args.cmd == 'classifier':
        build_classified(args.train, args.ltrain, args.eval)
    if args.cmd == 'queries':
        run_quries()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='privacy-ontology',
        description='Command line tool to control ontology framework'
    )

    parser.add_argument('cmd', help='One of: manual, annotations, classifier, queries')
    parser.add_argument('-e', '--eval', default=False, action='store_true')
    parser.add_argument('-l', '--ltrain', default=False, action='store_true')
    parser.add_argument('-t', '--train', default=False, action='store_true')
    args = parser.parse_args()

    try:
        main(args)
        sys.exit(0)
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(130)

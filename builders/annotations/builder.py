import json

from tqdm import tqdm

from utils.fsys import files
from ontology.interface import Ontology

from .annotation_scheme import get_manual_scheme
from .annotation_restrictions import get_manual_restrictions


class Builder:
    _id = 0
    objs = {}
    selections = []

    restrictions = get_manual_restrictions()
    attributes = {e['class']: e['attributeOf'] for e in get_manual_scheme()}
    subclasses = {e['class']: e['subclassOf'] for e in get_manual_scheme()}
    last_hash = None
    last_id = 0

    @classmethod
    def set_ontology(cls, ontology):
        cls.onto = ontology

    @classmethod
    def clear(cls):
        cls.objs = {}
        cls.selections = []
    
    @classmethod
    def get_activities(cls):
        activities = cls.get_subclasses('Activity')
        return [s for s in cls.selections if s.selection_class in activities]

    @classmethod
    def get_subclasses(cls, parent, tree=set()):
        tree.add(parent)
        for c, sub in cls.subclasses.items():
            if parent in sub:
                cls.get_subclasses(c, tree)
                tree.add(c)
        return tree

    @classmethod
    def resolve_property(cls, a_class, p_class):
        for k, v in cls.restrictions[p_class].items():
            if a_class in v:
                return k

    @classmethod
    def process_annotations(cls, onto, annotations, tqdm_conf):
        for a in annotations:
            cls(a)

        cls.set_ontology(onto)
        for a in tqdm(cls.get_activities(), desc='Annotations', **tqdm_conf):
            if a.hash != cls.last_hash:
                cls.last_id = 0
                cls.last_hash = a.hash
                cls.onto.new_policy(cls.last_hash)

            a.upload('previous_is', cls.last_id)
            cls.last_id = a.id
            for binded_activity in a.get_binded():
                binded_activity.upload('binded_to', a.id)

    def __init__(self, selection):
        self.id = Builder._id
        self.hash = selection['policy_hash']
        self.start = int(selection['starts_on'])
        self.end = int(selection['ends_on'])
        self.selection_content = selection['selection_content']
        self.selection_class = selection['selection_class']
        self.attribute_of = self.attributes[self.selection_class]
        self.selections.append(self)
        Builder._id += 1

    def get_properties(self):
        return [s for s in self.selections \
                    if ((self.start <= s.end and self.end >= s.start)) \
                        and self.selection_class in s.attribute_of \
                        and s.hash == s.last_hash]
    
    def get_binded(self):
        activities = self.get_subclasses('Activity')
        return [s for s in self.selections \
                    if ((self.start <= s.end and self.end >= s.start)) \
                        and s.selection_class in activities \
                        and s.id not in self.objs \
                        and s.hash == s.last_hash]

    def get_users(self):
        return [s for s in self.selections \
                    if ((self.start <= s.end and self.end >= s.start)) \
                        and s.selection_class == 'User' \
                        and s.id not in self.objs \
                        and s.hash == s.last_hash]

    def upload(self, relation, idx):

        if self.id in self.objs:
            return

        us = self.get_users()
        for u in us:
            if u.id in self.objs:
                continue
            self.objs[u.id] = self.onto.individual(u.selection_class, u.selection_content)

        ps = self.get_properties()
        for p in ps:
            if p.id in self.objs:
                continue

            if p.selection_class in self.get_subclasses('Data'):
                provided = [self.onto.property('provided_by', self.objs[u.id]) for u in us]
                self.objs[p.id] = self.onto.individual(p.selection_class, p.selection_content, provided)
                continue

            self.objs[p.id] = self.onto.individual(p.selection_class, p.selection_content)

        properties = [self.onto.property(relation, self.objs[idx])] if idx else []
        for p in ps:
            if pn := self.resolve_property(self.selection_class, p.selection_class):
                properties.append(self.onto.property(pn, self.objs[p.id]))

        self.objs[self.id] = self.onto.individual(self.selection_class, self.selection_content, properties)


def build(annotations, path, name, tqdm_conf, **kwargs):
    fs = files(annotations, r'.*\.json')
    
    annotations_list = []
    for file in fs:
        with open(file, 'r') as f:
            annotations_list.extend(json.load(f))

    onto = Ontology(path=path, name=f'{name}-summary', create_root_policy=False)
    Builder.process_annotations(onto, annotations_list, tqdm_conf)
    Builder.clear()
    onto.save()

    hashes = sorted(set(a['policy_hash'] for a in annotations_list))
    annotations_map = {}
    for h in hashes:
        annotations_map[h] = []
        for a in annotations_list:
            if a['policy_hash'] == h:
                annotations_map[h].append(a)

    del annotations_list

    for h in hashes:
        onto = Ontology(path=path, name=f'{name}-{h}', create_root_policy=False)
        Builder.process_annotations(onto, annotations_map[h], tqdm_conf)
        Builder.clear()
        onto.save()

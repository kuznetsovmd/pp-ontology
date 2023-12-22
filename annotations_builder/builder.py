import json

from ontology2.ontology.interface import Ontology as Ontology2

from annotations_builder.annotation_structures import SCHEME, RESTRICTIONS


class Builder:
    objs = {}
    selections = []
    attributes = {e['class']: e['attributeOf'] for e in SCHEME}
    subclasses = {e['class']: e['subclassOf'] for e in SCHEME}
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
    def get_subclasses(self, parent, tree=set()):
        tree.add(parent)
        for cls, sub in self.subclasses.items():
            if parent in sub:
                self.get_subclasses(cls, tree)
                tree.add(cls)
        return tree

    @classmethod
    def resolve_property(cls, a_class, p_class):
        for k, v in RESTRICTIONS[p_class].items():
            if a_class in v:
                return k

    def __init__(self, selection) -> None:
        self.id = int(selection['id'])
        self.hash = selection['policy_hash']
        self.start = int(selection['starts_on'])
        self.end = int(selection['ends_on'])
        self.selection_content = selection['selection_content']
        self.selection_class = selection['selection_class']
        self.attribute_of = self.attributes[self.selection_class]
        self.selections.append(self)

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
                self.objs[p.id] = self.onto.individual(
                    p.selection_class, p.selection_content, 
                    [self.onto.property('provided_by', self.objs[u.id]) for u in us]
                )
            else:
                self.objs[p.id] = self.onto.individual(p.selection_class, p.selection_content)

        properties = [self.onto.property(relation, self.objs[idx])] if idx else []
        for p in ps:
            if pn := self.resolve_property(self.selection_class, p.selection_class):
                properties.append(self.onto.property(pn, self.objs[p.id]))

        self.objs[self.id] = self.onto.individual(self.selection_class, self.selection_content, properties)


# DO NOT FORGET ABOUT CLASSIFIER OUTPUT
def read(file, out='test'):
    with open(file, 'r', encoding='utf-8') as f:
        records = json.load(f)
        for r in records:
            Builder(r)

    onto = Ontology2(out, create_root_policy=False)
    Builder.set_ontology(onto)

    for a in Builder.get_activities():
        
        if a.hash != Builder.last_hash:
            Builder.last_id = 0
            Builder.last_hash = a.hash
            Builder.onto.new_policy(Builder.last_hash)

        a.upload('previous_is', Builder.last_id)
        Builder.last_id = a.id
        for binded_activity in a.get_binded():
            binded_activity.upload('binded_to', a.id)

    onto.save()


if __name__ == '__main__':
    read('resources/70e376c538cfcbdbf9b66708a25e6f31.json')

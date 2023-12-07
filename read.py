import json
from ontology2.interface import Ontology as Ontology2

from annotation_structures import SCHEME, RESTRICTIONS


class Selection:
    objs = {}
    selections = []
    attributes = {e['class']: e['attributeOf'] for e in SCHEME}
    subclasses = {e['class']: e['subclassOf'] for e in SCHEME}

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
        self.start = int(selection['starts_on'])
        self.end = int(selection['ends_on'])
        self.selection_content = selection['selection_content']
        self.selection_class = selection['selection_class']
        self.attribute_of = self.attributes[self.selection_class]
        self.selections.append(self)

    def get_properties(self):
        return [s for s in self.selections \
                    if ((self.start <= s.end and self.end >= s.start)) \
                        and self.selection_class in s.attribute_of]
    
    def get_binded(self):
        activities = self.get_subclasses('Activity')
        return [s for s in self.selections \
                    if ((self.start <= s.end and self.end >= s.start)) \
                        and s.selection_class in activities \
                        and s.id not in self.objs]

    def get_users(self):
        return [s for s in self.selections \
                    if ((self.start <= s.end and self.end >= s.start)) \
                        and s.selection_class == 'User' \
                        and s.id not in self.objs]

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
                self.objs[p.id] = self.onto.individual(p.selection_class, p.selection_content, 
                    [self.onto.property('provided_by', self.objs[u.id]) for u in us])
            else:
                self.objs[p.id] = self.onto.individual(p.selection_class, p.selection_content)

        properties = [self.onto.property(relation, self.objs[idx])] if idx else []
        for p in ps:
            if pn := self.resolve_property(self.selection_class, p.selection_class):
                properties.append(self.onto.property(pn, self.objs[p.id]))

        self.objs[self.id] = self.onto.individual(self.selection_class, self.selection_content, properties)


def read(file='resources/8ccc769eff799819795af54253ea82b1.json'):
    with open(file, 'r', encoding='utf-8') as f:
        records = json.load(f)
        for r in records:
            Selection(r)


def ontology(name='first_annotation'):
    onto = Ontology2(name)
    Selection.set_ontology(onto)

    # RESET previous_id FOR DIFFERENT ONTOLOGIES
    previous_id = 0
    for a in Selection.get_activities():
            a.upload('previous_is', previous_id)
            previous_id = a.id
            for binded_activity in a.get_binded():
                binded_activity.upload('binded_to', a.id)

    onto.save()


def text(file='resources/output.txt'):
    with open(file, 'w', encoding='utf-8') as w:
        for leading_activity in Selection.get_activities():
            w.write(f'NEW ACTIVITY -> {leading_activity.selection_class} id: {leading_activity.id} '
                    f'({leading_activity.start}, {leading_activity.end})\n')

            if leading_activity.id not in Selection.objs:
                Selection.objs[leading_activity.id] = object()
                w.write(f'{" " * 4}CONTENT -> {leading_activity.selection_content}\n')

                properties = leading_activity.get_properties()
                for p in properties:
                    w.write(f'{" " * 8}PROPERTY -> {p.selection_class} id: {p.id} -> {p.selection_content}\n')

                for binded_activity in leading_activity.get_binded():
                    w.write(f'BINDED ACTIVITY -> {binded_activity.selection_class} id: {binded_activity.id} '
                            f'({binded_activity.start}, {binded_activity.end})\n')
                    
                    if binded_activity.id not in Selection.objs:
                        Selection.objs[binded_activity.id] = object()
                        w.write(f'{" " * 4}CONTENT -> {binded_activity.selection_content}\n')
                        
                        for p in binded_activity.get_properties():
                            w.write(f'{" " * 8}PROPERTY -> {p.selection_class} id: {p.id} -> {p.selection_content}\n')
                    else:
                        w.write(f'{" " * 4}ALREADY ANALYZED\n')
            else:
                w.write(f'{" " * 4}ALREADY ANALYZED\n')
            w.write(f'\n\n')


if __name__ == '__main__':
    read()
    ontology()
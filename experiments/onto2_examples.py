from ontology2.interface import Ontology


def process_onto2_test():

    o = Ontology('test', 'some url')


    # u = o.individual('User')

    # o.individual(

    #     'Notification',

    #     binds=[
    #         o.property('initiated_by', u),
    #         o.property('has_mechanism', o.individual('CommunicationMechanism')),
    #     ]
    # )


    fp = o.individual('Agent')

    o.individual(

        'Retention',

        binds=[
            o.property('initiated_by', fp),
            o.property('has_mechanism', o.individual('DataRetentionMechanism')),
        ]
    )

    o.save()

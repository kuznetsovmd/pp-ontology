from ontology2.interface import Ontology


def process_onto2_test():

    o = Ontology('test', 'some url')

    # u = o.individual('Agent')

    # o.individual(

    #     'Notification',

    #     binds=[
    #         o.property('initiated_by', u),
    #         o.property('has_mechanism', o.individual('CommunicationMechanism')),
    #     ]
    # )

    fp = o.individual('FirstParty')
    u = o.individual('User')
    tp = o.individual('ThirdParty')

    o.individual(

        'FPCollection',

        binds=[
            o.property('initiated_by', fp),
            o.property('collects', u),
            o.property('has_mechanism', o.individual('Email')),
        ]
    )

    o.individual(

        'UserNotification',

        binds=[
            o.property('initiated_by', u),
            o.property('notifies', fp),
            o.property('has_mechanism', o.individual('Email')),
        ]
    )

    o.individual(

        'FPNotification',

        binds=[
            o.property('initiated_by', fp),
            o.property('notifies', u),
            o.property('has_mechanism', o.individual('Email')),
        ]
    )

    # fp = o.individual('Criminal')

    # o.individual(

    #     'Activity',

    #     binds=[
    #         o.property('initiated_by', fp),
    #         o.property('has_mechanism', o.individual('PersonalVisit')),
    #     ]
    # )

    o.save()

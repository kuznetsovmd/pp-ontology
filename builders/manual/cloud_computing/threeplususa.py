from ontology.interface import Ontology


def build(**kwargs):
    """
    In order to be in line with Fair Information Practices, 
    should a data breach occur, we will notify users via email 
    within seven (7) business days.
    """

    o = Ontology(**kwargs, website='https://3plususa.com')

    user = o.individual('User', 'you')
    first_party = o.individual('FirstParty', 'we')

    b = o.individual(

        'DataBreachProcessing',

        "In order to be in line with Fair Information Practices, " \
        "should a data breach occur.",

        [
            o.property('initiated_by', first_party),

            o.property('caused_by', o.individual(
                'DataBreach'
            )),
        ]
    )

    n = o.individual(

        'FPNotification',

        "we will notify users via email " \
        "within seven (7) business days.",

        [
            o.property('initiated_by', first_party),
            o.property('notifies', user),
            o.property('lasts_for', o.individual(
                'NotificationTime',
                'within seven (7) business days'
            )),
            o.property('has_mechanism', o.individual(
                'Email',
                'we will notify users via email'
            )),
            
            o.property('binded_to', b)
        ]
    )

    o.save()

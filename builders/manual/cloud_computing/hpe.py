from ontology.interface import Ontology


def build(**kwargs):
    """
    If we modify this Privacy Statement, we will publish a revised 
    version with an updated revision date. The privacy link on 
    the footer of every HPE web page will then point to that new version.
    """

    o = Ontology(**kwargs, website='https://www.hpe.com')

    user = o.individual('User', 'you')
    first_party = o.individual('FirstParty', 'we')

    b = o.individual(

        'PolicyChange',

        "If we modify this Privacy Statement, we will publish a revised " \
        "version with an updated revision date. The privacy link on "\
        "the footer of every HPE web page will then point to that new version.",

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                binds=[o.property('provided_by', user)])),

            o.property('caused_by', o.individual(
                'PolicyChangeCause'
            )),
        ]
    )

    o.individual(

        'FPNotification',

        "we will publish a revised " \
        "version with an updated revision date.",

        [
            o.property('initiated_by', first_party),
            o.property('notifies', user),
            o.property('lasts_for', o.individual(
                'NotificationTime',
            )),
            o.property('has_mechanism', o.individual(
                'Email',
                'we will notify users via email'
            )),
            
            o.property('binded_to', b)
        ]
    )

    o.save()

from ontology.interface import Ontology


def build(**kwargs):

    o = Ontology(**kwargs, website='https://cloud.google.com')

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'we')

    pc = o.individual(

        'PolicyChange',

        "We may update this Privacy Notice from time to time. We "
        "will not make any significant changes without notifying "
        "you in advance by posting a prominent notice on this page "
        "describing the changes or by sending you a direct "
        "communication. We encourage you to regularly review this "
        "Privacy Notice, and we will always indicate the date the "
        "last changes were published.",

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual('Data', properties=[
                o.property('proveded_by', user)
            ])),

            o.property('caused_by', o.individual(
                'PolicyChangeCause'
            )),

            o.property('lasts_for', o.individual(
                'PolicyAcceptanceTime'
            )),
        ]
    )

    n = o.individual(

        'FPNotification',

        "You should check our website frequently to see " \
        "recent changes.",

        [
            o.property('initiated_by', first_party),

            o.property('notifies', user),

            o.property('has_mechanism', o.individual(
                'OnWebsitePage',
                'by posting a prominent notice on this page'
            )),

            o.property('has_mechanism', o.individual(
                'GeneralCommunicationMechanism',
                'sending you a direct communication.'
            )),

            o.property('binded_to', pc),
        ]
    )

    o.save()


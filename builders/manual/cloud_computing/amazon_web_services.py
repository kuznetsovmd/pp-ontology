from ontology.interface import Ontology


def build(**kwargs):
    """
    Our business changes constantly, and our Privacy Notice may
    also change. You should check our website frequently to see
    recent changes. You can see the date on which the latest
    version of this Privacy Notice was posted. Unless stated
    otherwise, our current Privacy Notice applies to all
    personal information we have about you and your account.
    We stand behind the promises we make, however, and will
    never materially change our policies and practices to make
    them less protective of personal information collected in
    the past without informing affected customers and giving
    them a choice.
    """

    o = Ontology(**kwargs, website='https://aws.amazon.com')

    user = o.individual('User', 'you')
    first_party = o.individual('FirstParty', 'we')

    data = o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])

    pc = o.individual(

        'PolicyChange',

        "Our business changes constantly, and our Privacy Notice may "
        "also change. You should check our website frequently to see "
        "recent changes. You can see the date on which the latest "
        "version of this Privacy Notice was posted. Unless stated "
        "otherwise, our current Privacy Notice applies to all "
        "personal information we have about you and your account.",

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', data),

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
                'check our website frequently'
            )),

            o.property('binded_to', pc),
        ]
    )

    ca = o.individual(

        'OptInOptOutControl',

        "We stand behind the promises we make, however, and will "
        "never materially change our policies and practices to make "
        "them less protective of personal information collected in "
        "the past without informing affected customers and giving "
        "them a choice.",

        [
            o.property('initiated_by', user),

            o.property('applies_to', data),

            o.property('binded_to', pc),
        ]
    )

    o.save()

from ontology.interface import Ontology


def build(**kwargs):
    """
    This Policy may be subject to amendments. Yandex shall be entitled 
    to make such amendments at its own discretion, including, without 
    limitation, to reflect changes in applicable legislation or amendments 
    to the Sites and/or Services. Yandex undertakes not to introduce 
    significant changes, imposing additional obligations or reducing your 
    rights under this Policy without proper notice to you. You will be 
    notified about such changes. If applicable, changes will be announced 
    on the Site or Services (e.g. via a pop-up or web banner) prior to 
    such changes taking effect, and you may also be notified via other 
    channels (e.g. by email) if you have provided us with your contact 
    details.
    """

    o = Ontology(**kwargs, website='https://yandex.ru')

    user = o.individual('User', 'you')
    first_party = o.individual('FirstParty', 'Yandex')

    b = o.individual(

        'PolicyChange',

        "This Policy may be subject to amendments. Yandex shall be entitled " \
        "to make such amendments at its own discretion, including, without " \
        "limitation, to reflect changes in applicable legislation or amendments " \
        "to the Sites and/or Services. Yandex undertakes not to introduce " \
        "significant changes, imposing additional obligations or reducing your " \
        "rights under this Policy without proper notice to you.",

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

        "You will be notified about such changes. If applicable, changes will be announced " \
        "on the Site or Services (e.g. via a pop-up or web banner) prior to " \
        "such changes taking effect, and you may also be notified via other " \
        "channels (e.g. by email) if you have provided us with your contact " \
        "details.",

        [
            o.property('initiated_by', first_party),
            o.property('notifies', user),
            o.property('lasts_for', o.individual(
                'NotificationTime',
            )),
            o.property('has_mechanism', o.individual(
                'OnWebsitePage',
                "If applicable, changes will be announced on the Site"
            )),
            o.property('has_mechanism', o.individual(
                'OnServiceApp',
                'or Services (e.g. via a pop-up or web banner'
            )),
            o.property('has_mechanism', o.individual(
                'Email',
                "and you may also be notified via other channels (e.g. by email) " \
                "if you have provided us with your contact details."
            )),
            
            o.property('binded_to', b)
        ]
    )

    o.save()

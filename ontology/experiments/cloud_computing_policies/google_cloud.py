def process_google_cloud(onto):
    """
    https://cloud.google.com/terms/cloud-privacy-notice
    Effective Date: April 20, 2022
    Updates to this Notice
    We may update this Privacy Notice from time to time. We will not make any
    significant changes without notifying you in advance by posting a prominent notice
    on this page describing the changes or by sending you a direct communication. We
    encourage you to regularly review this Privacy Notice, and we will always indicate
    the date the last changes were published.
    """
    user = onto.User()
    first_party = onto.FirstParty()
    third_party = onto.ThirdParties()

    policy_instance = onto.PrivacyPolicy()
    policy_instance.policyWebsite = "https://cloud.google.com"
    policy_instance.considersAgent.extend([user, first_party, third_party])

    policychangeactivity = onto.PolicyChangeActivity()
    e1 = onto.Evidence("evidence1")
    e1.evidenceContent = "We may update this Privacy Notice from time to time. We " \
                         "will not make any significant changes without notifying " \
                         "you in advance by posting a prominent notice on this page " \
                         "describing the changes or by sending you a direct " \
                         "communication. We encourage you to regularly review this " \
                         "Privacy Notice, and we will always indicate the date the " \
                         "last changes were published."
    policychangeactivity.hasEvidence.append(e1)

    inprivacypolicy = onto.InPrivacyPolicy("inprivacypolicy")
    e2 = onto.Evidence("evidence2")
    e2.evidenceContent = "posting a prominent notice on this page"
    inprivacypolicy.hasEvidence.append(e2)

    notificationmechanism = onto.NotificationMechanism("notificationmechanism")
    e3 = onto.Evidence("evidence3")
    e3.evidenceContent = "sending you a direct communication"
    notificationmechanism.hasEvidence.append(e3)

    policychangecause = onto.PolicyChangeCause("policychangecause")
    e4 = onto.Evidence("evidence4")
    e4.evidenceContent = "Not defined"
    policychangecause.hasEvidence.append(e4)

    policyacceptancetime = onto.PolicyAcceptanceTime("policyacceptancetime")
    e5 = onto.Evidence("evidence5")
    e5.evidenceContent = "Not defined"
    policyacceptancetime.hasEvidence.append(e5)

    policychangeactivity.hasMechanism.append(inprivacypolicy)
    policychangeactivity.hasMechanism.append(notificationmechanism)
    policychangeactivity.hasPolicyChangeCause.append(policychangecause)
    policychangeactivity.hasPolicyAcceptanceTime.append(policyacceptancetime)
    policy_instance.considersActivity.append(policychangeactivity)
    first_party.initiatesActivity.append(policychangeactivity)

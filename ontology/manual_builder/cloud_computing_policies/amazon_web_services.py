

def process_aws(onto):
    """
    https://aws.amazon.com/ru/privacy/
    Our business changes constantly, and our Privacy Notice may also change. You should
    check our website frequently to see recent changes. You can see the date on which
    the latest version of this Privacy Notice was posted. Unless stated otherwise, our
    current Privacy Notice applies to all personal information we have about you and
    your account. We stand behind the promises we make, however, and will never
    materially change our policies and practices to make them less protective of
    personal information collected in the past without informing affected customers and
    giving them a choice.
    """
    user = onto.User()
    first_party = onto.FirstParty()
    third_party = onto.ThirdParties()

    policy_instance = onto.PrivacyPolicy()
    policy_instance.policyWebsite = "https://aws.amazon.com"
    policy_instance.considersAgent.extend([user, first_party, third_party])

    policychangeactivity = onto.PolicyChangeActivity()
    e1 = onto.Evidence("evidence1")
    e1.evidenceContent = "Our business changes constantly, and our Privacy Notice may " \
                         "also change. You should check our website frequently to see " \
                         "recent changes. You can see the date on which the latest " \
                         "version of this Privacy Notice was posted. Unless stated " \
                         "otherwise, our current Privacy Notice applies to all " \
                         "personal information we have about you and your account. " \
                         "We stand behind the promises we make, however, and will " \
                         "never materially change our policies and practices to make " \
                         "them less protective of personal information collected in " \
                         "the past without informing affected customers and giving " \
                         "them a choice."
    policychangeactivity.hasEvidence.append(e1)

    inprivacypolicy = onto.InPrivacyPolicy("inprivacypolicy")
    e2 = onto.Evidence("evidence2")
    e2.evidenceContent = "You should check our website frequently to see recent changes."
    inprivacypolicy.hasEvidence.append(e2)

    policychangecause = onto.PolicyChangeCause("policychangecause")
    e3 = onto.Evidence("evidence3")
    e3.evidenceContent = "Not defined"
    policychangecause.hasEvidence.append(e3)

    policyacceptancetime = onto.PolicyAcceptanceTime("policyacceptancetime")
    e4 = onto.Evidence("evidence4")
    e4.evidenceContent = "Not defined"
    policyacceptancetime.hasEvidence.append(e4)

    consentactivity = onto.ConsentActivity("consentactivity")
    e5 = onto.Evidence("evidence5")
    e5.evidenceContent = "giving them a choice"
    consentactivity.hasEvidence.append(e5)

    policychangeactivity.hasMechanism.append(inprivacypolicy)
    policychangeactivity.hasPolicyChangeCause.append(policychangecause)
    policychangeactivity.hasPolicyAcceptanceTime.append(policyacceptancetime)
    policy_instance.considersActivity.append(policychangeactivity)
    policy_instance.considersActivity.append(consentactivity)
    first_party.initiatesActivity.append(policychangeactivity)
    user.initiatesActivity.append(consentactivity)

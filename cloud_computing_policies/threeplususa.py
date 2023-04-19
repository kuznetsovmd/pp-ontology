

def process_3plususa(onto):

    user = onto.User()
    first_party = onto.FirstParty()
    third_party = onto.ThirdParties()

    policy_instance = onto.PrivacyPolicy()
    policy_instance.policyWebsite = "https://3plususa.com"
    policy_instance.considersAgent.extend([user, first_party, third_party])

    breachnotificationactivity = onto.ReportBreachActivity()
    e1 = onto.Evidence("evidence1")
    e1.evidenceContent = "In order to be in line with Fair Information Practices, " \
                         "should a data breach occur, we will notify users via email " \
                         "within seven (7) business days."
    breachnotificationactivity.hasEvidence.append(e1)

    viaemail = onto.ViaEmail("viaemail")
    e2 = onto.Evidence("evidence2")
    e2.evidenceContent = "we will notify users via email"
    viaemail.hasEvidence.append(e2)

    breachcause = onto.BreachCause("breachcause")
    e3 = onto.Evidence("evidence3")
    e3.evidenceContent = "Not defined"
    breachcause.hasEvidence.append(e3)

    breachnotificationtime = onto.BreachNotificationTime("breachnotificationtime")
    e4 = onto.Evidence("evidence4")
    e4.evidenceContent = "within seven (7) business days"
    breachnotificationtime.hasEvidence.append(e4)

    breachnotificationactivity.hasMechanism.append(viaemail)
    breachnotificationactivity.hasBreachCause.append(breachcause)
    breachnotificationactivity.hasBreachReportTime.append(breachnotificationtime)
    policy_instance.considersActivity.append(breachnotificationactivity)
    first_party.initiatesActivity.append(breachnotificationactivity)

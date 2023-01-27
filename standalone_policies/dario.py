

def process_dario(onto):

    user = onto.User()
    first_party = onto.FirstParty()
    third_party = onto.ThirdParties()

    policy_instance = onto.PrivacyPolicy()
    policy_instance.policyWebsite = "https://mydario.com/privacy-policy"
    policy_instance.considersAgent.extend([user, first_party, third_party])


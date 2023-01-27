from tools.ontology_helpers import make


def process_zepp(onto):

    user = onto.User()
    first_party = onto.FirstParty()
    third_party = onto.ThirdParties()

    policy_instance = onto.PrivacyPolicy()
    policy_instance.policyWebsite = "https://upload-cdn.huami.com/tposts/8191"
    policy_instance.considersAgent.extend([user, first_party, third_party])




    #########################################################################
    #                                                                       #
    # OUR COMMITMENT TO YOU                                                 #
    #                                                                       #
    #########################################################################




    #########################################################################
    # The Privacy Policy is designed with you in mind, and it is important that you have a comprehensive understanding of and confidence in our personal information collection and usage practices of any personal information provided to us.

    make(onto, "DataActivity",
        evidence="The Privacy Policy is designed with you in mind, and it is important that you have a comprehensive understanding of and confidence in our personal information collection and usage practices of any personal information provided to us.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # We are committed to protecting the privacy, confidentiality and security of your personal information by complying with applicable laws. We are equally committed to ensuring that all our employees and agents uphold these obligations.

    make(onto, "DataActivity",
        evidence="We are committed to protecting the privacy, confidentiality and security of your personal information by complying with applicable laws. We are equally committed to ensuring that all our employees and agents uphold these obligations.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "SecurityMechanism",
                evidence="We are committed to protecting the privacy")),
            ("hasSecurityMechanism", make(onto, "SecurityMechanism",
                evidence="We are equally committed to ensuring that all our employees and agents uphold these obligations.")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="by complying with applicable laws.")),
        )
    )




    #########################################################################
    #                                                                       #
    # TRANSPARENCY: WHAT INFORMATION IS COLLECTED AND HOW WE USE IT         #
    #                                                                       #
    #########################################################################




    #########################################################################
    # The categories of personal information we may collect (directly from you or from third party sources) and our privacy practices depend on the nature of the relationship you have with us and the requirements of applicable law. Some of the ways that we may collect personal information include: You may provide personal information directly to us through interacting with our products and services, or requesting services or information from us. As you navigate the services, certain information may also be collected automatically, including through cookies and similar technologies as described below.

    make(onto, "DataCollectionActivity",
        evidence="The categories of personal information we may collect (directly from you or from third party sources) and our privacy practices depend on the nature of the relationship you have with us and the requirements of applicable law. As you navigate the services, certain information may also be collected automatically, including through cookies and similar technologies as described below.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="cookies and similar technologies",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="requirements of applicable law")),
        )
    )




    #########################################################################
    # We endeavor to collect only that information which is relevant for the purposes of processing.

    make(onto, "DataCollectionActivity",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="for the purposes of processing")),
        )
    )




    #########################################################################
    #                                                                       #
    # TYPES OF INFORMATION COLLECTED                                        #
    #                                                                       #
    #########################################################################




    #########################################################################
    # Information You Provide Directly to Us. When you use our services or engage in certain activities, such as registering for an account, responding to surveys, requesting services or information, requesting customer or technical support, or contacting us directly, we may ask you to provide certain personal information, such as email address or phone number.

    make(onto, "DataCollectionActivity",
        evidence="we may ask you to provide certain personal information, such as email address or phone number.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="email address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="phone number",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Automatic Data Collection. We may collect certain information automatically through our products, services or other methods of analysis, such as your Internet protocol (IP) address, cookie identifiers, mobile carrier, MAC address and other device identifiers that are automatically assigned to device when you access the Internet, hardware type, device name, operating system, system version, region & language, installation package name, App version, network status, source of App, device battery, Bluetooth status, Internet service provider, the usage of product and App features, pages that you visit before and after using the services, the date and time of your visit, the amount of time you spend on each page, information about the links you click and pages you view within the services, and other actions taken through use of the services such as preferences.

    make(onto, "DataCollectionActivity",
        evidence="We may collect certain information automatically through our products, services or other methods of analysis, such as your Internet protocol (IP) address, cookie identifiers, mobile carrier, MAC address and other device identifiers that are automatically assigned to device when you access the Internet, hardware type, device name, operating system, system version, region & language, installation package name, App version, network status, source of App, device battery, Bluetooth status, Internet service provider, the usage of product and App features, pages that you visit before and after using the services, the date and time of your visit, the amount of time you spend on each page, information about the links you click and pages you view within the services, and other actions taken through use of the services such as preferences.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="Internet protocol (IP) address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="cookie identifiers",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="mobile carrier",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="MAC address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="other device identifiers",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="hardware type",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="device name",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="operating system",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="system version",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="region & language",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="installation package name",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="App version",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="network status",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="source of App",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="device battery",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="Bluetooth status",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="Internet service provider",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="the usage of product and App features",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="pages that you visit before and after using the services",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="the date and time of your visit",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="the amount of time you spend on each page",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="information about the links you click",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="pages you view within the services",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="other actions taken through use of the services such as preferences.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Specific Information Collected Through Our Products and Services. We have a wide range of products, the personal information collected by different products may vary. We may collect the following types of information (which may or may not be personal information):

    make(onto, "DataCollectionActivity",
        evidence="We have a wide range of products, the personal information collected by different products may vary. We may collect the following types of information (which may or may not be personal information):",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="types of information (which may or may not be personal information)",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Information about You: When you register for an account or log into our service using your credentials from your Mi, WeChat, Google, Line or Facebook accounts (with your approval), we may collect and use your avatar, gender, country, email address, nicknames, time zones, languages, regions, birthday, height, weight.

    make(onto, "DataCollectionActivity",
        evidence="When you register for an account or log into our service using your credentials from your Mi, WeChat, Google, Line or Facebook accounts (with your approval), we may collect and use your avatar, gender, country, email address, nicknames, time zones, languages, regions, birthday, height, weight.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "AccountData",
                evidence="your credentials from your Mi, WeChat, Google, Line or Facebook accounts",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="avatar",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="gender",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="country",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="email address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="nicknames",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="time zones",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="languages",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="regions",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="birthday",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="height",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="weight",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Online Purchase Information. If you place an order with us, we will record the personal information and details associated with the transaction. We will collect your purchase/subscription information, such as, user ID, items purchased, order ID, payment information for fulling your order. Any payments made via the Services are processed by third-party payment processors. We do not directly collect or store your payment card information, which is handled by third-party service providers.

    make(onto, "DataCollectionActivity",
        evidence="If you place an order with us, we will record the personal information and details associated with the transaction. We will collect your purchase/subscription information, such as, user ID, items purchased, order ID, payment information for fulling your order. Any payments made via the Services are processed by third-party payment processors.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "FinancialData",
                evidence="details associated with the transaction",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "FinancialData",
                evidence="purchase/subscription information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="user ID",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="items purchased",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="order ID",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "FinancialData",
                evidence="payment information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="for fulling your order.")),
        )
    )

    # doesnt
    make(onto, "DataCollectionActivity",
        evidence="We do not directly collect or store your payment card information, which is handled by third-party service providers.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "FinancialData",
                evidence="not collect payment card information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Personal Body and Health Information: When you use Zepp App and our device, your personal body and health information may be collected, such as, heart rate, resting heart rate, heart rate zone, maximum heart rate, minimum heart rate, average heart rate, blood oxygen saturation, stress, PAI, PPG data, ECG data, weight, body fat, BMI.

    make(onto, "DataCollectionActivity",
        evidence="When you use Zepp App and our device, your personal body and health information may be collected, such as, heart rate, resting heart rate, heart rate zone, maximum heart rate, minimum heart rate, average heart rate, blood oxygen saturation, stress, PAI, PPG data, ECG data, weight, body fat, BMI.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="your personal body and health information may be collected",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="heart rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="resting heart rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="heart rate zone",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="maximum heart rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="minimum heart rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="average heart rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="blood oxygen saturation",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="stress",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="PAI",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="PPG data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="ECG data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="weight",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="body fat",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="BMI",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Exercising Information: When you use the Zepp App and our device for exercising, we may collect your exercising information, such as, steps, stand-up times, total distance, time, total time, total duration, burned calories, consumption, pace, speed, frequency, stride length, maximum oxygen uptake(VO2 Max), exercise capacity, training effects, sports loading, frequency of exercising, strokes, stroke rate, number of trips, number of jumping rope, average stroke distance, movement track, velocity, swolf index, stroke speed and number of floors climbed.

    make(onto, "DataCollectionActivity",
        evidence="Exercising Information: When you use the Zepp App and our device for exercising, we may collect your exercising information, such as, steps, stand-up times, total distance, time, total time, total duration, burned calories, consumption, pace, speed, frequency, stride length, maximum oxygen uptake(VO2 Max), exercise capacity, training effects, sports loading, frequency of exercising, strokes, stroke rate, number of trips, number of jumping rope, average stroke distance, movement track, velocity, swolf index, stroke speed and number of floors climbed.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="exercising information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="steps",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="stand-up times",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="total distance",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="time",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="total time",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="total duration",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="burned calories",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="consumption",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="pace",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="speed",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="frequency of exercising",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="strokes",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="stroke rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="number of trips",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="number of jumping rope",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="average stroke distance",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="movement track",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="velocity",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="swolf index",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="stroke speed",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="number of floors climbed.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Information Recorded by Your Device: When you use the Zepp App to synchronize device data, personal data is recorded. For example, altitude, air pressure, temperature, weather type, volume of earphone, ambient sound, sleep data, rapid eye movement(REM), activity information, the time length of one-legged standing with eyes closed testing and the time of measuring, resistance value.

    make(onto, "DataCollectionActivity",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="altitude",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="air pressure",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="temperature",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="weather type",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="volume of earphone",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="ambient sound",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="sleep data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="rapid eye movement(REM)",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="activity information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="the time length of one-legged standing with eyes closed testing and the time of measuring",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="resistance value.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Device Setting Information: We may collect information of your device settings. For example, status of notification, unit settings, dial layout settings, gesture settings, band wearing settings.

    make(onto, "DataCollectionActivity",
        evidence="We may collect information of your device settings. For example, status of notification, unit settings, dial layout settings, gesture settings, band wearing settings.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="information of your device settings",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="status of notification",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="unit settings",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="dial layout settings",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="gesture settings",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="band wearing settings.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Application Setting Information: We may collect information of your device settings on applications. For example, device system setting, exercising functional setting, target of steps, target of exercising, target of weight, target of calories, target of sleep, alarm settings. 

    make(onto, "DataCollectionActivity",
        evidence="information of your device settings on applications",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="device system setting on applications.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="exercising functional setting",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="target of steps",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="target of exercising",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="target of weight",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="target of calories",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="target of sleep",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="alarm settings.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Caller Information: When you use the Incoming Call or SMS Alert functions, you will receive an alert about your phone calls, SMS. Your contact information for incoming calls and messages will be synchronized to and displayed on the bundled device. We will not save your caller information in Zepp App or sever.

    make(onto, "DataCollectionActivity",
        evidence="We will not save your caller information in Zepp App or sever.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="not caller information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Network Usage Information: We may collect network types, network signals, WLAN information and other similar information related to certain features of the Zepp App.

    make(onto, "DataCollectionActivity",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="network types",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="network signals",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="WLAN information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="other similar information related to certain features of the Zepp App.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Music Information: When you use music or music control function, the music information (e.g., name of song, singer, the status of song) will be obtained from your mobile phone and synchronized to the device. This information will only be displayed on the device screen and we will not save this information. When you use the music storage function (only supported by certain devices), then your music will be synchronized to and stored in the device.

    make(onto, "DataCollectionActivity",
        evidence="When you use music or music control function, the music information (e.g., name of song, singer, the status of song) will be obtained from your mobile phone and synchronized to the device. This information will only be displayed on the device screen and we will not save this information.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="not the music information (e.g., name of song, singer, the status of song)",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Log Information: We may record some log information when you use the Zepp App. For example, we may collect operating information, hit log, firmware clicking statistics, and server log. When you give us feedback, at your option, your app log and device log will be collected by us.

    make(onto, "DataCollectionActivity",
        evidence="We may record some log information when you use the Zepp App. For example, we may collect operating information, hit log, firmware clicking statistics, and server log. When you give us feedback, at your option, your app log and device log will be collected by us.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="some log information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="operating information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="hit log",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="firmware clicking statistics",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="server log.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="your app log",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="device log",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Location Information: When you use location-based program services or features, we may collect your location information such as your GPS information.

    make(onto, "DataCollectionActivity",
        evidence="When you use location-based program services or features, we may collect your location information such as your GPS information.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="location information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="your GPS information.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="location-based program services or features")),
        )
    )




    #########################################################################
    # Mobile Phone Information: When you use Zepp App, we may collect your mobile phone information, such as, unique identifier (IDFA, IMEI), the operating system version, system time, time zone, alarm clock, brand and model of your mobile phone.

    make(onto, "DataCollectionActivity",
        evidence="When you use Zepp App, we may collect your mobile phone information, such as, unique identifier (IDFA, IMEI), the operating system version, system time, time zone, alarm clock, brand and model of your mobile phone.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="mobile phone information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="unique identifier (IDFA, IMEI)",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="the operating system version",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="system time",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="time zone",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="alarm clock",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="brand and model of your mobile phone.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Device Information: When you use Zepp App to connect a hardware device, such as an Amazfit watch, we may obtain information, such as: the device's unique identifier, device ID, MAC address, serial number, firmware version, Bluetooth, device size. The collection may also apply to your updated system or software and factory settings.  

    make(onto, "DataCollectionActivity",
        evidence="When you use Zepp App to connect a hardware device, such as an Amazfit watch, we may obtain information, such as: the device's unique identifier, device ID, MAC address, serial number, firmware version, Bluetooth, device size. The collection may also apply to your updated system or software and factory settings.  ",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="device's unique identifier",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="device ID",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="MAC address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="serial number",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="firmware version",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="Bluetooth",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="device size.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Device Unlock Information: When you use the device off-wrist lock function, we may collect your device unlock password to realize this function.

    make(onto, "DataCollectionActivity",
        evidence="When you use the device off-wrist lock function, we may collect your device unlock password to realize this function.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="device unlock password",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="use the device off-wrist lock function")),
        )
    )




    #########################################################################
    # Crash Information: When you choose to upload debug logs to help us analyze the problem, your application debug log file will be sent to the server.

    make(onto, "DataCollectionActivity",
        evidence="When you choose to upload debug logs to help us analyze the problem, your application debug log file will be sent to the server.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="application debug log file",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to upload debug logs to help us analyze the problem")),
        )
    )




    #########################################################################
    # Information from Friends: Zepp App allows you to add friends. After receiving permission from your friends, the weight, activity and sleep information of your friends will be displayed on your App.

    # Sharing from others to user is not implemented in the ontology




    #########################################################################
    # Information Submitted via Services. When you use various functionalities of the Zepp App, you may submit certain information, such as voice information, a reminder setting or tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.). When you use female health function, the information provided by you will be collected, such as duration of menstruation, menstruation interval, the starting date of your latest menstruation, the starting date and ending date of your menstruation, physical condition and mood during menstruation.

    make(onto, "DataCollectionActivity",
        evidence="When you use various functionalities of the Zepp App, you may submit certain information, such as voice information, a reminder setting or tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.).",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "AccountData",
                evidence="voice information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="reminder setting",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.).",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="use various functionalities")),
        )
    )

    make(onto, "DataCollectionActivity",
        evidence="When you use female health function, the information provided by you will be collected, such as duration of menstruation, menstruation interval, the starting date of your latest menstruation, the starting date and ending date of your menstruation, physical condition and mood during menstruation.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="duration of menstruation",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="menstruation interval",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="the starting date of your latest menstruation",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="the starting date and ending date of your menstruation",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="physical condition and mood during menstruation",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "HealthMonitoring",
                evidence="use female health function")),
        )
    )




    #########################################################################
    # Visitor Information: When using the visitor function of our smart scale, a visitor can experience our products and certain limited services. The data of the visitor (gender, height, date of birth) may be collected and used to calculate and present the results of certain services the visitor experiences. You can choose to save the visitor information or not, if you choose to save, the visitor’s gender, height, date of birth and weight will be collected by us.

    make(onto, "DataCollectionActivity",
        evidence="When using the visitor function of our smart scale, a visitor can experience our products and certain limited services. The data of the visitor (gender, height, date of birth) may be collected and used to calculate and present the results of certain services the visitor experiences. You can choose to save the visitor information or not, if you choose to save, the visitor’s gender, height, date of birth and weight will be collected by us.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="The data of the visitor",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="gender",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="height",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="date of birth",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to calculate and present the results of certain services the visitor experiences.")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
        )
    )




    #########################################################################
    # Other Information: We may also collect other types of information which is not directly or indirectly linked to an individual and which is aggregated, anonymized or de-identified. For example, the device function, system status, battery status, Startup & Shutdown status, charging status and connecting status of smartphone of your device may be collected when using a particular service. Such information is collected in order to improve the services we provide to you.

    make(onto, "DataCollectionActivity",
        evidence="We may also collect other types of information which is not directly or indirectly linked to an individual and which is aggregated, anonymized or de-identified. For example, the device function, system status, battery status, Startup & Shutdown status, charging status and connecting status of smartphone of your device may be collected when using a particular service. Such information is collected in order to improve the services we provide to you.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="other types of information which is not directly or indirectly linked to an individual",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="the device function",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="system status",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="battery status",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="Startup & Shutdown status",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="charging status",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="connecting status of smartphone",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "PseudoAnonymization",
                evidence="which is aggregated, anonymized or de-identified")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="in order to improve the services we provide to you.")),
        )
    )




    #########################################################################
    #                                                                       #
    # HOW THE PERSONAL INFORMATION IS USED                                  #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We acquire, hold, use and process personal information for a variety of business purposes including for providing services and/or products to you, to respond to information requested and to fulfill legal compliance on our part under applicable laws. We may also process and disclose personal information to our affiliated companies and to third-party service providers for the purposes stated in this Privacy Policy.

    make(onto, "DataUseActivity",
        evidence="We acquire, hold, use and process personal information for a variety of business purposes including for providing services and/or products to you, to respond to information requested and to fulfill legal compliance on our part under applicable laws.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="for a variety of business purposes including for providing services and/or products to you, to respond to information requested and to fulfill legal compliance on our part under applicable laws.")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="under applicable laws.")),
        )
    )

    make(onto, "DataSharingActivity",
        evidence="We may also process and disclose personal information to our affiliated companies and to third-party service providers for the purposes stated in this Privacy Policy.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="for the purposes stated in this Privacy Policy.")),
        )
    )




    #########################################################################
    # To Provide Products, Services, or Information Requested. We may use information about you to fulfill requests for products, Services, or information, including:
    # Providing, processing, maintaining, improving and developing our goods and/or services to you, including after-sales and customer support and for services on your device;
    # Communicating with you about your device, service or any general queries or other requests and comments, such as updates, customer inquiry support, information about our events, notices;
    # Providing access to certain areas, functionalities, and features of our products and services;
    # Conducting promotional activities, such as sweepstakes and Facebook events;
    # Analyzing and developing statistical information on the use of our products and services to better improve our products and services;
    # Optimizing the performance of your device;
    # Storing and maintaining information about you for our business operations or legal obligations; and
    # Providing local services without communicating with our servers.

    make(onto, "DataUseActivity",
        evidence="We may use information about you to fulfill requests for products, Services, or information, including: Providing, processing, maintaining, improving and developing our goods and/or services to you, including after-sales and customer support and for services on your device; Communicating with you about your device, service or any general queries or other requests and comments, such as updates, customer inquiry support, information about our events, notices; Providing access to certain areas, functionalities, and features of our products and services; Conducting promotional activities, such as sweepstakes and Facebook events; Analyzing and developing statistical information on the use of our products and services to better improve our products and services; Optimizing the performance of your device; Storing and maintaining information about you for our business operations or legal obligations; and Providing local services without communicating with our servers.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="information about you",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to fulfill requests for products, Services, or information, including:")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Providing, processing, maintaining, improving and developing our goods and/or services to you, including after-sales and customer support and for services on your device;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Communicating with you about your device, service or any general queries or other requests and comments, such as updates, customer inquiry support, information about our events, notices;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Providing access to certain areas, functionalities, and features of our products and services;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Conducting promotional activities, such as sweepstakes and Facebook events;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Analyzing and developing statistical information on the use of our products and services to better improve our products and services;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Optimizing the performance of your device;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Storing and maintaining information about you for our business operations or legal obligations; and")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Providing local services without communicating with our servers.")),
        )
    )




    #########################################################################
    # Administrative Purposes. We may use personal information about you for administrative purposes, including to: 
    # Measure interest in our services;
    # Develop new products and services;
    # Ensure internal quality control;
    # Verify your identity;
    # Communicate about accounts and activities on our services and systems, and, in our discretion, changes to any of our policies;
    # Send email to the email address you provide to us to verify your account and for informational and operational purposes, such as account management, customer service, or system maintenance;
    # Prevent potentially prohibited or illegal activities; and
    # Enforce our Service Agreement and/or Privacy Policy.

    make(onto, "DataUseActivity",
        evidence="We may use personal information about you for administrative purposes, including to: Measure interest in our services; Develop new products and services; Ensure internal quality control; Verify your identity; Communicate about accounts and activities on our services and systems, and, in our discretion, changes to any of our policies; Send email to the email address you provide to us to verify your account and for informational and operational purposes, such as account management, customer service, or system maintenance; Prevent potentially prohibited or illegal activities; and Enforce our Service Agreement and/or Privacy Policy.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Measure interest in our services;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Develop new products and services;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Ensure internal quality control;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Verify your identity;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Communicate about accounts and activities on our services and systems, and, in our discretion, changes to any of our policies;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Send email to the email address you provide to us to verify your account and for informational and operational purposes, such as account management, customer service, or system maintenance;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Prevent potentially prohibited or illegal activities; and")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Enforce our Service Agreement and/or Privacy Policy.")),
        )
    )




    #########################################################################
    # Marketing Our Products and Services. If permitted by applicable laws, we may use your personal information, such as your email address, account ID, to provide you with materials directly or through third-party service provider(s) about offers, products, and services, including new content or services. We may provide you with these materials by phone, postal mail, facsimile, or email, or as otherwise permitted by applicable law. Such uses include:
    # To notify you about offers, products, and services that may be of interest to you;
    # For other purposes disclosed at the time that individuals provide personal information; and
    # Otherwise with your consent.

    make(onto, "DataUseActivity",
        evidence="If permitted by applicable laws, we may use your personal information, such as your email address, account ID, to provide you with materials directly or through third-party service provider(s) about offers, products, and services, including new content or services. We may provide you with these materials by phone, postal mail, facsimile, or email, or as otherwise permitted by applicable law. Such uses include: To notify you about offers, products, and services that may be of interest to you; For other purposes disclosed at the time that individuals provide personal information; and Otherwise with your consent.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="email address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="account ID",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to provide you with materials directly or through third-party service provider(s) about offers, products, and services, including new content or services.")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="To notify you about offers, products, and services that may be of interest to you;")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="For other purposes disclosed at the time that individuals provide personal information; and")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="Otherwise with your consent.")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="permitted by applicable laws")),
        )
    )




    #########################################################################
    # You have the right to opt out of our proposed use of your personal information for direct marketing. If you no longer wish to receive certain types of email communication you may opt-out by following the unsubscribe link located at the bottom of each communication.

    make(onto, "UserOptControl",
        evidence="You have the right to opt out of our proposed use of your personal information for direct marketing. If you no longer wish to receive certain types of email communication you may opt-out by following the unsubscribe link located at the bottom of each communication.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", user)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="your personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="for direct marketing")),
        )
    )




    #########################################################################
    # Research and Development. We may use personal information to create non-identifiable information that we may use alone or in the aggregate with information obtained from other sources, in order to help us to optimally deliver our existing products and services or develop new products and services and we may share these statistics with the public or third parties in order to present the preference and trend analysis.

    make(onto, "DataUseActivity",
        evidence="We may use personal information to create non-identifiable information that we may use alone or in the aggregate with information obtained from other sources, in order to help us to optimally deliver our existing products and services or develop new products and services",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "PseudoAnonymization",
                evidence="non-identifiable")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to create non-identifiable information that we may use alone or in the aggregate with information obtained from other sources, in order to help us to optimally deliver our existing products and services or develop new products and services")),
        )
    )

    make(onto, "DataSharingActivity",
        evidence="and we may share these statistics with the public or third parties in order to present the preference and trend analysis.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "NonPersonalData",
                evidence="statistics",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="in order to present the preference and trend analysis.")),
        )
    )




    #########################################################################
    # Services via Mobile Devices (only in certain feature). From time to time, we may provide products and services that are specifically designed to be compatible and used on mobile devices. We will collect certain information that your mobile device sends when you use such products and services, like a device identifier, user settings, location information, mobile carrier, and the operating system of your device. Mobile versions of our products and services may require that users log in with an account. In such cases, information about use of mobile versions of the products and services may be associated with accounts. In addition, we may enable you to download an application, widget, or other tool that can be used on mobile or other computing devices. Some of these tools may store information on mobile or other devices. These tools may transmit personal information to us to enable you to access your accounts and to enable us and our third-party service providers to track use of these tools. Some of these tools may enable users to transmit reports and other information from the tool. We may use personal or non-identifiable information transmitted to us to enhance these tools, to develop new tools, for quality improvement and as otherwise described in this Privacy Policy or in other notices we provide.

    make(onto, "DataUseActivity",
        evidence="We will collect certain information that your mobile device sends when you use such products and services, like a device identifier, user settings, location information, mobile carrier, and the operating system of your device. Mobile versions of our products and services may require that users log in with an account. In such cases, information about use of mobile versions of the products and services may be associated with accounts. In addition, we may enable you to download an application, widget, or other tool that can be used on mobile or other computing devices. Some of these tools may store information on mobile or other devices. These tools may transmit personal information to us to enable you to access your accounts and to enable us and our third-party service providers to track use of these tools. Some of these tools may enable users to transmit reports and other information from the tool.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="information that your mobile device sends",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="device identifier,",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="user settings",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="location information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="mobile carrier",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="operating system of your device.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="users log in with an account.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="reports and other information from the tool.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to enable you to access your accounts and to enable us and our third-party service providers to track use of these tools.")),
        )
    )

    make(onto, "DataUseActivity",
        evidence="We may use personal or non-identifiable information transmitted to us to enhance these tools, to develop new tools, for quality improvement and as otherwise described in this Privacy Policy or in other notices we provide.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "NonPersonalData",
                evidence="non-identifiable information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "PseudoAnonymization",
                evidence="non-identifiable")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to enhance these tools, to develop new tools, for quality improvement and as otherwise described in this Privacy Policy or in other notices we provide.")),
        )
    )




    #########################################################################
    # De-identified, Anonymous and/or Aggregated Information Use. We may use personal information and other information about you to create de-identified, anonymized and/or aggregated information, such as de-identified demographic information, de-identified location information, information about the mobile phone or device from which you access Zepp App, or other analyses we create. De-identified, anonymized and/or aggregated information is not personal information, and we may use such information in a number of ways, including research, internal analysis, analytics, and any other legally permissible purposes.

    make(onto, "DataUseActivity",
        evidence="De-identified, Anonymous and/or Aggregated Information Use. We may use personal information and other information about you to create de-identified, anonymized and/or aggregated information, such as de-identified demographic information, de-identified location information, information about the mobile phone or device from which you access Zepp App, or other analyses we create. De-identified, anonymized and/or aggregated information is not personal information, and we may use such information in a number of ways, including research, internal analysis, analytics, and any other legally permissible purposes.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "PseudoAnonymization",
                evidence="de-identified, anonymized and/or aggregated")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to create de-identified, anonymized and/or aggregated information, such as de-identified demographic information, de-identified location information, information about the mobile phone or device from which you access Zepp App, or other analyses we create.")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="in a number of ways, including research, internal analysis, analytics, and any other legally permissible purposes.")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="legally permissible")),
        )
    )




    #########################################################################
    # Improving User Experience. Some opt-in features allow us or our third party partners to analyze data about how users use our products and services, so as to improve the user experience, such as sending crash reports.

    make(onto, "UserOptControl",
        evidence="Improving User Experience. Some opt-in features allow us or our third party partners to analyze data about how users use our products and services, so as to improve the user experience, such as sending crash reports.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="crash reports",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to improve the user experience")),
        )
    )




    #########################################################################
    # Specific Ways Personal Information is Used in Products and Services. Here are more details on how we may use your information (which may include personal information):

    make(onto, "DataUseActivity",
        evidence="Here are more details on how we may use your information (which may include personal information):",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # To Set Up Your Account for Zepp App. Personal information collected when creating an account through our Zepp App is used for creating the personal account and profile page for the user.

    make(onto, "DataCollectionActivity",
        evidence="Personal information collected when creating an account through our Zepp App is used for creating the personal account and profile page for the user.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="Personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="is used for creating the personal account and profile page for the user.")),
        )
    )




    #########################################################################
    # To Calculate Exercise Results. Personal body information is used to accurately calculate and display the exercise result to you, such as, exercising records, distance, exercising time, total duration, burned calories, consumption, pace, speed, maximum oxygen uptake (VO2 Max), exercise capacity, training effects.

    make(onto, "DataUseActivity",
        evidence="Personal body information is used to accurately calculate and display the exercise result to you, such as, exercising records, distance, exercising time, total duration, burned calories, consumption, pace, speed, maximum oxygen uptake (VO2 Max), exercise capacity, training effects.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="Personal body information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="exercising records",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="distance",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="exercising time",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="total duration",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="burned calories",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="consumption",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="pace",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="speed",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="maximum oxygen uptake (VO2 Max)",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="exercise capacity",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="training effects.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "HealthMonitoring",
                evidence="is used to accurately calculate and display the exercise result to you")),
        )
    )




    #########################################################################
    # Physical Analysis. Based on the personal information you provided and the data recorded by the device, we will provide you an analysis related to your physical condition for your reference, such as PAI, BMI, muscle mass, body fat percentage, water percentage, protein, basal metabolic rate, subcutaneous fat, skeletal muscle mass, visceral fat level, bone mass content, pressure, body shape, body age.

    make(onto, "DataUseActivity",
        evidence="Based on the personal information you provided and the data recorded by the device, we will provide you an analysis related to your physical condition for your reference, such as PAI, BMI, muscle mass, body fat percentage, water percentage, protein, basal metabolic rate, subcutaneous fat, skeletal muscle mass, visceral fat level, bone mass content, pressure, body shape, body age.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="data recorded by the device",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="PAI",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="BMI",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="muscle mass",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="body fat percentage",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="water percentage",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="protein",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="basal metabolic rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="subcutaneous fat",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="skeletal muscle mass",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="visceral fat level",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="bone mass content",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="pressure",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="body shape",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="body age",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "HealthMonitoring",
                evidence="provide you an analysis related to your physical condition for your reference")),
        )
    )




    #########################################################################
    # Sleep Analysis. Based on the personal information you have provided and the data recorded by the device, such as PPG, heart rate, we will record your naps, sleep time, sleep breathing and provide you a sleep score and sleep analysis related to your sleep quality for your reference.

    make(onto, "DataUseActivity",
        evidence="Based on the personal information you have provided and the data recorded by the device, such as PPG, heart rate, we will record your naps, sleep time, sleep breathing and provide you a sleep score and sleep analysis related to your sleep quality for your reference.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="naps",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="sleep time",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="sleep breathing",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="sleep score",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="sleep analysis",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "HealthMonitoring",
                evidence="for your reference")),
        )
    )




    #########################################################################
    # To Provide World Clock Service. When you add a world clock in Zepp App, we will calculate the local time corresponding to your selected area based on the time at your mobile phone and display it in Zepp App and the bundled devices that support the world clock function.

    make(onto, "DataUseActivity",
        evidence="we will calculate the local time corresponding to your selected area based on the time at your mobile phone and display it in Zepp App and the bundled devices that support the world clock function.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="your selected area",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="display it in Zepp App and the bundled devices that support the world clock function.")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
        )
    )




    #########################################################################
    # To Provide Alarm Clock Service: when you use alarm clock function, your alarm clock information will be displayed in Zepp App and the bundled device.

    make(onto, "DataUseActivity",
        evidence="when you use alarm clock function, your alarm clock information will be displayed in Zepp App and the bundled device.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="alarm clock information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="will be displayed in Zepp App and the bundled device.")),
        )
    )




    #########################################################################
    # To Provide Voice Related Service: When you use off-line or on-line voice assistant function (only supported by certain device in certain countries/areas), such as Alexa, we will collect your voice request, for the purpose of carrying out your orders. Your voice information may also be used to provide voice memo service to you.

    make(onto, "DataCollectionActivity",
        evidence="When you use off-line or on-line voice assistant function (only supported by certain device in certain countries/areas), such as Alexa, we will collect your voice request, for the purpose of carrying out your orders. Your voice information may also be used to provide voice memo service to you.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "BiometricData",
                evidence="your voice request",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="for the purpose of carrying out your orders.")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to provide voice memo service to you.")),
        )
    )




    #########################################################################
    # To Provide Female Health Service. When you use female health function, certain information related to menstrual period will be recorded and displayed in Zepp App or on some devices that support this function. If you turn on the physiological period intelligent prediction mode, we will predict your menstrual period and remind you based on the information you provided.

    make(onto, "DataUseActivity",
        evidence="When you use female health function, certain information related to menstrual period will be recorded and displayed in Zepp App or on some devices that support this function. If you turn on the physiological period intelligent prediction mode, we will predict your menstrual period and remind you based on the information you provided.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="information related to menstrual period",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "HealthMonitoring",
                evidence="predict your menstrual period and remind you based on the information you provided.")),
        )
    )




    #########################################################################
    # To Provide Blood Oxygen Saturation Measurement Function. When you turn on the blood oxygen measurement function, we will collect your blood oxygen saturation information to show the value to you or to assist providing a sleeping analysis to you.

    make(onto, "DataCollectionActivity",
        evidence="we will collect your blood oxygen saturation information to show the value to you or to assist providing a sleeping analysis to you.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="blood oxygen saturation information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "HealthMonitoring",
                evidence="to show the value to you or to assist providing a sleeping analysis to you.")),
        )
    )




    #########################################################################
    # To Provide Notification Reminder Service. When you enable the notification reminder function, the reminder information you set in the Zepp App will be pushed to the bundled device.

    make(onto, "DataUseActivity",
        evidence="When you enable the notification reminder function, the reminder information you set in the Zepp App will be pushed to the bundled device.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="reminder information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="reminder information you set in the Zepp App will be pushed to the bundled device.")),
        )
    )




    #########################################################################
    # To Provide Bluetooth Camera Function. When you use Bluetooth camera function, your mobile phone will be connected with the device through Bluetooth for controlling the camera.

    make(onto, "DataActivity",
        evidence="When you use Bluetooth camera function, your mobile phone will be connected with the device through Bluetooth for controlling the camera.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "SensitiveData",
                evidence="Bluetooth camera",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # To Provide Zepp App Services. When you connect certain devices with Zepp App, the information collected through the device will be shown to user.

    make(onto, "DataCollectionActivity",
        evidence="When you connect certain devices with Zepp App, the information collected through the device will be shown to user.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # To Provide eSIM(embedded SIM) Function. (only supported by certain devices and in certain countries/areas). After you successfully activate eSIM with telecom carriers, you may use the device alone to call or receive a call, to send or receive SMS (SMS service is subject to local telecom carriers). When you use eSIM function, we will collect your operation records. Your phone number, call records, short messages will be stored in the device, but if you choose to upload this information together with the log, this information will be uploaded and stored in our cloud.

    make(onto, "GiveConsentActivity",
        evidence="When you use eSIM function, we will collect your operation records. Your phone number, call records, short messages will be stored in the device, but if you choose to upload this information together with the log, this information will be uploaded and stored in our cloud.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="operation records.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="phone number",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="call records",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="short messages",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # To Display Caller Information. When you receive a call, text messages, caller information will be displayed on the device. You may even answer or reject a phone call by the device directly (only supported by certain devices).

    make(onto, "DataUseActivity",
        evidence="When you receive a call, text messages, caller information will be displayed on the device. You may even answer or reject a phone call by the device directly (only supported by certain devices).",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "SensitiveData",
                evidence="text messages",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="caller information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="will be displayed on the device.")),
        )
    )




    #########################################################################
    # To Provide Bluetooth Phone Services (only supported by certain devices). With the device successfully paired with your mobile phone’s Bluetooth, when you receive an incoming call, the incoming call information will be displayed on the device. You can even use the device to answer or hang up the call. If you have missed calls, the relevant information will also be displayed on the device. You may add or delete your frequent contacts information in Zepp App. The frequent contacts information added by you will be bound to your account and synchronized to the device and our cloud.

    make(onto, "DataCollectionActivity",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="incoming call information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="frequent contacts information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="You can even use the device to answer or hang up the call. If you have missed calls, the relevant information will also be displayed on the device.")),
        )
    )




    #########################################################################
    # To Display Music Information. When you use music control function, the music information (name of song, singer, volume, the status of song) will be displayed on the device.

    make(onto, "DataUseActivity",
        evidence="When you use music control function, the music information (name of song, singer, volume, the status of song) will be displayed on the device.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="music information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="name of song",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="singer",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="volume",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AppData",
                evidence="the status of song",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="will be displayed on the device.")),
        )
    )




    #########################################################################
    # To Provide AI Sleep Melody Service. When you use AI Sleep Melody service, we will collect and use your personal information, such as heart rate, activity data, sleep data and your music reference to recommend sleep melodies to you.

    make(onto, "DataCollectionActivity",
        evidence="When you use AI Sleep Melody service, we will collect and use your personal information, such as heart rate, activity data, sleep data and your music reference to recommend sleep melodies to you.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="heart rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="activity data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="sleep data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="your music reference",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to recommend sleep melodies to you.")),
        )
    )

    make(onto, "DataUseActivity",
        evidence="When you use AI Sleep Melody service, we will collect and use your personal information, such as heart rate, activity data, sleep data and your music reference to recommend sleep melodies to you.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="heart rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="activity data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="sleep data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "NonSensitiveData",
                evidence="your music reference",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to recommend sleep melodies to you.")),
        )
    )




    #########################################################################
    # To Provide Hearing Health Function (only supported by certain earphone). If you turn on this function, we will collect your earphone volume in real time and recommend listening time for the current week based on the hearing protection standards established by the World Health Organization (WHO).

    make(onto, "DataCollectionActivity",
        evidence="If you turn on this function, we will collect your earphone volume in real time and recommend listening time for the current week based on the hearing protection standards established by the World Health Organization (WHO).",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="earphone volume",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="recommend listening time for the current week based on the hearing protection standards established by the World Health Organization (WHO).")),
        )
    )




    #########################################################################
    # To Provide Cervical Protection Function (only supported by certain earphone). If you turn on this function, the earphone sensor will detect and present you with habitual head-lowering angle. If you turn on the relax prompt, the earphone will play music to remind you to relax your spine for long periods of time.

    make(onto, "DataCollectionActivity",
        evidence="If you turn on this function, the earphone sensor will detect and present you with habitual head-lowering angle. If you turn on the relax prompt, the earphone will play music to remind you to relax your spine for long periods of time.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="habitual head-lowering angle.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "HealthMonitoring",
                evidence="the earphone will play music to remind you to relax your spine for long periods of time.")),
        )
    )




    #########################################################################
    # To Provide Noise Control Function (only supported by certain earphone). When you turn on ANC function, we will collect and cancel ambient sound in accordance with the mode set by you.

    make(onto, "DataCollectionActivity",
        evidence="When you turn on ANC function, we will collect and cancel ambient sound in accordance with the mode set by you.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="ambient sound",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # To Provide Tap for Report Function (only supported by certain earphone). If you turn on this function, we will collect your current speed, heart rate and other workout information. By simply taping the earphone, this information will be broadcasted to you.

    make(onto, "DataCollectionActivity",
        evidence="If you turn on this function, we will collect your current speed, heart rate and other workout information. By simply taping the earphone, this information will be broadcasted to you.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="current speed",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="heart rate",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="other workout information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "HealthMonitoring",
                evidence="will be broadcasted to you.")),
        )
    )




    #########################################################################
    # To Determine Whether the Mobile Phone is Supported. Phone information will be used to determine if your device can use Zepp App.

    make(onto, "DataUseActivity",
        evidence="Phone information will be used to determine if your device can use Zepp App.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="Phone information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to determine if your device can use Zepp App.")),
        )
    )




    #########################################################################
    # To Measure the Temperature (only supported by certain devices). The device will measure the temperature and display the data to you.

    make(onto, "DataCollectionActivity",
        evidence="The device will measure the temperature and display the data to you.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="temperature",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "HealthMonitoring",
                evidence="display the data to you.")),
        )
    )




    #########################################################################
    # To Provide Network Related Services. We use network types, network signals, etc. to prompt the user to download updates in different network environments. Certain devices (such as Amazfit smart scale) can directly connect to the server via WLAN, and upload your measurement (such as your weight, body fat, BMI and etc.) and the device identifier to the cloud accessible in the Zepp App.

    make(onto, "DataCollectionActivity",
        evidence="We use network types, network signals, etc. to prompt the user to download updates in different network environments. Certain devices (such as Amazfit smart scale) can directly connect to the server via WLAN, and upload your measurement (such as your weight, body fat, BMI and etc.) and the device identifier to the cloud accessible in the Zepp App.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "HealthData",
                evidence="measurement",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="weight",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="body fat",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "HealthData",
                evidence="BMI",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "DeviceData",
                evidence="device identifier",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # To Provide Off-wrist Lock Function. Your device unlock password will be used to the off-wrist lock function. If you turn on this function, your device will be locked when the device detects that it is off-wrist. If the wrong password is entered on the device more than a certain number of times, your device will be locked up. To unlock the device, you need to change the device unlock password or restore the Factory Settings on device in Zepp App.

    make(onto, "DataUseActivity",
        evidence="Your device unlock password will be used to the off-wrist lock function.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "AccountData",
                evidence="device unlock password",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="will be used to the off-wrist lock function.")),
        )
    )




    #########################################################################
    # To Provide Location-based Services. In the course of using our services, location information may also be used by us or third-party service providers to provide and improve our services. For example, we may use your GPS information to provide you with weather details, calculating the distance of your outdoor sporting or mapping such activity. You may turn this off at any time by going into the device settings of your mobile devices or discontinue use of that application.

    make(onto, "DataSharingActivity",
        evidence="In the course of using our services, location information may also be used by us or third-party service providers to provide and improve our services. For example, we may use your GPS information to provide you with weather details, calculating the distance of your outdoor sporting or mapping such activity.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party),
            ("sharesDataWithAgent", third_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="location information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="GPS information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to provide and improve our services.")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to provide you with weather details, calculating the distance of your outdoor sporting or mapping such activity.")),
        )
    )

    make(onto, "GiveConsentActivity",
        evidence="You may turn this off at any time by going into the device settings of your mobile devices or discontinue use of that application.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", user)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="location information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="GPS information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # To Optimize Our Products and Services. We use your personal information, such as, Huami ID, log information, debug information, the information automatically collected to provide functionality, analyze performance, fix errors, and improve the quality of our products and services. For example, we may use these information to optimize pages/function display, determining the importance of each product function, guiding us to adjust the priority of the development of product features.

    make(onto, "DataUseActivity",
        evidence="We use your personal information, such as, Huami ID, log information, debug information, the information automatically collected to provide functionality, analyze performance, fix errors, and improve the quality of our products and services. For example, we may use these information to optimize pages/function display, determining the importance of each product function, guiding us to adjust the priority of the development of product features.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "AccountData",
                evidence="Huami ID",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="log information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="debug information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to provide functionality, analyze performance, fix errors, and improve the quality of our products and services.")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to optimize pages/function display, determining the importance of each product function, guiding us to adjust the priority of the development of product features.")),
        )
    )




    #########################################################################
    # To Manage Devices. This information provides the ability to manage the bundled devices.

    make(onto, "DataUseActivity",
        evidence="This information provides the ability to manage the bundled devices.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="provides the ability to manage the bundled devices.")),
        )
    )




    #########################################################################
    # To Improve Software Stability. We collect crash logs for analyzing software quality to provide better service.

    make(onto, "DataCollectionActivity",
        evidence="We collect crash logs for analyzing software quality to provide better service.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "ServiceData",
                evidence="crash logs",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="for analyzing software quality to provide better service.")),
        )
    )




    #########################################################################
    # To Improve Device Stability. We may use the information to improve the bundled devices.

    make(onto, "DataUseActivity",
        evidence="We may use the information to improve the bundled devices.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to improve the bundled devices.")),
        )
    )




    #########################################################################
    # To Send Notices. From time to time, we may use your personal information to send important notices, such as communications about changes to our terms, conditions, and policies.

    make(onto, "PolicyChangeActivity",
        evidence="From time to time, we may use your personal information to send important notices, such as communications about changes to our terms, conditions, and policies.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "PersonalData",
                evidence="your personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasNotificationMechanism", make(onto, "NotificationMechanism",
                evidence="communications")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to send important notices")),
        )
    )




    #########################################################################
    #                                                                       #
    # COOKIES AND OTHER TECHNOLOGIES                                        #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We, as well as our third-party service providers that provide content, advertising, or other functionality on our Services, may use cookies, pixel tags, local storage, and other technologies (“Technologies”) to automatically collect information through the Services. We use Technologies that are essentially small data files placed on your computer, tablet, mobile phone, or other devices that allow us to record certain pieces of information whenever you visit or interact with our websites, services, applications, messaging, and tools, and to recognize you across devices.

    make(onto, "DataCollectionActivity",
        evidence="We, as well as our third-party service providers that provide content, advertising, or other functionality on our Services, may use cookies, pixel tags, local storage, and other technologies (“Technologies”) to automatically collect information through the Services. We use Technologies that are essentially small data files placed on your computer, tablet, mobile phone, or other devices that allow us to record certain pieces of information whenever you visit or interact with our websites, services, applications, messaging, and tools, and to recognize you across devices.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "Data",
                evidence="information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="cookies",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to recognize you across devices.")),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="through the Services.")),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="pixel tags")),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="local storage")),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="cookies")),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="other technologies (“Technologies”)")),
        )
    )




    #########################################################################
    # What Information is Collected and How We Use Them: Technologies such as cookies, tags, and scripts are used by us and our third-party service providers. These Technologies are used in analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole. We may receive reports based on the use of these technologies by these companies on an individual as well as aggregated basis.

    make(onto, "DataCollectionActivity",
        evidence="Technologies such as cookies, tags, and scripts are used by us and our third-party service providers. These Technologies are used in analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole. We may receive reports based on the use of these technologies by these companies on an individual as well as aggregated basis.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="cookies",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="cookies")),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="tags")),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="scripts")),
            ("hasSecurityMechanism", make(onto, "PseudoAnonymization",
                evidence="aggregated basis.")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole.")),
        )
    )

    make(onto, "DataCollectionActivity",
        evidence="Technologies such as cookies, tags, and scripts are used by us and our third-party service providers. These Technologies are used in analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole. We may receive reports based on the use of these technologies by these companies on an individual as well as aggregated basis.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="cookies",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", third_party)))),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="cookies")),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="tags")),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="scripts")),
            ("hasSecurityMechanism", make(onto, "PseudoAnonymization",
                evidence="aggregated basis.")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole.")),
        )
    )




    #########################################################################
    # Cookies. Cookies are small text files placed in visitors’ device browsers to store their preferences. Most browsers allow you to block and delete cookies. However, if you do that, the website may not work properly.

    make(onto, "ConsentActivity",
        evidence="Cookies are small text files placed in visitors’ device browsers to store their preferences. Most browsers allow you to block and delete cookies. However, if you do that, the website may not work properly.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="cookies",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasUserChoiceConsequence", make(onto, "PartialServiceRestriction",
                evidence="However, if you do that, the website may not work properly.")),
        )
    )




    #########################################################################
    # Pixel Tags/Web Beacons. A pixel tag (also known as a web beacon) is a piece of code embedded on the website that collects information about users’ engagement on that web page. The use of a pixel allows us to record, for example, that a user has visited a particular web page or clicked on a particular advertisement.

    make(onto, "DataCollectionActivity",
        evidence="A pixel tag (also known as a web beacon) is a piece of code embedded on the website that collects information about users’ engagement on that web page. The use of a pixel allows us to record, for example, that a user has visited a particular web page or clicked on a particular advertisement.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "TrackingData",
                evidence="information about users’ engagement on that web page",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataCollectionMechanism", make(onto, "DataCollectionMechanism",
                evidence="pixel tag (also known as a web beacon)")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="to record, for example, that a user has visited a particular web page or clicked on a particular advertisement")),
        )
    )

    return


    #########################################################################
    # Social Media Widgets: Our products, services and website may include social media features such as connectivity with Facebook, Google,Twitter, Strava, Line (that might include widgets such as the share this button or other interactive mini-programs). These features may collect your IP address, which page you are visiting on our website, and may set a cookie/or use some device or location information to enable the feature to function properly. These social media features are either hosted by a third party or hosted directly by us. Your interactions with these features are governed by the privacy policy of the company providing it.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Log Files: As true of most websites, we gather certain information and store it in log files. This information may include Internet protocol (IP) addresses, browser type, Internet service provider (ISP), referring/exit pages, operating system, date/time stamp, and/or clickstream data.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Mobile Analytics: Within some of our mobile applications, we use mobile analytics software to allow us to better understand the functionality of our mobile software on your phone. This software may record information such as how often you use the application, the events that occur within the application, aggregated usage, performance data, and where crashes occur within the application.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Local Storage – HTML5: We use Local Storage Objects (LSOs) such as HTML5 to store content and preferences. Third parties with whom we partner to provide certain features on our websites or to display advertising based upon your web browsing activity also use HTML5 to collect and store information. Various browsers may offer their own management tool for removing HTML5 LSOs.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Website Analytics. We may use Technologies and other third-party tools to process analytics information on our Services (e.g., Google Analytics). For more about Google Analytics information, please visit Google Analytics’ Privacy Policy. To learn more about how to opt-out of Google Analytics’ use of your information on our website, please click here.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Operationally Necessary. We may use cookies, or other similar technologies that are necessary to the operation of our services, applications, and tools. This includes technologies that allow you access to our services, applications, and tools; that are required to identify irregular website behavior, prevent fraudulent activity and improve security; or that allow you to make use of our functions such as shopping-carts, saved search, or similar functions;

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Performance Related. We may use cookies, or other similar technologies to assess the performance of our websites, applications, services, and tools, including as part of our analytic practices to help us understand how our visitors use our websites, determine if you have interacted with our messaging, determine whether you have viewed an item or link, or to improve our website content, applications, services, or tools;

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Functionality Related. We may use cookies, web beacons, or other similar technologies that allow us to offer you enhanced functionality when accessing or using our websites, services, applications, or tools. This may include identifying you when you sign into our websites or keeping track of your specified preferences, interests, or past items viewed so that we may enhance the presentation of content on our websites;

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # If you would like to opt out of the Technologies we employ on our websites, services, applications, or tools, you may do so by blocking, deleting, or disabling them as your browser or device permits.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # THIRD PARTY WEBSITES, SOCIAL MEDIA PLATFORMS AND                      #
    # SOFTWARE DEVELOPMENT KITS                                             #
    #                                                                       #
    #########################################################################

    # The ontology does not have such scenarios




    #########################################################################
    #                                                                       #
    # HOW WE SHARE YOUR INFORMATION                                         #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We may disclose your personal information on occasion to third parties (as described below) in order to provide the products or services that you have requested.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Disclosure may be made to third-party service providers and affiliated companies listed in this section below. In each case described in this section, you can be assured that we will only share your personal information in accordance with this Privacy Policy and the applicable terms that govern your use of our services. We will engage sub-processors for the processing of your personal information. You should know that when we share your personal information with a third-party service provider under any circumstance described in this section, we will contractually specify that the third party is subject to practices and obligations to comply with applicable local data protection laws. We will contractually ensure compliance by any third-party service providers with the privacy standards that apply to them in your home jurisdiction.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # ONWARD TRANSFER: SHARING WITH OUR GROUP, THIRD PARTY                  #
    # SERVICE PROVIDERS AND OTHERS                                          #
    #                                                                       #
    #########################################################################




    #########################################################################
    # In order to conduct business operations smoothly in providing you with the full capabilities of our products and services, we may disclose your personal information from time to time to our affiliated companies. We may also share your information as described in this Privacy Policy with our third-party service providers, to comply with legal obligations, to protect and defend our rights and property or with your permission.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Our third-party service providers include, without limitation, our mailing houses, delivery service providers, telecommunications companies, data centers, data storage facilities, customer service providers, advertising and marketing service providers. Such third-party service providers will be processing your personal information on our behalf or for one or more of the purposes listed herein.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Vendors and Service Providers. We may share any information we receive with vendors and service providers. The types of service providers (processors) to whom we entrust personal information include service providers for: (i) provision of IT and related services; (ii) provision of information and services you have requested; (iii) customer service activities; and (iv) in connection with the provision of the products, services and website. We have executed appropriate contracts with the service providers that prohibit them from using or sharing personal information except as necessary to perform the contracted services on our behalf or to comply with applicable legal requirements.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Third-Party Services. You may choose to share personal information with other third-party services (e.g., Strava, Wechat, Google Fit, Relive). Once your personal information has been shared with a third-party service, it will also be subject to the third-party service’s privacy policy. We encourage you to closely read each third-party service’s privacy policy before sharing your personal information with them. Please note that we do not control and we are not responsible for the third-party service’s processing of your personal information.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Business Partners. We may share personal information with our business partners to provide you with a product or service that you have requested. We may also provide personal information to business partners with whom we may jointly offer products or services, or whose products or services we believe may be of interest to you. In such cases, our business partner’s name will appear, along with us. We require our business partners to agree in writing to maintain the confidentiality and security of personal information they maintain on our behalf and not to use it for any purpose other than the purpose for which we provided them.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Affiliates. We may share your personal information with our company affiliates for the purposes set forth in this Privacy Policy, including our administrative purposes, activities such as IT management, or for them to provide services to you or support and supplement the services we provide.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Displaying to Your Friends. With your prior consent, we may share your personal information, such as, steps, weight, calories burned, sleep data to your friends.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Disclosures to Protect Us or Others as Required by Law and Similar Disclosures. We may access, preserve, and disclose your personal information, other account information, and content if we believe doing so is required or appropriate to: (i) comply with law enforcement or national security requests and legal process, such as a court order or subpoena (including in a country other than your home country); (ii) respond to your requests; (iii) protect your, ours or others’ rights, property, or safety; (iv) to enforce our policies or contracts; (v) to collect amounts owed to us; (vi) when we believe disclosure is necessary or appropriate to prevent physical harm or financial loss or in connection with an investigation or prosecution of suspected or actual illegal activity; or (vii) if we, in good faith, believe that disclosure is otherwise necessary or advisable.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Merger, Sale, or Other Asset Transfers. If we are involved in a merger, acquisition, financing due diligence, reorganization, bankruptcy, receivership, transition of service to another provider or asset sale of all or a portion of our assets, then your information may be sold or transferred as part of such a transaction as permitted by law and/or contract. You will be notified via email and/or a prominent notice on our website or in the Zepp App of any changes in ownership, uses of your personal information, and choices you may have regarding your personal information. We will endeavor to direct the transferee to use personal information in a manner that is consistent with the Privacy Policy in effect at the time such personal information was collected.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # SECURITY SAFEGUARDS                                                   #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We are committed to ensuring that your personal information is secure, and we will take all practicable steps to safeguard your personal information. However, you should be aware that the use of the Internet is not entirely secure, and for this reason we cannot guarantee the security or integrity of any personal information we process.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # To prevent unauthorized access, disclosure or other similar risks and to comply with applicable privacy and security laws in the countries in which we operate, we have put in place reasonable administrative, technical and physical controls and procedures designed to safeguard and secure the information we collect from your use of our products and services. We will use reasonable efforts designed to safeguard your personal information.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # For example, when you access your account, you can choose to use our two-step verification process for better security. When you send or receive data from your device to our servers, we make sure they are encrypted using Secure Sockets Layer ("SSL") and other algorithms.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # All your personal information is stored on secure servers that are protected in controlled facilities. We classify your data based on importance and sensitivity, and endeavor to ensure that your personal information has an appropriate security level. The files and records containing your personal information will be kept in our offices and/or on our servers or those of our service providers and only those employees that require it for the purposes of their duties will have access to this file. We have also implemented controls to require that our third-party service providers and partners have appropriate safeguards designed to protect your personal information as well. We make sure that our employees and third-party service providers who access the information to help provide you with our products and services are subject to strict contractual confidentiality obligations and may be disciplined or terminated if they fail to meet such obligations. In some cases, we have special access controls for cloud-based data storage as well. All in all, we regularly review our information collection, storage and processing practices, including physical security measures, in an effort to guard against any unauthorized access and use.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # However, despite these efforts, no security measures are perfect or impenetrable and no method of data transmission can be guaranteed to prevent any interception or other type of misuse. We also depend on you to protect your information. If you become aware of any breach of security or privacy, please notify us immediately. To the fullest extent permitted by applicable law, we do not accept liability for unauthorized disclosure.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # By using our products and services or providing personal information to us, you agree that we may communicate with you electronically regarding security, privacy, and administrative issues relating to your use. If we learn of a security system’s breach, we may attempt to notify you electronically by posting a notice on the website or through the product or service and/or by sending an e-mail to you. You may have a legal right to receive this notice in writing.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # WHAT YOU CAN DO                                                       #
    #                                                                       #
    #########################################################################




    #########################################################################
    # You can play your part in safeguarding your personal information by not disclosing your login password or account information to anybody unless such person is duly authorized by you. Whenever you log in the Zepp App, particularly on somebody else's mobile phones or on public Internet terminals, you should always log out at the end of your session.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We cannot be held responsible for lapses in security caused by third party accesses to your personal information as a result of your failure to keep your personal information private. Notwithstanding the foregoing, you must notify us immediately if there is any unauthorized use of your account by any other Internet user or any other breach of security. Your assistance will help us protect the privacy of your personal information.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # YOUR PRIVACY CHOICES                                                  #
    #                                                                       #
    #########################################################################




    #########################################################################
    # The privacy choices you may have about your personal information are determined by applicable law and are described below.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We may occasionally send you push notifications through our mobile applications with version updates and other notices that may be of interest to you. You may at any time opt-out from receiving these types of communications by changing the settings on your mobile device. We may also collect location-based information if you use our mobile applications. You may opt-out of this collection by changing the settings on your mobile device.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Do Not Track (“DNT”) is a privacy preference that users can set in certain web browsers. DNT is a way for users to inform websites and services that they do not want certain information about their webpage visits collected over time and across websites or online services. Please note that we do not respond to or honor DNT signals or similar mechanisms transmitted by web browsers.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # As noted herein, you may stop or restrict the placement of cookies and other technologies on your computer or remove them from your browser by adjusting your web browser preferences. Please note that cookie-based opt-outs are not effective on mobile applications. However, on many mobile devices, application users may opt out of certain mobile ads via their device settings.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Our applications may need access to certain features on your device such as Wi-Fi network status. This information is used to allow the applications to run on your device and allow you to interact with the applications. At any time you may revoke your permissions by turning these off at the device level and/or contacting us via https://www.zepp.com/privacy-support.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # We recognize that privacy concerns differ from person to person. Therefore, we provide examples of ways we make available for you to choose to restrict the collection, use, disclosure or processing of your personal information and control your privacy settings:
    # Log in and out of the account;
    # Toggle on/off for other services and functionalities which deal with sensitive or personal information.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # RETENTION POLICY                                                      #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We retain personal information we receive as described in this Privacy Policy for as long as you use our products, services and websites or as necessary to fulfill the purpose(s) for which it was collected, provide our services, resolve disputes, establish legal defenses, conduct audits, pursue legitimate business purposes, enforce our agreements, and comply with applicable laws. We shall cease to retain personal information, or remove the means by which the personal information can be associated with particular individuals, as soon as it is reasonable to assume that the purpose for which that personal information was collected is no longer being served by retention of the personal information.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # If further processing is for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes according to the applicable laws, the data can be further retained by us even if the further processing is incompatible with original purposes in certain jurisdictions.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # YOUR PRIVACY RIGHTS                                                   #
    #                                                                       #
    #########################################################################




    #########################################################################
    # Access Personal Information about you, including: (i) confirming whether we are processing your personal information; (ii) obtaining access to or a copy of your personal information;

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Request Correction of your personal information where it is inaccurate, incomplete or outdated. In some cases, we may provide self-service tools that enable you to update your personal information;

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Request Deletion or Anonymization of your personal information when processing is based on your consent or when processing is unnecessary, excessive or non-compliant;

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Request Restriction or Blocking of or Object to our processing of your personal information;

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Withdraw Your Consent to our processing of your personal information. If you refrain from providing personal information or withdraw your consent to processing, some features of our Service may not be available;

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Request Data Portability and receive an electronic copy of personal information that you have provided to us;

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Be Informed about third parties with which your personal information has been shared; and

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Request any review of decisions which may have been taken exclusively based on automated processing if that could affect data subject rights.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # STORAGE AND TRANSFER OF PERSONAL INFORMATION                          #
    #                                                                       #
    #########################################################################

    # The ontology does not have aspects of international data transfer
    # and international laws compliancy




    #########################################################################
    #                                                                       #
    # MINORS/CHILDREN’S PRIVACY                                             #
    #                                                                       #
    #########################################################################




    #########################################################################
    # Our products and services are not directed to children under 16 (and in certain jurisdictions under the age of 13) years of age.We don’t seek or intend to seek to receive any personal information from minors. Should a parent or guardian have reasons to believe that a minor has provided us with personal information without their prior consent, please contact us to ensure that the personal information is removed and the minor unsubscribes from any of the applicable services. If we learn that we have collected any personal information from children under 16 (and in certain jurisdictions under the age of 13) and we do not obtain permission from a parent, we will promptly take steps to delete such information and terminate the minor’s account.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # UPDATES TO THE PRIVACY POLICY                                         #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We keep our Privacy Policy under regular review and may update this Privacy Policy to reflect changes to our information practices. You understand and agree that you will be deemed to have accepted the updated Privacy Policy if you use the products or services after the updated Privacy Policy is posted. If, at any point, you do not agree to any portion of the Privacy Policy then in effect, you must immediately stop using the products and services. If we make material changes to our Privacy Policy, we will notify you by email (sent to the e-mail address specified in your account) or post the changes in our App. Such changes to our Privacy Policy shall apply from the effective date as set out in the notice or in our App. We encourage you to periodically review this page for the latest information on our privacy practices. Your continued use of products and services on mobile phones and/or any other device will be taken as acceptance of the updated Privacy Policy. Before we use personal information for any new purpose not originally authorized by you, we will endeavor to provide information regarding the new purpose and give you the opportunity to opt-out. Where your consent for the processing of personal information is otherwise required by law or contract, we will endeavor to comply with the law or contract.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # THIRD PARTY TERMS AND CONDITIONS                                      #
    #                                                                       #
    #########################################################################

    # The ontology does not have aspect describing irresponsibility for TP services




    #########################################################################
    #                                                                       #
    # OUR APPROACH TO MANAGE YOUR PERSONAL INFORMATION UNDER GDPR           #
    #                                                                       #
    #########################################################################

    # The ontology does not have GDPR compliancy aspect




    #########################################################################
    #                                                                       #
    # SUPPLEMENTAL CALIFORNIA ADDENDUM TO THIS PRIVACY POLICY               #
    #                                                                       #
    #########################################################################




    #########################################################################
    # This Supplemental California Addendum to this Privacy Policy (“California Addendum”) supplements and should be read in conjunction with this Privacy Policy. This California Addendum only applies to our processing of personal information that is subject to the California Consumer Privacy Act of 2018 (“CCPA”). The CCPA provides California residents with the right to know what categories of personal information we have collected about them and whether we disclosed that personal information for a business purpose (e.g., to a service provider) in the preceding twelve months. California residents can find this information below:

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Categories of Third Parties Personal Information is Disclosed to for a Business Purpose
    # Identifiers such as alias, unique personal identifier, online identifier, IP address, email address, account name or other similar identifiers.
    # Service providers
    # Affiliates
    # Other users or third-party services you share or interact with

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Biometric Info such as an individual’s physiological, biological, or behavioral characteristics, that can be used, singly or in combination with each other or with other identifying data, to establish individual identity. Biometric information includes, but is not limited to, gait patterns or rhythms, and sleep, health, or exercise data that contain identifying information.
    # Service providers
    # Affiliates

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Internet or other electronic network activity information such as browsing history, search history and information regarding a consumer's interaction with a website, application, or advertisement.
    # Service providers
    # Affiliates
    # Other users or third-party services you share or interact with

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Geo-location such as physical location or movements.
    # Service providers
    # Affiliates
    # Other users or third-party services you share or interact with

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Inferences drawn from other personal information to create a profile about a consumer
    # Service providers
    # Affiliates

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # “Sales” of Personal Information under the CCPA. For purposes of the CCPA, we do not “sell” personal information, nor do we have actual knowledge of any “sale” of personal information of minors under 16 years of age.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Non-Discrimination. California residents have the right not to receive discriminatory treatment by us for the exercise of their rights conferred by the CCPA. 

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Authorized Agent. Only you, or someone legally authorized to act on your behalf, may make a verifiable consumer request related to your personal information. To designate an authorized agent, please contact us as set forth below.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    # Verification. When you make a request, we will ask you to provide sufficient information that allows us to reasonably verify you are the person about whom we collected personal information or an authorized representative, which may include confirming the email address associated with any personal information we have about you.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )




    #########################################################################
    #                                                                       #
    # DATA DESTRUCTION PERIOD                                               #
    #                                                                       #
    #########################################################################




    #########################################################################
    # Personal information, which has fulfilled the purpose for which it was collected or used, and has reached the period of time during which personal information was to be possessed, will be destroyed in an irreversible way. After the expiration of the applicable period, information under the obligation of retention by applicable laws will be promptly destroyed in an irreversible way. Personal information stored in electronic files will be deleted safely in an irreversible way by using technical methods, and printed information will be destroyed by shredding or incinerating such information. Furthermore, in compliance with applicable laws, measures will be taken to destroy or separate the personal information of the users who have not used our services for a period of one year.

    make(onto, "",
        evidence="",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo", make(onto, "",
                evidence="",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism", make(onto, "",
                evidence="")),
            ("hasNotificationMechanism", make(onto, "",
                evidence="")),
            ("hasDataActivityPurpose", make(onto, "DataActivityPurpose",
                evidence="")),
            ("hasDataRetentionTime", make(onto, "DataRetentionTime",
                evidence="")),
            ("hasUserChoiceConsequence", make(onto, "",
                evidence="")),
            ("hasLegalBasis", make(onto, "LegalBasis",
                evidence="")),
        )
    )

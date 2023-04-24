from ontology import Ontology


def process_zepp():

    o = Ontology('zepp', 'https://upload-cdn.huami.com/tposts/8191')

    #########################################################################
    #                                                                       #
    # OUR COMMITMENT TO YOU                                                 #
    #                                                                       #
    #########################################################################




    #########################################################################
    # The Privacy Policy is designed with you in mind, and it is important that you have a comprehensive understanding of and confidence in our personal information collection and usage practices of any personal information provided to us.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataActivity',

        'The Privacy Policy is designed with you in mind, and it is important that you have a comprehensive understanding of and confidence in our personal information collection and usage practices of any personal information provided to us.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # We are committed to protecting the privacy, confidentiality and security of your personal information by complying with applicable laws. We are equally committed to ensuring that all our employees and agents uphold these obligations.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataActivity',

        'We are committed to protecting the privacy, confidentiality and security of your personal information by complying with applicable laws. We are equally committed to ensuring that all our employees and agents uphold these obligations.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'SecurityMechanism',
                'We are committed to protecting the privacy')),

            o.connection('hasSecurityMechanism', o.individual(
                'SecurityMechanism',
                'We are equally committed to ensuring that all our employees and agents uphold these obligations.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'by complying with applicable laws.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # TRANSPARENCY: WHAT INFORMATION IS COLLECTED AND HOW WE USE IT         #
    #                                                                       #
    #########################################################################




    #########################################################################
    # The categories of personal information we may collect (directly from you or from third party sources) and our privacy practices depend on the nature of the relationship you have with us and the requirements of applicable law. Some of the ways that we may collect personal information include: You may provide personal information directly to us through interacting with our products and services, or requesting services or information from us. As you navigate the services, certain information may also be collected automatically, including through cookies and similar technologies as described below.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'The categories of personal information we may collect (directly from you or from third party sources) and our privacy practices depend on the nature of the relationship you have with us and the requirements of applicable law. As you navigate the services, certain information may also be collected automatically, including through cookies and similar technologies as described below.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'cookies and similar technologies',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'requirements of applicable law')),
        ]
    )




    #########################################################################
    # We endeavor to collect only that information which is relevant for the purposes of processing.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We endeavor to collect only that information which is relevant for the purposes of processing.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for the purposes of processing')),
        ]
    )




    #########################################################################
    #                                                                       #
    # TYPES OF INFORMATION COLLECTED                                        #
    #                                                                       #
    #########################################################################




    #########################################################################
    # Information You Provide Directly to Us. When you use our services or engage in certain activities, such as registering for an account, responding to surveys, requesting services or information, requesting customer or technical support, or contacting us directly, we may ask you to provide certain personal information, such as email address or phone number.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'we may ask you to provide certain personal information, such as email address or phone number.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'email address',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'phone number',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Automatic Data Collection. We may collect certain information automatically through our products, services or other methods of analysis, such as your Internet protocol (IP) address, cookie identifiers, mobile carrier, MAC address and other device identifiers that are automatically assigned to device when you access the Internet, hardware type, device name, operating system, system version, region & language, installation package name, App version, network status, source of App, device battery, Bluetooth status, Internet service provider, the usage of product and App features, pages that you visit before and after using the services, the date and time of your visit, the amount of time you spend on each page, information about the links you click and pages you view within the services, and other actions taken through use of the services such as preferences.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We may collect certain information automatically through our products, services or other methods of analysis, such as your Internet protocol (IP) address, cookie identifiers, mobile carrier, MAC address and other device identifiers that are automatically assigned to device when you access the Internet, hardware type, device name, operating system, system version, region & language, installation package name, App version, network status, source of App, device battery, Bluetooth status, Internet service provider, the usage of product and App features, pages that you visit before and after using the services, the date and time of your visit, the amount of time you spend on each page, information about the links you click and pages you view within the services, and other actions taken through use of the services such as preferences.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'Internet protocol (IP) address',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'cookie identifiers',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'mobile carrier',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'MAC address',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'other device identifiers',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'hardware type',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'device name',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'operating system',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'system version',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'region & language',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'installation package name',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'App version',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'network status',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'source of App',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'device battery',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'Bluetooth status',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'Internet service provider',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'the usage of product and App features',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'pages that you visit before and after using the services',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'the date and time of your visit',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'the amount of time you spend on each page',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'information about the links you click',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'pages you view within the services',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'other actions taken through use of the services such as preferences.',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Specific Information Collected Through Our Products and Services. We have a wide range of products, the personal information collected by different products may vary. We may collect the following types of information (which may or may not be personal information):

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We have a wide range of products, the personal information collected by different products may vary. We may collect the following types of information (which may or may not be personal information):',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'types of information (which may or may not be personal information)',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Information about You: When you register for an account or log into our service using your credentials from your Mi, WeChat, Google, Line or Facebook accounts (with your approval), we may collect and use your avatar, gender, country, email address, nicknames, time zones, languages, regions, birthday, height, weight.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you register for an account or log into our service using your credentials from your Mi, WeChat, Google, Line or Facebook accounts (with your approval), we may collect and use your avatar, gender, country, email address, nicknames, time zones, languages, regions, birthday, height, weight.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'your credentials from your Mi, WeChat, Google, Line or Facebook accounts',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'avatar',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'gender',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'country',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'email address',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'nicknames',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'time zones',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'languages',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'regions',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'birthday',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'height',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'weight',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Online Purchase Information. If you place an order with us, we will record the personal information and details associated with the transaction. We will collect your purchase/subscription information, such as, user ID, items purchased, order ID, payment information for fulling your order. Any payments made via the Services are processed by third-party payment processors. We do not directly collect or store your payment card information, which is handled by third-party service providers.

    user = o.individual('User')
    first_party = o.individual('FirstParty')
    
    o.individual(
                'DataCollectionActivity',

        'If you place an order with us, we will record the personal information and details associated with the transaction. We will collect your purchase/subscription information, such as, user ID, items purchased, order ID, payment information for fulling your order. Any payments made via the Services are processed by third-party payment processors.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'FinancialData',
                'details associated with the transaction',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'FinancialData',
                'purchase/subscription information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'user ID',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'items purchased',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'order ID',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'FinancialData',
                'payment information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for fulling your order.')),
        ]
    )

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    # doesnt
    o.individual(
                'DataCollectionActivity',

        'We do not directly collect or store your payment card information, which is handled by third-party service providers.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'FinancialData',
                'not collect payment card information',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Personal Body and Health Information: When you use Zepp App and our device, your personal body and health information may be collected, such as, heart rate, resting heart rate, heart rate zone, maximum heart rate, minimum heart rate, average heart rate, blood oxygen saturation, stress, PAI, PPG data, ECG data, weight, body fat, BMI.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use Zepp App and our device, your personal body and health information may be collected, such as, heart rate, resting heart rate, heart rate zone, maximum heart rate, minimum heart rate, average heart rate, blood oxygen saturation, stress, PAI, PPG data, ECG data, weight, body fat, BMI.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'your personal body and health information may be collected',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'heart rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'resting heart rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'heart rate zone',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'maximum heart rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'minimum heart rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'average heart rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'blood oxygen saturation',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'stress',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'PAI',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'PPG data',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'ECG data',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'weight',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'body fat',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'BMI',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Exercising Information: When you use the Zepp App and our device for exercising, we may collect your exercising information, such as, steps, stand-up times, total distance, time, total time, total duration, burned calories, consumption, pace, speed, frequency, stride length, maximum oxygen uptake(VO2 Max), exercise capacity, training effects, sports loading, frequency of exercising, strokes, stroke rate, number of trips, number of jumping rope, average stroke distance, movement track, velocity, swolf index, stroke speed and number of floors climbed.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'Exercising Information: When you use the Zepp App and our device for exercising, we may collect your exercising information, such as, steps, stand-up times, total distance, time, total time, total duration, burned calories, consumption, pace, speed, frequency, stride length, maximum oxygen uptake(VO2 Max), exercise capacity, training effects, sports loading, frequency of exercising, strokes, stroke rate, number of trips, number of jumping rope, average stroke distance, movement track, velocity, swolf index, stroke speed and number of floors climbed.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'exercising information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'steps',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'stand-up times',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'total distance',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'time',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'total time',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'total duration',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'burned calories',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'consumption',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'pace',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'speed',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'frequency of exercising',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'strokes',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'stroke rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'number of trips',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'number of jumping rope',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'average stroke distance',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'movement track',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'velocity',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'swolf index',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'stroke speed',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'number of floors climbed.',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Information Recorded by Your Device: When you use the Zepp App to synchronize device data, personal data is recorded. For example, altitude, air pressure, temperature, weather type, volume of earphone, ambient sound, sleep data, rapid eye movement(REM), activity information, the time length of one-legged standing with eyes closed testing and the time of measuring, resistance value.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        '',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'altitude',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'air pressure',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'temperature',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'weather type',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'volume of earphone',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'ambient sound',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'sleep data',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'rapid eye movement(REM)',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'activity information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'the time length of one-legged standing with eyes closed testing and the time of measuring',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'resistance value.',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Device Setting Information: We may collect information of your device settings. For example, status of notification, unit settings, dial layout settings, gesture settings, band wearing settings.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We may collect information of your device settings. For example, status of notification, unit settings, dial layout settings, gesture settings, band wearing settings.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'information of your device settings',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'status of notification',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'unit settings',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'dial layout settings',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'gesture settings',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'band wearing settings.',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Application Setting Information: We may collect information of your device settings on applications. For example, device system setting, exercising functional setting, target of steps, target of exercising, target of weight, target of calories, target of sleep, alarm settings. 

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'information of your device settings on applications',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'device system setting on applications.',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'exercising functional setting',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'target of steps',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'target of exercising',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'target of weight',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'target of calories',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'target of sleep',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'alarm settings.',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Caller Information: When you use the Incoming Call or SMS Alert functions, you will receive an alert about your phone calls, SMS. Your contact information for incoming calls and messages will be synchronized to and displayed on the bundled device. We will not save your caller information in Zepp App or sever.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We will not save your caller information in Zepp App or sever.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'not caller information',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Network Usage Information: We may collect network types, network signals, WLAN information and other similar information related to certain features of the Zepp App.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        '',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'network types',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'network signals',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'WLAN information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'other similar information related to certain features of the Zepp App.',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Music Information: When you use music or music control function, the music information (e.g., name of song, singer, the status of song) will be obtained from your mobile phone and synchronized to the device. This information will only be displayed on the device screen and we will not save this information. When you use the music storage function (only supported by certain devices), then your music will be synchronized to and stored in the device.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use music or music control function, the music information (e.g., name of song, singer, the status of song) will be obtained from your mobile phone and synchronized to the device. This information will only be displayed on the device screen and we will not save this information.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'not the music information (e.g., name of song, singer, the status of song)',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Log Information: We may record some log information when you use the Zepp App. For example, we may collect operating information, hit log, firmware clicking statistics, and server log. When you give us feedback, at your option, your app log and device log will be collected by us.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We may record some log information when you use the Zepp App. For example, we may collect operating information, hit log, firmware clicking statistics, and server log. When you give us feedback, at your option, your app log and device log will be collected by us.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'some log information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'operating information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'hit log',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'firmware clicking statistics',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'server log.',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'your app log',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'device log',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Location Information: When you use location-based program services or features, we may collect your location information such as your GPS information.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use location-based program services or features, we may collect your location information such as your GPS information.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'location information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'your GPS information.',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'location-based program services or features')),
        ]
    )




    #########################################################################
    # Mobile Phone Information: When you use Zepp App, we may collect your mobile phone information, such as, unique identifier (IDFA, IMEI), the operating system version, system time, time zone, alarm clock, brand and model of your mobile phone.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use Zepp App, we may collect your mobile phone information, such as, unique identifier (IDFA, IMEI), the operating system version, system time, time zone, alarm clock, brand and model of your mobile phone.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'mobile phone information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'unique identifier (IDFA, IMEI)',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'the operating system version',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'system time',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'time zone',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'alarm clock',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'brand and model of your mobile phone.',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Device Information: When you use Zepp App to connect a hardware device, such as an Amazfit watch, we may obtain information, such as: the device's unique identifier, device ID, MAC address, serial number, firmware version, Bluetooth, device size. The collection may also apply to your updated system or software and factory settings.  

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use Zepp App to connect a hardware device, such as an Amazfit watch, we may obtain information, such as: the device`s unique identifier, device ID, MAC address, serial number, firmware version, Bluetooth, device size. The collection may also apply to your updated system or software and factory settings.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'device`s unique identifier',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'device ID',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'MAC address',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'serial number',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'firmware version',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'Bluetooth',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'device size.',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Device Unlock Information: When you use the device off-wrist lock function, we may collect your device unlock password to realize this function.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use the device off-wrist lock function, we may collect your device unlock password to realize this function.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'device unlock password',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'use the device off-wrist lock function')),
        ]
    )




    #########################################################################
    # Crash Information: When you choose to upload debug logs to help us analyze the problem, your application debug log file will be sent to the server.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you choose to upload debug logs to help us analyze the problem, your application debug log file will be sent to the server.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'application debug log file',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to upload debug logs to help us analyze the problem')),
        ]
    )




    #########################################################################
    # Information from Friends: Zepp App allows you to add friends. After receiving permission from your friends, the weight, activity and sleep information of your friends will be displayed on your App.

    # Sharing from others to user is not implemented in the ontology




    #########################################################################
    # Information Submitted via Services. When you use various functionalities of the Zepp App, you may submit certain information, such as voice information, a reminder setting or tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.). When you use female health function, the information provided by you will be collected, such as duration of menstruation, menstruation interval, the starting date of your latest menstruation, the starting date and ending date of your menstruation, physical condition and mood during menstruation.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use various functionalities of the Zepp App, you may submit certain information, such as voice information, a reminder setting or tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.).',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'voice information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'reminder setting',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.).',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'use various functionalities')),
        ]
    )

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use female health function, the information provided by you will be collected, such as duration of menstruation, menstruation interval, the starting date of your latest menstruation, the starting date and ending date of your menstruation, physical condition and mood during menstruation.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'duration of menstruation',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'menstruation interval',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'the starting date of your latest menstruation',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'the starting date and ending date of your menstruation',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'physical condition and mood during menstruation',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'HealthMonitoring',
                'use female health function')),
        ]
    )




    #########################################################################
    # Visitor Information: When using the visitor function of our smart scale, a visitor can experience our products and certain limited services. The data of the visitor (gender, height, date of birth) may be collected and used to calculate and present the results of certain services the visitor experiences. You can choose to save the visitor information or not, if you choose to save, the visitor’s gender, height, date of birth and weight will be collected by us.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When using the visitor function of our smart scale, a visitor can experience our products and certain limited services. The data of the visitor (gender, height, date of birth) may be collected and used to calculate and present the results of certain services the visitor experiences. You can choose to save the visitor information or not, if you choose to save, the visitor’s gender, height, date of birth and weight will be collected by us.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'The data of the visitor',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'gender',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'height',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'date of birth',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to calculate and present the results of certain services the visitor experiences.')),

            o.connection('hasDataRetentionTime', o.individual(
                'DataRetentionTime',
                '')),
        ]
    )




    #########################################################################
    # Other Information: We may also collect other types of information which is not directly or indirectly linked to an individual and which is aggregated, anonymized or de-identified. For example, the device function, system status, battery status, Startup & Shutdown status, charging status and connecting status of smartphone of your device may be collected when using a particular service. Such information is collected in order to improve the services we provide to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We may also collect other types of information which is not directly or indirectly linked to an individual and which is aggregated, anonymized or de-identified. For example, the device function, system status, battery status, Startup & Shutdown status, charging status and connecting status of smartphone of your device may be collected when using a particular service. Such information is collected in order to improve the services we provide to you.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'other types of information which is not directly or indirectly linked to an individual',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'the device function',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'system status',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'battery status',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'Startup & Shutdown status',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'charging status',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'connecting status of smartphone',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'PseudoAnonymization',
                'which is aggregated, anonymized or de-identified')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'in order to improve the services we provide to you.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # HOW THE PERSONAL INFORMATION IS USED                                  #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We acquire, hold, use and process personal information for a variety of business purposes including for providing services and/or products to you, to respond to information requested and to fulfill legal compliance on our part under applicable laws. We may also process and disclose personal information to our affiliated companies and to third-party service providers for the purposes stated in this Privacy Policy.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'We acquire, hold, use and process personal information for a variety of business purposes including for providing services and/or products to you, to respond to information requested and to fulfill legal compliance on our part under applicable laws.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for a variety of business purposes including for providing services and/or products to you, to respond to information requested and to fulfill legal compliance on our part under applicable laws.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'under applicable laws.')),
        ]
    )

    o.individual(

        'DataSharingActivity',

        'We may also process and disclose personal information to our affiliated companies and to third-party service providers for the purposes stated in this Privacy Policy.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for the purposes stated in this Privacy Policy.')),
        ]
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

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'We may use information about you to fulfill requests for products, Services, or information, including: Providing, processing, maintaining, improving and developing our goods and/or services to you, including after-sales and customer support and for services on your device; Communicating with you about your device, service or any general queries or other requests and comments, such as updates, customer inquiry support, information about our events, notices; Providing access to certain areas, functionalities, and features of our products and services; Conducting promotional activities, such as sweepstakes and Facebook events; Analyzing and developing statistical information on the use of our products and services to better improve our products and services; Optimizing the performance of your device; Storing and maintaining information about you for our business operations or legal obligations; and Providing local services without communicating with our servers.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'information about you',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to fulfill requests for products, Services, or information, including:')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Providing, processing, maintaining, improving and developing our goods and/or services to you, including after-sales and customer support and for services on your device;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Communicating with you about your device, service or any general queries or other requests and comments, such as updates, customer inquiry support, information about our events, notices;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Providing access to certain areas, functionalities, and features of our products and services;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Conducting promotional activities, such as sweepstakes and Facebook events;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Analyzing and developing statistical information on the use of our products and services to better improve our products and services;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Optimizing the performance of your device;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Storing and maintaining information about you for our business operations or legal obligations; and')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Providing local services without communicating with our servers.')),
        ]
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

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'We may use personal information about you for administrative purposes, including to: Measure interest in our services; Develop new products and services; Ensure internal quality control; Verify your identity; Communicate about accounts and activities on our services and systems, and, in our discretion, changes to any of our policies; Send email to the email address you provide to us to verify your account and for informational and operational purposes, such as account management, customer service, or system maintenance; Prevent potentially prohibited or illegal activities; and Enforce our Service Agreement and/or Privacy Policy.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Measure interest in our services;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Develop new products and services;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Ensure internal quality control;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Verify your identity;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Communicate about accounts and activities on our services and systems, and, in our discretion, changes to any of our policies;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Send email to the email address you provide to us to verify your account and for informational and operational purposes, such as account management, customer service, or system maintenance;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Prevent potentially prohibited or illegal activities; and')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Enforce our Service Agreement and/or Privacy Policy.')),
        ]
    )




    #########################################################################
    # Marketing Our Products and Services. If permitted by applicable laws, we may use your personal information, such as your email address, account ID, to provide you with materials directly or through third-party service provider(s) about offers, products, and services, including new content or services. We may provide you with these materials by phone, postal mail, facsimile, or email, or as otherwise permitted by applicable law. Such uses include:
    # To notify you about offers, products, and services that may be of interest to you;
    # For other purposes disclosed at the time that individuals provide personal information; and
    # Otherwise with your consent.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'If permitted by applicable laws, we may use your personal information, such as your email address, account ID, to provide you with materials directly or through third-party service provider(s) about offers, products, and services, including new content or services. We may provide you with these materials by phone, postal mail, facsimile, or email, or as otherwise permitted by applicable law. Such uses include: To notify you about offers, products, and services that may be of interest to you; For other purposes disclosed at the time that individuals provide personal information; and Otherwise with your consent.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'email address',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'account ID',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to provide you with materials directly or through third-party service provider(s) about offers, products, and services, including new content or services.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'To notify you about offers, products, and services that may be of interest to you;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'For other purposes disclosed at the time that individuals provide personal information; and')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'Otherwise with your consent.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'permitted by applicable laws')),
        ]
    )




    #########################################################################
    # You have the right to opt out of our proposed use of your personal information for direct marketing. If you no longer wish to receive certain types of email communication you may opt-out by following the unsubscribe link located at the bottom of each communication.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'UserOptControl',

        'You have the right to opt out of our proposed use of your personal information for direct marketing. If you no longer wish to receive certain types of email communication you may opt-out by following the unsubscribe link located at the bottom of each communication.',

        [
            o.connection('activityIsInitiatedBy', user),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'your personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for direct marketing')),
        ]
    )




    #########################################################################
    # Research and Development. We may use personal information to create non-identifiable information that we may use alone or in the aggregate with information obtained from other sources, in order to help us to optimally deliver our existing products and services or develop new products and services and we may share these statistics with the public or third parties in order to present the preference and trend analysis.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'We may use personal information to create non-identifiable information that we may use alone or in the aggregate with information obtained from other sources, in order to help us to optimally deliver our existing products and services or develop new products and services',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'PseudoAnonymization',
                'non-identifiable')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to create non-identifiable information that we may use alone or in the aggregate with information obtained from other sources, in order to help us to optimally deliver our existing products and services or develop new products and services')),
        ]
    )

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataSharingActivity',

        'and we may share these statistics with the public or third parties in order to present the preference and trend analysis.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'NonPersonalData',
                'statistics',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'in order to present the preference and trend analysis.')),
        ]
    )




    #########################################################################
    # Services via Mobile Devices (only in certain feature). From time to time, we may provide products and services that are specifically designed to be compatible and used on mobile devices. We will collect certain information that your mobile device sends when you use such products and services, like a device identifier, user settings, location information, mobile carrier, and the operating system of your device. Mobile versions of our products and services may require that users log in with an account. In such cases, information about use of mobile versions of the products and services may be associated with accounts. In addition, we may enable you to download an application, widget, or other tool that can be used on mobile or other computing devices. Some of these tools may store information on mobile or other devices. These tools may transmit personal information to us to enable you to access your accounts and to enable us and our third-party service providers to track use of these tools. Some of these tools may enable users to transmit reports and other information from the tool. We may use personal or non-identifiable information transmitted to us to enhance these tools, to develop new tools, for quality improvement and as otherwise described in this Privacy Policy or in other notices we provide.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'We will collect certain information that your mobile device sends when you use such products and services, like a device identifier, user settings, location information, mobile carrier, and the operating system of your device. Mobile versions of our products and services may require that users log in with an account. In such cases, information about use of mobile versions of the products and services may be associated with accounts. In addition, we may enable you to download an application, widget, or other tool that can be used on mobile or other computing devices. Some of these tools may store information on mobile or other devices. These tools may transmit personal information to us to enable you to access your accounts and to enable us and our third-party service providers to track use of these tools. Some of these tools may enable users to transmit reports and other information from the tool.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'information that your mobile device sends',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'device identifier,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'user settings',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'location information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'mobile carrier',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'operating system of your device.',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'users log in with an account.',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'reports and other information from the tool.',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to enable you to access your accounts and to enable us and our third-party service providers to track use of these tools.')),
        ]
    )

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'We may use personal or non-identifiable information transmitted to us to enhance these tools, to develop new tools, for quality improvement and as otherwise described in this Privacy Policy or in other notices we provide.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'NonPersonalData',
                'non-identifiable information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'PseudoAnonymization',
                'non-identifiable')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to enhance these tools, to develop new tools, for quality improvement and as otherwise described in this Privacy Policy or in other notices we provide.')),
        ]
    )




    #########################################################################
    # De-identified, Anonymous and/or Aggregated Information Use. We may use personal information and other information about you to create de-identified, anonymized and/or aggregated information, such as de-identified demographic information, de-identified location information, information about the mobile phone or device from which you access Zepp App, or other analyses we create. De-identified, anonymized and/or aggregated information is not personal information, and we may use such information in a number of ways, including research, internal analysis, analytics, and any other legally permissible purposes.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'De-identified, Anonymous and/or Aggregated Information Use. We may use personal information and other information about you to create de-identified, anonymized and/or aggregated information, such as de-identified demographic information, de-identified location information, information about the mobile phone or device from which you access Zepp App, or other analyses we create. De-identified, anonymized and/or aggregated information is not personal information, and we may use such information in a number of ways, including research, internal analysis, analytics, and any other legally permissible purposes.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'PseudoAnonymization',
                'de-identified, anonymized and/or aggregated')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to create de-identified, anonymized and/or aggregated information, such as de-identified demographic information, de-identified location information, information about the mobile phone or device from which you access Zepp App, or other analyses we create.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'in a number of ways, including research, internal analysis, analytics, and any other legally permissible purposes.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'legally permissible')),
        ]
    )




    #########################################################################
    # Improving User Experience. Some opt-in features allow us or our third party partners to analyze data about how users use our products and services, so as to improve the user experience, such as sending crash reports.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'UserOptControl',

        'Improving User Experience. Some opt-in features allow us or our third party partners to analyze data about how users use our products and services, so as to improve the user experience, such as sending crash reports.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'crash reports',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to improve the user experience')),
        ]
    )




    #########################################################################
    # Specific Ways Personal Information is Used in Products and Services. Here are more details on how we may use your information (which may include personal information):

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'Here are more details on how we may use your information (which may include personal information):',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # To Set Up Your Account for Zepp App. Personal information collected when creating an account through our Zepp App is used for creating the personal account and profile page for the user.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'Personal information collected when creating an account through our Zepp App is used for creating the personal account and profile page for the user.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'Personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'is used for creating the personal account and profile page for the user.')),
        ]
    )




    #########################################################################
    # To Calculate Exercise Results. Personal body information is used to accurately calculate and display the exercise result to you, such as, exercising records, distance, exercising time, total duration, burned calories, consumption, pace, speed, maximum oxygen uptake (VO2 Max), exercise capacity, training effects.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'Personal body information is used to accurately calculate and display the exercise result to you, such as, exercising records, distance, exercising time, total duration, burned calories, consumption, pace, speed, maximum oxygen uptake (VO2 Max), exercise capacity, training effects.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'Personal body information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'exercising records',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'distance',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'exercising time',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'total duration',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'burned calories',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'consumption',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'pace',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'speed',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'maximum oxygen uptake (VO2 Max)',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'exercise capacity',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'training effects.',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'HealthMonitoring',
                'is used to accurately calculate and display the exercise result to you')),
        ]
    )




    #########################################################################
    # Physical Analysis. Based on the personal information you provided and the data recorded by the device, we will provide you an analysis related to your physical condition for your reference, such as PAI, BMI, muscle mass, body fat percentage, water percentage, protein, basal metabolic rate, subcutaneous fat, skeletal muscle mass, visceral fat level, bone mass content, pressure, body shape, body age.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'Based on the personal information you provided and the data recorded by the device, we will provide you an analysis related to your physical condition for your reference, such as PAI, BMI, muscle mass, body fat percentage, water percentage, protein, basal metabolic rate, subcutaneous fat, skeletal muscle mass, visceral fat level, bone mass content, pressure, body shape, body age.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'data recorded by the device',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'PAI',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'BMI',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'muscle mass',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'body fat percentage',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'water percentage',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'protein',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'basal metabolic rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'subcutaneous fat',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'skeletal muscle mass',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'visceral fat level',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'bone mass content',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'pressure',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'body shape',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'body age',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'HealthMonitoring',
                'provide you an analysis related to your physical condition for your reference')),
        ]
    )




    #########################################################################
    # Sleep Analysis. Based on the personal information you have provided and the data recorded by the device, such as PPG, heart rate, we will record your naps, sleep time, sleep breathing and provide you a sleep score and sleep analysis related to your sleep quality for your reference.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'Based on the personal information you have provided and the data recorded by the device, such as PPG, heart rate, we will record your naps, sleep time, sleep breathing and provide you a sleep score and sleep analysis related to your sleep quality for your reference.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'naps',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'sleep time',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'sleep breathing',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'sleep score',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'sleep analysis',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                '',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                '',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                '',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                '',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                '',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'HealthMonitoring',
                'for your reference')),
        ]
    )




    #########################################################################
    # To Provide World Clock Service. When you add a world clock in Zepp App, we will calculate the local time corresponding to your selected area based on the time at your mobile phone and display it in Zepp App and the bundled devices that support the world clock function.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'we will calculate the local time corresponding to your selected area based on the time at your mobile phone and display it in Zepp App and the bundled devices that support the world clock function.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'your selected area',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'display it in Zepp App and the bundled devices that support the world clock function.')),

            o.connection('hasDataRetentionTime', o.individual(
                'DataRetentionTime',
                '')),
        ]
    )




    #########################################################################
    # To Provide Alarm Clock Service: when you use alarm clock function, your alarm clock information will be displayed in Zepp App and the bundled device.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'when you use alarm clock function, your alarm clock information will be displayed in Zepp App and the bundled device.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'alarm clock information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'will be displayed in Zepp App and the bundled device.')),
        ]
    )




    #########################################################################
    # To Provide Voice Related Service: When you use off-line or on-line voice assistant function (only supported by certain device in certain countries/areas), such as Alexa, we will collect your voice request, for the purpose of carrying out your orders. Your voice information may also be used to provide voice memo service to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use off-line or on-line voice assistant function (only supported by certain device in certain countries/areas), such as Alexa, we will collect your voice request, for the purpose of carrying out your orders. Your voice information may also be used to provide voice memo service to you.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'BiometricData',
                'your voice request',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for the purpose of carrying out your orders.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to provide voice memo service to you.')),
        ]
    )




    #########################################################################
    # To Provide Female Health Service. When you use female health function, certain information related to menstrual period will be recorded and displayed in Zepp App or on some devices that support this function. If you turn on the physiological period intelligent prediction mode, we will predict your menstrual period and remind you based on the information you provided.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'When you use female health function, certain information related to menstrual period will be recorded and displayed in Zepp App or on some devices that support this function. If you turn on the physiological period intelligent prediction mode, we will predict your menstrual period and remind you based on the information you provided.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'information related to menstrual period',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'HealthMonitoring',
                'predict your menstrual period and remind you based on the information you provided.')),
        ]
    )




    #########################################################################
    # To Provide Blood Oxygen Saturation Measurement Function. When you turn on the blood oxygen measurement function, we will collect your blood oxygen saturation information to show the value to you or to assist providing a sleeping analysis to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'we will collect your blood oxygen saturation information to show the value to you or to assist providing a sleeping analysis to you.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'blood oxygen saturation information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'HealthMonitoring',
                'to show the value to you or to assist providing a sleeping analysis to you.')),
        ]
    )




    #########################################################################
    # To Provide Notification Reminder Service. When you enable the notification reminder function, the reminder information you set in the Zepp App will be pushed to the bundled device.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'When you enable the notification reminder function, the reminder information you set in the Zepp App will be pushed to the bundled device.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'reminder information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'reminder information you set in the Zepp App will be pushed to the bundled device.')),
        ]
    )




    #########################################################################
    # To Provide Bluetooth Camera Function. When you use Bluetooth camera function, your mobile phone will be connected with the device through Bluetooth for controlling the camera.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataActivity',

        'When you use Bluetooth camera function, your mobile phone will be connected with the device through Bluetooth for controlling the camera.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'SensitiveData',
                'Bluetooth camera',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # To Provide Zepp App Services. When you connect certain devices with Zepp App, the information collected through the device will be shown to user.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you connect certain devices with Zepp App, the information collected through the device will be shown to user.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # To Provide eSIM(embedded SIM) Function. (only supported by certain devices and in certain countries/areas). After you successfully activate eSIM with telecom carriers, you may use the device alone to call or receive a call, to send or receive SMS (SMS service is subject to local telecom carriers). When you use eSIM function, we will collect your operation records. Your phone number, call records, short messages will be stored in the device, but if you choose to upload this information together with the log, this information will be uploaded and stored in our cloud.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'GiveConsentActivity',

        'When you use eSIM function, we will collect your operation records. Your phone number, call records, short messages will be stored in the device, but if you choose to upload this information together with the log, this information will be uploaded and stored in our cloud.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'operation records.',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'phone number',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'call records',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'short messages',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # To Display Caller Information. When you receive a call, text messages, caller information will be displayed on the device. You may even answer or reject a phone call by the device directly (only supported by certain devices).

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'When you receive a call, text messages, caller information will be displayed on the device. You may even answer or reject a phone call by the device directly (only supported by certain devices).',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'SensitiveData',
                'text messages',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'caller information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'will be displayed on the device.')),
        ]
    )




    #########################################################################
    # To Provide Bluetooth Phone Services (only supported by certain devices). With the device successfully paired with your mobile phone’s Bluetooth, when you receive an incoming call, the incoming call information will be displayed on the device. You can even use the device to answer or hang up the call. If you have missed calls, the relevant information will also be displayed on the device. You may add or delete your frequent contacts information in Zepp App. The frequent contacts information added by you will be bound to your account and synchronized to the device and our cloud.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        '',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'incoming call information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'frequent contacts information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'You can even use the device to answer or hang up the call. If you have missed calls, the relevant information will also be displayed on the device.')),
        ]
    )




    #########################################################################
    # To Display Music Information. When you use music control function, the music information (name of song, singer, volume, the status of song) will be displayed on the device.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'When you use music control function, the music information (name of song, singer, volume, the status of song) will be displayed on the device.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'music information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'name of song',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'singer',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'volume',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'the status of song',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'will be displayed on the device.')),
        ]
    )




    #########################################################################
    # To Provide AI Sleep Melody Service. When you use AI Sleep Melody service, we will collect and use your personal information, such as heart rate, activity data, sleep data and your music reference to recommend sleep melodies to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you use AI Sleep Melody service, we will collect and use your personal information, such as heart rate, activity data, sleep data and your music reference to recommend sleep melodies to you.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'heart rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'activity data',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'sleep data',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'your music reference',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to recommend sleep melodies to you.')),
        ]
    )

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'When you use AI Sleep Melody service, we will collect and use your personal information, such as heart rate, activity data, sleep data and your music reference to recommend sleep melodies to you.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'heart rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'activity data',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'sleep data',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'NonSensitiveData',
                'your music reference',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to recommend sleep melodies to you.')),
        ]
    )




    #########################################################################
    # To Provide Hearing Health Function (only supported by certain earphone). If you turn on this function, we will collect your earphone volume in real time and recommend listening time for the current week based on the hearing protection standards established by the World Health Organization (WHO).

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'If you turn on this function, we will collect your earphone volume in real time and recommend listening time for the current week based on the hearing protection standards established by the World Health Organization (WHO).',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'earphone volume',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'recommend listening time for the current week based on the hearing protection standards established by the World Health Organization (WHO).')),
        ]
    )




    #########################################################################
    # To Provide Cervical Protection Function (only supported by certain earphone). If you turn on this function, the earphone sensor will detect and present you with habitual head-lowering angle. If you turn on the relax prompt, the earphone will play music to remind you to relax your spine for long periods of time.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'If you turn on this function, the earphone sensor will detect and present you with habitual head-lowering angle. If you turn on the relax prompt, the earphone will play music to remind you to relax your spine for long periods of time.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'habitual head-lowering angle.',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'HealthMonitoring',
                'the earphone will play music to remind you to relax your spine for long periods of time.')),
        ]
    )




    #########################################################################
    # To Provide Noise Control Function (only supported by certain earphone). When you turn on ANC function, we will collect and cancel ambient sound in accordance with the mode set by you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'When you turn on ANC function, we will collect and cancel ambient sound in accordance with the mode set by you.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'ambient sound',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # To Provide Tap for Report Function (only supported by certain earphone). If you turn on this function, we will collect your current speed, heart rate and other workout information. By simply taping the earphone, this information will be broadcasted to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'If you turn on this function, we will collect your current speed, heart rate and other workout information. By simply taping the earphone, this information will be broadcasted to you.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'current speed',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'heart rate',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'other workout information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'HealthMonitoring',
                'will be broadcasted to you.')),
        ]
    )




    #########################################################################
    # To Determine Whether the Mobile Phone is Supported. Phone information will be used to determine if your device can use Zepp App.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'Phone information will be used to determine if your device can use Zepp App.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'Phone information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to determine if your device can use Zepp App.')),
        ]
    )




    #########################################################################
    # To Measure the Temperature (only supported by certain devices). The device will measure the temperature and display the data to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'The device will measure the temperature and display the data to you.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'temperature',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'HealthMonitoring',
                'display the data to you.')),
        ]
    )




    #########################################################################
    # To Provide Network Related Services. We use network types, network signals, etc. to prompt the user to download updates in different network environments. Certain devices (such as Amazfit smart scale) can directly connect to the server via WLAN, and upload your measurement (such as your weight, body fat, BMI and etc.) and the device identifier to the cloud accessible in the Zepp App.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We use network types, network signals, etc. to prompt the user to download updates in different network environments. Certain devices (such as Amazfit smart scale) can directly connect to the server via WLAN, and upload your measurement (such as your weight, body fat, BMI and etc.) and the device identifier to the cloud accessible in the Zepp App.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'measurement',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'weight',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'body fat',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'BMI',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'device identifier',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # To Provide Off-wrist Lock Function. Your device unlock password will be used to the off-wrist lock function. If you turn on this function, your device will be locked when the device detects that it is off-wrist. If the wrong password is entered on the device more than a certain number of times, your device will be locked up. To unlock the device, you need to change the device unlock password or restore the Factory Settings on device in Zepp App.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'Your device unlock password will be used to the off-wrist lock function.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'device unlock password',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'will be used to the off-wrist lock function.')),
        ]
    )




    #########################################################################
    # To Provide Location-based Services. In the course of using our services, location information may also be used by us or third-party service providers to provide and improve our services. For example, we may use your GPS information to provide you with weather details, calculating the distance of your outdoor sporting or mapping such activity. You may turn this off at any time by going into the device settings of your mobile devices or discontinue use of that application.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataSharingActivity',

        'In the course of using our services, location information may also be used by us or third-party service providers to provide and improve our services. For example, we may use your GPS information to provide you with weather details, calculating the distance of your outdoor sporting or mapping such activity.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('sharesDataWithAgent', o.individual(
                'ThirdParties', 
                'third parties.')),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'location information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'GPS information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to provide and improve our services.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to provide you with weather details, calculating the distance of your outdoor sporting or mapping such activity.')),
        ]
    )

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'GiveConsentActivity',

        'You may turn this off at any time by going into the device settings of your mobile devices or discontinue use of that application.',

        [
            o.connection('activityIsInitiatedBy', user),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'location information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'GPS information',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # To Optimize Our Products and Services. We use your personal information, such as, Huami ID, log information, debug information, the information automatically collected to provide functionality, analyze performance, fix errors, and improve the quality of our products and services. For example, we may use these information to optimize pages/function display, determining the importance of each product function, guiding us to adjust the priority of the development of product features.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'We use your personal information, such as, Huami ID, log information, debug information, the information automatically collected to provide functionality, analyze performance, fix errors, and improve the quality of our products and services. For example, we may use these information to optimize pages/function display, determining the importance of each product function, guiding us to adjust the priority of the development of product features.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'Huami ID',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'log information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'debug information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to provide functionality, analyze performance, fix errors, and improve the quality of our products and services.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to optimize pages/function display, determining the importance of each product function, guiding us to adjust the priority of the development of product features.')),
        ]
    )




    #########################################################################
    # To Manage Devices. This information provides the ability to manage the bundled devices.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'This information provides the ability to manage the bundled devices.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'provides the ability to manage the bundled devices.')),
        ]
    )




    #########################################################################
    # To Improve Software Stability. We collect crash logs for analyzing software quality to provide better service.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We collect crash logs for analyzing software quality to provide better service.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'crash logs',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for analyzing software quality to provide better service.')),
        ]
    )




    #########################################################################
    # To Improve Device Stability. We may use the information to improve the bundled devices.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataUseActivity',

        'We may use the information to improve the bundled devices.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to improve the bundled devices.')),
        ]
    )




    #########################################################################
    # To Send Notices. From time to time, we may use your personal information to send important notices, such as communications about changes to our terms, conditions, and policies.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'PolicyChangeActivity',

        'From time to time, we may use your personal information to send important notices, such as communications about changes to our terms, conditions, and policies.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'your personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasNotificationMechanism', o.individual(
                'NotificationMechanism',
                'important notices, such as communications about changes')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to send important notices')),
        ]
    )




    #########################################################################
    #                                                                       #
    # COOKIES AND OTHER TECHNOLOGIES                                        #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We, as well as our third-party service providers that provide content, advertising, or other functionality on our Services, may use cookies, pixel tags, local storage, and other technologies (“Technologies”) to automatically collect information through the Services. We use Technologies that are essentially small data files placed on your computer, tablet, mobile phone, or other devices that allow us to record certain pieces of information whenever you visit or interact with our websites, services, applications, messaging, and tools, and to recognize you across devices.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'We, as well as our third-party service providers that provide content, advertising, or other functionality on our Services, may use cookies, pixel tags, local storage, and other technologies (“Technologies”) to automatically collect information through the Services. We use Technologies that are essentially small data files placed on your computer, tablet, mobile phone, or other devices that allow us to record certain pieces of information whenever you visit or interact with our websites, services, applications, messaging, and tools, and to recognize you across devices.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'cookies',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to recognize you across devices.')),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'through the Services.')),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'pixel tags')),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'local storage')),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'cookies')),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'other technologies (“Technologies”)')),
        ]
    )




    #########################################################################
    # What Information is Collected and How We Use Them: Technologies such as cookies, tags, and scripts are used by us and our third-party service providers. These Technologies are used in analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole. We may receive reports based on the use of these technologies by these companies on an individual as well as aggregated basis.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'Technologies such as cookies, tags, and scripts are used by us and our third-party service providers. These Technologies are used in analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole. We may receive reports based on the use of these technologies by these companies on an individual as well as aggregated basis.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'cookies',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'cookies')),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'tags')),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'scripts')),

            o.connection('hasSecurityMechanism', o.individual(
                'PseudoAnonymization',
                'aggregated basis.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole.')),
        ]
    )

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'Technologies such as cookies, tags, and scripts are used by us and our third-party service providers. These Technologies are used in analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole. We may receive reports based on the use of these technologies by these companies on an individual as well as aggregated basis.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'cookies',
                [o.connection('isProvidedBy', o.individual(
                'ThirdParties', 
                'third parties.'))])),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'cookies')),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'tags')),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'scripts')),

            o.connection('hasSecurityMechanism', o.individual(
                'PseudoAnonymization',
                'aggregated basis.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole.')),
        ]
    )




    #########################################################################
    # Cookies. Cookies are small text files placed in visitors’ device browsers to store their preferences. Most browsers allow you to block and delete cookies. However, if you do that, the website may not work properly.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'ConsentActivity',

        'Cookies are small text files placed in visitors’ device browsers to store their preferences. Most browsers allow you to block and delete cookies. However, if you do that, the website may not work properly.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'cookies',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasUserChoiceConsequence', o.individual(
                'PartialServiceRestriction',
                'However, if you do that, the website may not work properly.')),
        ]
    )




    #########################################################################
    # Pixel Tags/Web Beacons. A pixel tag (also known as a web beacon) is a piece of code embedded on the website that collects information about users’ engagement on that web page. The use of a pixel allows us to record, for example, that a user has visited a particular web page or clicked on a particular advertisement.

    user = o.individual('User')
    first_party = o.individual('FirstParty')
    
    o.individual(
                'DataCollectionActivity',

        'A pixel tag (also known as a web beacon) is a piece of code embedded on the website that collects information about users’ engagement on that web page. The use of a pixel allows us to record, for example, that a user has visited a particular web page or clicked on a particular advertisement.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'information about users’ engagement on that web page',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataCollectionMechanism', o.individual(
                'DataCollectionMechanism',
                'pixel tag (also known as a web beacon)')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to record, for example, that a user has visited a particular web page or clicked on a particular advertisement')),
        ]
    )




    #########################################################################
    # Social Media Widgets: Our products, services and website may include social media features such as connectivity with Facebook, Google,Twitter, Strava, Line (that might include widgets such as the share this button or other interactive mini-programs). These features may collect your IP address, which page you are visiting on our website, and may set a cookie/or use some device or location information to enable the feature to function properly. These social media features are either hosted by a third party or hosted directly by us. Your interactions with these features are governed by the privacy policy of the company providing it.

    # user = o.individual('User', 'your')
    first_party = o.individual('FirstParty')
    third_parties = [
        o.connection('isProvidedBy', o.individual('ThirdParties', 'third party')),
        o.connection('isProvidedBy', o.individual('ThirdParties', 'Facebook')),
        o.connection('isProvidedBy', o.individual('ThirdParties', 'Google')),
        o.connection('isProvidedBy', o.individual('ThirdParties', 'Twitter')),
        o.connection('isProvidedBy', o.individual('ThirdParties', 'Strava')),
        o.connection('isProvidedBy', o.individual('ThirdParties', 'Line')),
    ]

    data = [

        o.connection('isAppliedTo', o.individual(
            'TrackingData',
            'IP address',
            [*third_parties])),

        o.connection('isAppliedTo', o.individual(
            'TrackingData',
            'which page you are visiting on our website,',
            [*third_parties])),

        o.connection('isAppliedTo', o.individual(
            'TrackingData',
            'cookies',
            [*third_parties])),

        o.connection('isAppliedTo', o.individual(
            'DeviceData',
            'device',
            [*third_parties])),

        o.connection('isAppliedTo', o.individual(
            'TrackingData',
            'location information',
            [*third_parties])),
    ]

    o.individual(

        'DataCollectionActivity',

        'Social Media Widgets: Our products, services and website may include social media features such as connectivity with Facebook, Google,Twitter, Strava, Line (that might include widgets such as the share this button or other interactive mini-programs). These features may collect your IP address, which page you are visiting on our website, and may set a cookie/or use some device or location information to enable the feature to function properly. These social media features are either hosted by a third party or hosted directly by us. Your interactions with these features are governed by the privacy policy of the company providing it.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', data),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to enable the feature to function properly.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'Your interactions with these features are governed by the privacy policy of the company providing it.')),
        ]
    )




    #########################################################################
    # Log Files: As true of most websites, we gather certain information and store it in log files. This information may include Internet protocol (IP) addresses, browser type, Internet service provider (ISP), referring/exit pages, operating system, date/time stamp, and/or clickstream data.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'Log Files: As true of most websites, we gather certain information and store it in log files. This information may include Internet protocol (IP) addresses, browser type, Internet service provider (ISP), referring/exit pages, operating system, date/time stamp, and/or clickstream data.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'certain information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'Internet protocol (IP) addresses,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'browser type,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'Internet service provider (ISP),',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'referring/exit pages,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AppData',
                'operating system,',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'TrackingData',
                'date/time stamp,')),

            o.connection('hasNotificationMechanism', o.individual(
                'ServiceData',
                'clickstream data.')),
        ]
    )




    #########################################################################
    # Mobile Analytics: Within some of our mobile applications, we use mobile analytics software to allow us to better understand the functionality of our mobile software on your phone. This software may record information such as how often you use the application, the events that occur within the application, aggregated usage, performance data, and where crashes occur within the application.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'we')

    o.individual(

        'DataCollectionActivity',

        'Mobile Analytics: Within some of our mobile applications, we use mobile analytics software to allow us to better understand the functionality of our mobile software on your phone. This software may record information such as how often you use the application, the events that occur within the application, aggregated usage, performance data, and where crashes occur within the application.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'how often you use the application,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'the events that occur within the application,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'aggregated usage,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'performance data,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'where crashes occur within the application.',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to better understand the functionality of our mobile software on your phone.')),

            o.connection('hasSecurityMechanism', o.individual(
                'PseudoAnonymization',
                'aggregated')),
        ]
    )




    #########################################################################
    # Local Storage – HTML5: We use Local Storage Objects (LSOs) such as HTML5 to store content and preferences. Third parties with whom we partner to provide certain features on our websites or to display advertising based upon your web browsing activity also use HTML5 to collect and store information. Various browsers may offer their own management tool for removing HTML5 LSOs.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')
    third_parties = o.individual('ThirdParties')

    data = o.individual(
                'Data',
                'content and preferences.',
                [o.connection('isProvidedBy', user)])

    o.individual(

        'DataCollectionActivity',

        'Local Storage – HTML5: We use Local Storage Objects (LSOs) such as HTML5 to store content and preferences. Third parties with whom we partner to provide certain features on our websites or to display advertising based upon your web browsing activity also use HTML5 to collect and store information. Various browsers may offer their own management tool for removing HTML5 LSOs.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('activityIsInitiatedBy', o.individual(
                third_parties)),

            o.connection('isAppliedTo', data),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to provide certain features on our websites')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to display advertising based upon your web browsing activity')),

            o.connection('initiatesAnotherActivity', o.individual(
                'UserOptControl',
                'management tool for removing HTML5 LSOs.',
                [
                    o.connection('activityIsInitiatedBy', user),

                    o.connection('isAppliedTo', data),
                ])),
        ]
    )




    #########################################################################
    # Website Analytics. We may use Technologies and other third-party tools to process analytics information on our Services (e.g., Google Analytics). For more about Google Analytics information, please visit Google Analytics’ Privacy Policy. To learn more about how to opt-out of Google Analytics’ use of your information on our website, please click here.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')
    third_parties = o.individual('ThirdParties', 'Google Analytics')

    data = o.individual(
                'Data',
                'analytics information',
                [o.connection('isProvidedBy', third_parties)])

    o.individual(

        'DataCollectionActivity',

        'Website Analytics. We may use Technologies and other third-party tools to process analytics information on our Services (e.g., Google Analytics). For more about Google Analytics information, please visit Google Analytics’ Privacy Policy. To learn more about how to opt-out of Google Analytics’ use of your information on our website, please click here.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to process analytics information on our Services')),

            o.connection('initiatesAnotherActivity', o.individual(
                'UserAccessControl',
                'verifiable parental consent.',
                [
                    o.connection('activityIsInitiatedBy', user),

                    o.connection('isAppliedTo', data),
                ])),
        ]
    )




    #########################################################################
    # Operationally Necessary. We may use cookies, or other similar technologies that are necessary to the operation of our services, applications, and tools. This includes technologies that allow you access to our services, applications, and tools; that are required to identify irregular website behavior, prevent fraudulent activity and improve security; or that allow you to make use of our functions such as shopping-carts, saved search, or similar functions;

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    o.individual(

        'DataCollectionActivity',

        'Operationally Necessary. We may use cookies, or other similar technologies that are necessary to the operation of our services, applications, and tools. This includes technologies that allow you access to our services, applications, and tools; that are required to identify irregular website behavior, prevent fraudulent activity and improve security; or that allow you to make use of our functions such as shopping-carts, saved search, or similar functions;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'other similar technologies',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'cookies',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to the operation of our services, applications, and tools.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to identify irregular website behavior,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'prevent fraudulent activity and improve security;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to make use of our functions such as shopping-carts, saved search, or similar functions;')),
        ]
    )




    #########################################################################
    # Performance Related. We may use cookies, or other similar technologies to assess the performance of our websites, applications, services, and tools, including as part of our analytic practices to help us understand how our visitors use our websites, determine if you have interacted with our messaging, determine whether you have viewed an item or link, or to improve our website content, applications, services, or tools;

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    o.individual(

        'DataCollectionActivity',

        'Performance Related. We may use cookies, or other similar technologies to assess the performance of our websites, applications, services, and tools, including as part of our analytic practices to help us understand how our visitors use our websites, determine if you have interacted with our messaging, determine whether you have viewed an item or link, or to improve our website content, applications, services, or tools;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                '',
                'cookies',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                '',
                'other similar technologies',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to assess the performance of our websites, applications, services, and tools, including as part of our analytic practices to help us understand how our visitors use our websites,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'determine if you have interacted with our messaging,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'determine whether you have viewed an item or link,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to improve our website content, applications, services, or tools;')),
        ]
    )




    #########################################################################
    # Functionality Related. We may use cookies, web beacons, or other similar technologies that allow us to offer you enhanced functionality when accessing or using our websites, services, applications, or tools. This may include identifying you when you sign into our websites or keeping track of your specified preferences, interests, or past items viewed so that we may enhance the presentation of content on our websites;

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataCollectionActivity',

        'Functionality Related. We may use cookies, web beacons, or other similar technologies that allow us to offer you enhanced functionality when accessing or using our websites, services, applications, or tools. This may include identifying you when you sign into our websites or keeping track of your specified preferences, interests, or past items viewed so that we may enhance the presentation of content on our websites;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'cookies,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'web beacons,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'other similar technologies',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to offer you enhanced functionality when accessing or using our websites, services, applications, or tools.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'This may include identifying you when you sign into our websites or keeping track of your specified preferences, interests, or past items viewed so that we may enhance the presentation of content on our websites;')),
        ]
    )




    #########################################################################
    # If you would like to opt out of the Technologies we employ on our websites, services, applications, or tools, you may do so by blocking, deleting, or disabling them as your browser or device permits.

    user = o.individual('User', 'you')

    o.individual(

        'UserOptControl',

        'If you would like to opt out of the Technologies we employ on our websites, services, applications, or tools, you may do so by blocking, deleting, or disabling them as your browser or device permits.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),


            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'blocking, deleting, or disabling them as your browser or device permits.')),
        ]
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

    user = o.individual('User', 'your')
    first_party = o.individual('FirstParty', 'We')
    third_parties = o.individual('ThirdParties', 'third parties')

    o.individual(

        'DataSharingActivity',

        'We may disclose your personal information on occasion to third parties (as described below) in order to provide the products or services that you have requested.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('sharesDataWithAgent', o.individual(
                third_parties)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'in order to provide the products or services that you have requested.')),
        ]
    )




    #########################################################################
    # Disclosure may be made to third-party service providers and affiliated companies listed in this section below. In each case described in this section, you can be assured that we will only share your personal information in accordance with this Privacy Policy and the applicable terms that govern your use of our services. We will engage sub-processors for the processing of your personal information. You should know that when we share your personal information with a third-party service provider under any circumstance described in this section, we will contractually specify that the third party is subject to practices and obligations to comply with applicable local data protection laws. We will contractually ensure compliance by any third-party service providers with the privacy standards that apply to them in your home jurisdiction.

    user = o.individual('User', 'you')
    first_party = o.individual('FirstParty')


    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'third-party service providers')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'affiliated companies')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'sub-processors')),
    ]

    o.individual(

        'DataSharingActivity',

        'Disclosure may be made to third-party service providers and affiliated companies listed in this section below. In each case described in this section, you can be assured that we will only share your personal information in accordance with this Privacy Policy and the applicable terms that govern your use of our services. We will engage sub-processors for the processing of your personal information. You should know that when we share your personal information with a third-party service provider under any circumstance described in this section, we will contractually specify that the third party is subject to practices and obligations to comply with applicable local data protection laws. We will contractually ensure compliance by any third-party service providers with the privacy standards that apply to them in your home jurisdiction.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            *third_parties,

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'SecurityMechanism',
                'privacy standards')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'in accordance with this Privacy Policy')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'the applicable terms that govern your use of our services.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'applicable local data protection laws.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # ONWARD TRANSFER: SHARING WITH OUR GROUP, THIRD PARTY                  #
    # SERVICE PROVIDERS AND OTHERS                                          #
    #                                                                       #
    #########################################################################




    #########################################################################
    # In order to conduct business operations smoothly in providing you with the full capabilities of our products and services, we may disclose your personal information from time to time to our affiliated companies. We may also share your information as described in this Privacy Policy with our third-party service providers, to comply with legal obligations, to protect and defend our rights and property or with your permission.

    user = o.individual('User', 'you')
    first_party = o.individual('FirstParty', 'we')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'affiliated companies.')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'third-party service providers,')),
    ]

    o.individual(

        'DataSharingActivity',

        'In order to conduct business operations smoothly in providing you with the full capabilities of our products and services, we may disclose your personal information from time to time to our affiliated companies. We may also share your information as described in this Privacy Policy with our third-party service providers, to comply with legal obligations, to protect and defend our rights and property or with your permission.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            *third_parties,

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'In order to conduct business operations smoothly in providing you with the full capabilities of our products and services,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to protect and defend our rights and property or with your permission.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'as described in this Privacy Policy')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'to comply with legal obligations,')),
        ]
    )




    #########################################################################
    # Our third-party service providers include, without limitation, our mailing houses, delivery service providers, telecommunications companies, data centers, data storage facilities, customer service providers, advertising and marketing service providers. Such third-party service providers will be processing your personal information on our behalf or for one or more of the purposes listed herein.

    user = o.individual('User', 'your')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'third-party service providers')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'mailing houses,')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'delivery service providers,')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'telecommunications companies,')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'data centers,')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'data storage facilities,')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'customer service providers,')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'advertising and marketing service providers.')),
    ]

    o.individual(

        'DataSharingActivity',

        'Our third-party service providers include, without limitation, our mailing houses, delivery service providers, telecommunications companies, data centers, data storage facilities, customer service providers, advertising and marketing service providers. Such third-party service providers will be processing your personal information on our behalf or for one or more of the purposes listed herein.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            *third_parties,

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for one or more of the purposes listed herein.')),
        ]
    )




    #########################################################################
    # Vendors and Service Providers. We may share any information we receive with vendors and service providers. The types of service providers (processors) to whom we entrust personal information include service providers for: (i) provision of IT and related services; (ii) provision of information and services you have requested; (iii) customer service activities; and (iv) in connection with the provision of the products, services and website. We have executed appropriate contracts with the service providers that prohibit them from using or sharing personal information except as necessary to perform the contracted services on our behalf or to comply with applicable legal requirements.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'vendors')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'service providers.')),
    ]

    o.individual(

        'DataSharingActivity',

        'Vendors and Service Providers. We may share any information we receive with vendors and service providers. The types of service providers (processors) to whom we entrust personal information include service providers for: (i) provision of IT and related services; (ii) provision of information and services you have requested; (iii) customer service activities; and (iv) in connection with the provision of the products, services and website. We have executed appropriate contracts with the service providers that prohibit them from using or sharing personal information except as necessary to perform the contracted services on our behalf or to comply with applicable legal requirements.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'any information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'provision of IT and related services;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'provision of information and services you have requested;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'customer service activities;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'in connection with the provision of the products, services and website.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to perform the contracted services on our behalf')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to comply with applicable legal requirements.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'applicable legal requirements.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'We have executed appropriate contracts with the service providers that prohibit them from using or sharing personal information except as necessary')),
        ]
    )




    #########################################################################
    # Third-Party Services. You may choose to share personal information with other third-party services (e.g., Strava, Wechat, Google Fit, Relive). Once your personal information has been shared with a third-party service, it will also be subject to the third-party service’s privacy policy. We encourage you to closely read each third-party service’s privacy policy before sharing your personal information with them. Please note that we do not control and we are not responsible for the third-party service’s processing of your personal information.

    user = o.individual('User', 'You')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'other third-party services')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Strava')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Wechat')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Google Fit')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Relive')),
    ]

    data = [
        o.connection('isAppliedTo', o.individual(
            'PersonalData',
            'personal information',
            [o.connection('isProvidedBy', user)])),
    ]

    o.individual(

        'DataSharingActivity',

        'Third-Party Services. You may choose to share personal information with other third-party services (e.g., Strava, Wechat, Google Fit, Relive). Once your personal information has been shared with a third-party service, it will also be subject to the third-party service’s privacy policy. We encourage you to closely read each third-party service’s privacy policy before sharing your personal information with them. Please note that we do not control and we are not responsible for the third-party service’s processing of your personal information.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),
            
            *data,

            o.connection('initiatesAnotherActivity', o.individual(
                'UserAccessControl',
                'You may choose to share personal information with other third-party services',
                [
                    o.connection('activityIsInitiatedBy', user),

                    *data,
                ])),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'it will also be subject to the third-party service’s privacy policy.')),
        ]
    )




    #########################################################################
    # Business Partners. We may share personal information with our business partners to provide you with a product or service that you have requested. We may also provide personal information to business partners with whom we may jointly offer products or services, or whose products or services we believe may be of interest to you. In such cases, our business partner’s name will appear, along with us. We require our business partners to agree in writing to maintain the confidentiality and security of personal information they maintain on our behalf and not to use it for any purpose other than the purpose for which we provided them.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'our business partners')),
    ]

    o.individual(

        'DataSharingActivity',

        'Business Partners. We may share personal information with our business partners to provide you with a product or service that you have requested. We may also provide personal information to business partners with whom we may jointly offer products or services, or whose products or services we believe may be of interest to you. In such cases, our business partner’s name will appear, along with us. We require our business partners to agree in writing to maintain the confidentiality and security of personal information they maintain on our behalf and not to use it for any purpose other than the purpose for which we provided them.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            *third_parties,

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'OrganizationalMeasure',
                'We require our business partners to agree in writing to maintain the confidentiality and security of personal information they maintain on our behalf and not to use it for any purpose other than the purpose for which we provided them.')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to provide you with a product or service that you have requested.')),
        ]
    )




    #########################################################################
    # Affiliates. We may share your personal information with our company affiliates for the purposes set forth in this Privacy Policy, including our administrative purposes, activities such as IT management, or for them to provide services to you or support and supplement the services we provide.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'our company affiliates')),
    ]

    o.individual(

        'DataSharingActivity',

        'Affiliates. We may share your personal information with our company affiliates for the purposes set forth in this Privacy Policy, including our administrative purposes, activities such as IT management, or for them to provide services to you or support and supplement the services we provide.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            *third_parties,

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for the purposes set forth in this Privacy Policy,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'including our administrative purposes,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'activities such as IT management,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for them to provide services to you or support and supplement the services we provide.')),
        ]
    )




    #########################################################################
    # Displaying to Your Friends. With your prior consent, we may share your personal information, such as, steps, weight, calories burned, sleep data to your friends.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'your friends.')),
    ]

    o.individual(

        'DataSharingActivity',

        'Displaying to Your Friends. With your prior consent, we may share your personal information, such as, steps, weight, calories burned, sleep data to your friends.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'steps,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'weight,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'calories burned,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'sleep data',
                [o.connection('isProvidedBy', user)])),

            o.connection('initiatesAnotherActivity', o.individual(
                'UserAccessControl',
                'With your prior consent,',
                [
                    o.connection('activityIsInitiatedBy', user),

                    o.connection('isAppliedTo', data),
                ])),
        ]
    )




    #########################################################################
    # Disclosures to Protect Us or Others as Required by Law and Similar Disclosures. We may access, preserve, and disclose your personal information, other account information, and content if we believe doing so is required or appropriate to: (i) comply with law enforcement or national security requests and legal process, such as a court order or subpoena (including in a country other than your home country); (ii) respond to your requests; (iii) protect your, ours or others’ rights, property, or safety; (iv) to enforce our policies or contracts; (v) to collect amounts owed to us; (vi) when we believe disclosure is necessary or appropriate to prevent physical harm or financial loss or in connection with an investigation or prosecution of suspected or actual illegal activity; or (vii) if we, in good faith, believe that disclosure is otherwise necessary or advisable.

    user = o.individual('User', 'your')
    first_party = o.individual('FirstParty', 'we')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties')),
    ]

    o.individual(

        'DataSharingActivity',

        'Disclosures to Protect Us or Others as Required by Law and Similar Disclosures. We may access, preserve, and disclose your personal information, other account information, and content if we believe doing so is required or appropriate to: (i) comply with law enforcement or national security requests and legal process, such as a court order or subpoena (including in a country other than your home country); (ii) respond to your requests; (iii) protect your, ours or others’ rights, property, or safety; (iv) to enforce our policies or contracts; (v) to collect amounts owed to us; (vi) when we believe disclosure is necessary or appropriate to prevent physical harm or financial loss or in connection with an investigation or prosecution of suspected or actual illegal activity; or (vii) if we, in good faith, believe that disclosure is otherwise necessary or advisable.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'other account information,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'content',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'comply with law enforcement or national security requests and legal process, such as a court order or subpoena (including in a country other than your home country);')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'respond to your requests;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'protect your, ours or others’ rights, property, or safety;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to enforce our policies or contracts;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to collect amounts owed to us;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'when we believe disclosure is necessary or appropriate to prevent physical harm or financial loss or in connection with an investigation or prosecution of suspected or actual illegal activity;')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'if we, in good faith, believe that disclosure is otherwise necessary or advisable.')),
        ]
    )




    #########################################################################
    # Merger, Sale, or Other Asset Transfers. If we are involved in a merger, acquisition, financing due diligence, reorganization, bankruptcy, receivership, transition of service to another provider or asset sale of all or a portion of our assets, then your information may be sold or transferred as part of such a transaction as permitted by law and/or contract. You will be notified via email and/or a prominent notice on our website or in the Zepp App of any changes in ownership, uses of your personal information, and choices you may have regarding your personal information. We will endeavor to direct the transferee to use personal information in a manner that is consistent with the Privacy Policy in effect at the time such personal information was collected.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'PolicyChangeActivity',

        'Merger, Sale, or Other Asset Transfers. If we are involved in a merger, acquisition, financing due diligence, reorganization, bankruptcy, receivership, transition of service to another provider or asset sale of all or a portion of our assets, then your information may be sold or transferred as part of such a transaction as permitted by law and/or contract. You will be notified via email and/or a prominent notice on our website or in the Zepp App of any changes in ownership, uses of your personal information, and choices you may have regarding your personal information. We will endeavor to direct the transferee to use personal information in a manner that is consistent with the Privacy Policy in effect at the time such personal information was collected.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'your information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasNotificationMechanism', o.individual(
                'ViaEmail',
                'via email')),

            o.connection('hasNotificationMechanism', o.individual(
                'OnWebsitePage',
                'prominent notice on our website')),

            o.connection('hasNotificationMechanism', o.individual(
                'OnService',
                'in the Zepp App')),

            o.connection('hasPolicyChangeCause', o.individual(
                'MergeAcquisitionCause',
                'If we are involved in a merger, acquisition, financing due diligence, reorganization, bankruptcy, receivership, transition of service to another provider or asset sale of all or a portion of our assets,')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'as permitted by law and/or contract.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # SECURITY SAFEGUARDS                                                   #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We are committed to ensuring that your personal information is secure, and we will take all practicable steps to safeguard your personal information. However, you should be aware that the use of the Internet is not entirely secure, and for this reason we cannot guarantee the security or integrity of any personal information we process.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    o.individual(

        'DataActivity',

        'We are committed to ensuring that your personal information is secure, and we will take all practicable steps to safeguard your personal information. However, you should be aware that the use of the Internet is not entirely secure, and for this reason we cannot guarantee the security or integrity of any personal information we process.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'SecurityMechanism',
                'all practicable steps to safeguard your personal information.')),

            o.connection('hasSecurityMechanism', o.individual(
                'UserMaintain',
                'you should be aware that the use of the Internet is not entirely secure, and for this reason we cannot guarantee the security or integrity of any personal information we process.')),
        ]
    )




    #########################################################################
    # To prevent unauthorized access, disclosure or other similar risks and to comply with applicable privacy and security laws in the countries in which we operate, we have put in place reasonable administrative, technical and physical controls and procedures designed to safeguard and secure the information we collect from your use of our products and services. We will use reasonable efforts designed to safeguard your personal information.

    user = o.individual('User', 'your')
    first_party = o.individual('FirstParty', 'we')

    o.individual(

        'DataCollectionActivity',

        'To prevent unauthorized access, disclosure or other similar risks and to comply with applicable privacy and security laws in the countries in which we operate, we have put in place reasonable administrative, technical and physical controls and procedures designed to safeguard and secure the information we collect from your use of our products and services. We will use reasonable efforts designed to safeguard your personal information.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'OrganizationalMeasure',
                'reasonable administrative,')),

            o.connection('hasSecurityMechanism', o.individual(
                'TechnicalMeasure',
                'technical')),

            o.connection('hasSecurityMechanism', o.individual(
                'TechnicalMeasure',
                'and physical controls and procedures')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to safeguard and secure the information we collect from your use of our products and services.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'to comply with applicable privacy and security laws in the countries in which we operate,')),
        ]
    )




    #########################################################################
    # For example, when you access your account, you can choose to use our two-step verification process for better security. When you send or receive data from your device to our servers, we make sure they are encrypted using Secure Sockets Layer ('SSL') and other algorithms.

    user = o.individual('User', 'you')
    first_party = o.individual('FirstParty', 'we')

    o.individual(

        'DataActivity',

        'For example, when you access your account, you can choose to use our two-step verification process for better security. When you send or receive data from your device to our servers, we make sure they are encrypted using Secure Sockets Layer (`SSL`) and other algorithms.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'data',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'AccessControls',
                'two-step verification process')),

            o.connection('hasSecurityMechanism', o.individual(
                'TechnicalMeasure',
                'they are encrypted using Secure Sockets Layer (`SSL`) and other algorithms.')),
        ]
    )




    #########################################################################
    # All your personal information is stored on secure servers that are protected in controlled facilities. We classify your data based on importance and sensitivity, and endeavor to ensure that your personal information has an appropriate security level. The files and records containing your personal information will be kept in our offices and/or on our servers or those of our service providers and only those employees that require it for the purposes of their duties will have access to this file. We have also implemented controls to require that our third-party service providers and partners have appropriate safeguards designed to protect your personal information as well. We make sure that our employees and third-party service providers who access the information to help provide you with our products and services are subject to strict contractual confidentiality obligations and may be disciplined or terminated if they fail to meet such obligations. In some cases, we have special access controls for cloud-based data storage as well. All in all, we regularly review our information collection, storage and processing practices, including physical security measures, in an effort to guard against any unauthorized access and use.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataActivity',

        'All your personal information is stored on secure servers that are protected in controlled facilities. We classify your data based on importance and sensitivity, and endeavor to ensure that your personal information has an appropriate security level. The files and records containing your personal information will be kept in our offices and/or on our servers or those of our service providers and only those employees that require it for the purposes of their duties will have access to this file. We have also implemented controls to require that our third-party service providers and partners have appropriate safeguards designed to protect your personal information as well. We make sure that our employees and third-party service providers who access the information to help provide you with our products and services are subject to strict contractual confidentiality obligations and may be disciplined or terminated if they fail to meet such obligations. In some cases, we have special access controls for cloud-based data storage as well. All in all, we regularly review our information collection, storage and processing practices, including physical security measures, in an effort to guard against any unauthorized access and use.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'TechnicalMeasure',
                'secure servers that are protected in controlled facilities.')),

            o.connection('hasSecurityMechanism', o.individual(
                'OrganizationalMeasure',
                'We classify your data based on importance and sensitivity,')),

            o.connection('hasSecurityMechanism', o.individual(
                'LockedOffices',
                'in our offices and/or on our servers or those of our service providers')),

            o.connection('hasSecurityMechanism', o.individual(
                'SucurityTraining',
                'only those employees that require it for the purposes of their duties will have access to this file.')),

            o.connection('hasSecurityMechanism', o.individual(
                'AccessControls',
                'We have also implemented controls to require that our third-party service providers and partners have appropriate safeguards designed to protect your personal information as well.')),
        ]
    )




    #########################################################################
    # However, despite these efforts, no security measures are perfect or impenetrable and no method of data transmission can be guaranteed to prevent any interception or other type of misuse. We also depend on you to protect your information. If you become aware of any breach of security or privacy, please notify us immediately. To the fullest extent permitted by applicable law, we do not accept liability for unauthorized disclosure.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataActivity',

        'However, despite these efforts, no security measures are perfect or impenetrable and no method of data transmission can be guaranteed to prevent any interception or other type of misuse. We also depend on you to protect your information. If you become aware of any breach of security or privacy, please notify us immediately. To the fullest extent permitted by applicable law, we do not accept liability for unauthorized disclosure.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'UserMaintain',
                'We also depend on you to protect your information.')),
        ]
    )




    #########################################################################
    # By using our products and services or providing personal information to us, you agree that we may communicate with you electronically regarding security, privacy, and administrative issues relating to your use. If we learn of a security system’s breach, we may attempt to notify you electronically by posting a notice on the website or through the product or service and/or by sending an e-mail to you. You may have a legal right to receive this notice in writing.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'GiveConsentActivity',

        'By using our products and services or providing personal information to us, you agree that we may communicate with you electronically regarding security, privacy, and administrative issues relating to your use. If we learn of a security system’s breach, we may attempt to notify you electronically by posting a notice on the website or through the product or service and/or by sending an e-mail to you. You may have a legal right to receive this notice in writing.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('initiatesAnotherActivity', o.individual(
                'ReportBreachActivity',
                'If we learn of a security system’s breach, we may attempt to notify you electronically by posting a notice on the website or through the product or service and/or by sending an e-mail to you. You may have a legal right to receive this notice in writing.',
                [
                    o.connection('activityIsInitiatedBy', first_party),

                    o.connection('isAppliedTo', data),

                    o.connection('hasNotificationMechanism', o.individual(
                        'OnWebsitePage',
                        'electronically by posting a notice on the website')),

                    o.connection('hasNotificationMechanism', o.individual(
                        'OnService',
                        'through the product or service')),

                    o.connection('hasNotificationMechanism', o.individual(
                        'ViaEmail',
                        'sending an e-mail')),

                    o.connection('hasNotificationMechanism', o.individual(
                        'ViaPostalMail',
                        'notice in writing.')),
                ])),
        ]
    )




    #########################################################################
    #                                                                       #
    # WHAT YOU CAN DO                                                       #
    #                                                                       #
    #########################################################################




    #########################################################################
    # You can play your part in safeguarding your personal information by not disclosing your login password or account information to anybody unless such person is duly authorized by you. Whenever you log in the Zepp App, particularly on somebody else's mobile phones or on public Internet terminals, you should always log out at the end of your session.

    user = o.individual('User')

    o.individual(

        'DataActivity',

        'You can play your part in safeguarding your personal information by not disclosing your login password or account information to anybody unless such person is duly authorized by you. Whenever you log in the Zepp App, particularly on somebody else`s mobile phones or on public Internet terminals, you should always log out at the end of your session.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'UserMaintain',
                'by not disclosing your login password or account information to anybody unless such person is duly authorized by you. Whenever you log in the Zepp App, particularly on somebody else`s mobile phones or on public Internet terminals, you should always log out at the end of your session.')),
        ]
    )




    #########################################################################
    # We cannot be held responsible for lapses in security caused by third party accesses to your personal information as a result of your failure to keep your personal information private. Notwithstanding the foregoing, you must notify us immediately if there is any unauthorized use of your account by any other Internet user or any other breach of security. Your assistance will help us protect the privacy of your personal information.

    # This aspect is not implemented in ontology




    #########################################################################
    #                                                                       #
    # YOUR PRIVACY CHOICES                                                  #
    #                                                                       #
    #########################################################################




    #########################################################################
    # The privacy choices you may have about your personal information are determined by applicable law and are described below.

    user = o.individual('User')

    o.individual(

        'UserPrivacyControl',

        'The privacy choices you may have about your personal information are determined by applicable law and are described below.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                '',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'are determined by applicable law')),
        ]
    )




    #########################################################################
    # We may occasionally send you push notifications through our mobile applications with version updates and other notices that may be of interest to you. You may at any time opt-out from receiving these types of communications by changing the settings on your mobile device. We may also collect location-based information if you use our mobile applications. You may opt-out of this collection by changing the settings on your mobile device.

    user = o.individual('User')

    o.individual(

        'UserOptControl',

        'We may occasionally send you push notifications through our mobile applications with version updates and other notices that may be of interest to you. You may at any time opt-out from receiving these types of communications by changing the settings on your mobile device. We may also collect location-based information if you use our mobile applications. You may opt-out of this collection by changing the settings on your mobile device.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                '',
                'location-based information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataControlMechanism', o.individual(
                'ServiceForm',
                'by changing the settings on your mobile device.')),
        ]
    )




    #########################################################################
    # Do Not Track (“DNT”) is a privacy preference that users can set in certain web browsers. DNT is a way for users to inform websites and services that they do not want certain information about their webpage visits collected over time and across websites or online services. Please note that we do not respond to or honor DNT signals or similar mechanisms transmitted by web browsers.

    user = o.individual('User')

    o.individual(

        'UserPrivacyControl',

        'Do Not Track (“DNT”) is a privacy preference that users can set in certain web browsers. DNT is a way for users to inform websites and services that they do not want certain information about their webpage visits collected over time and across websites or online services. Please note that we do not respond to or honor DNT signals or similar mechanisms transmitted by web browsers.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'certain information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasPrivacyControlMechanism', o.individual(
                'PrivacyControlMechanism',
                'privacy preference that users can set in certain web browsers.')),
        ]
    )




    #########################################################################
    # As noted herein, you may stop or restrict the placement of cookies and other technologies on your computer or remove them from your browser by adjusting your web browser preferences. Please note that cookie-based opt-outs are not effective on mobile applications. However, on many mobile devices, application users may opt out of certain mobile ads via their device settings.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        '',

        'As noted herein, you may stop or restrict the placement of cookies and other technologies on your computer or remove them from your browser by adjusting your web browser preferences. Please note that cookie-based opt-outs are not effective on mobile applications. However, on many mobile devices, application users may opt out of certain mobile ads via their device settings.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'cookies',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasPrivacyControlMechanism', o.individual(
                'PrivacyControlMechanism',
                'by adjusting your web browser preferences.')),

            o.connection('hasPrivacyControlMechanism', o.individual(
                'PrivacyControlMechanism',
                'privacy preference that users can set in certain web browsers.')),
        ]
    )




    #########################################################################
    # Our applications may need access to certain features on your device such as Wi-Fi network status. This information is used to allow the applications to run on your device and allow you to interact with the applications. At any time you may revoke your permissions by turning these off at the device level and/or contacting us via https://www.zepp.com/privacy-support.

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Our applications may need access to certain features on your device such as Wi-Fi network status. This information is used to allow the applications to run on your device and allow you to interact with the applications. At any time you may revoke your permissions by turning these off at the device level and/or contacting us via https://www.zepp.com/privacy-support.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'DeviceData',
                'Wi-Fi network status',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'is used to allow the applications to run on your device')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'allow you to interact with the applications.')),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'At any time you may revoke your permissions by turning these off at the device level')),

            o.connection('hasDataControlMechanism', o.individual(
                'WebsiteForm',
                'contacting us via https://www.zepp.com/privacy-support.')),
        ]
    )




    #########################################################################
    # We recognize that privacy concerns differ from person to person. Therefore, we provide examples of ways we make available for you to choose to restrict the collection, use, disclosure or processing of your personal information and control your privacy settings: Log in and out of the account; Toggle on/off for other services and functionalities which deal with sensitive or personal information.

    user = o.individual('User', 'you')

    o.individual(

        'UserAccessControl',

        'We recognize that privacy concerns differ from person to person. Therefore, we provide examples of ways we make available for you to choose to restrict the collection, use, disclosure or processing of your personal information and control your privacy settings: Log in and out of the account; Toggle on/off for other services and functionalities which deal with sensitive or personal information.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'Log in and out of the account;')),

            o.connection('hasDataControlMechanism', o.individual(
                'ServiceForm',
                'Toggle on/off for other services and functionalities which deal with sensitive or personal information.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # RETENTION POLICY                                                      #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We retain personal information we receive as described in this Privacy Policy for as long as you use our products, services and websites or as necessary to fulfill the purpose(s) for which it was collected, provide our services, resolve disputes, establish legal defenses, conduct audits, pursue legitimate business purposes, enforce our agreements, and comply with applicable laws. We shall cease to retain personal information, or remove the means by which the personal information can be associated with particular individuals, as soon as it is reasonable to assume that the purpose for which that personal information was collected is no longer being served by retention of the personal information.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataRetentionActivity',

        'We retain personal information we receive as described in this Privacy Policy for as long as you use our products, services and websites or as necessary to fulfill the purpose(s) for which it was collected, provide our services, resolve disputes, establish legal defenses, conduct audits, pursue legitimate business purposes, enforce our agreements, and comply with applicable laws. We shall cease to retain personal information, or remove the means by which the personal information can be associated with particular individuals, as soon as it is reasonable to assume that the purpose for which that personal information was collected is no longer being served by retention of the personal information.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'provide our services,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'resolve disputes,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'establish legal defenses,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'conduct audits,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'pursue legitimate business purposes,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'enforce our agreements,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'comply with applicable laws.')),

            o.connection('hasDataRetentionTime', o.individual(
                'DataRetentionTime',
                'as long as you use our products, services and websites')),

            o.connection('hasDataRetentionTime', o.individual(
                'DataRetentionTime',
                'as necessary to fulfill the purpose(s) for which it was collected,')),

            o.connection('hasSecurityMechanism', o.individual(
                'SecurityMechanism',
                'We shall cease to retain personal information, or remove the means by which the personal information can be associated with particular individuals, as soon as it is reasonable to assume that the purpose for which that personal information was collected is no longer being served by retention of the personal information.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'as described in this Privacy Policy')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'pursue legitimate business purposes,')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'enforce our agreements,')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'comply with applicable laws.')),
        ]
    )




    #########################################################################
    # If further processing is for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes according to the applicable laws, the data can be further retained by us even if the further processing is incompatible with original purposes in certain jurisdictions.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataRetentionActivity',

        'If further processing is for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes according to the applicable laws, the data can be further retained by us even if the further processing is incompatible with original purposes in certain jurisdictions.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'Data',
                'data',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'If further processing is for archiving purposes in the public interest,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'scientific or historical research purposes')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'statistical purposes according')),

            o.connection('hasDataRetentionTime', o.individual(
                'DataRetentionTime',
                'the data can be further retained by us even if the further processing is incompatible with original purposes in certain jurisdictions.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'according to the applicable laws,')),
        ]
    )




    #########################################################################
    #                                                                       #
    # YOUR PRIVACY RIGHTS                                                   #
    #                                                                       #
    #########################################################################




    #########################################################################
    # Access Personal Information about you, including: (i) confirming whether we are processing your personal information; (ii) obtaining access to or a copy of your personal information;

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Access Personal Information about you, including: (i) confirming whether we are processing your personal information; (ii) obtaining access to or a copy of your personal information;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'Personal Information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'confirming whether we are processing your personal information;')),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'obtaining access to or a copy of your personal information;')),
        ]
    )




    #########################################################################
    # Request Correction of your personal information where it is inaccurate, incomplete or outdated. In some cases, we may provide self-service tools that enable you to update your personal information;

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Request Correction of your personal information where it is inaccurate, incomplete or outdated. In some cases, we may provide self-service tools that enable you to update your personal information;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'Request Correction of your personal information where it is inaccurate, incomplete or outdated.')),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'we may provide self-service tools that enable you to update your personal information;')),
        ]
    )




    #########################################################################
    # Request Deletion or Anonymization of your personal information when processing is based on your consent or when processing is unnecessary, excessive or non-compliant;

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Request Deletion or Anonymization of your personal information when processing is based on your consent or when processing is unnecessary, excessive or non-compliant;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'PseudoAnonymization',
                'Anonymization')),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'Request Deletion or Anonymization of your personal information when processing is based on your consent or when processing is unnecessary, excessive or non-compliant;')),
        ]
    )




    #########################################################################
    # Request Restriction or Blocking of or Object to our processing of your personal information;

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Request Restriction or Blocking of or Object to our processing of your personal information;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information;',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'Request Restriction or Blocking of or Object to our processing of your personal information;')),
        ]
    )




    #########################################################################
    # Withdraw Your Consent to our processing of your personal information. If you refrain from providing personal information or withdraw your consent to processing, some features of our Service may not be available;

    user = o.individual('User')

    o.individual(

        'WithdrawConsentActivity',

        'Withdraw Your Consent to our processing of your personal information. If you refrain from providing personal information or withdraw your consent to processing, some features of our Service may not be available;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information.',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasUserChoiceConsequence', o.individual(
                'WithdrawConsentActivity',
                'some features of our Service may not be available;')),
        ]
    )




    #########################################################################
    # Request Data Portability and receive an electronic copy of personal information that you have provided to us;

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Request Data Portability and receive an electronic copy of personal information that you have provided to us;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'Request Data Portability and receive an electronic copy of personal information that you have provided to us;')),
        ]
    )




    #########################################################################
    # Be Informed about third parties with which your personal information has been shared; and

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Be Informed about third parties with which your personal information has been shared;',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Request any review of decisions which may have been taken exclusively based on automated processing if that could affect data subject rights.

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Request any review of decisions which may have been taken exclusively based on automated processing if that could affect data subject rights.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'Request any review of decisions which may have been taken exclusively based on automated processing if that could affect data subject rights.')),
        ]
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

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        '',

        'Our products and services are not directed to children under 16 (and in certain jurisdictions under the age of 13) years of age.We don’t seek or intend to seek to receive any personal information from minors. Should a parent or guardian have reasons to believe that a minor has provided us with personal information without their prior consent, please contact us to ensure that the personal information is removed and the minor unsubscribes from any of the applicable services. If we learn that we have collected any personal information from children under 16 (and in certain jurisdictions under the age of 13) and we do not obtain permission from a parent, we will promptly take steps to delete such information and terminate the minor’s account.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                '',
                '',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                '',
                '')),

            o.connection('hasNotificationMechanism', o.individual(
                '',
                '')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                '')),

            o.connection('hasDataRetentionTime', o.individual(
                'DataRetentionTime',
                '')),

            o.connection('hasUserChoiceConsequence', o.individual(
                '',
                '')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                '')),
        ]
    )




    #########################################################################
    #                                                                       #
    # UPDATES TO THE PRIVACY POLICY                                         #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We keep our Privacy Policy under regular review and may update this Privacy Policy to reflect changes to our information practices. You understand and agree that you will be deemed to have accepted the updated Privacy Policy if you use the products or services after the updated Privacy Policy is posted. If, at any point, you do not agree to any portion of the Privacy Policy then in effect, you must immediately stop using the products and services. If we make material changes to our Privacy Policy, we will notify you by email (sent to the e-mail address specified in your account) or post the changes in our App. Such changes to our Privacy Policy shall apply from the effective date as set out in the notice or in our App. We encourage you to periodically review this page for the latest information on our privacy practices. Your continued use of products and services on mobile phones and/or any other device will be taken as acceptance of the updated Privacy Policy. Before we use personal information for any new purpose not originally authorized by you, we will endeavor to provide information regarding the new purpose and give you the opportunity to opt-out. Where your consent for the processing of personal information is otherwise required by law or contract, we will endeavor to comply with the law or contract.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'PolicyChangeActivity',

        'We keep our Privacy Policy under regular review and may update this Privacy Policy to reflect changes to our information practices. You understand and agree that you will be deemed to have accepted the updated Privacy Policy if you use the products or services after the updated Privacy Policy is posted. If, at any point, you do not agree to any portion of the Privacy Policy then in effect, you must immediately stop using the products and services. If we make material changes to our Privacy Policy, we will notify you by email (sent to the e-mail address specified in your account) or post the changes in our App. Such changes to our Privacy Policy shall apply from the effective date as set out in the notice or in our App. We encourage you to periodically review this page for the latest information on our privacy practices. Your continued use of products and services on mobile phones and/or any other device will be taken as acceptance of the updated Privacy Policy. Before we use personal information for any new purpose not originally authorized by you, we will endeavor to provide information regarding the new purpose and give you the opportunity to opt-out. Where your consent for the processing of personal information is otherwise required by law or contract, we will endeavor to comply with the law or contract.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasNotificationMechanism', o.individual(
                'ViaEmail',
                'by email')),

            o.connection('hasNotificationMechanism', o.individual(
                'OnService',
                'in our App.')),

            o.connection('hasNotificationMechanism', o.individual(
                'OnWebsitePage',
                'review this page for the latest information on our privacy practices.')),

            o.connection('hasPolicyAcceptanceTime', o.individual(
                'PolicyAcceptanceTime',
                'from the effective date')),

            o.connection('initiatesAnotherActivity', o.individual(
                'GiveConsentActivity',
                'You understand and agree that you will be deemed to have accepted the updated Privacy Policy if you use the products or services after the updated Privacy Policy is posted.',
                [o.connection('activityIsInitiatedBy', user)])),

            o.connection('initiatesAnotherActivity', o.individual(
                'GiveConsentActivity',
                'Your continued use of products and services on mobile phones and/or any other device will be taken as acceptance of the updated Privacy Policy.',
                [o.connection('activityIsInitiatedBy', user)])),

            o.connection('initiatesAnotherActivity', o.individual(
                'UserOptControl',
                'Before we use personal information for any new purpose not originally authorized by you, we will endeavor to provide information regarding the new purpose and give you the opportunity to opt-out.'
                [o.connection('activityIsInitiatedBy', user)])),

            o.connection('initiatesAnotherActivity', o.individual(
                'WithdrawConsentActivity',
                'If, at any point, you do not agree to any portion of the Privacy Policy then in effect, you must immediately stop using the products and services.',
                [
                    o.connection('hasUserChoiceConsequence', o.individual(
                        'UserChoiceConsequence',
                        'you must immediately stop using the products and services.')),

                    o.connection('activityIsInitiatedBy', user),
                ])),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'Where your consent for the processing of personal information is otherwise required by law or contract, we will endeavor to comply with the law or contract.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # THIRD PARTY TERMS AND CONDITIONS                                      #
    #                                                                       #
    #########################################################################

    # The ontology does not have aspect describing irresponsibility for TP services




    #########################################################################
    #                                                                       #
    # SUPPLEMENTAL CALIFORNIA ADDENDUM TO THIS PRIVACY POLICY               #
    #                                                                       #
    #########################################################################




    #########################################################################
    # This Supplemental California Addendum to this Privacy Policy (“California Addendum”) supplements and should be read in conjunction with this Privacy Policy. This California Addendum only applies to our processing of personal information that is subject to the California Consumer Privacy Act of 2018 (“CCPA”). The CCPA provides California residents with the right to know what categories of personal information we have collected about them and whether we disclosed that personal information for a business purpose (e.g., to a service provider) in the preceding twelve months. California residents can find this information below:

    user = o.individual('User', 'residents', [
        o.connection('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'California residents'))
    ])

    o.individual(

        'UserPrivacyControl',

        'This Supplemental California Addendum to this Privacy Policy (“California Addendum”) supplements and should be read in conjunction with this Privacy Policy. This California Addendum only applies to our processing of personal information that is subject to the California Consumer Privacy Act of 2018 (“CCPA”). The CCPA provides California residents with the right to know what categories of personal information we have collected about them and whether we disclosed that personal information for a business purpose (e.g., to a service provider) in the preceding twelve months. California residents can find this information below:',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataControlMechanism',
                'right to know what categories of personal information we have collected about them and whether we disclosed that personal information for a business purpose (e.g., to a service provider) in the preceding twelve months.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'California Consumer Privacy Act of 2018')),
        ]
    )




    #########################################################################
    # Categories of Third Parties Personal Information is Disclosed to for a Business Purpose. Identifiers such as alias, unique personal identifier, online identifier, IP address, email address, account name or other similar identifiers. Service providers, Affiliates, Other users or third-party services you share or interact with.

    user = o.individual('User', 'residents', [
        o.connection('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'California residents'))
    ])
    first_party = o.individual('FirstParty')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Service providers')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Affiliates')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Other users or third-party services you share or interact with')),
    ]

    o.individual(

        'DataSharingActivity',

        'Categories of Third Parties Personal Information is Disclosed to for a Business Purpose. Identifiers such as alias, unique personal identifier, online identifier, IP address, email address, account name or other similar identifiers. Service providers, Affiliates, Other users or third-party services you share or interact with.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            *third_parties,

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'Identifiers such as alias,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'unique personal identifier,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'online identifier,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'IP address,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'email address,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'account name',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'AccountData',
                'other similar identifiers.',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'for a Business Purpose')),
        ]
    )




    #########################################################################
    # Biometric Info such as an individual’s physiological, biological, or behavioral characteristics, that can be used, singly or in combination with each other or with other identifying data, to establish individual identity. Biometric information includes, but is not limited to, gait patterns or rhythms, and sleep, health, or exercise data that contain identifying information. Service providers Affiliates

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Service providers')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Affiliates')),
    ]

    o.individual(

        'DataSharingActivity',

        'Biometric Info such as an individual’s physiological, biological, or behavioral characteristics, that can be used, singly or in combination with each other or with other identifying data, to establish individual identity. Biometric information includes, but is not limited to, gait patterns or rhythms, and sleep, health, or exercise data that contain identifying information. Service providers Affiliates',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            *third_parties,

            o.connection('isAppliedTo', o.individual(
                'BiometricData',
                'Biometric Info',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'BiometricData',
                'physiological',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'BiometricData',
                'biological',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'BiometricData',
                'behavioral characteristics',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'gait patterns or rhythms,',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'BiometricData',
                'behavioral characteristics',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'sleep',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'health',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'HealthData',
                'exercise data that contain identifying information.',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'that can be used, singly or in combination with each other or with other identifying data, to establish individual identity.')),
        ]
    )




    #########################################################################
    # Internet or other electronic network activity information such as browsing history, search history and information regarding a consumer's interaction with a website, application, or advertisement. Service Affiliates Other users or third-party services you share or interact with

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Service providers')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Affiliates')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Other users or third-party services you share or interact with')),
    ]

    o.individual(

        'DataSharingActivity',

        'Internet or other electronic network activity information such as browsing history, search history and information regarding a consumer`s interaction with a website, application, or advertisement. Service Affiliates Other users or third-party services you share or interact with',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'Internet',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'electronic network activity information',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'browsing history',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'search history',
                [o.connection('isProvidedBy', user)])),

            o.connection('isAppliedTo', o.individual(
                'ServiceData',
                'information regarding a consumer`s interaction with a website, application, or advertisement.',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Geo-location such as physical location or movements. Service providers Affiliates Other users or third-party services you share or interact with

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Service providers')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Affiliates')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Other users or third-party services you share or interact with')),
    ]

    o.individual(

        'DataSharingActivity',

        'Geo-location such as physical location or movements. Service providers Affiliates Other users or third-party services you share or interact with',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            *third_parties,

            o.connection('isAppliedTo', o.individual(
                'TrackingData',
                'Geo-location',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Inferences drawn from other personal information to create a profile about a consumer. Service providers Affiliates

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Service providers')),
        o.connection('sharesDataWithAgent', o.individual('ThirdParties', 'Affiliates')),
    ]

    o.individual(

        'DataSharingActivity',

        'Inferences drawn from other personal information to create a profile about a consumer. Service providers Affiliates',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'to create a profile about a consumer.')),
        ]
    )




    #########################################################################
    # “Sales” of Personal Information under the CCPA. For purposes of the CCPA, we do not “sell” personal information, nor do we have actual knowledge of any “sale” of personal information of minors under 16 years of age.
   
    user = o.individual('User', 'residents', [
        o.connection('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'California residents')),
        o.connection('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'minors under 16 years of age.'))
    ])
    first_party = o.individual('FirstParty')

    o.individual(

        'DataSharingActivity',

        '“Sales” of Personal Information under the CCPA. For purposes of the CCPA, we do not “sell” personal information, nor do we have actual knowledge of any “sale” of personal information of minors under 16 years of age.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'Personal Information',
                [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Non-Discrimination. California residents have the right not to receive discriminatory treatment by us for the exercise of their rights conferred by the CCPA. 

    user = o.individual('User', 'residents', [
        o.connection('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'California residents')),
    ])

    o.individual(

        'UserPrivacyControl',

        'Non-Discrimination. California residents have the right not to receive discriminatory treatment by us for the exercise of their rights conferred by the CCPA.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'receive discriminatory treatment',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'California residents have the right')),
        ]
    )




    #########################################################################
    # Authorized Agent. Only you, or someone legally authorized to act on your behalf, may make a verifiable consumer request related to your personal information. To designate an authorized agent, please contact us as set forth below.

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Authorized Agent. Only you, or someone legally authorized to act on your behalf, may make a verifiable consumer request related to your personal information. To designate an authorized agent, please contact us as set forth below.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information.',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'Only you, or someone legally authorized to act on your behalf, may make a verifiable consumer request related to your personal information.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'someone legally authorized to act on your behalf,')),
        ]
    )




    #########################################################################
    # Verification. When you make a request, we will ask you to provide sufficient information that allows us to reasonably verify you are the person about whom we collected personal information or an authorized representative, which may include confirming the email address associated with any personal information we have about you.

    user = o.individual('User')

    o.individual(

        'UserAccessControl',

        'Verification. When you make a request, we will ask you to provide sufficient information that allows us to reasonably verify you are the person about whom we collected personal information or an authorized representative, which may include confirming the email address associated with any personal information we have about you.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                user)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasDataControlMechanism', o.individual(
                'DataControlMechanism',
                'you make a request,')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'an authorized representative,')),
        ]
    )




    #########################################################################
    #                                                                       #
    # DATA DESTRUCTION PERIOD                                               #
    #                                                                       #
    #########################################################################




    #########################################################################
    # Personal information, which has fulfilled the purpose for which it was collected or used, and has reached the period of time during which personal information was to be possessed, will be destroyed in an irreversible way. After the expiration of the applicable period, information under the obligation of retention by applicable laws will be promptly destroyed in an irreversible way. Personal information stored in electronic files will be deleted safely in an irreversible way by using technical methods, and printed information will be destroyed by shredding or incinerating such information. Furthermore, in compliance with applicable laws, measures will be taken to destroy or separate the personal information of the users who have not used our services for a period of one year.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    o.individual(

        'DataRetentionActivity',

        'Personal information, which has fulfilled the purpose for which it was collected or used, and has reached the period of time during which personal information was to be possessed, will be destroyed in an irreversible way. After the expiration of the applicable period, information under the obligation of retention by applicable laws will be promptly destroyed in an irreversible way. Personal information stored in electronic files will be deleted safely in an irreversible way by using technical methods, and printed information will be destroyed by shredding or incinerating such information. Furthermore, in compliance with applicable laws, measures will be taken to destroy or separate the personal information of the users who have not used our services for a period of one year.',

        [
            o.connection('activityIsInitiatedBy', o.individual(
                first_party)),

            o.connection('isAppliedTo', o.individual(
                'PersonalData',
                'Personal information',
                [o.connection('isProvidedBy', user)])),

            o.connection('hasSecurityMechanism', o.individual(
                'TechnicalMeasure',
                'technical methods,')),

            o.connection('hasDataActivityPurpose', o.individual(
                'DataActivityPurpose',
                'the purpose for which it was collected or used,')),

            o.connection('hasDataRetentionTime', o.individual(
                'DataRetentionTime',
                'has reached the period of time during which personal information was to be possessed,')),

            o.connection('hasDataRetentionTime', o.individual(
                'DataRetentionTime',
                'expiration of the applicable period,')),

            o.connection('hasDataRetentionTime', o.individual(
                'DataRetentionTime',
                'destroy or separate the personal information of the users who have not used our services for a period of one year.')),

            o.connection('hasLegalBasis', o.individual(
                'LegalBasis',
                'by applicable laws')),
        ]
    )

    o.write(reason=False)

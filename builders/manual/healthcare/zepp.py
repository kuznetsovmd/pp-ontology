from ontology.interface import Ontology


def build(**kwargs):

    o = Ontology(**kwargs, website='https://upload-cdn.huami.com/tposts/8191')

    #########################################################################
    #                                                                       #
    # OUR COMMITMENT TO YOU                                                 #
    #                                                                       #
    #########################################################################




    #########################################################################
    # The Privacy Policy is designed with you in mind, and it is important that you have a comprehensive understanding of and confidence in our personal information collection and usage practices of any personal information provided to us.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataActivity',

        'The Privacy Policy is designed with you in mind, and it is important that you have a comprehensive understanding of and confidence in our personal information collection and usage practices of any personal information provided to us.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),
            
        ]
    )




    #########################################################################
    # We are committed to protecting the privacy, confidentiality and security of your personal information by complying with applicable laws. We are equally committed to ensuring that all our employees and agents uphold these obligations.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataProtection',

        'We are committed to protecting the privacy, confidentiality and security of your personal information by complying with applicable laws. We are equally committed to ensuring that all our employees and agents uphold these obligations.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'SecurityMechanism',
                'We are committed to protecting the privacy')),

            o.property('has_mechanism', o.individual(
                'SecurityMechanism',
                'We are equally committed to ensuring that all our employees and agents uphold these obligations.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'by complying with applicable laws.')),

            o.property('previous_is', a),
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

    a = o.individual(

        'FPCollection',

        'The categories of personal information we may collect (directly from you or from third party sources) and our privacy practices depend on the nature of the relationship you have with us and the requirements of applicable law. As you navigate the services, certain information may also be collected automatically, including through cookies and similar technologies as described below.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'cookies and similar technologies',
                [o.property('provided_by', user)])),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'requirements of applicable law')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # We endeavor to collect only that information which is relevant for the purposes of processing.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'We endeavor to collect only that information which is relevant for the purposes of processing.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'for the purposes of processing')),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'FPCollection',

        'we may ask you to provide certain personal information, such as email address or phone number.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'email address',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'phone number',
                [o.property('provided_by', user)])),

            o.property('has_mode', o.individual(
                'TransmissionByRequest',
                'we may ask')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Automatic Data Collection. We may collect certain information automatically through our products, services or other methods of analysis, such as your Internet protocol (IP) address, cookie identifiers, mobile carrier, MAC address and other device identifiers that are automatically assigned to device when you access the Internet, hardware type, device name, operating system, system version, region & language, installation package name, App version, network status, source of App, device battery, Bluetooth status, Internet service provider, the usage of product and App features, pages that you visit before and after using the services, the date and time of your visit, the amount of time you spend on each page, information about the links you click and pages you view within the services, and other actions taken through use of the services such as preferences.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'We may collect certain information automatically through our products, services or other methods of analysis, such as your Internet protocol (IP) address, cookie identifiers, mobile carrier, MAC address and other device identifiers that are automatically assigned to device when you access the Internet, hardware type, device name, operating system, system version, region & language, installation package name, App version, network status, source of App, device battery, Bluetooth status, Internet service provider, the usage of product and App features, pages that you visit before and after using the services, the date and time of your visit, the amount of time you spend on each page, information about the links you click and pages you view within the services, and other actions taken through use of the services such as preferences.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'Internet protocol (IP) address',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'cookie identifiers',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'mobile carrier',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'MAC address',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'other device identifiers',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'hardware type',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'device name',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'operating system',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'system version',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'region & language',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'installation package name',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'App version',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'network status',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'source of App',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'device battery',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'Bluetooth status',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'Internet service provider',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'the usage of product and App features',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'pages that you visit before and after using the services',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'the date and time of your visit',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'the amount of time you spend on each page',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'information about the links you click',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'pages you view within the services',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'other actions taken through use of the services such as preferences.',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'AutomaticCommunicationMechanism',
                'automatically')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Specific Information Collected Through Our Products and Services. We have a wide range of products, the personal information collected by different products may vary. We may collect the following types of information (which may or may not be personal information):

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'We have a wide range of products, the personal information collected by different products may vary. We may collect the following types of information (which may or may not be personal information):',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'types of information (which may or may not be personal information)',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Information about You: When you register for an account or log into our service using your credentials from your Mi, WeChat, Google, Line or Facebook accounts (with your approval), we may collect and use your avatar, gender, country, email address, nicknames, time zones, languages, regions, birthday, height, weight.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'When you register for an account or log into our service using your credentials from your Mi, WeChat, Google, Line or Facebook accounts (with your approval), we may collect and use your avatar, gender, country, email address, nicknames, time zones, languages, regions, birthday, height, weight.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'AccountData',
                'your credentials from your Mi, WeChat, Google, Line or Facebook accounts',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'avatar',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'gender',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'country',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'email address',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'nicknames',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'time zones',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'languages',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'regions',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'birthday',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'height',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'weight',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Online Purchase Information. If you place an order with us, we will record the personal information and details associated with the transaction. We will collect your purchase/subscription information, such as, user ID, items purchased, order ID, payment information for fulling your order. Any payments made via the Services are processed by third-party payment processors. We do not directly collect or store your payment card information, which is handled by third-party service providers.

    user = o.individual('User')
    first_party = o.individual('FirstParty')
    
    a = o.individual(

        'FPCollection',

        'If you place an order with us, we will record the personal information and details associated with the transaction. We will collect your purchase/subscription information, such as, user ID, items purchased, order ID, payment information for fulling your order. Any payments made via the Services are processed by third-party payment processors.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'FinancialData',
                'details associated with the transaction',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'FinancialData',
                'purchase/subscription information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'user ID',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'items purchased',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'order ID',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'FinancialData',
                'payment information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'for fulling your order.')),
            
            o.property('previous_is', a),
        ]
    )

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    # doesnt
    a = o.individual(

        'FPCollection',

        'We do not directly collect or store your payment card information, which is handled by third-party service providers.',

        [
            o.property('does', False),

            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'FinancialData',
                'not collect payment card information',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Personal Body and Health Information: When you use Zepp App and our device, your personal body and health information may be collected, such as, heart rate, resting heart rate, heart rate zone, maximum heart rate, minimum heart rate, average heart rate, blood oxygen saturation, stress, PAI, PPG data, ECG data, weight, body fat, BMI.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'When you use Zepp App and our device, your personal body and health information may be collected, such as, heart rate, resting heart rate, heart rate zone, maximum heart rate, minimum heart rate, average heart rate, blood oxygen saturation, stress, PAI, PPG data, ECG data, weight, body fat, BMI.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'your personal body and health information may be collected',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'heart rate',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'resting heart rate',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'heart rate zone',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'maximum heart rate',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'minimum heart rate',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'average heart rate',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'blood oxygen saturation',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'stress',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'PAI',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'PPG data',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'ECG data',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'weight',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'body fat',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'BMI',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Exercising Information: When you use the Zepp App and our device for exercising, we may collect your exercising information, such as, steps, stand-up times, total distance, time, total time, total duration, burned calories, consumption, pace, speed, frequency, stride length, maximum oxygen uptake(VO2 Max), exercise capacity, training effects, sports loading, frequency of exercising, strokes, stroke rate, number of trips, number of jumping rope, average stroke distance, movement track, velocity, swolf index, stroke speed and number of floors climbed.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Exercising Information: When you use the Zepp App and our device for exercising, we may collect your exercising information, such as, steps, stand-up times, total distance, time, total time, total duration, burned calories, consumption, pace, speed, frequency, stride length, maximum oxygen uptake(VO2 Max), exercise capacity, training effects, sports loading, frequency of exercising, strokes, stroke rate, number of trips, number of jumping rope, average stroke distance, movement track, velocity, swolf index, stroke speed and number of floors climbed.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'exercising information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'steps',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'stand-up times',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'total distance',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'time',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'total time',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'total duration',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'burned calories',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'consumption',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'pace',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'speed',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'frequency of exercising',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'strokes',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'stroke rate',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'number of trips',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'number of jumping rope',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'average stroke distance',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'movement track',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'velocity',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'swolf index',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'stroke speed',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'number of floors climbed.',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Information Recorded by Your Device: When you use the Zepp App to synchronize device data, personal data is recorded. For example, altitude, air pressure, temperature, weather type, volume of earphone, ambient sound, sleep data, rapid eye movement(REM), activity information, the time length of one-legged standing with eyes closed testing and the time of measuring, resistance value.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Information Recorded by Your Device: When you use the Zepp App to synchronize device data, personal data is recorded. For example, altitude, air pressure, temperature, weather type, volume of earphone, ambient sound, sleep data, rapid eye movement(REM), activity information, the time length of one-legged standing with eyes closed testing and the time of measuring, resistance value.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'altitude',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'air pressure',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'temperature',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'weather type',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'volume of earphone',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'ambient sound',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'sleep data',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'rapid eye movement(REM)',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'activity information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'the time length of one-legged standing with eyes closed testing and the time of measuring',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'resistance value.',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Device Setting Information: We may collect information of your device settings. For example, status of notification, unit settings, dial layout settings, gesture settings, band wearing settings.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'We may collect information of your device settings. For example, status of notification, unit settings, dial layout settings, gesture settings, band wearing settings.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'information of your device settings',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'status of notification',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'unit settings',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'dial layout settings',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'gesture settings',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'band wearing settings.',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Application Setting Information: We may collect information of your device settings on applications. For example, device system setting, exercising functional setting, target of steps, target of exercising, target of weight, target of calories, target of sleep, alarm settings. 

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'information of your device settings on applications',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'device system setting on applications.',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'exercising functional setting',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'target of steps',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'target of exercising',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'target of weight',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'target of calories',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'target of sleep',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'alarm settings.',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Caller Information: When you use the Incoming Call or SMS Alert functions, you will receive an alert about your phone calls, SMS. Your contact information for incoming calls and messages will be synchronized to and displayed on the bundled device. We will not save your caller information in Zepp App or sever.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'We will not save your caller information in Zepp App or sever.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'not caller information',
                [o.property('provided_by', user)])),

            o.property('binded_to', o.individual(
                'FPNotification',
                'you will receive an alert about your phone calls, SMS.',
                [
                    o.property('initiated_by', first_party),
                    o.property('notifies', user),
                ])),
            
            o.property('previous_is', a),
        ]
    )

    




    #########################################################################
    # Network Usage Information: We may collect network types, network signals, WLAN information and other similar information related to certain features of the Zepp App.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Network Usage Information: We may collect network types, network signals, WLAN information and other similar information related to certain features of the Zepp App.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'network types',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'network signals',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'WLAN information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'other similar information related to certain features of the Zepp App.',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Music Information: When you use music or music control function, the music information (e.g., name of song, singer, the status of song) will be obtained from your mobile phone and synchronized to the device. This information will only be displayed on the device screen and we will not save this information. When you use the music storage function (only supported by certain devices), then your music will be synchronized to and stored in the device.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'When you use music or music control function, the music information (e.g., name of song, singer, the status of song) will be obtained from your mobile phone and synchronized to the device. This information will only be displayed on the device screen and we will not save this information.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'not the music information (e.g., name of song, singer, the status of song)',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Log Information: We may record some log information when you use the Zepp App. For example, we may collect operating information, hit log, firmware clicking statistics, and server log. When you give us feedback, at your option, your app log and device log will be collected by us.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Log Information: We may record some log information when you use the Zepp App. For example, we may collect operating information, hit log, firmware clicking statistics, and server log. When you give us feedback, at your option, your app log and device log will be collected by us.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'some log information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'operating information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'hit log',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'firmware clicking statistics',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'server log.',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'your app log',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'device log',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Location Information: When you use location-based program services or features, we may collect your location information such as your GPS information.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Location Information: When you use location-based program services or features, we may collect your location information such as your GPS information.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'location information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'your GPS information.',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'location-based program services or features')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Mobile Phone Information: When you use Zepp App, we may collect your mobile phone information, such as, unique identifier (IDFA, IMEI), the operating system version, system time, time zone, alarm clock, brand and model of your mobile phone.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Mobile Phone Information: When you use Zepp App, we may collect your mobile phone information, such as, unique identifier (IDFA, IMEI), the operating system version, system time, time zone, alarm clock, brand and model of your mobile phone.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'DeviceData',
                'mobile phone information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'unique identifier (IDFA, IMEI)',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'the operating system version',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'system time',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'time zone',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'alarm clock',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'brand and model of your mobile phone.',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Device Information: When you use Zepp App to connect a hardware device, such as an Amazfit watch, we may obtain information, such as: the device's unique identifier, device ID, MAC address, serial number, firmware version, Bluetooth, device size. The collection may also apply to your updated system or software and factory settings.  

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Device Information: When you use Zepp App to connect a hardware device, such as an Amazfit watch, we may obtain information, such as: the device`s unique identifier, device ID, MAC address, serial number, firmware version, Bluetooth, device size. The collection may also apply to your updated system or software and factory settings.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'device`s unique identifier',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'device ID',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'MAC address',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'serial number',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'firmware version',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'Bluetooth',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'device size.',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Device Unlock Information: When you use the device off-wrist lock function, we may collect your device unlock password to realize this function.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'When you use the device off-wrist lock function, we may collect your device unlock password to realize this function.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'device unlock password',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'use the device off-wrist lock function')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Crash Information: When you choose to upload debug logs to help us analyze the problem, your application debug log file will be sent to the server.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'When you choose to upload debug logs to help us analyze the problem, your application debug log file will be sent to the server.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'application debug log file',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to help us analyze the problem')),
            
            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'When you choose to upload debug logs',
                [
                    o.property('initiated_by', user),
                    o.property('applies_to', o.individual(
                        'ServiceData',
                        'application debug log file',
                        [o.property('provided_by', user)])),
                ])),
            
            o.property('previous_is', a),
        ]
    )






    #########################################################################
    # Information from Friends: Zepp App allows you to add friends. After receiving permission from your friends, the weight, activity and sleep information of your friends will be displayed on your App.

    user = o.individual('User')
    first_party = o.individual('FirstParty')
    third_party = o.individual('ThirdParty')

    data = [
        o.property('applies_to', o.individual(
            'AccountData',
            'voice information',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'ServiceData',
            'reminder setting',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'HealthData',
            'tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.).',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'TPSharing',

        'Information from Friends: Zepp App allows you to add friends. After receiving permission from your friends, the weight, activity and sleep information of your friends will be displayed on your App.',

        [
            o.property('initiated_by', first_party),
            
            o.property('shares_with', third_party),
            
            *data,

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'use various functionalities')),

            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'After receiving permission from your friends',
                [
                    o.property('initiated_by', user),
                    *data,
                ])),
            
            o.property('previous_is', a),
        ]
    )

    


    #########################################################################
    # Information Submitted via Services. When you use various functionalities of the Zepp App, you may submit certain information, such as voice information, a reminder setting or tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.). When you use female health function, the information provided by you will be collected, such as duration of menstruation, menstruation interval, the starting date of your latest menstruation, the starting date and ending date of your menstruation, physical condition and mood during menstruation.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    data = [
        o.property('applies_to', o.individual(
            'AccountData',
            'voice information',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'ServiceData',
            'reminder setting',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'HealthData',
            'tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.).',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'FPCollection',

        'When you use various functionalities of the Zepp App, you may submit certain information, such as voice information, a reminder setting or tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.).',

        [
            o.property('initiated_by', first_party),

            *data,

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'use various functionalities')),
            
            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'you may submit certain information, such as voice information, a reminder setting or tags for your current activity status (e.g. walking, pre-sleep state, wake-up mood, sleeping and etc.).',
                [
                    o.property('initiated_by', user),
                    *data
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Visitor Information: When using the visitor function of our smart scale, a visitor can experience our products and certain limited services. The data of the visitor (gender, height, date of birth) may be collected and used to calculate and present the results of certain services the visitor experiences. You can choose to save the visitor information or not, if you choose to save, the visitor’s gender, height, date of birth and weight will be collected by us.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'When using the visitor function of our smart scale, a visitor can experience our products and certain limited services. The data of the visitor (gender, height, date of birth) may be collected and used to calculate and present the results of certain services the visitor experiences. You can choose to save the visitor information or not, if you choose to save, the visitor’s gender, height, date of birth and weight will be collected by us.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'The data of the visitor',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'gender',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'height',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'date of birth',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to calculate and present the results of certain services the visitor experiences.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Other Information: We may also collect other types of information which is not directly or indirectly linked to an individual and which is aggregated, anonymized or de-identified. For example, the device function, system status, battery status, Startup & Shutdown status, charging status and connecting status of smartphone of your device may be collected when using a particular service. Such information is collected in order to improve the services we provide to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    data = [
        o.property('applies_to', o.individual(
            'Data',
            'other types of information which is not directly or indirectly linked to an individual',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'DeviceData',
            'the device function',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'ApplicationData',
            'system status',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'DeviceData',
            'battery status',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'DeviceData',
            'Startup & Shutdown status',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'DeviceData',
            'charging status',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'DeviceData',
            'connecting status of smartphone',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'FPCollection',

        'We may also collect other types of information which is not directly or indirectly linked to an individual and which is aggregated, anonymized or de-identified. For example, the device function, system status, battery status, Startup & Shutdown status, charging status and connecting status of smartphone of your device may be collected when using a particular service. Such information is collected in order to improve the services we provide to you.',

        [
            o.property('initiated_by', first_party),

            *data,

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'in order to improve the services we provide to you.')),
            
            o.property('binded_to', o.individual(
                'DataProtection',
                'which is aggregated, anonymized or de-identified. For example, the device function, system status, battery status, Startup & Shutdown status, charging status and connecting status of smartphone of your device',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_mechanism', o.individual(
                        'PseudoAnonymization',
                        'which is aggregated, anonymized or de-identified')),
                ])),

            o.property('previous_is', a),
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

    data = [
        o.property('applies_to', o.individual(
            'PersonalData',
            'personal information',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'DataUse',

        'We acquire, hold, use and process personal information for a variety of business purposes including for providing services and/or products to you, to respond to information requested and to fulfill legal compliance on our part under applicable laws.',

        [
            o.property('initiated_by', first_party),

            *data,

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'for a variety of business purposes including for providing services and/or products to you, to respond to information requested and to fulfill legal compliance on our part under applicable laws.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'under applicable laws.')),
            
            o.property('binded_to', o.individual(
                'TPSharing',
                'We may also process and disclose personal information to our affiliated companies and to third-party service providers for the purposes stated in this Privacy Policy.',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_purpose', o.individual(
                        'ServiceProvisionPurpose',
                        'for the purposes stated in this Privacy Policy.')),
                ])),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'DataUse',

        'We may use information about you to fulfill requests for products, Services, or information, including: Providing, processing, maintaining, improving and developing our goods and/or services to you, including after-sales and customer support and for services on your device; Communicating with you about your device, service or any general queries or other requests and comments, such as updates, customer inquiry support, information about our events, notices; Providing access to certain areas, functionalities, and features of our products and services; Conducting promotional activities, such as sweepstakes and Facebook events; Analyzing and developing statistical information on the use of our products and services to better improve our products and services; Optimizing the performance of your device; Storing and maintaining information about you for our business operations or legal obligations; and Providing local services without communicating with our servers.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'information about you',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to fulfill requests for products, Services, or information, including:')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Providing, processing, maintaining, improving and developing our goods and/or services to you, including after-sales and customer support and for services on your device;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Communicating with you about your device, service or any general queries or other requests and comments, such as updates, customer inquiry support, information about our events, notices;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Providing access to certain areas, functionalities, and features of our products and services;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Conducting promotional activities, such as sweepstakes and Facebook events;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Analyzing and developing statistical information on the use of our products and services to better improve our products and services;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Optimizing the performance of your device;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Storing and maintaining information about you for our business operations or legal obligations; and')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Providing local services without communicating with our servers.')),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'DataUse',

        'We may use personal information about you for administrative purposes, including to: Measure interest in our services; Develop new products and services; Ensure internal quality control; Verify your identity; Communicate about accounts and activities on our services and systems, and, in our discretion, changes to any of our policies; Send email to the email address you provide to us to verify your account and for informational and operational purposes, such as account management, customer service, or system maintenance; Prevent potentially prohibited or illegal activities; and Enforce our Service Agreement and/or Privacy Policy.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Measure interest in our services;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Develop new products and services;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Ensure internal quality control;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Verify your identity;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Communicate about accounts and activities on our services and systems, and, in our discretion, changes to any of our policies;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Send email to the email address you provide to us to verify your account and for informational and operational purposes, such as account management, customer service, or system maintenance;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Prevent potentially prohibited or illegal activities; and')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Enforce our Service Agreement and/or Privacy Policy.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Marketing Our Products and Services. If permitted by applicable laws, we may use your personal information, such as your email address, account ID, to provide you with materials directly or through third-party service provider(s) about offers, products, and services, including new content or services. We may provide you with these materials by phone, postal mail, facsimile, or email, or as otherwise permitted by applicable law. Such uses include:
    # To notify you about offers, products, and services that may be of interest to you;
    # For other purposes disclosed at the time that individuals provide personal information; and
    # Otherwise with your consent.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'If permitted by applicable laws, we may use your personal information, such as your email address, account ID, to provide you with materials directly or through third-party service provider(s) about offers, products, and services, including new content or services. We may provide you with these materials by phone, postal mail, facsimile, or email, or as otherwise permitted by applicable law. Such uses include: To notify you about offers, products, and services that may be of interest to you; For other purposes disclosed at the time that individuals provide personal information; and Otherwise with your consent.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'email address',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'account ID',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to provide you with materials directly or through third-party service provider(s) about offers, products, and services, including new content or services.')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'To notify you about offers, products, and services that may be of interest to you;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'For other purposes disclosed at the time that individuals provide personal information; and')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'Otherwise with your consent.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'permitted by applicable laws')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # You have the right to opt out of our proposed use of your personal information for direct marketing. If you no longer wish to receive certain types of email communication you may opt-out by following the unsubscribe link located at the bottom of each communication.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'AdvertisingDataControl',

        'You have the right to opt out of our proposed use of your personal information for direct marketing. If you no longer wish to receive certain types of email communication you may opt-out by following the unsubscribe link located at the bottom of each communication.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'your personal information',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Research and Development. We may use personal information to create non-identifiable information that we may use alone or in the aggregate with information obtained from other sources, in order to help us to optimally deliver our existing products and services or develop new products and services and we may share these statistics with the public or third parties in order to present the preference and trend analysis.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    data = [
        o.property('applies_to', o.individual(
            'NonPersonalData',
            'statistics',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'DataUse',

        'We may use personal information to create non-identifiable information that we may use alone or in the aggregate with information obtained from other sources, in order to help us to optimally deliver our existing products and services or develop new products and services',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to create non-identifiable information that we may use alone or in the aggregate with information obtained from other sources, in order to help us to optimally deliver our existing products and services or develop new products and services')),

            o.property('binded_to', o.individual(
                'TPSharing',
                'and we may share these statistics with the public or third parties in order to present the preference and trend analysis.',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_purpose', o.individual(
                        'ServiceProvisionPurpose',
                        'in order to present the preference and trend analysis.')),
                ])),

            o.property('binded_to', o.individual(
                'DataProtection',
                'and we may share these statistics with the public or third parties in order to present the preference and trend analysis.',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_mechanism', o.individual(
                        'PseudoAnonymization',
                        'non-identifiable')),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Services via Mobile Devices (only in certain feature). From time to time, we may provide products and services that are specifically designed to be compatible and used on mobile devices. We will collect certain information that your mobile device sends when you use such products and services, like a device identifier, user settings, location information, mobile carrier, and the operating system of your device. Mobile versions of our products and services may require that users log in with an account. In such cases, information about use of mobile versions of the products and services may be associated with accounts. In addition, we may enable you to download an application, widget, or other tool that can be used on mobile or other computing devices. Some of these tools may store information on mobile or other devices. These tools may transmit personal information to us to enable you to access your accounts and to enable us and our third-party service providers to track use of these tools. Some of these tools may enable users to transmit reports and other information from the tool. We may use personal or non-identifiable information transmitted to us to enhance these tools, to develop new tools, for quality improvement and as otherwise described in this Privacy Policy or in other notices we provide.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    data = [
        o.property('applies_to', o.individual(
            'PersonalData',
            'personal',
            [o.property('provided_by', user)])),
        o.property('applies_to', o.individual(
            'NonPersonalData',
            'non-identifiable information',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'DataUse',

        'We will collect certain information that your mobile device sends when you use such products and services, like a device identifier, user settings, location information, mobile carrier, and the operating system of your device. Mobile versions of our products and services may require that users log in with an account. In such cases, information about use of mobile versions of the products and services may be associated with accounts. In addition, we may enable you to download an application, widget, or other tool that can be used on mobile or other computing devices. Some of these tools may store information on mobile or other devices. These tools may transmit personal information to us to enable you to access your accounts and to enable us and our third-party service providers to track use of these tools. Some of these tools may enable users to transmit reports and other information from the tool.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'information that your mobile device sends',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'device identifier,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'user settings',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'location information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'mobile carrier',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'operating system of your device.',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'users log in with an account.',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'reports and other information from the tool.',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to enable you to access your accounts and to enable us and our third-party service providers to track use of these tools.')),
            
            o.property('binded_to', o.individual(
                'DataUse',
                'We may use personal or non-identifiable information transmitted to us to enhance these tools, to develop new tools, for quality improvement and as otherwise described in this Privacy Policy or in other notices we provide.',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_purpose', o.individual(
                        'ServiceProvisionPurpose',
                        'to enhance these tools, to develop new tools, for quality improvement and as otherwise described in this Privacy Policy or in other notices we provide.')),
                ])),
            
            o.property('binded_to', o.individual(
                'DataProtection',
                'non-identifiable information',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_mechanism', o.individual(
                        'PseudoAnonymization',
                        'non-identifiable')),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # De-identified, Anonymous and/or Aggregated Information Use. We may use personal information and other information about you to create de-identified, anonymized and/or aggregated information, such as de-identified demographic information, de-identified location information, information about the mobile phone or device from which you access Zepp App, or other analyses we create. De-identified, anonymized and/or aggregated information is not personal information, and we may use such information in a number of ways, including research, internal analysis, analytics, and any other legally permissible purposes.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'De-identified, Anonymous and/or Aggregated Information Use. We may use personal information and other information about you to create de-identified, anonymized and/or aggregated information, such as de-identified demographic information, de-identified location information, information about the mobile phone or device from which you access Zepp App, or other analyses we create. De-identified, anonymized and/or aggregated information is not personal information, and we may use such information in a number of ways, including research, internal analysis, analytics, and any other legally permissible purposes.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to create de-identified, anonymized and/or aggregated information, such as de-identified demographic information, de-identified location information, information about the mobile phone or device from which you access Zepp App, or other analyses we create.')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'in a number of ways, including research, internal analysis, analytics, and any other legally permissible purposes.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'legally permissible')),
            
            o.property('binded_to', o.individual(
                'DataProtection',
                'non-identifiable information',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_mechanism', o.individual(
                        'PseudoAnonymization',
                        'de-identified, anonymized and/or aggregated')),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Improving User Experience. Some opt-in features allow us or our third party partners to analyze data about how users use our products and services, so as to improve the user experience, such as sending crash reports.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'AdvertisingDataControl',

        'Improving User Experience. Some opt-in features allow us or our third party partners to analyze data about how users use our products and services, so as to improve the user experience, such as sending crash reports.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'ServiceData',
                'crash reports',
                [o.property('provided_by', user)])),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Specific Ways Personal Information is Used in Products and Services. Here are more details on how we may use your information (which may include personal information):

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'Here are more details on how we may use your information (which may include personal information):',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Set Up Your Account for Zepp App. Personal information collected when creating an account through our Zepp App is used for creating the personal account and profile page for the user.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Personal information collected when creating an account through our Zepp App is used for creating the personal account and profile page for the user.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'Personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'is used for creating the personal account and profile page for the user.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Calculate Exercise Results. Personal body information is used to accurately calculate and display the exercise result to you, such as, exercising records, distance, exercising time, total duration, burned calories, consumption, pace, speed, maximum oxygen uptake (VO2 Max), exercise capacity, training effects.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'Personal body information is used to accurately calculate and display the exercise result to you, such as, exercising records, distance, exercising time, total duration, burned calories, consumption, pace, speed, maximum oxygen uptake (VO2 Max), exercise capacity, training effects.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'Personal body information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'exercising records',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'distance',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'exercising time',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'total duration',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'burned calories',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'consumption',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'pace',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'speed',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'maximum oxygen uptake (VO2 Max)',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'exercise capacity',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'training effects.',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'HealthMonitoringPurpose',
                'is used to accurately calculate and display the exercise result to you')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Physical Analysis. Based on the personal information you provided and the data recorded by the device, we will provide you an analysis related to your physical condition for your reference, such as PAI, BMI, muscle mass, body fat percentage, water percentage, protein, basal metabolic rate, subcutaneous fat, skeletal muscle mass, visceral fat level, bone mass content, pressure, body shape, body age.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'Based on the personal information you provided and the data recorded by the device, we will provide you an analysis related to your physical condition for your reference, such as PAI, BMI, muscle mass, body fat percentage, water percentage, protein, basal metabolic rate, subcutaneous fat, skeletal muscle mass, visceral fat level, bone mass content, pressure, body shape, body age.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'data recorded by the device',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'PAI',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'BMI',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'muscle mass',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'body fat percentage',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'water percentage',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'protein',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'basal metabolic rate',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'subcutaneous fat',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'skeletal muscle mass',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'visceral fat level',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'bone mass content',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'pressure',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'body shape',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'body age',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'HealthMonitoringPurpose',
                'provide you an analysis related to your physical condition for your reference')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Sleep Analysis. Based on the personal information you have provided and the data recorded by the device, such as PPG, heart rate, we will record your naps, sleep time, sleep breathing and provide you a sleep score and sleep analysis related to your sleep quality for your reference.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'Based on the personal information you have provided and the data recorded by the device, such as PPG, heart rate, we will record your naps, sleep time, sleep breathing and provide you a sleep score and sleep analysis related to your sleep quality for your reference.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'naps',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'sleep time',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'sleep breathing',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'sleep score',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'sleep analysis',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                '',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                '',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                '',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                '',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                '',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'HealthMonitoringPurpose',
                'for your reference')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide World Clock Service. When you add a world clock in Zepp App, we will calculate the local time corresponding to your selected area based on the time at your mobile phone and display it in Zepp App and the bundled devices that support the world clock function.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'we will calculate the local time corresponding to your selected area based on the time at your mobile phone and display it in Zepp App and the bundled devices that support the world clock function.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'your selected area',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'display it in Zepp App and the bundled devices that support the world clock function.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Alarm Clock Service: when you use alarm clock function, your alarm clock information will be displayed in Zepp App and the bundled device.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'when you use alarm clock function, your alarm clock information will be displayed in Zepp App and the bundled device.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'alarm clock information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'will be displayed in Zepp App and the bundled device.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Voice Related Service: When you use off-line or on-line voice assistant function (only supported by certain device in certain countries/areas), such as Alexa, we will collect your voice request, for the purpose of carrying out your orders. Your voice information may also be used to provide voice memo service to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'When you use off-line or on-line voice assistant function (only supported by certain device in certain countries/areas), such as Alexa, we will collect your voice request, for the purpose of carrying out your orders. Your voice information may also be used to provide voice memo service to you.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'BiometricData',
                'your voice request',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'for the purpose of carrying out your orders.')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to provide voice memo service to you.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Female Health Service. When you use female health function, certain information related to menstrual period will be recorded and displayed in Zepp App or on some devices that support this function. If you turn on the physiological period intelligent prediction mode, we will predict your menstrual period and remind you based on the information you provided.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'When you use female health function, certain information related to menstrual period will be recorded and displayed in Zepp App or on some devices that support this function. If you turn on the physiological period intelligent prediction mode, we will predict your menstrual period and remind you based on the information you provided.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'information related to menstrual period',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'HealthMonitoringPurpose',
                'predict your menstrual period and remind you based on the information you provided.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Blood Oxygen Saturation Measurement Function. When you turn on the blood oxygen measurement function, we will collect your blood oxygen saturation information to show the value to you or to assist providing a sleeping analysis to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'we will collect your blood oxygen saturation information to show the value to you or to assist providing a sleeping analysis to you.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'blood oxygen saturation information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'HealthMonitoringPurpose',
                'to show the value to you or to assist providing a sleeping analysis to you.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Notification Reminder Service. When you enable the notification reminder function, the reminder information you set in the Zepp App will be pushed to the bundled device.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'When you enable the notification reminder function, the reminder information you set in the Zepp App will be pushed to the bundled device.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'reminder information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'reminder information you set in the Zepp App will be pushed to the bundled device.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Bluetooth Camera Function. When you use Bluetooth camera function, your mobile phone will be connected with the device through Bluetooth for controlling the camera.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'When you use Bluetooth camera function, your mobile phone will be connected with the device through Bluetooth for controlling the camera.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'SensitiveData',
                'Bluetooth camera',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Zepp App Services. When you connect certain devices with Zepp App, the information collected through the device will be shown to user.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    data = [
        o.property('applies_to', o.individual(
            'Data',
            'information',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'FPCollection',

        'When you connect certain devices with Zepp App, the information collected through the device will be shown to user.',

        [
            o.property('initiated_by', first_party),

            *data,

            o.property('binded_to', o.individual(
                'FPNotification',
                'with Zepp App, the information collected through the device will be shown to user.',
                [
                    o.property('initiated_by', first_party),
                    o.property('has_mechanism', o.individual(
                        'OnServiceApp',
                        'with Zepp App'
                    )),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide eSIM(embedded SIM) Function. (only supported by certain devices and in certain countries/areas). After you successfully activate eSIM with telecom carriers, you may use the device alone to call or receive a call, to send or receive SMS (SMS service is subject to local telecom carriers). When you use eSIM function, we will collect your operation records. Your phone number, call records, short messages will be stored in the device, but if you choose to upload this information together with the log, this information will be uploaded and stored in our cloud.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    data = [
        o.property('applies_to', o.individual(
            'TrackingData',
            'operation records.',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'TrackingData',
            'phone number',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'TrackingData',
            'call records',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'TrackingData',
            'short messages',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'FPCollection',

        'When you use eSIM function, we will collect your operation records. Your phone number, call records, short messages will be stored in the device, but if you choose to upload this information together with the log, this information will be uploaded and stored in our cloud.',

        [
            o.property('initiated_by', first_party),

            *data,

            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'When you use eSIM function, we will collect your operation records. Your phone number, call records, short messages will be stored in the device, but if you choose to upload this information together with the log, this information will be uploaded and stored in our cloud.',
                [
                    o.property('initiated_by', user),
                    *data,
                ]
            )),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Display Caller Information. When you receive a call, text messages, caller information will be displayed on the device. You may even answer or reject a phone call by the device directly (only supported by certain devices).

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'When you receive a call, text messages, caller information will be displayed on the device. You may even answer or reject a phone call by the device directly (only supported by certain devices).',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'SensitiveData',
                'text messages',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'caller information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'will be displayed on the device.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Bluetooth Phone Services (only supported by certain devices). With the device successfully paired with your mobile phone’s Bluetooth, when you receive an incoming call, the incoming call information will be displayed on the device. You can even use the device to answer or hang up the call. If you have missed calls, the relevant information will also be displayed on the device. You may add or delete your frequent contacts information in Zepp App. The frequent contacts information added by you will be bound to your account and synchronized to the device and our cloud.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'To Provide Bluetooth Phone Services (only supported by certain devices). With the device successfully paired with your mobile phone’s Bluetooth, when you receive an incoming call, the incoming call information will be displayed on the device. You can even use the device to answer or hang up the call. If you have missed calls, the relevant information will also be displayed on the device. You may add or delete your frequent contacts information in Zepp App. The frequent contacts information added by you will be bound to your account and synchronized to the device and our cloud.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'incoming call information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'frequent contacts information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'You can even use the device to answer or hang up the call. If you have missed calls, the relevant information will also be displayed on the device.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Display Music Information. When you use music control function, the music information (name of song, singer, volume, the status of song) will be displayed on the device.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'When you use music control function, the music information (name of song, singer, volume, the status of song) will be displayed on the device.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'music information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'name of song',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'singer',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'volume',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'the status of song',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'will be displayed on the device.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide AI Sleep Melody Service. When you use AI Sleep Melody service, we will collect and use your personal information, such as heart rate, activity data, sleep data and your music reference to recommend sleep melodies to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')
    
    data = [
        o.property('applies_to', o.individual(
            'PersonalData',
            'personal information',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'HealthData',
            'heart rate',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'HealthData',
            'activity data',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'HealthData',
            'sleep data',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'PersonalData',
            'your music reference',
            [o.property('provided_by', user)])),
    ]
    
    purposes = [
        o.property('has_purpose', o.individual(
            'ServiceProvisionPurpose',
            'to recommend sleep melodies to you.')),
    ]

    a = o.individual(

        'FPCollection',

        'When you use AI Sleep Melody service, we will collect and use your personal information, such as heart rate, activity data, sleep data and your music reference to recommend sleep melodies to you.',

        [
            o.property('initiated_by', first_party),
            *data,
            *purposes,
            o.property('binded_to', o.individual(
                'DataUse',
                'When you use AI Sleep Melody service, we will collect and use your personal information, such as heart rate, activity data, sleep data and your music reference to recommend sleep melodies to you.',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    *purposes,
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Hearing Health Function (only supported by certain earphone). If you turn on this function, we will collect your earphone volume in real time and recommend listening time for the current week based on the hearing protection standards established by the World Health Organization (WHO).

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'If you turn on this function, we will collect your earphone volume in real time and recommend listening time for the current week based on the hearing protection standards established by the World Health Organization (WHO).',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'DeviceData',
                'earphone volume',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'recommend listening time for the current week based on the hearing protection standards established by the World Health Organization (WHO).')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Cervical Protection Function (only supported by certain earphone). If you turn on this function, the earphone sensor will detect and present you with habitual head-lowering angle. If you turn on the relax prompt, the earphone will play music to remind you to relax your spine for long periods of time.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'If you turn on this function, the earphone sensor will detect and present you with habitual head-lowering angle. If you turn on the relax prompt, the earphone will play music to remind you to relax your spine for long periods of time.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'habitual head-lowering angle.',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'HealthMonitoringPurpose',
                'the earphone will play music to remind you to relax your spine for long periods of time.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Noise Control Function (only supported by certain earphone). When you turn on ANC function, we will collect and cancel ambient sound in accordance with the mode set by you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'When you turn on ANC function, we will collect and cancel ambient sound in accordance with the mode set by you.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'ambient sound',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Tap for Report Function (only supported by certain earphone). If you turn on this function, we will collect your current speed, heart rate and other workout information. By simply taping the earphone, this information will be broadcasted to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'If you turn on this function, we will collect your current speed, heart rate and other workout information. By simply taping the earphone, this information will be broadcasted to you.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'current speed',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'heart rate',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'other workout information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'HealthMonitoringPurpose',
                'will be broadcasted to you.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Determine Whether the Mobile Phone is Supported. Phone information will be used to determine if your device can use Zepp App.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'Phone information will be used to determine if your device can use Zepp App.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'DeviceData',
                'Phone information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to determine if your device can use Zepp App.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Measure the Temperature (only supported by certain devices). The device will measure the temperature and display the data to you.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'The device will measure the temperature and display the data to you.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'temperature',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'HealthMonitoringPurpose',
                'display the data to you.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Network Related Services. We use network types, network signals, etc. to prompt the user to download updates in different network environments. Certain devices (such as Amazfit smart scale) can directly connect to the server via WLAN, and upload your measurement (such as your weight, body fat, BMI and etc.) and the device identifier to the cloud accessible in the Zepp App.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'We use network types, network signals, etc. to prompt the user to download updates in different network environments. Certain devices (such as Amazfit smart scale) can directly connect to the server via WLAN, and upload your measurement (such as your weight, body fat, BMI and etc.) and the device identifier to the cloud accessible in the Zepp App.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'HealthData',
                'measurement',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'weight',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'body fat',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'BMI',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'DeviceData',
                'device identifier',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Off-wrist Lock Function. Your device unlock password will be used to the off-wrist lock function. If you turn on this function, your device will be locked when the device detects that it is off-wrist. If the wrong password is entered on the device more than a certain number of times, your device will be locked up. To unlock the device, you need to change the device unlock password or restore the Factory Settings on device in Zepp App.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'Your device unlock password will be used to the off-wrist lock function.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'AccountData',
                'device unlock password',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'will be used to the off-wrist lock function.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Provide Location-based Services. In the course of using our services, location information may also be used by us or third-party service providers to provide and improve our services. For example, we may use your GPS information to provide you with weather details, calculating the distance of your outdoor sporting or mapping such activity. You may turn this off at any time by going into the device settings of your mobile devices or discontinue use of that application.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    data = [
        o.property('applies_to', o.individual(
            'TrackingData',
            'location information',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'TrackingData',
            'GPS information',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'TPSharing',

        'In the course of using our services, location information may also be used by us or third-party service providers to provide and improve our services. For example, we may use your GPS information to provide you with weather details, calculating the distance of your outdoor sporting or mapping such activity.',

        [
            o.property('initiated_by', first_party),

            o.property('shares_with', o.individual(
                'ThirdParty', 
                'third parties.')),

            *data,

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to provide and improve our services.')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to provide you with weather details, calculating the distance of your outdoor sporting or mapping such activity.')),

            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'You may turn this off at any time by going into the device settings of your mobile devices or discontinue use of that application.',
                [
                    o.property('initiated_by', user),
                    *data,
                ])),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Optimize Our Products and Services. We use your personal information, such as, Huami ID, log information, debug information, the information automatically collected to provide functionality, analyze performance, fix errors, and improve the quality of our products and services. For example, we may use these information to optimize pages/function display, determining the importance of each product function, guiding us to adjust the priority of the development of product features.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'We use your personal information, such as, Huami ID, log information, debug information, the information automatically collected to provide functionality, analyze performance, fix errors, and improve the quality of our products and services. For example, we may use these information to optimize pages/function display, determining the importance of each product function, guiding us to adjust the priority of the development of product features.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'Huami ID',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'log information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'debug information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to provide functionality, analyze performance, fix errors, and improve the quality of our products and services.')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to optimize pages/function display, determining the importance of each product function, guiding us to adjust the priority of the development of product features.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Manage Devices. This information provides the ability to manage the bundled devices.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'This information provides the ability to manage the bundled devices.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'provides the ability to manage the bundled devices.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Improve Software Stability. We collect crash logs for analyzing software quality to provide better service.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'We collect crash logs for analyzing software quality to provide better service.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'ServiceData',
                'crash logs',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'for analyzing software quality to provide better service.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Improve Device Stability. We may use the information to improve the bundled devices.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataUse',

        'We may use the information to improve the bundled devices.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to improve the bundled devices.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To Send Notices. From time to time, we may use your personal information to send important notices, such as communications about changes to our terms, conditions, and policies.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'PolicyChange',

        'From time to time, we may use your personal information to send important notices, such as communications about changes to our terms, conditions, and policies.',

        [
            o.property('initiated_by', first_party),

            o.property('binded_to', o.individual(
                'FPNotification',
                'From time to time, we may use your personal information to send important notices, such as communications about changes to our terms, conditions, and policies.',
                [
                    o.property('initiated_by', first_party),
                    o.property('has_mechanism', o.individual(
                        'CommunicationMechanism',
                        'important notices, such as communications about changes')),
                    o.property('notifiesAgent', user),
                ])),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'FPCollection',

        'We, as well as our third-party service providers that provide content, advertising, or other functionality on our Services, may use cookies, pixel tags, local storage, and other technologies (“Technologies”) to automatically collect information through the Services. We use Technologies that are essentially small data files placed on your computer, tablet, mobile phone, or other devices that allow us to record certain pieces of information whenever you visit or interact with our websites, services, applications, messaging, and tools, and to recognize you across devices.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'cookies',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to recognize you across devices.')),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'through the Services.')),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'pixel tags')),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'local storage')),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'cookies')),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'other technologies (“Technologies”)')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # What Information is Collected and How We Use Them: Technologies such as cookies, tags, and scripts are used by us and our third-party service providers. These Technologies are used in analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole. We may receive reports based on the use of these technologies by these companies on an individual as well as aggregated basis.

    user = o.individual('User')
    first_party = o.individual('FirstParty')
    third_party = o.individual('ThirdParty', 'third parties.')

    data = [
        o.property('applies_to', o.individual(
            'TrackingData',
            'cookies',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'TPCollection',

        'Technologies such as cookies, tags, and scripts are used by us and our third-party service providers. These Technologies are used in analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole. We may receive reports based on the use of these technologies by these companies on an individual as well as aggregated basis.',

        [
            o.property('initiated_by', first_party),

            o.property('collects_from', third_party),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole.')),
            
            o.property('binded_to', o.individual(
                'DataProtection',
                'Technologies such as cookies, tags, and scripts are used by us and our third-party service providers. These Technologies are used in analyzing trends, administering the website, tracking users’ movements around the website and to gather demographic information about our user base as a whole. We may receive reports based on the use of these technologies by these companies on an individual as well as aggregated basis.',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_mechanism', o.individual(
                        'PseudoAnonymization',
                        'aggregated basis.')),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Cookies. Cookies are small text files placed in visitors’ device browsers to store their preferences. Most browsers allow you to block and delete cookies. However, if you do that, the website may not work properly.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'OptInOptOutControl',

        'Cookies are small text files placed in visitors’ device browsers to store their preferences. Most browsers allow you to block and delete cookies. However, if you do that, the website may not work properly.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'TrackingData',
                'cookies',
                [o.property('provided_by', user)])),

            o.property('has_consequence', o.individual(
                'PartialServiceRestriction',
                'However, if you do that, the website may not work properly.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Pixel Tags/Web Beacons. A pixel tag (also known as a web beacon) is a piece of code embedded on the website that collects information about users’ engagement on that web page. The use of a pixel allows us to record, for example, that a user has visited a particular web page or clicked on a particular advertisement.

    user = o.individual('User')
    first_party = o.individual('FirstParty')
    
    a = o.individual(

        'FPCollection',

        'A pixel tag (also known as a web beacon) is a piece of code embedded on the website that collects information about users’ engagement on that web page. The use of a pixel allows us to record, for example, that a user has visited a particular web page or clicked on a particular advertisement.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'information about users’ engagement on that web page',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'ViaWebsite',
                'pixel tag (also known as a web beacon)')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to record, for example, that a user has visited a particular web page or clicked on a particular advertisement')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Social Media Widgets: Our products, services and website may include social media features such as connectivity with Facebook, Google,Twitter, Strava, Line (that might include widgets such as the share this button or other interactive mini-programs). These features may collect your IP address, which page you are visiting on our website, and may set a cookie/or use some device or location information to enable the feature to function properly. These social media features are either hosted by a third party or hosted directly by us. Your interactions with these features are governed by the privacy policy of the company providing it.

    user = o.individual('User', 'your')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.property('collects_from', o.individual('ThirdParty', 'third party')),
        o.property('collects_from', o.individual('ThirdParty', 'Facebook')),
        o.property('collects_from', o.individual('ThirdParty', 'Google')),
        o.property('collects_from', o.individual('ThirdParty', 'Twitter')),
        o.property('collects_from', o.individual('ThirdParty', 'Strava')),
        o.property('collects_from', o.individual('ThirdParty', 'Line')),
    ]

    data = [
        o.property('applies_to', o.individual(
            'TrackingData',
            'IP address',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'TrackingData',
            'which page you are visiting on our website,',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'TrackingData',
            'cookies',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'DeviceData',
            'device',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'TrackingData',
            'location information',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'TPCollection',

        'Social Media Widgets: Our products, services and website may include social media features such as connectivity with Facebook, Google,Twitter, Strava, Line (that might include widgets such as the share this button or other interactive mini-programs). These features may collect your IP address, which page you are visiting on our website, and may set a cookie/or use some device or location information to enable the feature to function properly. These social media features are either hosted by a third party or hosted directly by us. Your interactions with these features are governed by the privacy policy of the company providing it.',

        [
            o.property('initiated_by', first_party),
            
            *third_parties,

            *data,

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to enable the feature to function properly.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'Your interactions with these features are governed by the privacy policy of the company providing it.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Log Files: As true of most websites, we gather certain information and store it in log files. This information may include Internet protocol (IP) addresses, browser type, Internet service provider (ISP), referring/exit pages, operating system, date/time stamp, and/or clickstream data.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Log Files: As true of most websites, we gather certain information and store it in log files. This information may include Internet protocol (IP) addresses, browser type, Internet service provider (ISP), referring/exit pages, operating system, date/time stamp, and/or clickstream data.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'certain information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'Internet protocol (IP) addresses,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'browser type,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'Internet service provider (ISP),',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'referring/exit pages,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ApplicationData',
                'operating system,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'date/time stamp,')),

            o.property('has_mechanism', o.individual(
                'AutomaticCommunicationMechanism',
                'clickstream data.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Mobile Analytics: Within some of our mobile applications, we use mobile analytics software to allow us to better understand the functionality of our mobile software on your phone. This software may record information such as how often you use the application, the events that occur within the application, aggregated usage, performance data, and where crashes occur within the application.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'we')

    data = [
        o.property('applies_to', o.individual(
            'TrackingData',
            'how often you use the application,',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'ServiceData',
            'the events that occur within the application,',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'ServiceData',
            'aggregated usage,',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'ServiceData',
            'performance data,',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'ServiceData',
            'where crashes occur within the application.',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'FPCollection',

        'Mobile Analytics: Within some of our mobile applications, we use mobile analytics software to allow us to better understand the functionality of our mobile software on your phone. This software may record information such as how often you use the application, the events that occur within the application, aggregated usage, performance data, and where crashes occur within the application.',

        [
            o.property('initiated_by', first_party),

            *data,

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to better understand the functionality of our mobile software on your phone.')),

            o.property('binded_to', o.individual(
                'DataProtection',
                'management tool for removing HTML5 LSOs.',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_mechanism', o.individual(
                        'PseudoAnonymization',
                        'aggregated')),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Local Storage – HTML5: We use Local Storage Objects (LSOs) such as HTML5 to store content and preferences. Third parties with whom we partner to provide certain features on our websites or to display advertising based upon your web browsing activity also use HTML5 to collect and store information. Various browsers may offer their own management tool for removing HTML5 LSOs.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')
    third_parties = o.individual('ThirdParty')

    data = o.individual(
                'Data',
                'content and preferences.',
                [o.property('provided_by', user)])

    a = o.individual(

        'TPCollection',

        'Local Storage – HTML5: We use Local Storage Objects (LSOs) such as HTML5 to store content and preferences. Third parties with whom we partner to provide certain features on our websites or to display advertising based upon your web browsing activity also use HTML5 to collect and store information. Various browsers may offer their own management tool for removing HTML5 LSOs.',

        [
            o.property('initiated_by', first_party),

            o.property('collects_from', third_parties),

            o.property('applies_to', data),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to provide certain features on our websites')),

            o.property('has_purpose', o.individual(
                'MarketingPurpose',
                'to display advertising based upon your web browsing activity')),

            o.property('binded_to', o.individual(
                'AdvertisingDataControl',
                'management tool for removing HTML5 LSOs.',
                [
                    o.property('initiated_by', user),
                    o.property('applies_to', data),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Website Analytics. We may use Technologies and other third-party tools to process analytics information on our Services (e.g., Google Analytics). For more about Google Analytics information, please visit Google Analytics’ Privacy Policy. To learn more about how to opt-out of Google Analytics’ use of your information on our website, please click here.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')
    third_parties = o.individual('ThirdParty', 'Google Analytics')

    data = o.individual(
                'Data',
                'analytics information',
                [o.property('provided_by', third_parties)])

    a = o.individual(

        'FPCollection',

        'Website Analytics. We may use Technologies and other third-party tools to process analytics information on our Services (e.g., Google Analytics). For more about Google Analytics information, please visit Google Analytics’ Privacy Policy. To learn more about how to opt-out of Google Analytics’ use of your information on our website, please click here.',

        [
            o.property('initiated_by', first_party),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to process analytics information on our Services')),

            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'verifiable parental consent.',
                [
                    o.property('initiated_by', user),
                    o.property('applies_to', data),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Operationally Necessary. We may use cookies, or other similar technologies that are necessary to the operation of our services, applications, and tools. This includes technologies that allow you access to our services, applications, and tools; that are required to identify irregular website behavior, prevent fraudulent activity and improve security; or that allow you to make use of our functions such as shopping-carts, saved search, or similar functions;

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    a = o.individual(

        'FPCollection',

        'Operationally Necessary. We may use cookies, or other similar technologies that are necessary to the operation of our services, applications, and tools. This includes technologies that allow you access to our services, applications, and tools; that are required to identify irregular website behavior, prevent fraudulent activity and improve security; or that allow you to make use of our functions such as shopping-carts, saved search, or similar functions;',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'other similar technologies',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'cookies',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to the operation of our services, applications, and tools.')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to identify irregular website behavior,')),

            o.property('has_purpose', o.individual(
                'SecurityPurpose',
                'prevent fraudulent activity and improve security;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to make use of our functions such as shopping-carts, saved search, or similar functions;')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Performance Related. We may use cookies, or other similar technologies to assess the performance of our websites, applications, services, and tools, including as part of our analytic practices to help us understand how our visitors use our websites, determine if you have interacted with our messaging, determine whether you have viewed an item or link, or to improve our website content, applications, services, or tools;

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    a = o.individual(

        'FPCollection',

        'Performance Related. We may use cookies, or other similar technologies to assess the performance of our websites, applications, services, and tools, including as part of our analytic practices to help us understand how our visitors use our websites, determine if you have interacted with our messaging, determine whether you have viewed an item or link, or to improve our website content, applications, services, or tools;',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'cookies',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'Data',
                'other similar technologies',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to assess the performance of our websites, applications, services, and tools, including as part of our analytic practices to help us understand how our visitors use our websites,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'determine if you have interacted with our messaging,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'determine whether you have viewed an item or link,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to improve our website content, applications, services, or tools;')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Functionality Related. We may use cookies, web beacons, or other similar technologies that allow us to offer you enhanced functionality when accessing or using our websites, services, applications, or tools. This may include identifying you when you sign into our websites or keeping track of your specified preferences, interests, or past items viewed so that we may enhance the presentation of content on our websites;

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Functionality Related. We may use cookies, web beacons, or other similar technologies that allow us to offer you enhanced functionality when accessing or using our websites, services, applications, or tools. This may include identifying you when you sign into our websites or keeping track of your specified preferences, interests, or past items viewed so that we may enhance the presentation of content on our websites;',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'cookies,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'web beacons,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'Data',
                'other similar technologies',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to offer you enhanced functionality when accessing or using our websites, services, applications, or tools.')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'This may include identifying you when you sign into our websites or keeping track of your specified preferences, interests, or past items viewed so that we may enhance the presentation of content on our websites;')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # If you would like to opt out of the Technologies we employ on our websites, services, applications, or tools, you may do so by blocking, deleting, or disabling them as your browser or device permits.

    user = o.individual('User', 'you')

    a = o.individual(

        'AdvertisingDataControl',

        'If you would like to opt out of the Technologies we employ on our websites, services, applications, or tools, you may do so by blocking, deleting, or disabling them as your browser or device permits.',

        [
            o.property('initiated_by', user),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'blocking, deleting, or disabling them as your browser or device permits.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    #                                                                       #
    # HOW WE SHARE YOUR INFORMATION                                         #
    #                                                                       #
    #########################################################################




    #########################################################################
    # We may disclose your personal information on occasion to third parties (as described below) in order to provide the products or services that you have requested.

    user = o.individual('User', 'your')
    first_party = o.individual('FirstParty', 'We')
    third_parties = o.individual('ThirdParty', 'third parties')

    a = o.individual(

        'TPSharing',

        'We may disclose your personal information on occasion to third parties (as described below) in order to provide the products or services that you have requested.',

        [
            o.property('initiated_by', first_party),

            o.property('shares_with', third_parties),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'in order to provide the products or services that you have requested.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Disclosure may be made to third-party service providers and affiliated companies listed in this section below. In each case described in this section, you can be assured that we will only share your personal information in accordance with this Privacy Policy and the applicable terms that govern your use of our services. We will engage sub-processors for the processing of your personal information. You should know that when we share your personal information with a third-party service provider under any circumstance described in this section, we will contractually specify that the third party is subject to practices and obligations to comply with applicable local data protection laws. We will contractually ensure compliance by any third-party service providers with the privacy standards that apply to them in your home jurisdiction.

    user = o.individual('User', 'you')
    first_party = o.individual('FirstParty')


    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'third-party service providers')),
        o.property('shares_with', o.individual('ThirdParty', 'affiliated companies')),
        o.property('shares_with', o.individual('ThirdParty', 'sub-processors')),
    ]

    data = [
        o.property('applies_to', o.individual(
            'PersonalData',
            'personal information',
            [o.property('provided_by', user)])),
    ]

    basis = [
        o.property('has_basis', o.individual(
            'LegalBasis',
            'in accordance with this Privacy Policy')),

        o.property('has_basis', o.individual(
            'LegalBasis',
            'the applicable terms that govern your use of our services.')),

        o.property('has_basis', o.individual(
            'LegalBasis',
            'applicable local data protection laws.')),
    ]

    a = o.individual(

        'TPSharing',

        'Disclosure may be made to third-party service providers and affiliated companies listed in this section below. In each case described in this section, you can be assured that we will only share your personal information in accordance with this Privacy Policy and the applicable terms that govern your use of our services. We will engage sub-processors for the processing of your personal information. You should know that when we share your personal information with a third-party service provider under any circumstance described in this section, we will contractually specify that the third party is subject to practices and obligations to comply with applicable local data protection laws. We will contractually ensure compliance by any third-party service providers with the privacy standards that apply to them in your home jurisdiction.',

        [
            o.property('initiated_by', first_party),

            *third_parties,

            *data,

            *basis,
            
            o.property('binded_to', o.individual(
                'DataProtection',
                'Disclosure may be made to third-party service providers and affiliated companies listed in this section below. In each case described in this section, you can be assured that we will only share your personal information in accordance with this Privacy Policy and the applicable terms that govern your use of our services. We will engage sub-processors for the processing of your personal information. You should know that when we share your personal information with a third-party service provider under any circumstance described in this section, we will contractually specify that the third party is subject to practices and obligations to comply with applicable local data protection laws. We will contractually ensure compliance by any third-party service providers with the privacy standards that apply to them in your home jurisdiction.',
                [
                    o.property('initiated_by', first_party),

                    *data,

                    *basis,

                    o.property('has_mechanism', o.individual(
                        'SecurityMechanism',
                        'privacy standards')),
                ]
            )),
            
            o.property('previous_is', a),
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
        o.property('shares_with', o.individual('ThirdParty', 'affiliated companies.')),
        o.property('shares_with', o.individual('ThirdParty', 'third-party service providers,')),
    ]

    a = o.individual(

        'TPSharing',

        'In order to conduct business operations smoothly in providing you with the full capabilities of our products and services, we may disclose your personal information from time to time to our affiliated companies. We may also share your information as described in this Privacy Policy with our third-party service providers, to comply with legal obligations, to protect and defend our rights and property or with your permission.',

        [
            o.property('initiated_by', first_party),

            *third_parties,

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'In order to conduct business operations smoothly in providing you with the full capabilities of our products and services,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to protect and defend our rights and property or with your permission.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'as described in this Privacy Policy')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'to comply with legal obligations,')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Our third-party service providers include, without limitation, our mailing houses, delivery service providers, telecommunications companies, data centers, data storage facilities, customer service providers, advertising and marketing service providers. Such third-party service providers will be processing your personal information on our behalf or for one or more of the purposes listed herein.

    user = o.individual('User', 'your')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'third-party service providers')),
        o.property('shares_with', o.individual('ThirdParty', 'mailing houses,')),
        o.property('shares_with', o.individual('ThirdParty', 'delivery service providers,')),
        o.property('shares_with', o.individual('ThirdParty', 'telecommunications companies,')),
        o.property('shares_with', o.individual('ThirdParty', 'data centers,')),
        o.property('shares_with', o.individual('ThirdParty', 'data storage facilities,')),
        o.property('shares_with', o.individual('ThirdParty', 'customer service providers,')),
        o.property('shares_with', o.individual('ThirdParty', 'advertising and marketing service providers.')),
    ]

    a = o.individual(

        'TPSharing',

        'Our third-party service providers include, without limitation, our mailing houses, delivery service providers, telecommunications companies, data centers, data storage facilities, customer service providers, advertising and marketing service providers. Such third-party service providers will be processing your personal information on our behalf or for one or more of the purposes listed herein.',

        [
            o.property('initiated_by', first_party),

            *third_parties,

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'for one or more of the purposes listed herein.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Vendors and Service Providers. We may share any information we receive with vendors and service providers. The types of service providers (processors) to whom we entrust personal information include service providers for: (i) provision of IT and related services; (ii) provision of information and services you have requested; (iii) customer service activities; and (iv) in connection with the provision of the products, services and website. We have executed appropriate contracts with the service providers that prohibit them from using or sharing personal information except as necessary to perform the contracted services on our behalf or to comply with applicable legal requirements.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'vendors')),
        o.property('shares_with', o.individual('ThirdParty', 'service providers.')),
    ]

    a = o.individual(

        'TPSharing',

        'Vendors and Service Providers. We may share any information we receive with vendors and service providers. The types of service providers (processors) to whom we entrust personal information include service providers for: (i) provision of IT and related services; (ii) provision of information and services you have requested; (iii) customer service activities; and (iv) in connection with the provision of the products, services and website. We have executed appropriate contracts with the service providers that prohibit them from using or sharing personal information except as necessary to perform the contracted services on our behalf or to comply with applicable legal requirements.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'any information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'provision of IT and related services;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'provision of information and services you have requested;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'customer service activities;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'in connection with the provision of the products, services and website.')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to perform the contracted services on our behalf')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to comply with applicable legal requirements.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'applicable legal requirements.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'We have executed appropriate contracts with the service providers that prohibit them from using or sharing personal information except as necessary')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Third-Party Services. You may choose to share personal information with other third-party services (e.g., Strava, Wechat, Google Fit, Relive). Once your personal information has been shared with a third-party service, it will also be subject to the third-party service’s privacy policy. We encourage you to closely read each third-party service’s privacy policy before sharing your personal information with them. Please note that we do not control and we are not responsible for the third-party service’s processing of your personal information.

    user = o.individual('User', 'You')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'other third-party services')),
        o.property('shares_with', o.individual('ThirdParty', 'Strava')),
        o.property('shares_with', o.individual('ThirdParty', 'Wechat')),
        o.property('shares_with', o.individual('ThirdParty', 'Google Fit')),
        o.property('shares_with', o.individual('ThirdParty', 'Relive')),
    ]

    data = [
        o.property('applies_to', o.individual(
            'PersonalData',
            'personal information',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'TPSharing',

        'Third-Party Services. You may choose to share personal information with other third-party services (e.g., Strava, Wechat, Google Fit, Relive). Once your personal information has been shared with a third-party service, it will also be subject to the third-party service’s privacy policy. We encourage you to closely read each third-party service’s privacy policy before sharing your personal information with them. Please note that we do not control and we are not responsible for the third-party service’s processing of your personal information.',

        [
            o.property('initiated_by', first_party),
            
            *data,

            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'You may choose to share personal information with other third-party services',
                [
                    o.property('initiated_by', user),
                    *data,
                ])),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'it will also be subject to the third-party service’s privacy policy.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Business Partners. We may share personal information with our business partners to provide you with a product or service that you have requested. We may also provide personal information to business partners with whom we may jointly offer products or services, or whose products or services we believe may be of interest to you. In such cases, our business partner’s name will appear, along with us. We require our business partners to agree in writing to maintain the confidentiality and security of personal information they maintain on our behalf and not to use it for any purpose other than the purpose for which we provided them.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'our business partners')),
    ]

    data = [
        o.property('applies_to', o.individual(
            'PersonalData',
            'personal information',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'TPSharing',

        'Business Partners. We may share personal information with our business partners to provide you with a product or service that you have requested. We may also provide personal information to business partners with whom we may jointly offer products or services, or whose products or services we believe may be of interest to you. In such cases, our business partner’s name will appear, along with us. We require our business partners to agree in writing to maintain the confidentiality and security of personal information they maintain on our behalf and not to use it for any purpose other than the purpose for which we provided them.',

        [
            o.property('initiated_by', first_party),

            *third_parties,

            *data,

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to provide you with a product or service that you have requested.')),

            o.property('binded_to', o.individual(
                    'DataProtection',
                    'Business Partners. We may share personal information with our business partners to provide you with a product or service that you have requested. We may also provide personal information to business partners with whom we may jointly offer products or services, or whose products or services we believe may be of interest to you. In such cases, our business partner’s name will appear, along with us. We require our business partners to agree in writing to maintain the confidentiality and security of personal information they maintain on our behalf and not to use it for any purpose other than the purpose for which we provided them.',
                    [
                        o.property('initiated_by', first_party),
                        *data,
                        o.property('has_mechanism', o.individual(
                            'OrganizationalSecurityMeasure',
                            'We require our business partners to agree in writing to maintain the confidentiality and security of personal information they maintain on our behalf and not to use it for any purpose other than the purpose for which we provided them.')),
                    ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Affiliates. We may share your personal information with our company affiliates for the purposes set forth in this Privacy Policy, including our administrative purposes, activities such as IT management, or for them to provide services to you or support and supplement the services we provide.

    user = o.individual('User')
    first_party = o.individual('FirstParty', 'We')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'our company affiliates')),
    ]

    a = o.individual(

        'TPSharing',

        'Affiliates. We may share your personal information with our company affiliates for the purposes set forth in this Privacy Policy, including our administrative purposes, activities such as IT management, or for them to provide services to you or support and supplement the services we provide.',

        [
            o.property('initiated_by', first_party),

            *third_parties,

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'for the purposes set forth in this Privacy Policy,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'including our administrative purposes,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'activities such as IT management,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'for them to provide services to you or support and supplement the services we provide.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Displaying to Your Friends. With your prior consent, we may share your personal information, such as, steps, weight, calories burned, sleep data to your friends.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'your friends.')),
    ]

    data = [
        o.property('applies_to', o.individual(
            'PersonalData',
            'personal information,',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'HealthData',
            'steps,',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'HealthData',
            'weight,',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'HealthData',
            'calories burned,',
            [o.property('provided_by', user)])),

        o.property('applies_to', o.individual(
            'HealthData',
            'sleep data',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'TPSharing',

        'Displaying to Your Friends. With your prior consent, we may share your personal information, such as, steps, weight, calories burned, sleep data to your friends.',

        [
            o.property('initiated_by', first_party),

            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'With your prior consent,',
                [
                    o.property('initiated_by', user),
                    *data
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Disclosures to Protect Us or Others as Required by Law and Similar Disclosures. We may access, preserve, and disclose your personal information, other account information, and content if we believe doing so is required or appropriate to: (i) comply with law enforcement or national security requests and legal process, such as a court order or subpoena (including in a country other than your home country); (ii) respond to your requests; (iii) protect your, ours or others’ rights, property, or safety; (iv) to enforce our policies or contracts; (v) to collect amounts owed to us; (vi) when we believe disclosure is necessary or appropriate to prevent physical harm or financial loss or in connection with an investigation or prosecution of suspected or actual illegal activity; or (vii) if we, in good faith, believe that disclosure is otherwise necessary or advisable.

    user = o.individual('User', 'your')
    first_party = o.individual('FirstParty', 'we')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty')),
    ]

    a = o.individual(

        'TPSharing',

        'Disclosures to Protect Us or Others as Required by Law and Similar Disclosures. We may access, preserve, and disclose your personal information, other account information, and content if we believe doing so is required or appropriate to: (i) comply with law enforcement or national security requests and legal process, such as a court order or subpoena (including in a country other than your home country); (ii) respond to your requests; (iii) protect your, ours or others’ rights, property, or safety; (iv) to enforce our policies or contracts; (v) to collect amounts owed to us; (vi) when we believe disclosure is necessary or appropriate to prevent physical harm or financial loss or in connection with an investigation or prosecution of suspected or actual illegal activity; or (vii) if we, in good faith, believe that disclosure is otherwise necessary or advisable.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'other account information,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'Data',
                'content',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'SecurityPurpose',
                'comply with law enforcement or national security requests and legal process, such as a court order or subpoena (including in a country other than your home country);')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'respond to your requests;')),

            o.property('has_purpose', o.individual(
                'SecurityPurpose',
                'protect your, ours or others’ rights, property, or safety;')),

            o.property('has_purpose', o.individual(
                'SecurityPurpose',
                'to enforce our policies or contracts;')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to collect amounts owed to us;')),

            o.property('has_purpose', o.individual(
                'SecurityPurpose',
                'when we believe disclosure is necessary or appropriate to prevent physical harm or financial loss or in connection with an investigation or prosecution of suspected or actual illegal activity;')),

            o.property('has_purpose', o.individual(
                'DataActivityPurpose',
                'if we, in good faith, believe that disclosure is otherwise necessary or advisable.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Merger, Sale, or Other Asset Transfers. If we are involved in a merger, acquisition, financing due diligence, reorganization, bankruptcy, receivership, transition of service to another provider or asset sale of all or a portion of our assets, then your information may be sold or transferred as part of such a transaction as permitted by law and/or contract. You will be notified via email and/or a prominent notice on our website or in the Zepp App of any changes in ownership, uses of your personal information, and choices you may have regarding your personal information. We will endeavor to direct the transferee to use personal information in a manner that is consistent with the Privacy Policy in effect at the time such personal information was collected.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'PolicyChange',

        'Merger, Sale, or Other Asset Transfers. If we are involved in a merger, acquisition, financing due diligence, reorganization, bankruptcy, receivership, transition of service to another provider or asset sale of all or a portion of our assets, then your information may be sold or transferred as part of such a transaction as permitted by law and/or contract. You will be notified via email and/or a prominent notice on our website or in the Zepp App of any changes in ownership, uses of your personal information, and choices you may have regarding your personal information. We will endeavor to direct the transferee to use personal information in a manner that is consistent with the Privacy Policy in effect at the time such personal information was collected.',

        [
            o.property('initiated_by', first_party),

            o.property('has_cause', o.individual(
                'MergeAcquisitionCause',
                'If we are involved in a merger, acquisition, financing due diligence, reorganization, bankruptcy, receivership, transition of service to another provider or asset sale of all or a portion of our assets,')),
            
            o.property('binded_to', o.individual(
                'FPNotification',
                'Merger, Sale, or Other Asset Transfers. If we are involved in a merger, acquisition, financing due diligence, reorganization, bankruptcy, receivership, transition of service to another provider or asset sale of all or a portion of our assets, then your information may be sold or transferred as part of such a transaction as permitted by law and/or contract. You will be notified via email and/or a prominent notice on our website or in the Zepp App of any changes in ownership, uses of your personal information, and choices you may have regarding your personal information. We will endeavor to direct the transferee to use personal information in a manner that is consistent with the Privacy Policy in effect at the time such personal information was collected.',
                [
                    o.property('initiated_by', first_party),
                    o.property('notifies', user),
                    o.property('has_mechanism', o.individual(
                        'Email',
                        'via email')),
                    o.property('has_mechanism', o.individual(
                        'OnWebsitePage',
                        'prominent notice on our website')),
                    o.property('has_mechanism', o.individual(
                        'OnServiceApp',
                        'in the Zepp App')),
                ])),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'DataProtection',

        'We are committed to ensuring that your personal information is secure, and we will take all practicable steps to safeguard your personal information. However, you should be aware that the use of the Internet is not entirely secure, and for this reason we cannot guarantee the security or integrity of any personal information we process.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'SecurityMechanism',
                'all practicable steps to safeguard your personal information.')),

            o.property('has_mechanism', o.individual(
                'UserMaintainsSecurity',
                'you should be aware that the use of the Internet is not entirely secure, and for this reason we cannot guarantee the security or integrity of any personal information we process.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # To prevent unauthorized access, disclosure or other similar risks and to comply with applicable privacy and security laws in the countries in which we operate, we have put in place reasonable administrative, technical and physical controls and procedures designed to safeguard and secure the information we collect from your use of our products and services. We will use reasonable efforts designed to safeguard your personal information.

    user = o.individual('User', 'your')
    first_party = o.individual('FirstParty', 'we')

    a = o.individual(

        'FPCollection',

        'To prevent unauthorized access, disclosure or other similar risks and to comply with applicable privacy and security laws in the countries in which we operate, we have put in place reasonable administrative, technical and physical controls and procedures designed to safeguard and secure the information we collect from your use of our products and services. We will use reasonable efforts designed to safeguard your personal information.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to safeguard and secure the information we collect from your use of our products and services.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'to comply with applicable privacy and security laws in the countries in which we operate,')),
            
            o.property('binded_to', o.individual(
                'DataProtection',
                'To prevent unauthorized access, disclosure or other similar risks and to comply with applicable privacy and security laws in the countries in which we operate, we have put in place reasonable administrative, technical and physical controls and procedures designed to safeguard and secure the information we collect from your use of our products and services. We will use reasonable efforts designed to safeguard your personal information.',
                [
                    o.property('initiated_by', first_party),
                    o.property('has_mechanism', o.individual(
                        'OrganizationalSecurityMeasure',
                        'reasonable administrative,')),
                    o.property('has_mechanism', o.individual(
                        'TechnicalSecurityMeasure',
                        'technical')),
                    o.property('has_mechanism', o.individual(
                        'TechnicalSecurityMeasure',
                        'and physical controls and procedures')),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # For example, when you access your account, you can choose to use our two-step verification process for better security. When you send or receive data from your device to our servers, we make sure they are encrypted using Secure Sockets Layer ('SSL') and other algorithms.

    user = o.individual('User', 'you')
    first_party = o.individual('FirstParty', 'we')

    a = o.individual(

        'DataProtection',

        'For example, when you access your account, you can choose to use our two-step verification process for better security. When you send or receive data from your device to our servers, we make sure they are encrypted using Secure Sockets Layer (`SSL`) and other algorithms.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'data',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'AccessControls',
                'two-step verification process')),

            o.property('has_mechanism', o.individual(
                'TechnicalSecurityMeasure',
                'they are encrypted using Secure Sockets Layer (`SSL`) and other algorithms.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # All your personal information is stored on secure servers that are protected in controlled facilities. We classify your data based on importance and sensitivity, and endeavor to ensure that your personal information has an appropriate security level. The files and records containing your personal information will be kept in our offices and/or on our servers or those of our service providers and only those employees that require it for the purposes of their duties will have access to this file. We have also implemented controls to require that our third-party service providers and partners have appropriate safeguards designed to protect your personal information as well. We make sure that our employees and third-party service providers who access the information to help provide you with our products and services are subject to strict contractual confidentiality obligations and may be disciplined or terminated if they fail to meet such obligations. In some cases, we have special access controls for cloud-based data storage as well. All in all, we regularly review our information collection, storage and processing practices, including physical security measures, in an effort to guard against any unauthorized access and use.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataProtection',

        'All your personal information is stored on secure servers that are protected in controlled facilities. We classify your data based on importance and sensitivity, and endeavor to ensure that your personal information has an appropriate security level. The files and records containing your personal information will be kept in our offices and/or on our servers or those of our service providers and only those employees that require it for the purposes of their duties will have access to this file. We have also implemented controls to require that our third-party service providers and partners have appropriate safeguards designed to protect your personal information as well. We make sure that our employees and third-party service providers who access the information to help provide you with our products and services are subject to strict contractual confidentiality obligations and may be disciplined or terminated if they fail to meet such obligations. In some cases, we have special access controls for cloud-based data storage as well. All in all, we regularly review our information collection, storage and processing practices, including physical security measures, in an effort to guard against any unauthorized access and use.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'TechnicalSecurityMeasure',
                'secure servers that are protected in controlled facilities.')),

            o.property('has_mechanism', o.individual(
                'OrganizationalSecurityMeasure',
                'We classify your data based on importance and sensitivity,')),

            o.property('has_mechanism', o.individual(
                'LockedOffice',
                'in our offices and/or on our servers or those of our service providers')),

            o.property('has_mechanism', o.individual(
                'SecurityTraining',
                'only those employees that require it for the purposes of their duties will have access to this file.')),

            o.property('has_mechanism', o.individual(
                'AccessControls',
                'We have also implemented controls to require that our third-party service providers and partners have appropriate safeguards designed to protect your personal information as well.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # However, despite these efforts, no security measures are perfect or impenetrable and no method of data transmission can be guaranteed to prevent any interception or other type of misuse. We also depend on you to protect your information. If you become aware of any breach of security or privacy, please notify us immediately. To the fullest extent permitted by applicable law, we do not accept liability for unauthorized disclosure.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataProtection',

        'However, despite these efforts, no security measures are perfect or impenetrable and no method of data transmission can be guaranteed to prevent any interception or other type of misuse. We also depend on you to protect your information. If you become aware of any breach of security or privacy, please notify us immediately. To the fullest extent permitted by applicable law, we do not accept liability for unauthorized disclosure.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'UserMaintainsSecurity',
                'We also depend on you to protect your information.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # By using our products and services or providing personal information to us, you agree that we may communicate with you electronically regarding security, privacy, and administrative issues relating to your use. If we learn of a security system’s breach, we may attempt to notify you electronically by posting a notice on the website or through the product or service and/or by sending an e-mail to you. You may have a legal right to receive this notice in writing.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    data = [
        o.property('applies_to', o.individual(
            'PersonalData',
            'personal information',
            [o.property('provided_by', user)])),
    ]

    a = o.individual(

        'OptInOptOutControl',

        'By using our products and services or providing personal information to us, you agree that we may communicate with you electronically regarding security, privacy, and administrative issues relating to your use. If we learn of a security system’s breach, we may attempt to notify you electronically by posting a notice on the website or through the product or service and/or by sending an e-mail to you. You may have a legal right to receive this notice in writing.',

        [
            o.property('initiated_by', user),

            o.property('has_mechanism', o.individual(
                'DataProvision',
                'By using our products and services or providing personal information to us, you agree that we may communicate with you electronically')),

            o.property('binded_to', o.individual(
                'FPNotification',
                'If we learn of a security system’s breach, we may attempt to notify you electronically by posting a notice on the website or through the product or service and/or by sending an e-mail to you. You may have a legal right to receive this notice in writing.',
                [
                    o.property('initiated_by', first_party),

                    o.property('has_mechanism', o.individual(
                        'OnWebsitePage',
                        'electronically by posting a notice on the website')),

                    o.property('has_mechanism', o.individual(
                        'OnServiceApp',
                        'through the product or service')),

                    o.property('has_mechanism', o.individual(
                        'Email',
                        'sending an e-mail')),

                    o.property('has_mechanism', o.individual(
                        'PostalMail',
                        'notice in writing.')),
                ])),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'DataProtection',

        'You can play your part in safeguarding your personal information by not disclosing your login password or account information to anybody unless such person is duly authorized by you. Whenever you log in the Zepp App, particularly on somebody else`s mobile phones or on public Internet terminals, you should always log out at the end of your session.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'UserMaintainsSecurity',
                'by not disclosing your login password or account information to anybody unless such person is duly authorized by you. Whenever you log in the Zepp App, particularly on somebody else`s mobile phones or on public Internet terminals, you should always log out at the end of your session.')),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'OptInOptOutControl',

        'The privacy choices you may have about your personal information are determined by applicable law and are described below.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'are determined by applicable law')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # We may occasionally send you push notifications through our mobile applications with version updates and other notices that may be of interest to you. You may at any time opt-out from receiving these types of communications by changing the settings on your mobile device. We may also collect location-based information if you use our mobile applications. You may opt-out of this collection by changing the settings on your mobile device.

    user = o.individual('User')

    a = o.individual(

        'AdvertisingDataControl',

        'We may occasionally send you push notifications through our mobile applications with version updates and other notices that may be of interest to you. You may at any time opt-out from receiving these types of communications by changing the settings on your mobile device. We may also collect location-based information if you use our mobile applications. You may opt-out of this collection by changing the settings on your mobile device.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'TrackingData',
                'location-based information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'ServiceAppForm',
                'by changing the settings on your mobile device.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Do Not Track (“DNT”) is a privacy preference that users can set in certain web browsers. DNT is a way for users to inform websites and services that they do not want certain information about their webpage visits collected over time and across websites or online services. Please note that we do not respond to or honor DNT signals or similar mechanisms transmitted by web browsers.

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Do Not Track (“DNT”) is a privacy preference that users can set in certain web browsers. DNT is a way for users to inform websites and services that they do not want certain information about their webpage visits collected over time and across websites or online services. Please note that we do not respond to or honor DNT signals or similar mechanisms transmitted by web browsers.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'Data',
                'certain information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'privacy preference that users can set in certain web browsers.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # As noted herein, you may stop or restrict the placement of cookies and other technologies on your computer or remove them from your browser by adjusting your web browser preferences. Please note that cookie-based opt-outs are not effective on mobile applications. However, on many mobile devices, application users may opt out of certain mobile ads via their device settings.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'OptInOptOutControl',

        'As noted herein, you may stop or restrict the placement of cookies and other technologies on your computer or remove them from your browser by adjusting your web browser preferences. Please note that cookie-based opt-outs are not effective on mobile applications. However, on many mobile devices, application users may opt out of certain mobile ads via their device settings.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'TrackingData',
                'cookies',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'by adjusting your web browser preferences.')),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'privacy preference that users can set in certain web browsers.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Our applications may need access to certain features on your device such as Wi-Fi network status. This information is used to allow the applications to run on your device and allow you to interact with the applications. At any time you may revoke your permissions by turning these off at the device level and/or contacting us via https://www.zepp.com/privacy-support.

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Our applications may need access to certain features on your device such as Wi-Fi network status. This information is used to allow the applications to run on your device and allow you to interact with the applications. At any time you may revoke your permissions by turning these off at the device level and/or contacting us via https://www.zepp.com/privacy-support.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'DeviceData',
                'Wi-Fi network status',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'Data',
                'information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'At any time you may revoke your permissions by turning these off at the device level')),

            o.property('has_mechanism', o.individual(
                'WebsiteForm',
                'contacting us via https://www.zepp.com/privacy-support.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # We recognize that privacy concerns differ from person to person. Therefore, we provide examples of ways we make available for you to choose to restrict the collection, use, disclosure or processing of your personal information and control your privacy settings: Log in and out of the account; Toggle on/off for other services and functionalities which deal with sensitive or personal information.

    user = o.individual('User', 'you')

    a = o.individual(

        'OptInOptOutControl',

        'We recognize that privacy concerns differ from person to person. Therefore, we provide examples of ways we make available for you to choose to restrict the collection, use, disclosure or processing of your personal information and control your privacy settings: Log in and out of the account; Toggle on/off for other services and functionalities which deal with sensitive or personal information.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'Log in and out of the account;')),

            o.property('has_mechanism', o.individual(
                'ServiceAppForm',
                'Toggle on/off for other services and functionalities which deal with sensitive or personal information.')),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'DataRetention',

        'We retain personal information we receive as described in this Privacy Policy for as long as you use our products, services and websites or as necessary to fulfill the purpose(s) for which it was collected, provide our services, resolve disputes, establish legal defenses, conduct audits, pursue legitimate business purposes, enforce our agreements, and comply with applicable laws. We shall cease to retain personal information, or remove the means by which the personal information can be associated with particular individuals, as soon as it is reasonable to assume that the purpose for which that personal information was collected is no longer being served by retention of the personal information.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'provide our services,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'resolve disputes,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'establish legal defenses,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'conduct audits,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'pursue legitimate business purposes,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'enforce our agreements,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'comply with applicable laws.')),

            o.property('lasts_for', o.individual(
                'DataRetentionTime',
                'as long as you use our products, services and websites')),

            o.property('lasts_for', o.individual(
                'DataRetentionTime',
                'as necessary to fulfill the purpose(s) for which it was collected,')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'as described in this Privacy Policy')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'pursue legitimate business purposes,')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'enforce our agreements,')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'comply with applicable laws.')),
            
            o.property('binded_to', o.individual(
                'DataProtection',
                'We shall cease to retain personal information, or remove the means by which the personal information can be associated with particular individuals, as soon as it is reasonable to assume that the purpose for which that personal information was collected is no longer being served by retention of the personal information.',
                [
                    o.property('has_mechanism', o.individual(
                        'SecurityMechanism',
                        'We shall cease to retain personal information, or remove the means by which the personal information can be associated with particular individuals, as soon as it is reasonable to assume that the purpose for which that personal information was collected is no longer being served by retention of the personal information.')),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # If further processing is for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes according to the applicable laws, the data can be further retained by us even if the further processing is incompatible with original purposes in certain jurisdictions.

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    a = o.individual(

        'DataRetention',

        'If further processing is for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes according to the applicable laws, the data can be further retained by us even if the further processing is incompatible with original purposes in certain jurisdictions.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'Data',
                'data',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'If further processing is for archiving purposes in the public interest,')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'scientific or historical research purposes')),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'statistical purposes according')),

            o.property('lasts_for', o.individual(
                'DataRetentionTime',
                'the data can be further retained by us even if the further processing is incompatible with original purposes in certain jurisdictions.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'according to the applicable laws,')),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'OptInOptOutControl',

        'Access Personal Information about you, including: (i) confirming whether we are processing your personal information; (ii) obtaining access to or a copy of your personal information;',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'Personal Information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'confirming whether we are processing your personal information;')),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'obtaining access to or a copy of your personal information;')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Request Correction of your personal information where it is inaccurate, incomplete or outdated. In some cases, we may provide self-service tools that enable you to update your personal information;

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Request Correction of your personal information where it is inaccurate, incomplete or outdated. In some cases, we may provide self-service tools that enable you to update your personal information;',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'Request Correction of your personal information where it is inaccurate, incomplete or outdated.')),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'we may provide self-service tools that enable you to update your personal information;')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Request Deletion or Anonymization of your personal information when processing is based on your consent or when processing is unnecessary, excessive or non-compliant;

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Request Deletion or Anonymization of your personal information when processing is based on your consent or when processing is unnecessary, excessive or non-compliant;',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),
            
            o.property('binded_to', o.individual(
                'DataProtection',
                'Deletion or Anonymization of your personal information when processing is based on your consent or when processing is unnecessary, excessive or non-compliant;',
                [
                    o.property('has_mechanism', o.individual(
                        'PseudoAnonymization',
                        'Anonymization'))
                ])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'Request Deletion or Anonymization of your personal information when processing is based on your consent or when processing is unnecessary, excessive or non-compliant;')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Request Restriction or Blocking of or Object to our processing of your personal information;

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Request Restriction or Blocking of or Object to our processing of your personal information;',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information;',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'Request Restriction or Blocking of or Object to our processing of your personal information;')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Withdraw Your Consent to our processing of your personal information. If you refrain from providing personal information or withdraw your consent to processing, some features of our Service may not be available;

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Withdraw Your Consent to our processing of your personal information. If you refrain from providing personal information or withdraw your consent to processing, some features of our Service may not be available;',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information.',
                [o.property('provided_by', user)])),

            o.property('has_consequence', o.individual(
                'PartialServiceRestriction',
                'some features of our Service may not be available;')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Request Data Portability and receive an electronic copy of personal information that you have provided to us;

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Request Data Portability and receive an electronic copy of personal information that you have provided to us;',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'Request Data Portability and receive an electronic copy of personal information that you have provided to us;')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Be Informed about third parties with which your personal information has been shared; and

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Be Informed about third parties with which your personal information has been shared;',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Request any review of decisions which may have been taken exclusively based on automated processing if that could affect data subject rights.

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Request any review of decisions which may have been taken exclusively based on automated processing if that could affect data subject rights.',

        [
            o.property('initiated_by', user),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'Request any review of decisions which may have been taken exclusively based on automated processing if that could affect data subject rights.')),
            
            o.property('previous_is', a),
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

    user = o.individual('User', 'children', [
        o.property('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'children under 16'))
    ])
    first_party = o.individual('FirstParty')

    a = o.individual(

        'FPCollection',

        'Our products and services are not directed to children under 16 (and in certain jurisdictions under the age of 13) years of age.We don’t seek or intend to seek to receive any personal information from minors. Should a parent or guardian have reasons to believe that a minor has provided us with personal information without their prior consent, please contact us to ensure that the personal information is removed and the minor unsubscribes from any of the applicable services. If we learn that we have collected any personal information from children under 16 (and in certain jurisdictions under the age of 13) and we do not obtain permission from a parent, we will promptly take steps to delete such information and terminate the minor’s account.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'certain jurisdictions')),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'PolicyChange',

        'We keep our Privacy Policy under regular review and may update this Privacy Policy to reflect changes to our information practices. You understand and agree that you will be deemed to have accepted the updated Privacy Policy if you use the products or services after the updated Privacy Policy is posted. If, at any point, you do not agree to any portion of the Privacy Policy then in effect, you must immediately stop using the products and services. If we make material changes to our Privacy Policy, we will notify you by email (sent to the e-mail address specified in your account) or post the changes in our App. Such changes to our Privacy Policy shall apply from the effective date as set out in the notice or in our App. We encourage you to periodically review this page for the latest information on our privacy practices. Your continued use of products and services on mobile phones and/or any other device will be taken as acceptance of the updated Privacy Policy. Before we use personal information for any new purpose not originally authorized by you, we will endeavor to provide information regarding the new purpose and give you the opportunity to opt-out. Where your consent for the processing of personal information is otherwise required by law or contract, we will endeavor to comply with the law or contract.',

        [
            o.property('initiated_by', first_party),

            o.property('lasts_for', o.individual(
                'PolicyAcceptanceTime',
                'from the effective date')),

            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'You understand and agree that you will be deemed to have accepted the updated Privacy Policy if you use the products or services after the updated Privacy Policy is posted.',
                [o.property('initiated_by', user)])),

            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'Your continued use of products and services on mobile phones and/or any other device will be taken as acceptance of the updated Privacy Policy.',
                [o.property('initiated_by', user)])),

            o.property('binded_to', o.individual(
                'AdvertisingDataControl',
                'Before we use personal information for any new purpose not originally authorized by you, we will endeavor to provide information regarding the new purpose and give you the opportunity to opt-out.',
                [o.property('initiated_by', user)])),

            o.property('binded_to', o.individual(
                'OptInOptOutControl',
                'If, at any point, you do not agree to any portion of the Privacy Policy then in effect, you must immediately stop using the products and services.',
                [
                    o.property('has_consequence', o.individual(
                        'UserChoiceConsequence',
                        'you must immediately stop using the products and services.')),

                    o.property('initiated_by', user),
                ])),

            o.property('binded_to', o.individual(
                'FPNotification',
                'we will notify you by email (sent to the e-mail address specified in your account) or post the changes in our App.',
                [
                    o.property('initiated_by', first_party),
                    o.property('has_mechanism', o.individual(
                        'Email',
                        'by email')),
                    o.property('has_mechanism', o.individual(
                        'OnServiceApp',
                        'in our App.')),
                    o.property('has_mechanism', o.individual(
                        'OnWebsitePage',
                        'review this page for the latest information on our privacy practices.')),
                ])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    #                                                                       #
    # SUPPLEMENTAL CALIFORNIA ADDENDUM TO THIS PRIVACY POLICY               #
    #                                                                       #
    #########################################################################




    #########################################################################
    # This Supplemental California Addendum to this Privacy Policy (“California Addendum”) supplements and should be read in conjunction with this Privacy Policy. This California Addendum only applies to our processing of personal information that is subject to the California Consumer Privacy Act of 2018 (“CCPA”). The CCPA provides California residents with the right to know what categories of personal information we have collected about them and whether we disclosed that personal information for a business purpose (e.g., to a service provider) in the preceding twelve months. California residents can find this information below:

    user = o.individual('User', 'residents', [
        o.property('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'California residents'))
    ])

    a = o.individual(

        'OptInOptOutControl',

        'This Supplemental California Addendum to this Privacy Policy (“California Addendum”) supplements and should be read in conjunction with this Privacy Policy. This California Addendum only applies to our processing of personal information that is subject to the California Consumer Privacy Act of 2018 (“CCPA”). The CCPA provides California residents with the right to know what categories of personal information we have collected about them and whether we disclosed that personal information for a business purpose (e.g., to a service provider) in the preceding twelve months. California residents can find this information below:',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'California Consumer Privacy Act of 2018')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Categories of Third Parties Personal Information is Disclosed to for a Business Purpose. Identifiers such as alias, unique personal identifier, online identifier, IP address, email address, account name or other similar identifiers. Service providers, Affiliates, Other users or third-party services you share or interact with.

    user = o.individual('User', 'residents', [
        o.property('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'California residents'))
    ])
    first_party = o.individual('FirstParty')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'Service providers')),
        o.property('shares_with', o.individual('ThirdParty', 'Affiliates')),
        o.property('shares_with', o.individual('ThirdParty', 'Other users or third-party services you share or interact with')),
    ]

    a = o.individual(

        'TPSharing',

        'Categories of Third Parties Personal Information is Disclosed to for a Business Purpose. Identifiers such as alias, unique personal identifier, online identifier, IP address, email address, account name or other similar identifiers. Service providers, Affiliates, Other users or third-party services you share or interact with.',

        [
            o.property('initiated_by', first_party),

            *third_parties,

            o.property('applies_to', o.individual(
                'AccountData',
                'Identifiers such as alias,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'unique personal identifier,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'online identifier,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'IP address,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'email address,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'account name',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'AccountData',
                'other similar identifiers.',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'for a Business Purpose')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Biometric Info such as an individual’s physiological, biological, or behavioral characteristics, that can be used, singly or in combination with each other or with other identifying data, to establish individual identity. Biometric information includes, but is not limited to, gait patterns or rhythms, and sleep, health, or exercise data that contain identifying information. Service providers Affiliates

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'Service providers')),
        o.property('shares_with', o.individual('ThirdParty', 'Affiliates')),
    ]

    a = o.individual(

        'TPSharing',

        'Biometric Info such as an individual’s physiological, biological, or behavioral characteristics, that can be used, singly or in combination with each other or with other identifying data, to establish individual identity. Biometric information includes, but is not limited to, gait patterns or rhythms, and sleep, health, or exercise data that contain identifying information. Service providers Affiliates',

        [
            o.property('initiated_by', first_party),

            *third_parties,

            o.property('applies_to', o.individual(
                'BiometricData',
                'Biometric Info',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'BiometricData',
                'physiological',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'BiometricData',
                'biological',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'BiometricData',
                'behavioral characteristics',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'gait patterns or rhythms,',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'BiometricData',
                'behavioral characteristics',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'sleep',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'health',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'HealthData',
                'exercise data that contain identifying information.',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'that can be used, singly or in combination with each other or with other identifying data, to establish individual identity.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Internet or other electronic network activity information such as browsing history, search history and information regarding a consumer's interaction with a website, application, or advertisement. Service Affiliates Other users or third-party services you share or interact with

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'Service providers')),
        o.property('shares_with', o.individual('ThirdParty', 'Affiliates')),
        o.property('shares_with', o.individual('ThirdParty', 'Other users or third-party services you share or interact with')),
    ]

    a = o.individual(

        'TPSharing',

        'Internet or other electronic network activity information such as browsing history, search history and information regarding a consumer`s interaction with a website, application, or advertisement. Service Affiliates Other users or third-party services you share or interact with',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'TrackingData',
                'Internet',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'electronic network activity information',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'TrackingData',
                'browsing history',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'search history',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'ServiceData',
                'information regarding a consumer`s interaction with a website, application, or advertisement.',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Geo-location such as physical location or movements. Service providers Affiliates Other users or third-party services you share or interact with

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'Service providers')),
        o.property('shares_with', o.individual('ThirdParty', 'Affiliates')),
        o.property('shares_with', o.individual('ThirdParty', 'Other users or third-party services you share or interact with')),
    ]

    a = o.individual(

        'TPSharing',

        'Geo-location such as physical location or movements. Service providers Affiliates Other users or third-party services you share or interact with',

        [
            o.property('initiated_by', first_party),

            *third_parties,

            o.property('applies_to', o.individual(
                'TrackingData',
                'Geo-location',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Inferences drawn from other personal information to create a profile about a consumer. Service providers Affiliates

    user = o.individual('User')
    first_party = o.individual('FirstParty')

    third_parties = [
        o.property('shares_with', o.individual('ThirdParty', 'Service providers')),
        o.property('shares_with', o.individual('ThirdParty', 'Affiliates')),
    ]

    a = o.individual(

        'TPSharing',

        'Inferences drawn from other personal information to create a profile about a consumer. Service providers Affiliates',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'AnalyticsPurpose',
                'to create a profile about a consumer.')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # “Sales” of Personal Information under the CCPA. For purposes of the CCPA, we do not “sell” personal information, nor do we have actual knowledge of any “sale” of personal information of minors under 16 years of age.
   
    user = o.individual('User', 'residents', [
        o.property('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'California residents')),
        o.property('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'minors under 16 years of age.'))
    ])
    first_party = o.individual('FirstParty')

    a = o.individual(

        'TPSharing',

        '“Sales” of Personal Information under the CCPA. For purposes of the CCPA, we do not “sell” personal information, nor do we have actual knowledge of any “sale” of personal information of minors under 16 years of age.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'Personal Information',
                [o.property('provided_by', user)])),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Non-Discrimination. California residents have the right not to receive discriminatory treatment by us for the exercise of their rights conferred by the CCPA. 

    user = o.individual('User', 'residents', [
        o.property('hasSpecialCategory', o.individual(
            'UserSpecialCategory', 
            'California residents')),
    ])

    a = o.individual(

        'OptInOptOutControl',

        'Non-Discrimination. California residents have the right not to receive discriminatory treatment by us for the exercise of their rights conferred by the CCPA.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'receive discriminatory treatment',
                [o.property('provided_by', user)])),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'California residents have the right')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Authorized Agent. Only you, or someone legally authorized to act on your behalf, may make a verifiable consumer request related to your personal information. To designate an authorized agent, please contact us as set forth below.

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Authorized Agent. Only you, or someone legally authorized to act on your behalf, may make a verifiable consumer request related to your personal information. To designate an authorized agent, please contact us as set forth below.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information.',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'Only you, or someone legally authorized to act on your behalf, may make a verifiable consumer request related to your personal information.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'someone legally authorized to act on your behalf,')),
            
            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Verification. When you make a request, we will ask you to provide sufficient information that allows us to reasonably verify you are the person about whom we collected personal information or an authorized representative, which may include confirming the email address associated with any personal information we have about you.

    user = o.individual('User')

    a = o.individual(

        'OptInOptOutControl',

        'Verification. When you make a request, we will ask you to provide sufficient information that allows us to reasonably verify you are the person about whom we collected personal information or an authorized representative, which may include confirming the email address associated with any personal information we have about you.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information',
                [o.property('provided_by', user)])),

            o.property('has_mechanism', o.individual(
                'CommunicationMechanism',
                'you make a request,')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'an authorized representative,')),
            
            o.property('previous_is', a),
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

    a = o.individual(

        'DataRetention',

        'Personal information, which has fulfilled the purpose for which it was collected or used, and has reached the period of time during which personal information was to be possessed, will be destroyed in an irreversible way. After the expiration of the applicable period, information under the obligation of retention by applicable laws will be promptly destroyed in an irreversible way. Personal information stored in electronic files will be deleted safely in an irreversible way by using technical methods, and printed information will be destroyed by shredding or incinerating such information. Furthermore, in compliance with applicable laws, measures will be taken to destroy or separate the personal information of the users who have not used our services for a period of one year.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'PersonalData',
                'Personal information',
                [o.property('provided_by', user)])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'the purpose for which it was collected or used,')),

            o.property('lasts_for', o.individual(
                'DataRetentionTime',
                'has reached the period of time during which personal information was to be possessed,')),

            o.property('lasts_for', o.individual(
                'DataRetentionTime',
                'expiration of the applicable period,')),

            o.property('lasts_for', o.individual(
                'DataRetentionTime',
                'destroy or separate the personal information of the users who have not used our services for a period of one year.')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'by applicable laws')),
            
            o.property('binded_to', o.individual(
                'DataProtection',
                'Personal information stored in electronic files will be deleted safely in an irreversible way by using technical methods,',
                [
                    o.property('has_mechanism', o.individual(
                        'TechnicalSecurityMeasure',
                        'technical methods,')),
                ])),
            
            o.property('previous_is', a),
        ]
    )

    o.save()

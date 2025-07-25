from ontology.interface import Ontology


def build(**kwargs):

    o = Ontology(**kwargs, website='https://www.caresense.com/privacypolicy')

    #########################################################################
    #                                                                       #
    # POLICY CHANGE                                                         #
    #                                                                       #
    #########################################################################


    #########################################################################
    # MedTrak reserves the right to amend the Policy at any time—these changes will apply to all old and new data collected by MedTrak but will never relax the privacy and security standards currently in place. Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.

    first_party = o.individual('FirstParty', 'MedTrak')

    a = o.individual(

        'PolicyChange',

        'MedTrak reserves the right to amend the Policy at any time—these changes will apply to all old and new data collected by MedTrak but will never relax the privacy and security standards currently in place. Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.',

        [
            o.property('initiated_by', first_party),

            o.property('binded_to', o.individual(
                'FPNotification',
                'Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.',
                [
                    o.property('initiated_by', first_party),

                    o.property('has_mechanism', o.individual(
                        'OnWebsitePage',
                        'Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.')),
                ])),
        ]
    )




    #########################################################################
    #                                                                       #
    # FIRST PARTY COLLECTION                                                #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak gathers information from users who sign-up for our services (“Service”) through contracts, discussions and the website. Users are required to provide contact information such as name, company name, address, phone number, and email address. This information is used to setup the Service and provide support.

    a = o.individual(
        
        'FPCollection',
                 
        'MedTrak gathers information from users who sign-up for our services (“Service”) through contracts, discussions and the website. Users are required to provide contact information such as name, company name, address, phone number, and email address. This information is used to setup the Service and provide support.',

        [
            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('applies_to', o.individual(
                'AccountData', 
                'name',
                [o.property('provided_by', o.individual('User'))])),

            o.property('applies_to', o.individual(
                'AccountData', 
                'address', 
                [o.property('provided_by', o.individual('User'))])),

            o.property('applies_to', o.individual(
                'AccountData', 
                'phone number', 
                [o.property('provided_by', o.individual('User'))])),

            o.property('applies_to', o.individual(
                'AccountData', 
                'email address', 
                [o.property('provided_by', o.individual('User'))])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose', 
                'This information is used to setup the Service and provide support.')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # MedTrak also collects and logs information (IP addresses, login attempts) concerning website usage. This information is used to monitor attempted security penetrations, detect technical problems, and review site usage patterns.


    a = o.individual(
        
        'FPCollection',
                 
        'MedTrak also collects and logs information (IP addresses, login attempts) concerning website usage. This information is used to monitor attempted security penetrations, detect technical problems, and review site usage patterns.',

        [
            o.property('applies_to', o.individual(
                'TrackingData', 
                'IP addresses',
                [o.property('provided_by', o.individual('User'))])),

            o.property('applies_to', o.individual(
                'AccountData', 
                'login attempts',
                [o.property('provided_by', o.individual('User'))])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose', 
                'This information is used to monitor attempted security penetrations, detect technical problems, and review site usage patterns.')),

            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Potential users may sign-up on www.caresense.com to be contacted by a MedTrak representative. They will submit contact information that will only be used to set-up an appointment or demonstration.


    a = o.individual(
        
        'FPCollection',
                 
        'Potential users may sign-up on www.caresense.com to be contacted by a MedTrak representative. They will submit contact information that will only be used to set-up an appointment or demonstration.',

        [
            o.property('applies_to', o.individual(
                'TrackingData', 
                'contact information',
                [o.property('provided_by', o.individual('User'))])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose', 
                'that will only be used to set-up an appointment or demonstration.')),

            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    #                                                                       #
    # THIRD PARTY SHARING                                                   #
    #                                                                       #
    #########################################################################



    #########################################################################
    # Except as required to perform the Service, no information will be disclosed to third parties.

    a = o.individual(
        
        'TPSharing',
                 
        'Except as required to perform the Service, no information will be disclosed to third parties.',

        [
            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('shares_with', o.individual(
                'ThirdParty', 
                'third parties.')),

            o.property('applies_to', o.individual(
                'Data',
                'no information',
                [o.property('provided_by', o.individual('User'))])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose', 
                'to perform the Service')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # MedTrak does not currently transfer personal information to third parties. 

    a = o.individual(

        'TPSharing',

        'MedTrak does not currently transfer personal information to third parties.',

        [
            o.property('does', False),

            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('shares_with', o.individual(
                'ThirdParty', 
                'third parties.')),

            o.property('applies_to', o.individual(
                'PersonalData', 
                'personal information',
                [o.property('provided_by', o.individual('User'))])),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Information and data users collect using CareSense and store on MedTrak’s servers will not be reviewed, shared, or disseminated except as stated in the Business Associates Agreement and Software License Agreement or as required by law. 

    a = o.individual(

        'TPSharing',

        'Information and data users collect using CareSense and store on MedTrak’s servers will not be reviewed, shared, or disseminated except as stated in the Business Associates Agreement and Software License Agreement or as required by law.',

        [
            o.property('does', False),

            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('shares_with', o.individual(
                'ThirdParty', 
                'third parties.')),

            o.property('applies_to', o.individual(
                'Data', 
                'Information and data',
                [o.property('provided_by', o.individual('User'))])),

            o.property('has_basis', o.individual(
                'LegalBasis', 
                'Business Associates Agreement and Software License Agreement or as required by law.')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Personal information will not be shared with third parties.

    a = o.individual(

        'TPSharing',

        'Personal information will not be shared with third parties.',

        [
            o.property('does', False),

            o.property('initiated_by', o.individual(
                'FirstParty')),

            o.property('shares_with', o.individual(
                'ThirdParty', 
                'third parties.')),

            o.property('applies_to', o.individual(
                'PersonalData', 
                'Personal information',
                [o.property('provided_by', o.individual('User'))])),

            o.property('previous_is', a),
        ]
    )
    



    #########################################################################
    # Marketing statistics will be made available to third parties.

    a = o.individual(

        'TPSharing',

        'Marketing statistics will be made available to third parties.',

        [
            o.property('applies_to', o.individual(
                'NonPersonalData', 
                'Marketing statistics',
                [o.property('provided_by', o.individual('User'))])),

            o.property('initiated_by', o.individual(
                'FirstParty')),

            o.property('shares_with', o.individual(
                'ThirdParty', 
                'third parties.')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # MedTrak also may be required to disclose an individual’s personal information in response to a lawful request by public authorities, including to meet national security or law enforcement requirements. 

    a = o.individual(
        
        'TPSharing',

        'MedTrak also may be required to disclose an individual’s personal information in response to a lawful request by public authorities, including to meet national security or law enforcement requirements.',

        [
            o.property('applies_to', o.individual(
                'PersonalData', 
                'personal information',
                [o.property('provided_by', o.individual('User'))])),

            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('shares_with', o.individual(
                'ThirdParty', 
                'third parties.')),
                
            o.property('has_basis',
                o.individual(
                'LegalBasis',
                'in response to a lawful request by public authorities, including to meet national security or law enforcement requirements.')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    #                                                                       #
    # DATA SECURITY                                                         #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak provides high quality security controls and protocols to ensure that all information and data is protected against loss, misuse, alteration, or unintentional destruction. MedTrak employs Secure Sockets Layer (SSL) technology to protect information traveling to and from the website and a firewall to block unauthorized use of the web server and database. Information and data are protected by access controls, passwords, employee training regarding security issues, and storage of sensitive information in locked offices, encrypted files, or behind the firewall.

    a = o.individual(
        
        'DataProtection',
        
        'MedTrak provides high quality security controls and protocols to ensure that all information and data is protected against loss, misuse, alteration, or unintentional destruction. MedTrak employs Secure Sockets Layer (SSL) technology to protect information traveling to and from the website and a firewall to block unauthorized use of the web server and database. Information and data are protected by access controls, passwords, employee training regarding security issues, and storage of sensitive information in locked offices, encrypted files, or behind the firewall.',
        
        [
            o.property('applies_to', o.individual(
                'Data', 
                'information and data',
                [o.property('provided_by', o.individual('User'))])),

            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('has_mechanism', o.individual(
                'TechnicalSecurityMeasure',
                'Secure Sockets Layer (SSL) technology')),

            o.property('has_mechanism', o.individual(
                'TechnicalSecurityMeasure',
                'firewall')),

            o.property('has_mechanism', o.individual(
                'TechnicalSecurityMeasure',
                'access controls, passwords')),

            o.property('has_mechanism', o.individual(
                'TechnicalSecurityMeasure',
                'encrypted files')),

            o.property('has_mechanism', o.individual(
                'TechnicalSecurityMeasure',
                'employee training regarding security issues')),

            o.property('has_mechanism', o.individual(
                'TechnicalSecurityMeasure',
                'storage of sensitive information in locked offices')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    #                                                                       #
    # USER CHOICE                                                           #
    #                                                                       #
    #########################################################################



    #########################################################################
    # If we ever were to engage in any onward transfers of your data with third parties, for a purpose other than which it was originally collected or subsequently authorized, we would provide you with an opt-out choice to limit the use and disclosure of your personal data. 

    user = o.individual('User', 'you')

    a = o.individual(
        
        'OptInOptOutControl',

        'If we ever were to engage in any onward transfers of your data with third parties, for a purpose other than which it was originally collected or subsequently authorized, we would provide you with an opt-out choice to limit the use and disclosure of your personal data.',

        [

            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'Data', 
                'data',
                [o.property('provided_by', user)])),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Users may request that MedTrak discontinues use of their contact information by contacting their MedTrak representative or by emailing info@caresense.com.

    user = o.individual('User', 'Users')

    a = o.individual(
        
        'AdvertisingDataControl',

        'Users may request that MedTrak discontinues use of their contact information by contacting their MedTrak representative or by emailing info@caresense.com.',

        [
            o.property('applies_to', o.individual(
                'TrackingData', 
                'contact information',
                [o.property('provided_by', user)])),

            o.property('initiated_by', user),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # If a patient would like to withdraw or refuse consent for a study, the patient should inform his/her doctor and MedTrak. A patient will always make the choice about the ways that personal information is used and disclosed.

    user = o.individual('User', 'patient')

    a = o.individual(
        
        'AdvertisingDataControl',

        'If a patient would like to withdraw or refuse consent for a study, the patient should inform his/her doctor and MedTrak. A patient will always make the choice about the ways that personal information is used and disclosed.',

        [
            o.property('applies_to', o.individual(
                'PersonalData', 
                'personal information',
                [o.property('provided_by', user)])),

            o.property('initiated_by', user),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # When using the iOS CareSense patient app, MedTrak will ask for permission to access HealthKit data to track your step count. If HealthKit permission is not granted, only the step counting aspects of the app will stop working. 

    user = o.individual('User', 'your')

    a = o.individual(
        
        'OptInOptOutControl',

        'When using the iOS CareSense patient app, MedTrak will ask for permission to access HealthKit data to track your step count. If HealthKit permission is not granted, only the step counting aspects of the app will stop working.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'HealthData',
                'step count',
                [o.property('provided_by', user)])),

            o.property('has_consequence', o.individual(
                'PartialServiceRestriction',
                'only the step counting aspects of the app will stop working.')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    #                                                                       #
    # DATA RETENTION                                                        #
    #                                                                       #
    #########################################################################



    #########################################################################
    # Personal information will be stored only as long as is necessary for the purposes for which it was collected, or as permitted by law. 

    a = o.individual(
        'DataRetention',

        'Personal information will be stored only as long as is necessary for the purposes for which it was collected, or as permitted by law.',

        [
            o.property('applies_to', o.individual(
                'PersonalData', 
                'Personal information',
                [o.property('provided_by', o.individual('User'))])),

            o.property('initiated_by', o.individual('FirstParty')),

            o.property('lasts_for', o.individual(
                'DataRetentionTime',
                'as long as is necessary')),

            o.property('has_basis', o.individual(
                'LegalBasis',
                'as permitted by law.')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    #                                                                       #
    # DATA USE                                                              #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak uses aggregated, de-identified information and data to create marketing statistics and average scores viewable by all users.

    first_party = o.individual('FirstParty', 'MedTrak')
    user = o.individual('User')

    data = [
        o.property('applies_to', o.individual(
            'Data',
            'information and data',
            [o.property('provided_by', user)])),
    ]
    
    a = o.individual(
        
        'DataUse',

        'MedTrak uses aggregated, de-identified information and data to create marketing statistics and average scores viewable by all users.',

        [
            o.property('initiated_by', first_party),

            *data,

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to create marketing statistics and average scores viewable by all users.')),

            o.property('binded_to', o.individual(
                'DataProtection',
                'uses aggregated, de-identified information and data',
                [
                    o.property('initiated_by', first_party),
                    *data,
                    o.property('has_mechanism', o.individual(
                        'PseudoAnonymization',
                        'de-identified')),
                ])),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Individual records in MedTrak’s databases may be accessed to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.

    a = o.individual(

        'DataUse',

        'Individual records in MedTrak’s databases may be accessed to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.',

        [
            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('applies_to', o.individual(
                'Data',
                'Individual records',
                [o.property('provided_by', o.individual('User'))])),

            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Personal information will be used in a manner consistent with the consent provided by the patient. 

    a = o.individual(

        'DataUse',

        'Personal information will be used in a manner consistent with the consent provided by the patient.',

        [
            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('applies_to', o.individual(
                'PersonalData',
                'Personal information',
                [o.property('provided_by', o.individual('User', 'patient'))])),
                    
            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.')),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    # Patient name and date of birth will be used to match patient records properly, and the email address will be used to collect information from the patient outside of the office. 

    user = o.individual('User', 'Patient')

    a = o.individual(

        'DataUse',

        'Patient name and date of birth will be used to match patient records properly',

        [
            o.property('initiated_by', o.individual(
                'FirstParty', 
                'MedTrak')),

            o.property('applies_to', o.individual(
                'GenericData', 
                'name',
                [o.property('provided_by', user)])),

            o.property('applies_to', o.individual(
                'GenericData', 
                'date of birth',
                [o.property('provided_by', user)])),
                    
            o.property('has_purpose', o.individual(
                'ServiceProvisionPurpose',
                'to match patient records properly')),

            o.property('binded_to', o.individual(
                'DataUse',
                'the email address will be used to collect information from the patient outside of the office.',
                [
                    o.property('initiated_by', o.individual('FirstParty')),
                    o.property('applies_to', o.individual(
                        'TrackingData',
                        'email address',
                        [o.property('provided_by', user)])),
                    o.property('has_purpose', o.individual(
                        'ServiceProvisionPurpose',
                        'to collect information from the patient outside of the office.')),
                ])),

            o.property('previous_is', a),
        ]
    )




    #########################################################################
    #                                                                       #
    # USER ACCESS                                                           #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak acknowledges that individuals have the right to access the personal information/data that we maintain about them. Patients will be provided access to their own personal information stored on MedTrak’s servers in order to correct any problems or delete it. An individual who seeks access, or who seeks to correct, amend, or delete inaccurate data, should direct his query to info@caresense.com. If requested to remove data, we will respond within a reasonable timeframe.

    user = o.individual('User', 'individuals')

    a = o.individual(
        
        'OptInOptOutControl',
                 
        'MedTrak acknowledges that individuals have the right to access the personal information/data that we maintain about them. Patients will be provided access to their own personal information stored on MedTrak’s servers in order to correct any problems or delete it. An individual who seeks access, or who seeks to correct, amend, or delete inaccurate data, should direct his query to info@caresense.com. If requested to remove data, we will respond within a reasonable timeframe.',

        [
            o.property('initiated_by', user),

            o.property('applies_to', o.individual(
                'PersonalData',
                'personal information/data that we maintain about them.',
                [o.property('provided_by', user)])),

            o.property('previous_is', a),
        ]
    )
    



    #########################################################################
    # Users are required to maintain the security of their User Name and password as outlined in MedTrak’s password policy.

    user = o.individual('User', 'individuals')
    first_party = o.individual('FirstParty', 'MedTrak')

    a = o.individual(

        'DataProtection',

        'Users are required to maintain the security of their User Name and password as outlined in MedTrak’s password policy.',

        [
            o.property('initiated_by', first_party),

            o.property('applies_to', o.individual(
                'AccountData',
                'email address',
                [o.property('provided_by', user)])),
                    
            o.property('applies_to', o.individual(
                'AccountData',
                'password',
                [o.property('provided_by', user)])),
                    
            o.property('has_mechanism', o.individual(
                'OrganizationalSecurityMeasure',
                'Users are required to maintain the security')),

            o.property('previous_is', a),
        ]
    )

    o.save()

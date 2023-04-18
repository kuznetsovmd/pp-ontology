from ontology import Ontology


def process_caresense():

    o = Ontology('caresense', 'https://www.caresense.com/privacypolicy')

    #########################################################################
    #                                                                       #
    # POLICY CHANGE                                                         #
    #                                                                       #
    #########################################################################


    #########################################################################
    # MedTrak reserves the right to amend the Policy at any time—these changes will apply to all old and new data collected by MedTrak but will never relax the privacy and security standards currently in place. Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.


    o.individual(

        'PolicyChangeActivity',

        'MedTrak reserves the right to amend the Policy at any time—these changes will apply to all old and new data collected by MedTrak but will never relax the privacy and security standards currently in place. Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.',

        [
            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'hasNotificationMechanism', 
                o.individual(
                    'OnWebsitePage',
                    'Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # FIRST PARTY COLLECTION                                                #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak gathers information from users who sign-up for our services (“Service”) through contracts, discussions and the website. Users are required to provide contact information such as name, company name, address, phone number, and email address. This information is used to setup the Service and provide support.

    o.individual(
        
        'DataCollectionActivity',
                 
        'MedTrak gathers information from users who sign-up for our services (“Service”) through contracts, discussions and the website. Users are required to provide contact information such as name, company name, address, phone number, and email address. This information is used to setup the Service and provide support.',

        [
            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'isAppliedTo', 
                o.individual(
                    'AccountData', 
                    'name',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'isAppliedTo', 
                o.individual(
                    'AccountData', 
                    'address', 
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'isAppliedTo', 
                o.individual(
                    'AccountData', 
                    'phone number', 
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'isAppliedTo', 
                o.individual(
                    'AccountData', 
                    'email address', 
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'hasDataActivityPurpose', 
                o.individual(
                    'DataActivityPurpose', 
                    'This information is used to setup the Service and provide support.')),
        ]
    )




    #########################################################################
    # MedTrak also collects and logs information (IP addresses, login attempts) concerning website usage. This information is used to monitor attempted security penetrations, detect technical problems, and review site usage patterns.


    o.individual(
        
        'DataCollectionActivity',
                 
        'MedTrak also collects and logs information (IP addresses, login attempts) concerning website usage. This information is used to monitor attempted security penetrations, detect technical problems, and review site usage patterns.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'TrackingData', 
                    'IP addresses',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'isAppliedTo', 
                o.individual(
                    'AccountData', 
                    'login attempts',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'hasDataActivityPurpose', 
                o.individual(
                    'DataActivityPurpose', 
                    'This information is used to monitor attempted security penetrations, detect technical problems, and review site usage patterns.')),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),
        ]
    )




    #########################################################################
    # Potential users may sign-up on www.caresense.com to be contacted by a MedTrak representative. They will submit contact information that will only be used to set-up an appointment or demonstration.


    o.individual(
        
        'DataCollectionActivity',
                 
        'Potential users may sign-up on www.caresense.com to be contacted by a MedTrak representative. They will submit contact information that will only be used to set-up an appointment or demonstration.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'TrackingData', 
                    'contact information',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'hasDataActivityPurpose', 
                o.individual(
                    'DataActivityPurpose', 
                    'that will only be used to set-up an appointment or demonstration.')),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),
        ]
    )




    #########################################################################
    #                                                                       #
    # THIRD PARTY SHARING                                                   #
    #                                                                       #
    #########################################################################



    #########################################################################
    # Except as required to perform the Service, no information will be disclosed to third parties.


    o.individual(
        
        'DataSharingActivity',
                 
        'Except as required to perform the Service, no information will be disclosed to third parties.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'Data',
                    'no information',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'hasDataActivityPurpose', 
                o.individual(
                    'DataActivityPurpose', 
                    '')),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'sharesDataWithAgent', 
                o.individual(
                    'ThirdParties', 
                    'third parties.')),
        ]
    )




    #########################################################################
    # MedTrak does not currently transfer personal information to third parties. 
    # !!!!!!!!!! doesnt !!!!!!!!!!


    o.individual(

        'DataSharingActivity',

        'MedTrak does not currently transfer personal information to third parties.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'PersonalData', 
                    'personal information',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'sharesDataWithAgent', 
                o.individual(
                    'ThirdParties', 
                    'third parties.')),
        ]
    )




    #########################################################################
    # Information and data users collect using CareSense and store on MedTrak’s servers will not be reviewed, shared, or disseminated except as stated in the Business Associates Agreement and Software License Agreement or as required by law. 
    # !!!!!!!!!! doesnt !!!!!!!!!!


    o.individual(

        'DataSharingActivity',

        'Information and data users collect using CareSense and store on MedTrak’s servers will not be reviewed, shared, or disseminated except as stated in the Business Associates Agreement and Software License Agreement or as required by law.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'Data', 
                    'Information and data',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'sharesDataWithAgent', 
                o.individual(
                    'ThirdParties', 
                    'third parties.')),

            o.connection(
                'hasLegalBasis', 
                o.individual(
                    'LegalBasis', 
                    'Business Associates Agreement and Software License Agreement or as required by law.')),
        ]
    )




    #########################################################################
    # Personal information will not be shared with third parties.
    # !!!!!!!!!! doesnt !!!!!!!!!!


    o.individual(

        'DataSharingActivity',

        'Personal information will not be shared with third parties.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'PersonalData', 
                    'Personal information',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty')),

            o.connection(
                'sharesDataWithAgent', 
                o.individual(
                    'ThirdParties', 
                    'third parties.')),
        ]
    )
    



    #########################################################################
    # Marketing statistics will be made available to third parties.
    # !!!!!!!!!! does !!!!!!!!!!


    o.individual(

        'DataSharingActivity',

        'Marketing statistics will be made available to third parties.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'NonPersonalData', 
                    'Marketing statistics',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty')),

            o.connection(
                'sharesDataWithAgent', 
                o.individual(
                    'ThirdParties', 
                    'third parties.')),
        ]
    )




    #########################################################################
    # MedTrak also may be required to disclose an individual’s personal information in response to a lawful request by public authorities, including to meet national security or law enforcement requirements. 
    # !!!!!!!!!! does !!!!!!!!!!


    o.individual(
        'DataSharingActivity',

        'MedTrak also may be required to disclose an individual’s personal information in response to a lawful request by public authorities, including to meet national security or law enforcement requirements.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'PersonalData', 
                    'personal information',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'sharesDataWithAgent', 
                o.individual(
                    'ThirdParties', 
                    'third parties.')),
                    
            o.connection(
                'hasLegalBasis',
                o.individual(
                    'LegalBasis',
                    'in response to a lawful request by public authorities, including to meet national security or law enforcement requirements.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # DATA SECURITY                                                         #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak provides high quality security controls and protocols to ensure that all information and data is protected against loss, misuse, alteration, or unintentional destruction. MedTrak employs Secure Sockets Layer (SSL) technology to protect information traveling to and from the website and a firewall to block unauthorized use of the web server and database. Information and data are protected by access controls, passwords, employee training regarding security issues, and storage of sensitive information in locked offices, encrypted files, or behind the firewall.
    # !!!!!!!!!! does !!!!!!!!!!


    o.individual(
        
        'Activity',
        
        'MedTrak provides high quality security controls and protocols to ensure that all information and data is protected against loss, misuse, alteration, or unintentional destruction. MedTrak employs Secure Sockets Layer (SSL) technology to protect information traveling to and from the website and a firewall to block unauthorized use of the web server and database. Information and data are protected by access controls, passwords, employee training regarding security issues, and storage of sensitive information in locked offices, encrypted files, or behind the firewall.',
        
        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'Data', 
                    'information and data',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'hasSecurityMechanism',  
                o.individual(
                    'TechnicalMeasure',
                    'Secure Sockets Layer (SSL) technology')),

            o.connection(
                'hasSecurityMechanism',  
                o.individual(
                    'TechnicalMeasure',
                    'firewall')),

            o.connection(
                'hasSecurityMechanism',  
                o.individual(
                    'TechnicalMeasure',
                    'access controls, passwords')),

            o.connection(
                'hasSecurityMechanism',  
                o.individual(
                    'TechnicalMeasure',
                    'encrypted files')),

            o.connection(
                'hasSecurityMechanism',  
                o.individual(
                    'TechnicalMeasure',
                    'employee training regarding security issues')),

            o.connection(
                'hasSecurityMechanism',  
                o.individual(
                    'TechnicalMeasure',
                    'storage of sensitive information in locked offices')),
        ]
    )




    #########################################################################
    #                                                                       #
    # USER CHOICE                                                           #
    #                                                                       #
    #########################################################################



    #########################################################################
    # If we ever were to engage in any onward transfers of your data with third parties, for a purpose other than which it was originally collected or subsequently authorized, we would provide you with an opt-out choice to limit the use and disclosure of your personal data. 
    # !!!!!!!!!! does !!!!!!!!!!

    user = o.individual('User', 'you')

    o.individual(
        
        'GiveConsentActivity',

        'If we ever were to engage in any onward transfers of your data with third parties, for a purpose other than which it was originally collected or subsequently authorized, we would provide you with an opt-out choice to limit the use and disclosure of your personal data.',

        [

            o.connection(
                'activityIsInitiatedBy', 
                user),

            o.connection(
                'isAppliedTo', 
                o.individual(
                    'Data', 
                    'data',
                    [o.connection('isProvidedBy', user)])),
        ]
    )




    #########################################################################
    # Users may request that MedTrak discontinues use of their contact information by contacting their MedTrak representative or by emailing info@caresense.com.

    user = o.individual('User', 'Users')

    o.individual(
        
        'UserOptControl',

        'Users may request that MedTrak discontinues use of their contact information by contacting their MedTrak representative or by emailing info@caresense.com.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'TrackingData', 
                    'contact information',
                    [o.connection('isProvidedBy', user)])),

            o.connection(
                'activityIsInitiatedBy', 
                user),
        ]
    )




    #########################################################################
    # If a patient would like to withdraw or refuse consent for a study, the patient should inform his/her doctor and MedTrak. A patient will always make the choice about the ways that personal information is used and disclosed.

    user = o.individual('User', 'patient')

    o.individual(
        
        'UserOptControl',

        'If a patient would like to withdraw or refuse consent for a study, the patient should inform his/her doctor and MedTrak. A patient will always make the choice about the ways that personal information is used and disclosed.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'PersonalData', 
                    'personal information',
                    [o.connection('isProvidedBy', user)])),

            o.connection(
                'activityIsInitiatedBy', 
                user),
        ]
    )




    #########################################################################
    # When using the iOS CareSense patient app, MedTrak will ask for permission to access HealthKit data to track your step count. If HealthKit permission is not granted, only the step counting aspects of the app will stop working. 

    user = o.individual('User', 'your')

    o.individual(
        
        'ConsentActivity',

        'When using the iOS CareSense patient app, MedTrak will ask for permission to access HealthKit data to track your step count. If HealthKit permission is not granted, only the step counting aspects of the app will stop working.',

        [
            o.connection(
                'activityIsInitiatedBy', user),

            o.connection(
                'isAppliedTo', 
                o.individual(
                    'HealthData',
                    'step count',
                    [o.connection('isProvidedBy', user)])),

            o.connection(
                'hasUserChoiceConsequence',  
                o.individual(
                    'PartialServiceRestriction',
                    'only the step counting aspects of the app will stop working.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # DATA RETENTION                                                        #
    #                                                                       #
    #########################################################################



    #########################################################################
    # Personal information will be stored only as long as is necessary for the purposes for which it was collected, or as permitted by law. 


    o.individual(
        'DataRetentionActivity',

        'Personal information will be stored only as long as is necessary for the purposes for which it was collected, or as permitted by law.',

        [
            o.connection(
                'isAppliedTo', 
                o.individual(
                    'PersonalData', 
                    'Personal information',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty')),

            o.connection(
                'hasDataRetentionTime',  
                o.individual(
                    'DataRetentionTime',
                    'as long as is necessary')),

            o.connection(
                'hasLegalBasis',  
                o.individual(
                    'LegalBasis',
                    'as permitted by law.')),
        ]
    )




    #########################################################################
    #                                                                       #
    # DATA USE                                                              #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak uses aggregated, de-identified information and data to create marketing statistics and average scores viewable by all users.


    o.individual(
        
        'DataUseActivity',

        'MedTrak uses aggregated, de-identified information and data to create marketing statistics and average scores viewable by all users.',

        [
            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'isAppliedTo',  
                o.individual(
                    'Data',
                    'information and data',
                    [o.connection('isProvidedBy', o.individual('User'))])),
                    
            o.connection(
                'hasSecurityMechanism',  
                o.individual(
                    'PseudoAnonymization',
                    'de-identified')),
    
            o.connection(
                'hasDataActivityPurpose',  
                o.individual(
                    'DataActivityPurpose',
                    'to create marketing statistics and average scores viewable by all users.')),
        ]
    )




    #########################################################################
    # Individual records in MedTrak’s databases may be accessed to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.


    o.individual(

        'DataUseActivity',

        'Individual records in MedTrak’s databases may be accessed to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.',

        [
            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'isAppliedTo',  
                o.individual(
                    'Data',
                    'Individual records',
                    [o.connection('isProvidedBy', o.individual('User'))])),

            o.connection(
                'hasDataActivityPurpose',  
                o.individual(
                    'DataActivityPurpose',
                    'to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.')),
        ]
    )




    #########################################################################
    # Personal information will be used in a manner consistent with the consent provided by the patient. 


    o.individual(

        'DataUseActivity',

        'Personal information will be used in a manner consistent with the consent provided by the patient.',

        [
            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'isAppliedTo',  
                o.individual(
                    'PersonalData',
                    'Personal information',
                    [o.connection('isProvidedBy', o.individual('User', 'patient'))])),
                    
            o.connection(
                'hasDataActivityPurpose',  
                o.individual(
                    'DataActivityPurpose',
                    'to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.')),
        ]
    )




    #########################################################################
    # Patient name and date of birth will be used to match patient records properly, and the email address will be used to collect information from the patient outside of the office. 

    user = o.individual('User', 'Patient')

    o.individual(

        'DataUseActivity',

        'Patient name and date of birth will be used to match patient records properly',

        [
            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty', 
                    'MedTrak')),

            o.connection(
                'isAppliedTo', 
                o.individual(
                    'GenericData', 
                    'name',
                    [o.connection('isProvidedBy', user)])),

            o.connection(
                'isAppliedTo', 
                o.individual(
                    'GenericData', 
                    'date of birth',
                    [o.connection('isProvidedBy', user)])),
                    
            o.connection(
                'hasDataActivityPurpose',  
                o.individual(
                    'DataActivityPurpose',
                    'to match patient records properly')),
        ]
    )



    o.individual(

        'DataUseActivity',

        'the email address will be used to collect information from the patient outside of the office.',

        [
            o.connection(
                'activityIsInitiatedBy', 
                o.individual(
                    'FirstParty')),
            
            o.connection(
                'isAppliedTo',  
                o.individual(
                    'TrackingData',
                    'email address',
                    [o.connection('isProvidedBy', user)])),
                    
            o.connection(
                'hasDataActivityPurpose',  
                o.individual(
                    'DataActivityPurpose',
                    'to collect information from the patient outside of the office.')),
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

    o.individual(
        
        'UserAccessActivity',
                 
        'MedTrak acknowledges that individuals have the right to access the personal information/data that we maintain about them. Patients will be provided access to their own personal information stored on MedTrak’s servers in order to correct any problems or delete it. An individual who seeks access, or who seeks to correct, amend, or delete inaccurate data, should direct his query to info@caresense.com. If requested to remove data, we will respond within a reasonable timeframe.',

        [
            o.connection(
                'activityIsInitiatedBy', 
                user),

            o.connection(
                'isAppliedTo',  
                o.individual(
                    'PersonalData',
                    'personal information/data that we maintain about them.',
                    [o.connection('isProvidedBy', user)])),
                    
            o.connection(
                'hasDataActivityPurpose',  
                o.individual(
                    'DataActivityPurpose',
                    'to collect information from the patient outside of the office.')),
        ]
    )
    



    #########################################################################
    # Users are required to maintain the security of their User Name and password as outlined in MedTrak’s password policy.

    user = o.individual('User', 'individuals')

    o.individual(

        'Activity',

        'Users are required to maintain the security of their User Name and password as outlined in MedTrak’s password policy.',

        [
            o.connection(
                'activityIsInitiatedBy', user),

            o.connection(
                'isAppliedTo',  
                o.individual(
                    'AccountData',
                    'email address',
                    [o.connection('isProvidedBy', user)])),
                    
            o.connection(
                'isAppliedTo',  
                o.individual(
                    'AccountData',
                    'password',
                    [o.connection('isProvidedBy', user)])),
                    
            o.connection(
                'hasSecurityMechanism',  
                o.individual('OrganizationalMeasure',
                    'Users are required to maintain the security')),
        ]
    )

    o.write(reason=False)

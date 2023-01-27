from tools.ontology_helpers import make


def process_caresense(onto):

    user = onto.User()
    first_party = onto.FirstParty()
    third_party = onto.ThirdParties()

    policy_instance = onto.PrivacyPolicy()
    policy_instance.policyWebsite = "https://www.caresense.com/privacypolicy"
    policy_instance.considersAgent.extend([user, first_party, third_party])




    #########################################################################
    #                                                                       #
    # POLICY CHANGE                                                         #
    #                                                                       #
    #########################################################################


    #########################################################################
    # MedTrak reserves the right to amend the Policy at any time—these changes will apply to all old and new data collected by MedTrak but will never relax the privacy and security standards currently in place. Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.

    make(onto, "PolicyChangeActivity",
        evidence="MedTrak reserves the right to amend the Policy at any time—these changes will apply to all old and new data collected by MedTrak but will never relax the privacy and security standards currently in place. Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("hasNotificationMechanism",  make(onto, "OnWebsitePage",
                evidence="Any changes to the Policy will be posted on www.caresense.com along with a notice of the policy changes.")),
        )
    )




    #########################################################################
    #                                                                       #
    # FIRST PARTY COLLECTION                                                #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak gathers information from users who sign-up for our services (“Service”) through contracts, discussions and the website. Users are required to provide contact information such as name, company name, address, phone number, and email address. This information is used to setup the Service and provide support.

    make(onto, "DataCollectionActivity",
        evidence="MedTrak gathers information from users who sign-up for our services (“Service”) through contracts, discussions and the website. Users are required to provide contact information such as name, company name, address, phone number, and email address. This information is used to setup the Service and provide support.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "AccountData",
                evidence="name",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo",  make(onto, "AccountData",
                evidence="address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo",  make(onto, "AccountData",
                evidence="phone number",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo",  make(onto, "AccountData",
                evidence="email address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose",  make(onto, "DataActivityPurpose",
                evidence="This information is used to setup the Service and provide support.")),
        )
    )




    #########################################################################
    # MedTrak also collects and logs information (IP addresses, login attempts) concerning website usage. This information is used to monitor attempted security penetrations, detect technical problems, and review site usage patterns.

    make(onto, "DataCollectionActivity",
        evidence="MedTrak also collects and logs information (IP addresses, login attempts) concerning website usage. This information is used to monitor attempted security penetrations, detect technical problems, and review site usage patterns.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "TrackingData",
                evidence="IP addresses",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo",  make(onto, "AccountData",
                evidence="login attempts",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose",  make(onto, "DataActivityPurpose",
                evidence="This information is used to monitor attempted security penetrations, detect technical problems, and review site usage patterns.")),
        )
    )




    #########################################################################
    # Potential users may sign-up on www.caresense.com to be contacted by a MedTrak representative. They will submit contact information that will only be used to set-up an appointment or demonstration.

    make(onto, "DataCollectionActivity",
        evidence="Potential users may sign-up on www.caresense.com to be contacted by a MedTrak representative. They will submit contact information that will only be used to set-up an appointment or demonstration.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "TrackingData",
                evidence="contact information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose",  make(onto, "DataActivityPurpose",
                evidence="that will only be used to set-up an appointment or demonstration.")),
        )
    )




    #########################################################################
    #                                                                       #
    # THIRD PARTY SHARING                                                   #
    #                                                                       #
    #########################################################################



    #########################################################################
    # Except as required to perform the Service, no information will be disclosed to third parties.

    make(onto, "DataSharingActivity",
        evidence="Except as required to perform the Service, no information will be disclosed to third parties.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "Data",
                evidence="no information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # MedTrak does not currently transfer personal information to third parties. 
    # !!!!!!!!!! doesnt !!!!!!!!!!

    make(onto, "DataSharingActivity",
        evidence="MedTrak does not currently transfer personal information to third parties.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Information and data users collect using CareSense and store on MedTrak’s servers will not be reviewed, shared, or disseminated except as stated in the Business Associates Agreement and Software License Agreement or as required by law. 
    # !!!!!!!!!! doesnt !!!!!!!!!!

    make(onto, "DataSharingActivity",
        evidence="Information and data users collect using CareSense and store on MedTrak’s servers will not be reviewed, shared, or disseminated except as stated in the Business Associates Agreement and Software License Agreement or as required by law.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "Data",
                evidence="Information and data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasLegalBasis",  make(onto, "LegalBasis",
                evidence="Business Associates Agreement and Software License Agreement or as required by law.")),
        )
    )




    #########################################################################
    # Personal information will not be shared with third parties.
    # !!!!!!!!!! doesnt !!!!!!!!!!

    make(onto, "DataSharingActivity",
        evidence="Personal information will not be shared with third parties.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "PersonalData",
                evidence="Personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )
    



    #########################################################################
    # Marketing statistics will be made available to third parties.
    # !!!!!!!!!! does !!!!!!!!!!

    make(onto, "DataSharingActivity",
        evidence="Marketing statistics will be made available to third parties.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "NonPersonalData",
                evidence="Marketing statistics",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # MedTrak also may be required to disclose an individual’s personal information in response to a lawful request by public authorities, including to meet national security or law enforcement requirements. 
    # !!!!!!!!!! does !!!!!!!!!!

    make(onto, "DataSharingActivity",
        evidence="MedTrak also may be required to disclose an individual’s personal information in response to a lawful request by public authorities, including to meet national security or law enforcement requirements.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "PersonalData",
                evidence="personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasLegalBasis",  make(onto, "LegalBasis",
                evidence="in response to a lawful request by public authorities, including to meet national security or law enforcement requirements.")),
        )
    )




    #########################################################################
    #                                                                       #
    # DATA SECURITY                                                         #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak provides high quality security controls and protocols to ensure that all information and data is protected against loss, misuse, alteration, or unintentional destruction. MedTrak employs Secure Sockets Layer (SSL) technology to protect information traveling to and from the website and a firewall to block unauthorized use of the web server and database. Information and data are protected by access controls, passwords, employee training regarding security issues, and storage of sensitive information in locked offices, encrypted files, or behind the firewall.
    # !!!!!!!!!! does !!!!!!!!!!

    make(onto, "Activity",
        evidence="MedTrak provides high quality security controls and protocols to ensure that all information and data is protected against loss, misuse, alteration, or unintentional destruction. MedTrak employs Secure Sockets Layer (SSL) technology to protect information traveling to and from the website and a firewall to block unauthorized use of the web server and database. Information and data are protected by access controls, passwords, employee training regarding security issues, and storage of sensitive information in locked offices, encrypted files, or behind the firewall.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("hasSecurityMechanism",  make(onto, "TechnicalMeasure",
                evidence="Secure Sockets Layer (SSL) technology")),
            ("hasSecurityMechanism",  make(onto, "TechnicalMeasure",
                evidence="firewall")),
            ("hasSecurityMechanism",  make(onto, "TechnicalMeasure",
                evidence="access controls, passwords")),
            ("hasSecurityMechanism",  make(onto, "TechnicalMeasure",
                evidence="encrypted files")),
            ("hasSecurityMechanism",  make(onto, "TechnicalMeasure",
                evidence="employee training regarding security issues")),
            ("hasSecurityMechanism",  make(onto, "TechnicalMeasure",
                evidence="storage of sensitive information in locked offices")),
        )
    )




    #########################################################################
    #                                                                       #
    # USER CHOICE                                                           #
    #                                                                       #
    #########################################################################



    #########################################################################
    # If we ever were to engage in any onward transfers of your data with third parties, for a purpose other than which it was originally collected or subsequently authorized, we would provide you with an opt-out choice to limit the use and disclosure of your personal data. 
    # !!!!!!!!!! does !!!!!!!!!!

    make(onto, "GiveConsentActivity",
        evidence="If we ever were to engage in any onward transfers of your data with third parties, for a purpose other than which it was originally collected or subsequently authorized, we would provide you with an opt-out choice to limit the use and disclosure of your personal data.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", user)
        ),
        children=(
            ("isAppliedTo",  make(onto, "Data",
                evidence="data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # Users may request that MedTrak discontinues use of their contact information by contacting their MedTrak representative or by emailing info@caresense.com.

    make(onto, "UserOptControl",
        evidence="Users may request that MedTrak discontinues use of their contact information by contacting their MedTrak representative or by emailing info@caresense.com.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", user)
        ),
        children=(
            ("isAppliedTo",  make(onto, "AccountData",
                evidence="contact information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
        )
    )




    #########################################################################
    # If a patient would like to withdraw or refuse consent for a study, the patient should inform his/her doctor and MedTrak. A patient will always make the choice about the ways that personal information is used and disclosed.

    make(onto, "UserOptControl",
        evidence="If a patient would like to withdraw or refuse consent for a study, the patient should inform his/her doctor and MedTrak. A patient will always make the choice about the ways that personal information is used and disclosed.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", user)
        ),
    )




    #########################################################################
    # When using the iOS CareSense patient app, MedTrak will ask for permission to access HealthKit data to track your step count. If HealthKit permission is not granted, only the step counting aspects of the app will stop working. 

    make(onto, "ConsentActivity",
        evidence="When using the iOS CareSense patient app, MedTrak will ask for permission to access HealthKit data to track your step count. If HealthKit permission is not granted, only the step counting aspects of the app will stop working.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", user)
        ),
        children=(
            ("isAppliedTo",  make(onto, "HealthData",
                evidence="step count",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasUserChoiceConsequence",  make(onto, "PartialServiceRestriction",
                evidence="only the step counting aspects of the app will stop working.")),
        )
    )




    #########################################################################
    #                                                                       #
    # DATA RETENTION                                                        #
    #                                                                       #
    #########################################################################



    #########################################################################
    # Personal information will be stored only as long as is necessary for the purposes for which it was collected, or as permitted by law. 

    make(onto, "DataRetentionActivity",
        evidence="Personal information will be stored only as long as is necessary for the purposes for which it was collected, or as permitted by law.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "PersonalData",
                evidence="Personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataRetentionTime",  make(onto, "DataRetentionTime",
                evidence="as long as is necessary")),
            ("hasLegalBasis",  make(onto, "LegalBasis",
                evidence="as permitted by law.")),
        )
    )




    #########################################################################
    #                                                                       #
    # DATA USE                                                              #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak uses aggregated, de-identified information and data to create marketing statistics and average scores viewable by all users.

    make(onto, "DataUseActivity",
        evidence="MedTrak uses aggregated, de-identified information and data to create marketing statistics and average scores viewable by all users.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "Data",
                evidence="information and data",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism",  make(onto, "PseudoAnonymization",
                evidence="de-identified")),
            ("hasDataActivityPurpose",  make(onto, "DataActivityPurpose",
                evidence="to create marketing statistics and average scores viewable by all users.")),
        )
    )




    #########################################################################
    # Individual records in MedTrak’s databases may be accessed to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.

    make(onto, "DataUseActivity",
        evidence="Individual records in MedTrak’s databases may be accessed to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "Data",
                evidence="Individual records",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose",  make(onto, "DataActivityPurpose",
                evidence="to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.")),
        )
    )




    #########################################################################
    # Personal information will be used in a manner consistent with the consent provided by the patient. 

    make(onto, "DataUseActivity",
        evidence="Personal information will be used in a manner consistent with the consent provided by the patient.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "PersonalData",
                evidence="Personal information",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose",  make(onto, "DataActivityPurpose",
                evidence="to provide the Service, resolve an issue, evaluate usage patterns, provide support services, or review contractual issues.")),
        )
    )




    #########################################################################
    # Patient name and date of birth will be used to match patient records properly, and the email address will be used to collect information from the patient outside of the office. 

    make(onto, "DataUseActivity",
        evidence="Patient name and date of birth will be used to match patient records properly",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "GenericData",
                evidence="name",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo",  make(onto, "GenericData",
                evidence="date of birth",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose",  make(onto, "DataActivityPurpose",
                evidence="to match patient records properly")),
        )
    )


    make(onto, "DataUseActivity",
        evidence="the email address will be used to collect information from the patient outside of the office.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", first_party)
        ),
        children=(
            ("isAppliedTo",  make(onto, "AccountData",
                evidence="email address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose",  make(onto, "DataActivityPurpose",
                evidence="to collect information from the patient outside of the office.")),
        )
    )




    #########################################################################
    #                                                                       #
    # USER ACCESS                                                           #
    #                                                                       #
    #########################################################################



    #########################################################################
    # MedTrak acknowledges that individuals have the right to access the personal information/data that we maintain about them. Patients will be provided access to their own personal information stored on MedTrak’s servers in order to correct any problems or delete it. An individual who seeks access, or who seeks to correct, amend, or delete inaccurate data, should direct his query to info@caresense.com. If requested to remove data, we will respond within a reasonable timeframe.

    make(onto, "UserAccessActivity",
        evidence="MedTrak acknowledges that individuals have the right to access the personal information/data that we maintain about them. Patients will be provided access to their own personal information stored on MedTrak’s servers in order to correct any problems or delete it. An individual who seeks access, or who seeks to correct, amend, or delete inaccurate data, should direct his query to info@caresense.com. If requested to remove data, we will respond within a reasonable timeframe.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", user)
        ),
        children=(
            ("isAppliedTo",  make(onto, "PersonalData",
                evidence="personal information/data that we maintain about them.",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasDataActivityPurpose",  make(onto, "DataActivityPurpose",
                evidence="to collect information from the patient outside of the office.")),
        )
    )
    



    #########################################################################
    # Users are required to maintain the security of their User Name and password as outlined in MedTrak’s password policy.

    make(onto, "Activity",
        evidence="Users are required to maintain the security of their User Name and password as outlined in MedTrak’s password policy.",
        parents=(
            ("isConsideredBy", policy_instance),
            ("activityIsInitiatedBy", user)
        ),
        children=(
            ("isAppliedTo",  make(onto, "AccountData",
                evidence="email address",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("isAppliedTo",  make(onto, "AccountData",
                evidence="password",
                parents=(
                    ("isConsideredBy", policy_instance),
                    ("isProvidedBy", user)))),
            ("hasSecurityMechanism",  make(onto, "OrganizationalMeasure",
                evidence="Users are required to maintain the security")),
        )
    )
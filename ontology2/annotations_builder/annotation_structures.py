'''
REVERT RELATIONS
REVISE ALL
RECURSIVE ASPECTS
'''

# BACKWARD READING
RESTRICTIONS = {

    # AGENTS
    'User': {
        'initiated_by': [
            'DataControl', 
            'AdvertisingDataControl', 'OptInOptOutControl', 'UserNotification'
        ],
        'collects_from': [
            'FPCollection'
        ],
        'notifies': [
            'FPNotification'
        ],
        'special_category_for': [
            'EuropeanResident',
            'RussianFederationResident'
            'CaliforniaResident',
            'Child'
        ],
        'provides': ['Data'],
    },
    'FirstParty': {
        'initiated_by': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange'
        ],
        'notifies': [
            'UserNotification'
        ],
    },
    'ThirdParty': {
        'shares_with': [
            'TPSharing'
        ],
        'collects_from': [
            'TPCollection'
        ],
    },

    # DATA
    'Data': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'NonPersonalData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'PersonalData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'ServiceData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'FinancialData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'DeviceData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'ApplicationData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'AccountData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'TrackingData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'SensitiveData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'ReligionData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'RacialData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'GenericData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'CrimeData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },
    'BiometricData': {
        'applies_to': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange', 
            'OptInOptOutControl', 'AdvertisingDataControl'
        ]
    },

    # MECHANISMS
    'Mechanism': {
        'has_mechanism': ['Activity']
    },
    'DataRetentionMechanism': {
        'has_mechanism': ['DataRetention']
    },
    'StoreOnOwnServers': {
        'has_mechanism': ['DataRetention']
    },
    'StoreOnEmployedServers': {
        'has_mechanism': ['DataRetention']
    },
    'TPSharingAndCollectionCMechanism': {
        'has_mechanism': ['TPSharing', 'TPCollection']
    },
    'TPSharingOrCollectionByContract': {
        'has_mechanism': ['TPSharing', 'TPCollection']
    },
    'TPSharingOrCollectionForFree': {
        'has_mechanism': ['TPSharing', 'TPCollection']
    },
    'SecurityMechanism': {
        'has_mechanism': ['DataProtection']
    },
    'TechnicalSecurityMeasure': {
        'has_mechanism': ['DataProtection']
    },
    'PseudoAnonymization': {
        'has_mechanism': ['DataProtection']
    },
    'Encryption': {
        'has_mechanism': ['DataProtection']
    },
    'SecureStorage': {
        'has_mechanism': ['DataProtection']
    },
    'SecuredCommunication': {
        'has_mechanism': ['DataProtection']
    },
    'Firewall': {
        'has_mechanism': ['DataProtection']
    },
    'AccessControls': {
        'has_mechanism': ['DataProtection']
    },
    'OrganizationalSecurityMeasure': {
        'has_mechanism': ['DataProtection']
    },
    'LockedOffice': {
        'has_mechanism': ['DataProtection']
    },
    'SecurityTraining': {
        'has_mechanism': ['DataProtection']
    },
    'UserMaintainsSecurity': {
        'has_mechanism': ['DataProtection']
    },

    'CommunicationMechanism': {
        'has_mechanism': ['FPCollection', 'FPCollection', 'Notification', 'UserNotification', 'FPNotification']
    },
    'UserSpecificCommunicationMechanism': {
        'has_mechanism': ['FPCollection', 'FPCollection', 'UserNotification']
    },
    'AutomaticCommunicationMechanism': {
        'has_mechanism': ['FPCollection']
    },
    'ViaServiceApp': {
        'has_mechanism': ['FPCollection']
    },
    'ViaWebsite': {
        'has_mechanism': ['FPCollection']
    },
    'ManualCommunicationMechanism': {
        'has_mechanism': ['FPCollection', 'UserNotification']
    },
    'WebsiteForm': {
        'has_mechanism': ['FPCollection', 'UserNotification']
    },
    'ServiceAppForm': {
        'has_mechanism': ['FPCollection' 'UserNotification']
    },
    'DataProvision': {
        'has_mechanism': ['FPCollection' 'UserNotification']
    },
    'PersonalVisit': {
        'has_mechanism': ['FPCollection' 'UserNotification']
    },
    'GeneralCommunicationMechanism': {
        'has_mechanism': ['FPCollection', 'UserNotification', 'FPNotification']
    },
    'Email': {
        'has_mechanism': ['FPCollection', 'UserNotification', 'FPNotification']
    },
    'PostalMail': {
        'has_mechanism': ['FPCollection', 'UserNotification', 'FPNotification']
    },
    'PhoneCall': {
        'has_mechanism': ['FPCollection', 'UserNotification', 'FPNotification']
    },
    'SMS': {
        'has_mechanism': ['FPCollection', 'UserNotification', 'FPNotification']
    },
    'FPSpecificCommunicationMechanism': {
        'has_mechanism': ['FPNotification']
    },
    'OnWebsitePage': {
        'has_mechanism': ['FPNotification']
    },
    'OnServiceApp': {
        'has_mechanism': ['FPNotification']
    },
    'InPrivacyPolicy': {
        'has_mechanism': ['FPNotification']
    },

    # MODES
    'FPCollection': {
        'mode_for': [
            'Mode', 
            'DataTransmissionMode', 
            'PermanentTransmission', 
            'TransmissionByRequest', 
        ]
    },
    'TPCollection': {
        'mode_for': [
            'Mode', 
            'DataTransmissionMode', 
            'PermanentTransmission', 
            'TransmissionByRequest', 
        ]
    },
    'TPSharing': {
        'mode_for': [
            'Mode', 
            'DataTransmissionMode', 
            'PermanentTransmission', 
            'TransmissionByRequest', 
        ]
    },

    # CAUSES
    'Cause': {
        'caused_by': ['Activity']
    },
    'DataBreach': {
        'caused_by': [
            'Mode', 
            'DataTransmissionMode', 
            'PermanentTransmission', 
            'TransmissionByRequest', 
        ]
    },
    'ForceMajeurIncident': {
        'caused_by': ['DataBreachProcessing']
    },
    'IntentionalBreach': {
        'caused_by': ['DataBreachProcessing']
    },
    'UnintentionalBreach': {
        'caused_by': ['DataBreachProcessing']
    },
    'PolicyChangeCause': {
        'caused_by': ['PolicyChange']
    },
    'PrivacyRelatedCause': {
        'caused_by': ['PolicyChange']
    },
    'NonPrivacyRelatedCause': {
        'caused_by': ['PolicyChange']
    },
    'MergeAcquisitionCause': {
        'caused_by': ['PolicyChange']
    },

    # CONSEQUENCES
    'Consequence': {
        'consequence_for': ['Activity']
    },
    'DataBreachConsequence': {
        'consequence_for': ['DataBreachProcessing']
    },
    'RemoveCompromisedInformation': {
        'consequence_for': ['DataBreachProcessing']
    },
    'DataBreachCompensation': {
        'consequence_for': ['DataBreachProcessing']
    },
    'PolicyChangeConsequence': {
        'consequence_for': ['PolicyChange']
    },
    'UserChoiceConsequence': {
        'consequence_for': [
            'DataControl', 
            'AdvertisingDataControl', 
            'OptInOptOutControl'
        ]
    },
    'NoServiceRestriction': {
        'consequence_for': [
            'DataControl', 
            'AdvertisingDataControl', 
            'OptInOptOutControl'
        ]
    },
    'PartialServiceRestriction': {
        'consequence_for': [
            'DataControl', 
            'AdvertisingDataControl', 
            'OptInOptOutControl'
        ]
    },
    'FullServiceRestriction': {
        'consequence_for': [
            'DataControl', 
            'AdvertisingDataControl', 
            'OptInOptOutControl'
        ]
    },

    # PURPOSES
    'Purpose': {
        'has_purpose': ['Activity']
    },
    'DataActivityPurpose': {
        'has_purpose': [
            'DataActivity', 'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'FPNotification', 'DataBreachProcessing', 'PolicyChange'
        ]
    },
    'LegalCompliancePurpose': {
        'has_purpose': [
            'DataActivity', 'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention'
        ]
    },
    'ServiceProvisionPurpose': {
        'has_purpose': [
            'DataActivity', 'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention'
        ]
    },
    'HealthMonitoringPurpose': {
        'has_purpose': [
            'DataActivity', 'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention'
        ]
    },
    'ServiceEnhancementPurpose': {
        'has_purpose': [
            'DataActivity', 'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention'
        ]
    },
    'AnalyticsPurpose': {
        'has_purpose': [
            'DataActivity', 'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention'
        ]
    },
    'SecurityPurpose': {
        'has_purpose': [
            'DataActivity', 'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention'
        ]
    },
    'ResearchPurpose': {
        'has_purpose': [
            'DataActivity', 'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention'
        ]
    },
    'MarketingPurpose': {
        'has_purpose': [
            'DataActivity', 'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention'
        ]
    },

    # TIME PERIODS
    'TimePeriod': {
        'lasts_for': ['Activity']
    },
    'DataRetentionTime': {
        'lasts_for': ['DataRetention']
    },
    'NotificationTime': {
        'lasts_for': ['DataBreachProcessing']
    },
    'DataBreachProcessingTime': {
        'lasts_for': ['DataBreachProcessing']
    },
    'PolicyAcceptanceTime': {
        'lasts_for': ['PolicyChange']
    },

    # BASIS
    'Basis': {
        'has_basis': ['Activity']
    },
    'LegalBasis': {
        'has_basis': [
            'DataUse', 'DataProtection', 'FPCollection', 'TPCollection', 'TPSharing', 
            'DataRetention', 'PolicyChange'
        ]
    },

    # POLICY CHANGE SCOPE
    'PolicyChangeScope': {
        'has_scope': ['PolicyChange']
    },

}


SCHEME = [

# Activities
    {
        "class": "Activity",
        "subclassOf": [],
        "attributeOf": [],
    },  # Activity Thing
    {
        "class": "DataBreachProcessing",
        "subclassOf": ["Activity"],
        "attributeOf": [],
    },  # DataBreachProcessing Activity
    {
        "class": "DataActivity",
        "subclassOf": ["Activity"],
        "attributeOf": [],
    },  # DataActivity Activity
    {
        "class": "PolicyChange",
        "subclassOf": ["DataActivity", "Activity"],
        "attributeOf": [],
    },  # PolicyChange DataActivity
    {
        "class": "DataUse",
        "subclassOf": ["DataActivity", "Activity"],
        "attributeOf": [],
    },  # DataUse DataActivity
    {
        "class": "DataProtection",
        "subclassOf": ["DataActivity", "Activity"],
        "attributeOf": [],
    },  # DataProtection DataActivity
    {
        "class": "FPCollection",
        "subclassOf": ["DataActivity", "Activity"],
        "attributeOf": [],
    },  # FPCollection DataActivity
    {
        "class": "TPCollection",
        "subclassOf": ["DataActivity", "Activity"],
        "attributeOf": [],
    },  # TPCollection DataActivity
    {
        "class": "TPSharing",
        "subclassOf": ["DataActivity", "Activity"],
        "attributeOf": [],
    },  # TPSharing DataActivity
    {
        "class": "DataRetention",
        "subclassOf": ["DataActivity", "Activity"],
        "attributeOf": [],
    },  # DataRetention DataActivity
    {
        "class": "NotificationActivity",
        "subclassOf": ["Activity"],
        "attributeOf": [],
    },  # NotificationActivity Activity
    {
        "class": "FPNotification",
        "subclassOf": ["NotificationActivity", "Activity"],
        "attributeOf": [],
    },  # FPNotification NotificationActivity
    {
        "class": "UserNotification",
        "subclassOf": ["NotificationActivity", "Activity"],
        "attributeOf": [],
    },  # UserNotification NotificationActivity
    {
        "class": "DataControl",
        "subclassOf": ["Activity"],
        "attributeOf": [],
    },  # DataControl Activity
    {
        "class": "AdvertisingDataControl",
        "subclassOf": ["DataControl", "Activity"],
        "attributeOf": [],
    },  # AdvertisingDataControl DataControl
    {
        "class": "OptInOptOutControl",
        "subclassOf": ["DataControl", "Activity"],
        "attributeOf": [],
    },  # OptInOptOutControl DataControl

# Agents
    {
        "class": "Agent",
        "subclassOf": [],
        "attributeOf": ["NotificationActivity", "Activity"],
    },  # Agent Thing
    {
        "class": "User",
        "subclassOf": ["Agent"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "OptInOptOutControl", "AdvertisingDataControl", "DataControl", "UserNotification", "FPNotification", "FPCollection", "Activity"],
    },  # User Agent
    {
        "class": "FirstParty",
        "subclassOf": ["Agent"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "UserNotification", "FPNotification", "DataBreachProcessing", "Activity"],
    },  # FirstParty Agent
    {
        "class": "ThirdParty",
        "subclassOf": ["Agent"],
        "attributeOf": ["TPCollection", "TPSharing", "Activity"],
    },  # ThirdParty Agent

# Data
    {
        "class": "Data",
        "subclassOf": [],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # Data Thing
    {
        "class": "PersonalData",
        "subclassOf": ["Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # PersonalData Data
    {
        "class": "NonPersonalData",
        "subclassOf": ["Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # NonPersonalData Data
    {
        "class": "ServiceData",
        "subclassOf": ["PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # ServiceData PersonalData
    {
        "class": "FinancialData",
        "subclassOf": ["PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # FinancialData PersonalData
    {
        "class": "DeviceData",
        "subclassOf": ["PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # DeviceData PersonalData
    {
        "class": "ApplicationData",
        "subclassOf": ["PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # ApplicationData PersonalData
    {
        "class": "AccountData",
        "subclassOf": ["PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # AccountData PersonalData
    {
        "class": "TrackingData",
        "subclassOf": ["PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # TrackingData PersonalData
    {
        "class": "SensitiveData",
        "subclassOf": ["PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # SensitiveData PersonalData
    {
        "class": "ReligionData",
        "subclassOf": ["SensitiveData", "PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # ReligionData SensitiveData
    {
        "class": "RacialData",
        "subclassOf": ["SensitiveData", "PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # RacialData SensitiveData
    {
        "class": "HealthData",
        "subclassOf": ["SensitiveData", "PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # HealthData SensitiveData
    {
        "class": "GenericData",
        "subclassOf": ["SensitiveData", "PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # GenericData SensitiveData
    {
        "class": "CrimeData",
        "subclassOf": ["SensitiveData", "PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # CrimeData SensitiveData
    {
        "class": "BiometricData",
        "subclassOf": ["SensitiveData", "PersonalData", "Data"],
        "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"],
    },  # BiometricData SensitiveData

# Mechanisms
    {
        "class": "Mechanism",
        "subclassOf": [],
        "attributeOf": ["Activity"],
    },  # Mechanism Thing
    {
        "class": "DataRetentionMechanism",
        "subclassOf": ["Mechanism"],
        "attributeOf": ["DataRetention"],
    },  # DataRetentionMechanism Mechanism
    {
        "class": "StoreOnOwnServers",
        "subclassOf": ["DataRetentionMechanism", "Mechanism"],
        "attributeOf": ["DataRetention"],
    },  # StoreOnOwnServers DataRetentionMechanism
    {
        "class": "StoreOnEmployedServers",
        "subclassOf": ["DataRetentionMechanism", "Mechanism"],
        "attributeOf": ["DataRetention"],
    },  # StoreOnEmployedServers DataRetentionMechanism
    {
        "class": "TPSharingAndCollectionCMechanism",
        "subclassOf": ["Mechanism"],
        "attributeOf": ["TPSharing", "TPCollection"],
    },  # TPSharingAndCollectionCMechanism Mechanism
    {
        "class": "TPSharingOrCollectionByContract",
        "subclassOf": ["TPSharingAndCollectionCMechanism", "Mechanism"],
        "attributeOf": ["TPSharing", "TPCollection"],
    },  # TPSharingOrCollectionByContract TPSharingAndCollectionCMechanism
    {
        "class": "TPSharingOrCollectionForFree",
        "subclassOf": ["TPSharingAndCollectionCMechanism", "Mechanism"],
        "attributeOf": ["TPSharing", "TPCollection"],
    },  # TPSharingOrCollectionForFree TPSharingAndCollectionCMechanism
    {
        "class": "SecurityMechanism",
        "subclassOf": ["Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # SecurityMechanism Mechanism
    {
        "class": "TechnicalSecurityMeasure",
        "subclassOf": ["SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # TechnicalSecurityMeasure SecurityMechanism
    {
        "class": "PseudoAnonymization",
        "subclassOf": ["TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # PseudoAnonymization TechnicalSecurityMeasure
    {
        "class": "Encryption",
        "subclassOf": ["TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # Encryption TechnicalSecurityMeasure
    {
        "class": "SecureStorage",
        "subclassOf": ["Encryption", "TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # SecureStorage Encryption
    {
        "class": "SecuredCommunication",
        "subclassOf": ["Encryption", "TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # SecuredCommunication Encryption
    {
        "class": "Firewall",
        "subclassOf": ["TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # Firewall TechnicalSecurityMeasure
    {
        "class": "AccessControls",
        "subclassOf": ["TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # AccessControls TechnicalSecurityMeasure
    {
        "class": "OrganizationalSecurityMeasure",
        "subclassOf": ["SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # OrganizationalSecurityMeasure SecurityMechanism
    {
        "class": "LockedOffice",
        "subclassOf": ["OrganizationalSecurityMeasure", "SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # LockedOffice OrganizationalSecurityMeasure
    {
        "class": "SecurityTraining",
        "subclassOf": ["OrganizationalSecurityMeasure", "SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # SecurityTraining OrganizationalSecurityMeasure
    {
        "class": "UserMaintainsSecurity",
        "subclassOf": ["OrganizationalSecurityMeasure", "SecurityMechanism", "Mechanism"],
        "attributeOf": ["DataProtection"],
    },  # UserMaintainsSecurity OrganizationalSecurityMeasure
    {
        "class": "CommunicationMechanism",
        "subclassOf": ["Mechanism"],
        "attributeOf": ["NotificationActivity"],
    },  # CommunicationMechanism Mechanism
    {
        "class": "UserSpecificCommunicationMechanism",
        "subclassOf": ["CommunicationMechanism", "Mechanism"],
        "attributeOf": ["UserNotification", "FPCollection"],
    },  # UserSpecificCommunicationMechanism CommunicationMechanism
    {
        "class": "AutomaticCommunicationMechanism",
        "subclassOf": ["UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["UserNotification", "FPCollection"],
    },  # AutomaticCommunicationMechanism UserSpecificCommunicationMechanism
    {
        "class": "ViaServiceApp",
        "subclassOf": ["AutomaticCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["UserNotification", "FPCollection"],
    },  # ViaServiceApp AutomaticCommunicationMechanism
    {
        "class": "ViaWebsite",
        "subclassOf": ["AutomaticCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["UserNotification", "FPCollection"],
    },  # ViaWebsite AutomaticCommunicationMechanism
    {
        "class": "ManualCommunicationMechanism",
        "subclassOf": ["UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["UserNotification", "FPCollection"],
    },  # ManualCommunicationMechanism UserSpecificCommunicationMechanism
    {
        "class": "WebsiteForm",
        "subclassOf": ["ManualCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["UserNotification", "FPCollection"],
    },  # WebsiteForm ManualCommunicationMechanism
    {
        "class": "ServiceAppForm",
        "subclassOf": ["ManualCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["UserNotification", "FPCollection"],
    },  # ServiceAppForm ManualCommunicationMechanism
    {
        "class": "DataProvision",
        "subclassOf": ["ManualCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["UserNotification", "FPCollection"],
    },  # DataProvision ManualCommunicationMechanism
    {
        "class": "PersonalVisit",
        "subclassOf": ["ManualCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["UserNotification", "FPCollection"],
    },  # PersonalVisit ManualCommunicationMechanism
    {
        "class": "GeneralCommunicationMechanism",
        "subclassOf": ["CommunicationMechanism", "Mechanism"],
        "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"],
    },  # GeneralCommunicationMechanism CommunicationMechanism
    {
        "class": "Email",
        "subclassOf": ["GeneralCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"],
    },  # Email GeneralCommunicationMechanism
    {
        "class": "PostalMail",
        "subclassOf": ["GeneralCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"],
    },  # PostalMail GeneralCommunicationMechanism
    {
        "class": "PhoneCall",
        "subclassOf": ["GeneralCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"],
    },  # PhoneCall GeneralCommunicationMechanism
    {
        "class": "SMS",
        "subclassOf": ["GeneralCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"],
    },  # SMS GeneralCommunicationMechanism
    {
        "class": "FPSpecificCommunicationMechanism",
        "subclassOf": ["CommunicationMechanism", "Mechanism"],
        "attributeOf": ["FPNotification"],
    },  # FPSpecificCommunicationMechanism CommunicationMechanism
    {
        "class": "OnWebsitePage",
        "subclassOf": ["FPSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["FPNotification"],
    },  # OnWebsitePage FPSpecificCommunicationMechanism
    {
        "class": "OnServiceApp",
        "subclassOf": ["FPSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["FPNotification"],
    },  # OnServiceApp FPSpecificCommunicationMechanism
    {
        "class": "InPrivacyPolicy",
        "subclassOf": ["FPSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
        "attributeOf": ["FPNotification"],
    },  # InPrivacyPolicy FPSpecificCommunicationMechanism

# Modes
    {
        "class": "Mode",
        "subclassOf": [],
        "attributeOf": ["Activity"],
    },  # Mode Thing
    {
        "class": "DataTransmissionMode",
        "subclassOf": ["Mode"],
        "attributeOf": ["FPCollection", "TPCollection", "TPSharing"],
    },  # DataTransmissionMode Mode
    {
        "class": "PermanentTransmission",
        "subclassOf": ["DataTransmissionMode", "Mode"],
        "attributeOf": ["FPCollection", "TPCollection", "TPSharing"],
    },  # PermanentTransmission DataTransmissionMode
    {
        "class": "TransmissionByRequest",
        "subclassOf": ["DataTransmissionMode", "Mode"],
        "attributeOf": ["FPCollection", "TPCollection", "TPSharing"],
    },  # TransmissionByRequest DataTransmissionMode

# Causes
    {
        "class": "Cause",
        "subclassOf": [],
        "attributeOf": ["Activity"],
    },  # Cause Thing
    {
        "class": "DataBreach",
        "subclassOf": ["Cause"],
        "attributeOf": ["DataBreachProcessing"],
    },  # DataBreach Cause
    {
        "class": "ForceMajeurIncident",
        "subclassOf": ["DataBreach", "Cause"],
        "attributeOf": ["DataBreachProcessing"],
    },  # ForceMajeurIncident DataBreach
    {
        "class": "IntentionalBreach",
        "subclassOf": ["DataBreach", "Cause"],
        "attributeOf": ["DataBreachProcessing"],
    },  # IntentionalBreach DataBreach
    {
        "class": "UnintentionalBreach",
        "subclassOf": ["DataBreach", "Cause"],
        "attributeOf": ["DataBreachProcessing"],
    },  # UnintentionalBreach DataBreach
    {
        "class": "PolicyChangeCause",
        "subclassOf": ["Cause"],
        "attributeOf": ["PolicyChange"],
    },  # PolicyChangeCause Cause
    {
        "class": "PrivacyRelatedCause",
        "subclassOf": ["PolicyChangeCause", "Cause"],
        "attributeOf": ["PolicyChange"],
    },  # PrivacyRelatedCause PolicyChangeCause
    {
        "class": "NonPrivacyRelatedCause",
        "subclassOf": ["PolicyChangeCause", "Cause"],
        "attributeOf": ["PolicyChange"],
    },  # NonPrivacyRelatedCause PolicyChangeCause
    {
        "class": "MergeAcquisitionCause",
        "subclassOf": ["PolicyChangeCause", "Cause"],
        "attributeOf": ["PolicyChange"],
    },  # MergeAcquisitionCause PolicyChangeCause

# Consequences
    {
        "class": "Consequence",
        "subclassOf": [],
        "attributeOf": ["Activity"],
    },  # Consequence Thing
    {
        "class": "DataBreachConsequence",
        "subclassOf": ["Consequence"],
        "attributeOf": ["DataBreachProcessing"],
    },  # DataBreachConsequence Consequence
    {
        "class": "RemoveCompromisedInformation",
        "subclassOf": ["DataBreachConsequence", "Consequence"],
        "attributeOf": ["DataBreachProcessing"],
    },  # RemoveCompromisedInformation DataBreachConsequence
    {
        "class": "DataBreachCompensation",
        "subclassOf": ["DataBreachConsequence", "Consequence"],
        "attributeOf": ["DataBreachProcessing"],
    },  # DataBreachCompensation DataBreachConsequence
    {
        "class": "PolicyChangeConsequence",
        "subclassOf": ["Consequence"],
        "attributeOf": ["PolicyChange"],
    },  # PolicyChangeConsequence Consequence
    {
        "class": "UserChoiceConsequence",
        "subclassOf": ["Consequence"],
        "attributeOf": ["PrivacyControl", "OptInOptOutControl"],
    },  # UserChoiceConsequence Consequence
    {
        "class": "NoServiceRestriction",
        "subclassOf": ["UserChoiceConsequence", "Consequence"],
        "attributeOf": ["PrivacyControl", "OptInOptOutControl"],
    },  # NoServiceRestriction UserChoiceConsequence
    {
        "class": "PartialServiceRestriction",
        "subclassOf": ["UserChoiceConsequence", "Consequence"],
        "attributeOf": ["PrivacyControl", "OptInOptOutControl"],
    },  # PartialServiceRestriction UserChoiceConsequence
    {
        "class": "FullServiceRestriction",
        "subclassOf": ["UserChoiceConsequence", "Consequence"],
        "attributeOf": ["PrivacyControl", "OptInOptOutControl"],
    },  # FullServiceRestriction UserChoiceConsequence

# Purposes
    {
        "class": "Purpose",
        "subclassOf": [],
        "attributeOf": ["Activity"],
    },  # Purpose Thing
    {
        "class": "DataActivityPurpose",
        "subclassOf": ["Purpose"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # DataActivityPurpose Purpose
    {
        "class": "LegalCompliancePurpose",
        "subclassOf": ["DataActivityPurpose", "Purpose"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # LegalCompliancePurpose DataActivityPurpose
    {
        "class": "ServiceProvisionPurpose",
        "subclassOf": ["DataActivityPurpose", "Purpose"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # ServiceProvisionPurpose DataActivityPurpose
    {
        "class": "HealthMonitoringPurpose",
        "subclassOf": ["ServiceProvisionPurpose", "DataActivityPurpose", "Purpose"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # HealthMonitoringPurpose ServiceProvisionPurpose
    {
        "class": "ServiceEnhancementPurpose",
        "subclassOf": ["DataActivityPurpose", "Purpose"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # ServiceEnhancementPurpose DataActivityPurpose
    {
        "class": "AnalyticsPurpose",
        "subclassOf": ["ServiceEnhancementPurpose", "DataActivityPurpose", "Purpose"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # AnalyticsPurpose ServiceEnhancementPurpose
    {
        "class": "SecurityPurpose",
        "subclassOf": ["ServiceEnhancementPurpose", "DataActivityPurpose", "Purpose"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # SecurityPurpose ServiceEnhancementPurpose
    {
        "class": "ResearchPurpose",
        "subclassOf": ["ServiceEnhancementPurpose", "DataActivityPurpose", "Purpose"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # ResearchPurpose ServiceEnhancementPurpose
    {
        "class": "MarketingPurpose",
        "subclassOf": ["ServiceEnhancementPurpose", "DataActivityPurpose", "Purpose"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # MarketingPurpose ServiceEnhancementPurpose

# Time periods
    {
        "class": "TimePeriod",
        "subclassOf": [],
        "attributeOf": ["Activity"],
    },  # TimePeriod Thing
    {
        "class": "DataRetentionTime",
        "subclassOf": ["TimePeriod"],
        "attributeOf": ["DataRetention"],
    },  # DataRetentionTime TimePeriod
    {
        "class": "NotificationTime",
        "subclassOf": ["TimePeriod"],
        "attributeOf": ["FPNotification", "UserNotification", "NotificationActivity"],
    },  # NotificationTime TimePeriod
    {
        "class": "DataBreachProcessingTime",
        "subclassOf": ["TimePeriod"],
        "attributeOf": ["DataBreachProcessing"],
    },  # DataBreachProcessingTime TimePeriod
    {
        "class": "PolicyAcceptanceTime",
        "subclassOf": ["TimePeriod"],
        "attributeOf": ["PolicyChange"],
    },  # PolicyAcceptanceTime TimePeriod

# Basis
    {
        "class": "Basis",
        "subclassOf": [],
        "attributeOf": ["Activity"],
    },  # Basis Thing
    {
        "class": "LegalBasis",
        "subclassOf": ["Basis"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # LegalBasis Basis

# Policy change scope
    {
        "class": "PolicyChangeScope",
        "subclassOf": [],
        "attributeOf": ["PolicyChange"],
    },  # PolicyChangeScope Thing

# User special category
    {
        "class": "UserSpecialCategory",
        "subclassOf": [],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # UserSpecialCategory Thing
    {
        "class": "EuropeanResident",
        "subclassOf": ["UserSpecialCategory"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # EuropeanResident UserSpecialCategory
    {
        "class": "CaliforniaResident",
        "subclassOf": ["UserSpecialCategory"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # CaliforniaResident UserSpecialCategory
    {
        "class": "RussianFederationResident",
        "subclassOf": ["UserSpecialCategory"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # RussianFederationResident UserSpecialCategory
    {
        "class": "ChildCategory",
        "subclassOf": ["UserSpecialCategory"],
        "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"],
    },  # ChildCategory UserSpecialCategory

]
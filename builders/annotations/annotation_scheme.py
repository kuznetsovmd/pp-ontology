

def get_manual_scheme():
    return [
        {
            "class": "Activity",
            "subclassOf": [],
            "attributeOf": []
        },  
        {
            "class": "DataBreachProcessing",
            "subclassOf": ["Activity"],
            "attributeOf": []
        },  
        {
            "class": "DataActivity",
            "subclassOf": ["Activity"],
            "attributeOf": []
        },  
        {
            "class": "PolicyChange",
            "subclassOf": ["DataActivity", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "DataUse",
            "subclassOf": ["DataActivity", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "DataProtection",
            "subclassOf": ["DataActivity", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "FPCollection",
            "subclassOf": ["DataActivity", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "TPCollection",
            "subclassOf": ["DataActivity", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "TPSharing",
            "subclassOf": ["DataActivity", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "DataRetention",
            "subclassOf": ["DataActivity", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "NotificationActivity",
            "subclassOf": ["Activity"],
            "attributeOf": []
        },  
        {
            "class": "FPNotification",
            "subclassOf": ["NotificationActivity", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "UserNotification",
            "subclassOf": ["NotificationActivity", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "DataControl",
            "subclassOf": ["Activity"],
            "attributeOf": []
        },  
        {
            "class": "AdvertisingDataControl",
            "subclassOf": ["DataControl", "Activity"],
            "attributeOf": []
        },  
        {
            "class": "OptInOptOutControl",
            "subclassOf": ["DataControl", "Activity"],
            "attributeOf": []
        },  


        {
            "class": "Agent",
            "subclassOf": [],
            "attributeOf": ["NotificationActivity", "Activity"]
        },  
        {
            "class": "User",
            "subclassOf": ["Agent"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "OptInOptOutControl", "AdvertisingDataControl", "DataControl", "UserNotification", "FPNotification", "FPCollection", "Activity"]
        },  
        {
            "class": "FirstParty",
            "subclassOf": ["Agent"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "UserNotification", "FPNotification", "DataBreachProcessing", "Activity"]
        },  
        {
            "class": "ThirdParty",
            "subclassOf": ["Agent"],
            "attributeOf": ["TPCollection", "TPSharing", "Activity"]
        },  


        {
            "class": "Data",
            "subclassOf": [],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "PersonalData",
            "subclassOf": ["Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "NonPersonalData",
            "subclassOf": ["Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "ServiceData",
            "subclassOf": ["PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "FinancialData",
            "subclassOf": ["PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "DeviceData",
            "subclassOf": ["PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "ApplicationData",
            "subclassOf": ["PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "AccountData",
            "subclassOf": ["PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "TrackingData",
            "subclassOf": ["PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "SensitiveData",
            "subclassOf": ["PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "ReligionData",
            "subclassOf": ["SensitiveData", "PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "RacialData",
            "subclassOf": ["SensitiveData", "PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "HealthData",
            "subclassOf": ["SensitiveData", "PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "GenericData",
            "subclassOf": ["SensitiveData", "PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "CrimeData",
            "subclassOf": ["SensitiveData", "PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  
        {
            "class": "BiometricData",
            "subclassOf": ["SensitiveData", "PersonalData", "Data"],
            "attributeOf": ["OptInOptOutControl", "AdvertisingDataControl", "DataControl", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "DataActivity", "DataBreachProcessing"]
        },  


        {
            "class": "Mechanism",
            "subclassOf": [],
            "attributeOf": ["Activity"]
        },  
        {
            "class": "DataRetentionMechanism",
            "subclassOf": ["Mechanism"],
            "attributeOf": ["DataRetention"]
        },  
        {
            "class": "StoreOnOwnServers",
            "subclassOf": ["DataRetentionMechanism", "Mechanism"],
            "attributeOf": ["DataRetention"]
        },  
        {
            "class": "StoreOnEmployedServers",
            "subclassOf": ["DataRetentionMechanism", "Mechanism"],
            "attributeOf": ["DataRetention"]
        },  
        {
            "class": "TPSharingAndCollectionCMechanism",
            "subclassOf": ["Mechanism"],
            "attributeOf": ["TPSharing", "TPCollection"]
        },  
        {
            "class": "TPSharingOrCollectionByContract",
            "subclassOf": ["TPSharingAndCollectionCMechanism", "Mechanism"],
            "attributeOf": ["TPSharing", "TPCollection"]
        },  
        {
            "class": "TPSharingOrCollectionForFree",
            "subclassOf": ["TPSharingAndCollectionCMechanism", "Mechanism"],
            "attributeOf": ["TPSharing", "TPCollection"]
        },  
        {
            "class": "SecurityMechanism",
            "subclassOf": ["Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "TechnicalSecurityMeasure",
            "subclassOf": ["SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "PseudoAnonymization",
            "subclassOf": ["TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "Encryption",
            "subclassOf": ["TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "SecureStorage",
            "subclassOf": ["Encryption", "TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "SecuredCommunication",
            "subclassOf": ["Encryption", "TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "Firewall",
            "subclassOf": ["TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "AccessControls",
            "subclassOf": ["TechnicalSecurityMeasure", "SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "OrganizationalSecurityMeasure",
            "subclassOf": ["SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "LockedOffice",
            "subclassOf": ["OrganizationalSecurityMeasure", "SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "SecurityTraining",
            "subclassOf": ["OrganizationalSecurityMeasure", "SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "UserMaintainsSecurity",
            "subclassOf": ["OrganizationalSecurityMeasure", "SecurityMechanism", "Mechanism"],
            "attributeOf": ["DataProtection"]
        },  
        {
            "class": "CommunicationMechanism",
            "subclassOf": ["Mechanism"],
            "attributeOf": ["NotificationActivity"]
        },  
        {
            "class": "UserSpecificCommunicationMechanism",
            "subclassOf": ["CommunicationMechanism", "Mechanism"],
            "attributeOf": ["UserNotification", "FPCollection"]
        },  
        {
            "class": "AutomaticCommunicationMechanism",
            "subclassOf": ["UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["UserNotification", "FPCollection"]
        },  
        {
            "class": "ViaServiceApp",
            "subclassOf": ["AutomaticCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["UserNotification", "FPCollection"]
        },  
        {
            "class": "ViaWebsite",
            "subclassOf": ["AutomaticCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["UserNotification", "FPCollection"]
        },  
        {
            "class": "ManualCommunicationMechanism",
            "subclassOf": ["UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["UserNotification", "FPCollection"]
        },  
        {
            "class": "WebsiteForm",
            "subclassOf": ["ManualCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["UserNotification", "FPCollection"]
        },  
        {
            "class": "ServiceAppForm",
            "subclassOf": ["ManualCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["UserNotification", "FPCollection"]
        },  
        {
            "class": "DataProvision",
            "subclassOf": ["ManualCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["UserNotification", "FPCollection"]
        },  
        {
            "class": "PersonalVisit",
            "subclassOf": ["ManualCommunicationMechanism", "UserSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["UserNotification", "FPCollection"]
        },  
        {
            "class": "GeneralCommunicationMechanism",
            "subclassOf": ["CommunicationMechanism", "Mechanism"],
            "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"]
        },  
        {
            "class": "Email",
            "subclassOf": ["GeneralCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"]
        },  
        {
            "class": "PostalMail",
            "subclassOf": ["GeneralCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"]
        },  
        {
            "class": "PhoneCall",
            "subclassOf": ["GeneralCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"]
        },  
        {
            "class": "SMS",
            "subclassOf": ["GeneralCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["FPNotification", "UserNotification", "FPCollection", "NotificationActivity"]
        },  
        {
            "class": "FPSpecificCommunicationMechanism",
            "subclassOf": ["CommunicationMechanism", "Mechanism"],
            "attributeOf": ["FPNotification"]
        },  
        {
            "class": "OnWebsitePage",
            "subclassOf": ["FPSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["FPNotification"]
        },  
        {
            "class": "OnServiceApp",
            "subclassOf": ["FPSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["FPNotification"]
        },  
        {
            "class": "InPrivacyPolicy",
            "subclassOf": ["FPSpecificCommunicationMechanism", "CommunicationMechanism", "Mechanism"],
            "attributeOf": ["FPNotification"]
        },  


        {
            "class": "Mode",
            "subclassOf": [],
            "attributeOf": ["Activity"]
        },  
        {
            "class": "DataTransmissionMode",
            "subclassOf": ["Mode"],
            "attributeOf": ["FPCollection", "TPCollection", "TPSharing"]
        },  
        {
            "class": "PermanentTransmission",
            "subclassOf": ["DataTransmissionMode", "Mode"],
            "attributeOf": ["FPCollection", "TPCollection", "TPSharing"]
        },  
        {
            "class": "TransmissionByRequest",
            "subclassOf": ["DataTransmissionMode", "Mode"],
            "attributeOf": ["FPCollection", "TPCollection", "TPSharing"]
        },  


        {
            "class": "Cause",
            "subclassOf": [],
            "attributeOf": ["Activity"]
        },  
        {
            "class": "DataBreach",
            "subclassOf": ["Cause"],
            "attributeOf": ["DataBreachProcessing"]
        },  
        {
            "class": "ForceMajeurIncident",
            "subclassOf": ["DataBreach", "Cause"],
            "attributeOf": ["DataBreachProcessing"]
        },  
        {
            "class": "IntentionalBreach",
            "subclassOf": ["DataBreach", "Cause"],
            "attributeOf": ["DataBreachProcessing"]
        },  
        {
            "class": "UnintentionalBreach",
            "subclassOf": ["DataBreach", "Cause"],
            "attributeOf": ["DataBreachProcessing"]
        },  
        {
            "class": "PolicyChangeCause",
            "subclassOf": ["Cause"],
            "attributeOf": ["PolicyChange"]
        },  
        {
            "class": "PrivacyRelatedCause",
            "subclassOf": ["PolicyChangeCause", "Cause"],
            "attributeOf": ["PolicyChange"]
        },  
        {
            "class": "NonPrivacyRelatedCause",
            "subclassOf": ["PolicyChangeCause", "Cause"],
            "attributeOf": ["PolicyChange"]
        },  
        {
            "class": "MergeAcquisitionCause",
            "subclassOf": ["PolicyChangeCause", "Cause"],
            "attributeOf": ["PolicyChange"]
        },  


        {
            "class": "Consequence",
            "subclassOf": [],
            "attributeOf": ["Activity"]
        },  
        {
            "class": "DataBreachConsequence",
            "subclassOf": ["Consequence"],
            "attributeOf": ["DataBreachProcessing"]
        },  
        {
            "class": "RemoveCompromisedInformation",
            "subclassOf": ["DataBreachConsequence", "Consequence"],
            "attributeOf": ["DataBreachProcessing"]
        },  
        {
            "class": "DataBreachCompensation",
            "subclassOf": ["DataBreachConsequence", "Consequence"],
            "attributeOf": ["DataBreachProcessing"]
        },  
        {
            "class": "PolicyChangeConsequence",
            "subclassOf": ["Consequence"],
            "attributeOf": ["PolicyChange"]
        },  
        {
            "class": "UserChoiceConsequence",
            "subclassOf": ["Consequence"],
            "attributeOf": ["PrivacyControl", "OptInOptOutControl"]
        },  
        {
            "class": "NoServiceRestriction",
            "subclassOf": ["UserChoiceConsequence", "Consequence"],
            "attributeOf": ["PrivacyControl", "OptInOptOutControl"]
        },  
        {
            "class": "PartialServiceRestriction",
            "subclassOf": ["UserChoiceConsequence", "Consequence"],
            "attributeOf": ["PrivacyControl", "OptInOptOutControl"]
        },  
        {
            "class": "FullServiceRestriction",
            "subclassOf": ["UserChoiceConsequence", "Consequence"],
            "attributeOf": ["PrivacyControl", "OptInOptOutControl"]
        },  


        {
            "class": "Purpose",
            "subclassOf": [],
            "attributeOf": ["Activity"]
        },  
        {
            "class": "DataActivityPurpose",
            "subclassOf": ["Purpose"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "LegalCompliancePurpose",
            "subclassOf": ["DataActivityPurpose", "Purpose"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "ServiceProvisionPurpose",
            "subclassOf": ["DataActivityPurpose", "Purpose"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "HealthMonitoringPurpose",
            "subclassOf": ["ServiceProvisionPurpose", "DataActivityPurpose", "Purpose"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "ServiceEnhancementPurpose",
            "subclassOf": ["DataActivityPurpose", "Purpose"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "AnalyticsPurpose",
            "subclassOf": ["ServiceEnhancementPurpose", "DataActivityPurpose", "Purpose"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "SecurityPurpose",
            "subclassOf": ["ServiceEnhancementPurpose", "DataActivityPurpose", "Purpose"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "ResearchPurpose",
            "subclassOf": ["ServiceEnhancementPurpose", "DataActivityPurpose", "Purpose"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "MarketingPurpose",
            "subclassOf": ["ServiceEnhancementPurpose", "DataActivityPurpose", "Purpose"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  


        {
            "class": "TimePeriod",
            "subclassOf": [],
            "attributeOf": ["Activity"]
        },  
        {
            "class": "DataRetentionTime",
            "subclassOf": ["TimePeriod"],
            "attributeOf": ["DataRetention"]
        },  
        {
            "class": "NotificationTime",
            "subclassOf": ["TimePeriod"],
            "attributeOf": ["FPNotification", "UserNotification", "NotificationActivity"]
        },  
        {
            "class": "DataBreachProcessingTime",
            "subclassOf": ["TimePeriod"],
            "attributeOf": ["DataBreachProcessing"]
        },  
        {
            "class": "PolicyAcceptanceTime",
            "subclassOf": ["TimePeriod"],
            "attributeOf": ["PolicyChange"]
        },  


        {
            "class": "Basis",
            "subclassOf": [],
            "attributeOf": ["Activity"]
        },  
        {
            "class": "LegalBasis",
            "subclassOf": ["Basis"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  


        {
            "class": "PolicyChangeScope",
            "subclassOf": [],
            "attributeOf": ["PolicyChange"]
        },  


        {
            "class": "UserSpecialCategory",
            "subclassOf": [],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "EuropeanResident",
            "subclassOf": ["UserSpecialCategory"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "CaliforniaResident",
            "subclassOf": ["UserSpecialCategory"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "RussianFederationResident",
            "subclassOf": ["UserSpecialCategory"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        },  
        {
            "class": "ChildCategory",
            "subclassOf": ["UserSpecialCategory"],
            "attributeOf": ["DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", "DataRetention", "PolicyChange", "DataActivity"]
        }
    ]

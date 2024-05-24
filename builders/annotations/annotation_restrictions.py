

def get_manual_restrictions():
    return {
        "User": {
            "initiated_by": [
                "DataControl", 
                "AdvertisingDataControl", "OptInOptOutControl", "UserNotification"
            ],
            "collects_from": [
                "FPCollection"
            ],
            "notifies": [
                "FPNotification"
            ],
            "special_category_for": [
                "EuropeanResident",
                "RussianFederationResident",
                "CaliforniaResident",
                "Child"
            ],
            "provides": ["Data"]
        },
        "FirstParty": {
            "initiated_by": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange"
            ],
            "notifies": [
                "UserNotification"
            ]
        },
        "ThirdParty": {
            "shares_with": [
                "TPSharing"
            ],
            "collects_from": [
                "TPCollection"
            ]
        },



        "Data": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "NonPersonalData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "PersonalData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "ServiceData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "FinancialData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "DeviceData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "ApplicationData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "AccountData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "TrackingData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "SensitiveData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "ReligionData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "RacialData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "GenericData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "CrimeData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },
        "BiometricData": {
            "applies_to": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange", 
                "OptInOptOutControl", "AdvertisingDataControl"
            ]
        },



        "Mechanism": {
            "has_mechanism": ["Activity"]
        },
        "DataRetentionMechanism": {
            "has_mechanism": ["DataRetention"]
        },
        "StoreOnOwnServers": {
            "has_mechanism": ["DataRetention"]
        },
        "StoreOnEmployedServers": {
            "has_mechanism": ["DataRetention"]
        },
        "TPSharingAndCollectionCMechanism": {
            "has_mechanism": ["TPSharing", "TPCollection"]
        },
        "TPSharingOrCollectionByContract": {
            "has_mechanism": ["TPSharing", "TPCollection"]
        },
        "TPSharingOrCollectionForFree": {
            "has_mechanism": ["TPSharing", "TPCollection"]
        },
        "SecurityMechanism": {
            "has_mechanism": ["DataProtection"]
        },
        "TechnicalSecurityMeasure": {
            "has_mechanism": ["DataProtection"]
        },
        "PseudoAnonymization": {
            "has_mechanism": ["DataProtection"]
        },
        "Encryption": {
            "has_mechanism": ["DataProtection"]
        },
        "SecureStorage": {
            "has_mechanism": ["DataProtection"]
        },
        "SecuredCommunication": {
            "has_mechanism": ["DataProtection"]
        },
        "Firewall": {
            "has_mechanism": ["DataProtection"]
        },
        "AccessControls": {
            "has_mechanism": ["DataProtection"]
        },
        "OrganizationalSecurityMeasure": {
            "has_mechanism": ["DataProtection"]
        },
        "LockedOffice": {
            "has_mechanism": ["DataProtection"]
        },
        "SecurityTraining": {
            "has_mechanism": ["DataProtection"]
        },
        "UserMaintainsSecurity": {
            "has_mechanism": ["DataProtection"]
        },



        "CommunicationMechanism": {
            "has_mechanism": ["FPCollection", "FPCollection", "Notification", "UserNotification", "FPNotification"]
        },
        "UserSpecificCommunicationMechanism": {
            "has_mechanism": ["FPCollection", "FPCollection", "UserNotification"]
        },
        "AutomaticCommunicationMechanism": {
            "has_mechanism": ["FPCollection"]
        },
        "ViaServiceApp": {
            "has_mechanism": ["FPCollection"]
        },
        "ViaWebsite": {
            "has_mechanism": ["FPCollection"]
        },
        "ManualCommunicationMechanism": {
            "has_mechanism": ["FPCollection", "UserNotification"]
        },
        "WebsiteForm": {
            "has_mechanism": ["FPCollection", "UserNotification"]
        },
        "ServiceAppForm": {
            "has_mechanism": ["FPCollection", "UserNotification"]
        },
        "DataProvision": {
            "has_mechanism": ["FPCollection", "UserNotification"]
        },
        "PersonalVisit": {
            "has_mechanism": ["FPCollection", "UserNotification"]
        },
        "GeneralCommunicationMechanism": {
            "has_mechanism": ["FPCollection", "UserNotification", "FPNotification"]
        },
        "Email": {
            "has_mechanism": ["FPCollection", "UserNotification", "FPNotification"]
        },
        "PostalMail": {
            "has_mechanism": ["FPCollection", "UserNotification", "FPNotification"]
        },
        "PhoneCall": {
            "has_mechanism": ["FPCollection", "UserNotification", "FPNotification"]
        },
        "SMS": {
            "has_mechanism": ["FPCollection", "UserNotification", "FPNotification"]
        },
        "FPSpecificCommunicationMechanism": {
            "has_mechanism": ["FPNotification"]
        },
        "OnWebsitePage": {
            "has_mechanism": ["FPNotification"]
        },
        "OnServiceApp": {
            "has_mechanism": ["FPNotification"]
        },
        "InPrivacyPolicy": {
            "has_mechanism": ["FPNotification"]
        },



        "FPCollection": {
            "mode_for": [
                "Mode", 
                "DataTransmissionMode", 
                "PermanentTransmission", 
                "TransmissionByRequest"
            ]
        },
        "TPCollection": {
            "mode_for": [
                "Mode", 
                "DataTransmissionMode", 
                "PermanentTransmission", 
                "TransmissionByRequest"
            ]
        },
        "TPSharing": {
            "mode_for": [
                "Mode", 
                "DataTransmissionMode", 
                "PermanentTransmission", 
                "TransmissionByRequest"
            ]
        },

        


        "Cause": {
            "caused_by": ["Activity"]
        },
        "DataBreach": {
            "caused_by": [
                "Mode", 
                "DataTransmissionMode", 
                "PermanentTransmission", 
                "TransmissionByRequest"
            ]
        },
        "ForceMajeurIncident": {
            "caused_by": ["DataBreachProcessing"]
        },
        "IntentionalBreach": {
            "caused_by": ["DataBreachProcessing"]
        },
        "UnintentionalBreach": {
            "caused_by": ["DataBreachProcessing"]
        },
        "PolicyChangeCause": {
            "caused_by": ["PolicyChange"]
        },
        "PrivacyRelatedCause": {
            "caused_by": ["PolicyChange"]
        },
        "NonPrivacyRelatedCause": {
            "caused_by": ["PolicyChange"]
        },
        "MergeAcquisitionCause": {
            "caused_by": ["PolicyChange"]
        },



        "Consequence": {
            "consequence_for": ["Activity"]
        },
        "DataBreachConsequence": {
            "consequence_for": ["DataBreachProcessing"]
        },
        "RemoveCompromisedInformation": {
            "consequence_for": ["DataBreachProcessing"]
        },
        "DataBreachCompensation": {
            "consequence_for": ["DataBreachProcessing"]
        },
        "PolicyChangeConsequence": {
            "consequence_for": ["PolicyChange"]
        },
        "UserChoiceConsequence": {
            "consequence_for": [
                "DataControl", 
                "AdvertisingDataControl", 
                "OptInOptOutControl"
            ]
        },
        "NoServiceRestriction": {
            "consequence_for": [
                "DataControl", 
                "AdvertisingDataControl", 
                "OptInOptOutControl"
            ]
        },
        "PartialServiceRestriction": {
            "consequence_for": [
                "DataControl", 
                "AdvertisingDataControl", 
                "OptInOptOutControl"
            ]
        },
        "FullServiceRestriction": {
            "consequence_for": [
                "DataControl", 
                "AdvertisingDataControl", 
                "OptInOptOutControl"
            ]
        },

        

        "Purpose": {
            "has_purpose": ["Activity"]
        },
        "DataActivityPurpose": {
            "has_purpose": [
                "DataActivity", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "FPNotification", "DataBreachProcessing", "PolicyChange"
            ]
        },
        "LegalCompliancePurpose": {
            "has_purpose": [
                "DataActivity", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention"
            ]
        },
        "ServiceProvisionPurpose": {
            "has_purpose": [
                "DataActivity", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention"
            ]
        },
        "HealthMonitoringPurpose": {
            "has_purpose": [
                "DataActivity", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention"
            ]
        },
        "ServiceEnhancementPurpose": {
            "has_purpose": [
                "DataActivity", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention"
            ]
        },
        "AnalyticsPurpose": {
            "has_purpose": [
                "DataActivity", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention"
            ]
        },
        "SecurityPurpose": {
            "has_purpose": [
                "DataActivity", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention"
            ]
        },
        "ResearchPurpose": {
            "has_purpose": [
                "DataActivity", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention"
            ]
        },
        "MarketingPurpose": {
            "has_purpose": [
                "DataActivity", "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention"
            ]
        },

        

        "TimePeriod": {
            "lasts_for": ["Activity"]
        },
        "DataRetentionTime": {
            "lasts_for": ["DataRetention"]
        },
        "NotificationTime": {
            "lasts_for": ["DataBreachProcessing"]
        },
        "DataBreachProcessingTime": {
            "lasts_for": ["DataBreachProcessing"]
        },
        "PolicyAcceptanceTime": {
            "lasts_for": ["PolicyChange"]
        },

        

        "Basis": {
            "has_basis": ["Activity"]
        },
        "LegalBasis": {
            "has_basis": [
                "DataUse", "DataProtection", "FPCollection", "TPCollection", "TPSharing", 
                "DataRetention", "PolicyChange"
            ]
        },

        

        "PolicyChangeScope": {
            "has_scope": ["PolicyChange"]
        }
    }

from owlready2 import *


def construct(onto):
    with onto:
        """
        Classes
        """
        # Privacy policy
        class PrivacyPolicy(Thing): ...

        # Activities
        class Activity(Thing): ...
        class DataBreachProcessing(Activity): ...
        class DataActivity(Activity): ...
        class PolicyChange(DataActivity): ...
        class DataUse(DataActivity): ...
        class DataProtection(DataActivity): ...
        class FPCollection(DataActivity): ...
        class TPCollection(DataActivity): ...
        class TPSharing(DataActivity): ...
        class DataRetention(DataActivity): ...
        class NotificationActivity(Activity): ...
        class FPNotification(NotificationActivity): ...
        class UserNotification(NotificationActivity): ...
        class DataControl(Activity): ...
        class AdvertisingDataControl(DataControl): ...
        class OptInOptOutControl(DataControl): ...

        # Agents
        class Agent(Thing): ...
        class User(Agent): ...
        class FirstParty(Agent): ...
        class ThirdParty(Agent): ...

        # Data
        class Data(Thing): ...
        class NonPersonalData(Data): ...
        class PersonalData(Data): ...
        class ServiceData(PersonalData): ...
        class FinancialData(PersonalData): ...
        class DeviceData(PersonalData): ...
        class ApplicationData(PersonalData): ...
        class AccountData(PersonalData): ...
        class TrackingData(PersonalData): ...
        class SensitiveData(PersonalData): ...
        class ReligionData(SensitiveData): ...
        class RacialData(SensitiveData): ...
        class HealthData(SensitiveData): ...
        class GenericData(SensitiveData): ...
        class CrimeData(SensitiveData): ...
        class BiometricData(SensitiveData): ...

        # Mechanisms
        class Mechanism(Thing): ...

        class DataRetentionMechanism(Mechanism): ...
        class StoreOnOwnServers(DataRetentionMechanism): ...
        class StoreOnEmployedServers(DataRetentionMechanism): ...

        class TPSharingAndCollectionCMechanism(Mechanism): ...
        class TPSharingOrCollectionByContract(TPSharingAndCollectionCMechanism): ...
        class TPSharingOrCollectionForFree(TPSharingAndCollectionCMechanism): ...

        class SecurityMechanism(Mechanism): ...
        class TechnicalSecurityMeasure(SecurityMechanism): ...
        class PseudoAnonymization(TechnicalSecurityMeasure): ...
        class Encryption(TechnicalSecurityMeasure): ...
        class SecureStorage(Encryption): ...
        class SecuredCommunication(Encryption): ...
        class Firewall(TechnicalSecurityMeasure): ...
        class AccessControls(TechnicalSecurityMeasure): ...
        class OrganizationalSecurityMeasure(SecurityMechanism): ...
        class LockedOffice(OrganizationalSecurityMeasure): ...
        class SecurityTraining(OrganizationalSecurityMeasure): ...
        class UserMaintainsSecurity(OrganizationalSecurityMeasure): ...

        class CommunicationMechanism(Mechanism): ...
        class UserSpecificCommunicationMechanism(CommunicationMechanism): ...
        class AutomaticCommunicationMechanism(UserSpecificCommunicationMechanism): ...
        class ViaServiceApp(AutomaticCommunicationMechanism): ...
        class ViaWebsite(AutomaticCommunicationMechanism): ...
        class ManualCommunicationMechanism(UserSpecificCommunicationMechanism): ...
        class WebsiteForm(ManualCommunicationMechanism): ...
        class ServiceAppForm(ManualCommunicationMechanism): ...
        class DataProvision(ManualCommunicationMechanism): ...
        class PersonalVisit(ManualCommunicationMechanism): ...
        class GeneralCommunicationMechanism(CommunicationMechanism): ...
        class Email(GeneralCommunicationMechanism): ...
        class PostalMail(GeneralCommunicationMechanism): ...
        class PhoneCall(GeneralCommunicationMechanism): ...
        class SMS(GeneralCommunicationMechanism): ...
        class FPSpecificCommunicationMechanism(CommunicationMechanism): ...
        class OnWebsitePage(FPSpecificCommunicationMechanism): ...
        class OnServiceApp(FPSpecificCommunicationMechanism): ...
        class InPrivacyPolicy(FPSpecificCommunicationMechanism): ...

        # Modes
        class Mode(Thing): ...
        class DataTransmissionMode(Mode): ...
        class PermanentTransmission(DataTransmissionMode): ...
        class TransmissionByRequest(DataTransmissionMode): ...

        # Causes
        class Cause(Thing): ...
        class DataBreach(Cause): ...
        class ForceMajeurIncident(DataBreach): ...
        class IntentionalBreach(DataBreach): ...
        class UnintentionalBreach(DataBreach): ...
        class PolicyChangeCause(Cause): ...
        class PrivacyRelatedCause(PolicyChangeCause): ...
        class NonPrivacyRelatedCause(PolicyChangeCause): ...
        class MergeAcquisitionCause(PolicyChangeCause): ...

        # Consequences
        class Consequence(Thing): ...
        class DataBreachConsequence(Consequence): ...
        class RemoveCompromisedInformation(DataBreachConsequence): ...
        class DataBreachCompensation(DataBreachConsequence): ...
        class PolicyChangeConsequence(Consequence): ...
        class UserChoiceConsequence(Consequence): ...
        class NoServiceRestriction(UserChoiceConsequence): ...
        class PartialServiceRestriction(UserChoiceConsequence): ...
        class FullServiceRestriction(UserChoiceConsequence): ...

        # Purposes
        class Purpose(Thing): ...
        class DataActivityPurpose(Purpose): ...
        class LegalCompliancePurpose(DataActivityPurpose): ...
        class ServiceProvisionPurpose(DataActivityPurpose): ...
        class HealthMonitoringPurpose(ServiceProvisionPurpose): ...
        class ServiceEnhancementPurpose(DataActivityPurpose): ...
        class AnalyticsPurpose(ServiceEnhancementPurpose): ...
        class SecurityPurpose(ServiceEnhancementPurpose): ...
        class ResearchPurpose(ServiceEnhancementPurpose): ...
        class MarketingPurpose(ServiceEnhancementPurpose): ...

        # Time periods
        class TimePeriod(Thing): ...
        class DataRetentionTime(TimePeriod): ...
        class NotificationTime(TimePeriod): ...
        class DataBreachProcessingTime(TimePeriod): ...
        class PolicyAcceptanceTime(TimePeriod): ...

        # Basis
        class Basis(Thing): ...
        class LegalBasis(Basis): ...

        # Policy change scope
        class PolicyChangeScope(Thing): ...

        # User special category
        class UserSpecialCategory(Thing): ...
        class EuropeanResident(UserSpecialCategory): ...
        class CaliforniaResident(UserSpecialCategory): ...
        class RussianFederationResident(UserSpecialCategory): ...
        class ChildCategory(UserSpecialCategory): ...

        """
        Class disjoints

        Make classes of same level different (involves subclasses)
        """
        AllDisjoint([PrivacyPolicy, Agent, Activity, Data, Basis, Purpose, Mode, 
                     Cause, Consequence, TimePeriod, PolicyChangeScope, UserSpecialCategory])

        AllDisjoint([User, FirstParty, ThirdParty])

        AllDisjoint([DataBreachProcessing, DataActivity, DataControl, NotificationActivity])

        AllDisjoint([DataUse, DataProtection, FPCollection, TPCollection, TPSharing, DataRetention, PolicyChange])
        AllDisjoint([FPNotification, UserNotification])
        AllDisjoint([DataControl, PolicyChange])
        AllDisjoint([AdvertisingDataControl, OptInOptOutControl])

        AllDisjoint([LegalCompliancePurpose, ServiceEnhancementPurpose, ServiceProvisionPurpose])
        AllDisjoint([AnalyticsPurpose, MarketingPurpose, ResearchPurpose, SecurityPurpose])

        AllDisjoint([TransmissionByRequest, PermanentTransmission])

        AllDisjoint([SecurityMechanism, TPSharingAndCollectionCMechanism, DataRetentionMechanism, CommunicationMechanism])

        AllDisjoint([StoreOnOwnServers, StoreOnEmployedServers])
        AllDisjoint([TPSharingOrCollectionByContract, TPSharingOrCollectionForFree])
        AllDisjoint([TechnicalSecurityMeasure, OrganizationalSecurityMeasure])
        AllDisjoint([LockedOffice, SecurityTraining, UserMaintainsSecurity])
        AllDisjoint([Firewall, PseudoAnonymization, AccessControls, Encryption])
        AllDisjoint([SecuredCommunication, SecureStorage])

        AllDisjoint([UserSpecificCommunicationMechanism, FPSpecificCommunicationMechanism, GeneralCommunicationMechanism])

        AllDisjoint([InPrivacyPolicy, OnWebsitePage, OnServiceApp])
        AllDisjoint([Email, SMS, PhoneCall, PostalMail])
        AllDisjoint([ManualCommunicationMechanism, AutomaticCommunicationMechanism])
        AllDisjoint([ViaServiceApp, ViaWebsite])
        AllDisjoint([PersonalVisit, DataProvision, WebsiteForm, ServiceAppForm])

        AllDisjoint([PolicyChangeCause, DataBreach])
        AllDisjoint([ForceMajeurIncident, UnintentionalBreach, IntentionalBreach])
        AllDisjoint([MergeAcquisitionCause, NonPrivacyRelatedCause, PrivacyRelatedCause])

        AllDisjoint([PolicyChangeConsequence, DataBreachConsequence, UserChoiceConsequence])
        AllDisjoint([DataBreachCompensation, RemoveCompromisedInformation])
        AllDisjoint([PartialServiceRestriction, NoServiceRestriction, FullServiceRestriction])

        AllDisjoint([PolicyAcceptanceTime, DataRetentionTime, NotificationTime, DataBreachProcessingTime])

        AllDisjoint([PersonalData, NonPersonalData])
        AllDisjoint([SensitiveData, ServiceData, FinancialData, DeviceData, ApplicationData, AccountData, TrackingData])
        AllDisjoint([GenericData, CrimeData, HealthData, RacialData, BiometricData, ReligionData])
        
        AllDisjoint([EuropeanResident, RussianFederationResident, CaliforniaResident, ChildCategory])

        """
        Object properties
        """
        # Considers
        class considered_by(ObjectProperty): ...
        class considers(ObjectProperty): ...

        # Applies
        class applied_by(ObjectProperty): ...
        class applies_to(ObjectProperty): ...

        # Provides
        class provided_by(ObjectProperty): ...
        class provides(ObjectProperty): ...

        # Activities
        class initiated_by(ObjectProperty): ...
        class initiates(ObjectProperty): ...

        # Mechanisms
        class mechanism_of(ObjectProperty): ...
        class has_mechanism(ObjectProperty): ...

        # Modes
        class is_mode_for(ObjectProperty): ...
        class has_mode(ObjectProperty): ...

        # Durations
        class is_period_of(ObjectProperty): ...
        class lasts_for(ObjectProperty): ...

        # Causes
        class causes(ObjectProperty): ...
        class caused_by(ObjectProperty): ...

        # Consequences
        class is_consequence_of(ObjectProperty): ...
        class has_consequence(ObjectProperty): ...

        # Purposes
        class is_purpose_for(ObjectProperty): ...
        class has_purpose(ObjectProperty): ...

        # Basis
        class is_basis_for(ObjectProperty): ...
        class has_basis(ObjectProperty): ...

        # Basis
        class is_scope_for(ObjectProperty): ...
        class has_scope(ObjectProperty): ...

        # Basis
        class is_special_category_for(ObjectProperty): ...
        class has_special_category(ObjectProperty): ...

        # Collects
        class collects_from(ObjectProperty): ...
        class is_collected_by(ObjectProperty): ...

        # Shares
        class shares_with(ObjectProperty): ...
        class is_shared_by(ObjectProperty): ...

        # Shares
        class notifies(ObjectProperty): ...
        class notified_by(ObjectProperty): ...

        # Ordering & Navigation
        class following(ObjectProperty, TransitiveProperty): ...
        class followed_by(ObjectProperty, TransitiveProperty): ...
        class next_is(followed_by, IrreflexiveProperty, FunctionalProperty): ...
        class previous_is(following, IrreflexiveProperty, FunctionalProperty): ...
        class binded_to(ObjectProperty, SymmetricProperty, IrreflexiveProperty): ...
        
        class newer_than(ObjectProperty): ...
        class older_than(ObjectProperty): ...

        """
        Data properties
        """
        class uuid(DataProperty, FunctionalProperty): ...
        class evidence(DataProperty, FunctionalProperty): ...
        class policyId(DataProperty, FunctionalProperty): ...
        class policyUpdate(DataProperty, FunctionalProperty): ...
        class policyWebsite(DataProperty, FunctionalProperty): ...
        class does(DataProperty, FunctionalProperty): ...

        """
        Class restrictions
        """
        PrivacyPolicy.is_a.extend([
            considers.only(Agent | Activity | Data)
        ])

        # Activities
        Activity.is_a.extend([
            considered_by.only(PrivacyPolicy)
            & has_basis.only(Basis)
            & has_purpose.only(Purpose)
            & has_mode.only(Mode)
            & has_mechanism.only(Mechanism)
            & caused_by.only(Cause)
            & has_consequence.only(Consequence)
            & lasts_for.only(TimePeriod)
            & has_scope.only(PolicyChangeScope)
        ])

        DataBreachProcessing.is_a.extend([
            initiated_by.only(FirstParty)
            & applies_to.only(Data)
            & caused_by.only(DataBreach)
            & has_consequence.only(DataBreachConsequence)
        ])

        DataActivity.is_a.extend([
            initiated_by.only(FirstParty)
            & has_purpose.only(DataActivityPurpose)
            & applies_to.only(Data)
            & has_basis.only(LegalBasis)
        ])

        DataUse.is_a.extend([
            DataActivity
        ])

        DataProtection.is_a.extend([
            has_mechanism.only(SecurityMechanism)
        ])

        FPCollection.is_a.extend([
            collects_from.only(User)
            & has_mechanism.only(UserSpecificCommunicationMechanism | GeneralCommunicationMechanism)
            & has_mode.only(DataTransmissionMode)
        ])

        TPCollection.is_a.extend([
            collects_from.only(ThirdParty)
            & has_mechanism.only(TPSharingAndCollectionCMechanism)
            & has_mode.only(DataTransmissionMode)
        ])

        TPSharing.is_a.extend([
            shares_with.only(ThirdParty)
            & has_mechanism.only(TPSharingAndCollectionCMechanism)
            & has_mode.only(DataTransmissionMode)
        ])

        DataRetention.is_a.extend([
            has_mechanism.only(DataRetentionMechanism)
            & lasts_for.only(DataRetentionTime)
        ])

        PolicyChange.is_a.extend([
            has_consequence.only(PolicyChangeConsequence)
            & caused_by.only(PolicyChangeCause)
            & lasts_for.only(PolicyAcceptanceTime)
            & has_scope.only(PolicyChangeScope)
        ])

        NotificationActivity.is_a.extend([
            initiated_by.only(Agent)
            & notifies.only(Agent)
            & has_mechanism.only(CommunicationMechanism)
            & lasts_for.only(NotificationTime)
        ])

        FPNotification.is_a.extend([
            initiated_by.only(FirstParty)
            & notifies.only(User)
            & has_mechanism.only(FPSpecificCommunicationMechanism | GeneralCommunicationMechanism)
        ])

        UserNotification.is_a.extend([
            initiated_by.only(User)
            & notifies.only(FirstParty)
            & has_mechanism.only(ManualCommunicationMechanism | GeneralCommunicationMechanism)
        ])

        DataControl.is_a.extend([
            initiated_by.only(User)
            & applies_to.only(Data)
            & has_basis.only(LegalBasis)
            & has_mechanism.only(ManualCommunicationMechanism | GeneralCommunicationMechanism)
        ])

        AdvertisingDataControl.is_a.extend([
            
        ])

        OptInOptOutControl.is_a.extend([

        ])

        # Agents
        Agent.is_a.extend([
            considered_by.only(PrivacyPolicy)
            & initiates.only(Activity)
        ])

        User.is_a.extend([
            provides.only(Data)
            & initiates.only(DataControl | UserNotification)
            & has_special_category.only(UserSpecialCategory)
            & is_collected_by.only(FPCollection)
            & notified_by.only(FPNotification)
        ])

        FirstParty.is_a.extend([
            initiates.only(DataActivity | FPNotification | DataBreachProcessing)
            & notified_by.only(UserNotification)
        ])

        ThirdParty.is_a.extend([
            is_shared_by.only(TPSharing)
            & is_collected_by.only(TPCollection)
        ])


        # Data
        Data.is_a.extend([
            considered_by.only(PrivacyPolicy)
        ])

        PersonalData.is_a.extend([

        ])

        NonPersonalData.is_a.extend([

        ])

        ServiceData.is_a.extend([

        ])

        FinancialData.is_a.extend([

        ])

        DeviceData.is_a.extend([

        ])

        ApplicationData.is_a.extend([

        ])

        AccountData.is_a.extend([

        ])

        TrackingData.is_a.extend([

        ])

        SensitiveData.is_a.extend([

        ])

        ReligionData.is_a.extend([

        ])

        RacialData.is_a.extend([

        ])

        HealthData.is_a.extend([

        ])

        GenericData.is_a.extend([

        ])

        CrimeData.is_a.extend([

        ])

        BiometricData.is_a.extend([

        ])

        # Mechanisms
        Mechanism.is_a.extend([
            mechanism_of.only(Activity)
        ])

        DataRetentionMechanism.is_a.extend([
            mechanism_of.only(DataRetention)
        ])

        StoreOnOwnServers.is_a.extend([

        ])

        StoreOnEmployedServers.is_a.extend([

        ])

        TPSharingAndCollectionCMechanism.is_a.extend([
            mechanism_of.only(TPCollection | TPSharing)
        ])

        TPSharingOrCollectionByContract.is_a.extend([

        ])

        TPSharingOrCollectionForFree.is_a.extend([

        ])

        SecurityMechanism.is_a.extend([
            mechanism_of.only(DataProtection)
        ])

        TechnicalSecurityMeasure.is_a.extend([

        ])

        PseudoAnonymization.is_a.extend([

        ])

        Encryption.is_a.extend([

        ])

        SecureStorage.is_a.extend([

        ])

        SecuredCommunication.is_a.extend([

        ])

        Firewall.is_a.extend([

        ])

        AccessControls.is_a.extend([

        ])

        OrganizationalSecurityMeasure.is_a.extend([

        ])

        LockedOffice.is_a.extend([

        ])

        SecurityTraining.is_a.extend([

        ])

        UserMaintainsSecurity.is_a.extend([

        ])

        CommunicationMechanism.is_a.extend([
            mechanism_of.only(NotificationActivity | DataControl | FPCollection)
        ])

        UserSpecificCommunicationMechanism.is_a.extend([
            mechanism_of.only(Not(FPNotification))
        ])

        AutomaticCommunicationMechanism.is_a.extend([

        ])

        ViaServiceApp.is_a.extend([

        ])

        ViaWebsite.is_a.extend([

        ])

        ManualCommunicationMechanism.is_a.extend([
            mechanism_of.only(Not(FPNotification))
        ])

        WebsiteForm.is_a.extend([

        ])

        ServiceAppForm.is_a.extend([

        ])

        DataProvision.is_a.extend([

        ])

        PersonalVisit.is_a.extend([

        ])

        GeneralCommunicationMechanism.is_a.extend([
            
        ])

        Email.is_a.extend([

        ])

        PostalMail.is_a.extend([

        ])

        PhoneCall.is_a.extend([

        ])

        SMS.is_a.extend([

        ])

        FPSpecificCommunicationMechanism.is_a.extend([
            mechanism_of.only(FPNotification)
        ])

        OnWebsitePage.is_a.extend([

        ])

        OnServiceApp.is_a.extend([

        ])

        InPrivacyPolicy.is_a.extend([

        ])

        # Modes
        Mode.is_a.extend([
            is_mode_for.only(Activity)
        ])

        DataTransmissionMode.is_a.extend([
            is_mode_for.only(FPCollection | TPCollection | TPSharing)
        ])

        PermanentTransmission.is_a.extend([

        ])

        TransmissionByRequest.is_a.extend([

        ])

        # Causes
        Cause.is_a.extend([
            causes.only(Activity)
        ])

        DataBreach.is_a.extend([
            causes.only(DataBreachProcessing)
        ])

        ForceMajeurIncident.is_a.extend([

        ])

        IntentionalBreach.is_a.extend([

        ])

        UnintentionalBreach.is_a.extend([

        ])

        PolicyChangeCause.is_a.extend([
            causes.only(PolicyChange)
        ])

        PrivacyRelatedCause.is_a.extend([

        ])

        NonPrivacyRelatedCause.is_a.extend([

        ])

        MergeAcquisitionCause.is_a.extend([

        ])


        # Consequences
        Consequence.is_a.extend([
            is_consequence_of.only(Activity)
        ])

        DataBreachConsequence.is_a.extend([
            is_consequence_of.only(DataBreachProcessing)
        ])

        RemoveCompromisedInformation.is_a.extend([

        ])

        DataBreachCompensation.is_a.extend([

        ])

        DataBreachProcessing.is_a.extend([

        ])

        PolicyChangeConsequence.is_a.extend([
            is_consequence_of.only(PolicyChange)
        ])

        UserChoiceConsequence.is_a.extend([
            is_consequence_of.only(DataControl)
        ])

        NoServiceRestriction.is_a.extend([

        ])

        PartialServiceRestriction.is_a.extend([

        ])

        FullServiceRestriction.is_a.extend([

        ])

        # Purposes
        Purpose.is_a.extend([
            is_purpose_for.only(Activity)
        ])

        DataActivityPurpose.is_a.extend([
            is_purpose_for.only(DataActivity)
        ])

        ServiceProvisionPurpose.is_a.extend([

        ])

        HealthMonitoringPurpose.is_a.extend([

        ])

        ServiceEnhancementPurpose.is_a.extend([

        ])

        AnalyticsPurpose.is_a.extend([

        ])

        SecurityPurpose.is_a.extend([

        ])

        ResearchPurpose.is_a.extend([

        ])

        MarketingPurpose.is_a.extend([

        ])


        # Time periods
        TimePeriod.is_a.extend([
            is_period_of.only(Activity)
        ])

        DataRetentionTime.is_a.extend([
            is_period_of.only(DataRetention)
        ])

        NotificationTime.is_a.extend([
            is_period_of.only(NotificationActivity)
        ])

        DataBreachProcessingTime.is_a.extend([
            is_period_of.only(DataBreachProcessing)
        ])

        PolicyAcceptanceTime.is_a.extend([
            is_period_of.only(PolicyChange)
        ])

        # Basis
        Basis.is_a.extend([
            is_basis_for.only(Activity)
        ])

        LegalBasis.is_a.extend([
            is_basis_for.only(DataActivity | DataControl)
        ])

        # Policy change scope
        PolicyChangeScope.is_a.extend([
            is_scope_for.only(PolicyChange)
        ])

        # User special category
        UserSpecialCategory.is_a.extend([
            is_special_category_for.only(User)
        ])

        EuropeanResident.is_a.extend([

        ])

        CaliforniaResident.is_a.extend([

        ])

        RussianFederationResident.is_a.extend([

        ])

        ChildCategory.is_a.extend([

        ])

        """
        Object properties restrictions
        """
        considered_by.inverse_property = considers
        applies_to.inverse_property = applied_by
        provides.inverse_property = provided_by
        initiates.inverse_property = initiated_by
        has_mechanism.inverse_property = mechanism_of
        collects_from.inverse_property = is_collected_by
        shares_with.inverse_property = is_shared_by
        notifies.inverse_property = notified_by
        has_mode.inverse_property = is_mode_for
        lasts_for.inverse_property = is_period_of
        causes.inverse_property = caused_by
        has_consequence.inverse_property = is_consequence_of
        has_purpose.inverse_property = is_purpose_for
        has_scope.inverse_property = is_scope_for
        has_special_category.inverse_property = is_special_category_for
        has_basis.inverse_property = is_basis_for

        binded_to.domain = [Activity]
        binded_to.range = [Activity]

        followed_by.domain = [Activity]
        followed_by.range = [Activity]
        followed_by.inverse_property = following

        next_is.inverse = previous_is

        newer_than.domain = [PrivacyPolicy]
        newer_than.range = [PrivacyPolicy]
        newer_than.inverse_property = older_than

        """
        Data properties restrictions
        """
        uuid.domain = [Thing]
        uuid.range = [str]

        evidence.domain = [Thing & Not(PrivacyPolicy)]
        evidence.range = [str]

        policyId.domain = [PrivacyPolicy]
        policyId.range = [int]

        policyUpdate.domain = [PrivacyPolicy]
        policyUpdate.range = [str]

        policyWebsite.domain = [PrivacyPolicy]
        policyWebsite.range = [str]

        does.domain = [Activity]
        does.range = [bool]

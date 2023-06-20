from owlready2 import *


def construct(onto):
    with onto:
        """
        Classes
        """
        # Privacy policy
        class PrivacyPolicy(Thing): pass

        # Activities
        class Activity(Thing): pass
        class DataActivity(Activity): pass
        class Use(DataActivity): pass
        class Protection(DataActivity): pass
        class FPCollection(DataActivity): pass
        class TPCollection(DataActivity): pass
        class TPSharing(DataActivity): pass
        class Retention(DataActivity): pass
        class Notification(Activity): pass
        class FPNotification(Notification): pass
        class UserNotification(Notification): pass
        class Breach(Activity): pass
        class ControlActivity(Activity): pass
        class PolicyChange(ControlActivity): pass
        class DataControl(ControlActivity): pass
        class ProvidedDataControl(DataControl): pass
        class PrivacyControl(DataControl): pass
        class OptControl(DataControl): pass

        # Agents
        class Agent(Thing): pass
        class User(Agent): pass
        class FirstParty(Agent): pass
        class ThirdParty(Agent): pass
        class Criminal(Agent): pass
        class DataProtectionOfficer(Agent): pass

        # Data
        class Data(Thing): pass
        class PersonalData(Data): pass
        class NonPersonalData(Data): pass
        class NonSensitiveData(PersonalData): pass
        class ServiceData(NonSensitiveData): pass
        class FinancialData(NonSensitiveData): pass
        class DeviceData(NonSensitiveData): pass
        class ApplicationData(NonSensitiveData): pass
        class AccountData(NonSensitiveData): pass
        class TrackingData(NonSensitiveData): pass
        class SensitiveData(PersonalData): pass
        class ReligionData(SensitiveData): pass
        class RacialData(SensitiveData): pass
        class HealthData(SensitiveData): pass
        class GenericData(SensitiveData): pass
        class CrimeData(SensitiveData): pass
        class BiometricData(SensitiveData): pass

        # Mechanisms
        class Mechanism(Thing): pass
        class DataRetentionMechanism(Mechanism): pass
        class OwnServers(DataRetentionMechanism): pass
        class EmployedServers(DataRetentionMechanism): pass
        class TPSaCMechanism(Mechanism): pass
        class Contract(TPSaCMechanism): pass
        class ForFree(TPSaCMechanism): pass
        class SecurityMechanism(Mechanism): pass
        class TechnicalMeasure(SecurityMechanism): pass
        class PseudoAnonymization(TechnicalMeasure): pass
        class Encryption(TechnicalMeasure): pass
        class SecureStorage(Encryption): pass
        class SecureTunnel(Encryption): pass
        class Firewall(TechnicalMeasure): pass
        class AccessControls(TechnicalMeasure): pass
        class OrganizationalMeasure(SecurityMechanism): pass
        class LockedOffice(OrganizationalMeasure): pass
        class SecurityTraining(OrganizationalMeasure): pass
        class UserMaintain(OrganizationalMeasure): pass
        class CommunicationMechanism(Mechanism): pass
        class UserSpecific(CommunicationMechanism): pass
        class Automatic(UserSpecific): pass
        class ThroughServiceApp(Automatic): pass
        class ThroughWebsite(Automatic): pass
        class Manual(UserSpecific): pass
        class WebsiteForm(Manual): pass
        class ServiceAppForm(Manual): pass
        class DataProvision(Manual): pass
        class PersonalVisit(Manual): pass
        class Mutual(CommunicationMechanism): pass
        class Email(Mutual): pass
        class PostalMail(Mutual): pass
        class PhoneCall(Mutual): pass
        class SMS(Mutual): pass
        class FPSpecific(CommunicationMechanism): pass
        class OnWebsitePage(FPSpecific): pass
        class OnServiceApp(FPSpecific): pass
        class InPrivacyPolicy(FPSpecific): pass

        # Modes
        class Mode(Thing): pass
        class DataTransmissionMode(Mode): pass
        class Permanent(DataTransmissionMode): pass
        class ByRequest(DataTransmissionMode): pass

        # Causes
        class Cause(Thing): pass
        class BreachCause(Cause): pass
        class ForceMajeur(BreachCause): pass
        class Intentional(BreachCause): pass
        class Unintentional(BreachCause): pass
        class PolicyChangeCause(Cause): pass
        class PrivacyRelated(PolicyChangeCause): pass
        class NonPrivacyRelated(PolicyChangeCause): pass
        class MergeAcquisition(PolicyChangeCause): pass

        # Consequences
        class Consequence(Thing): pass
        class BreachConsequence(Consequence): pass
        class RemoveCompromisedInformation(BreachConsequence): pass
        class Compensation(BreachConsequence): pass
        class BreachInvestigation(BreachConsequence): pass
        class PolicyChangeConsequence(Consequence): pass
        class UserChoiceConsequence(Consequence): pass
        class NoServiceRestriction(UserChoiceConsequence): pass
        class PartialServiceRestriction(UserChoiceConsequence): pass
        class FullServiceRestriction(UserChoiceConsequence): pass

        # Purposes
        class Purpose(Thing): pass
        class DataActivityPurpose(Purpose): pass
        class ServiceProvision(DataActivityPurpose): pass
        class HealthMonitoring(ServiceProvision): pass
        class ServiceEnhancement(DataActivityPurpose): pass
        class Analytics(ServiceEnhancement): pass
        class Security(ServiceEnhancement): pass
        class Research(ServiceEnhancement): pass
        class Marketing(ServiceEnhancement): pass

        # Time periods
        class TimePeriod(Thing): pass
        class DataRetentionTime(TimePeriod): pass
        class NotificationTime(TimePeriod): pass
        class BreachInvestigationTime(TimePeriod): pass
        class PolicyAcceptanceTime(TimePeriod): pass

        # Basis
        class Basis(Thing): pass
        class LegalBasis(Basis): pass

        # Policy change scope
        class PolicyChangeScope(Thing): pass

        # User special category
        class UserSpecialCategory(Thing): pass
        class EuropeanResident(UserSpecialCategory): pass
        class CaliforniaResident(UserSpecialCategory): pass
        class RussianFederationResident(UserSpecialCategory): pass
        class Child(UserSpecialCategory): pass

        """
        Object properties
        """
        # Considers
        class considered_by(ObjectProperty): pass
        class considers(ObjectProperty): pass

        # Applies
        class applied_by(ObjectProperty): pass
        class applies_to(ObjectProperty): pass

        # Provides
        class provided_by(ObjectProperty): pass
        class provides(ObjectProperty): pass

        # Activities
        class initiated_by(ObjectProperty): pass
        class initiates(ObjectProperty): pass

        # Mechanisms
        class mechanism_of(ObjectProperty): pass
        class has_mechanism(ObjectProperty): pass

        # Modes
        class is_mode_for(ObjectProperty): pass
        class has_mode(ObjectProperty): pass

        # Durations
        class is_period_of(ObjectProperty): pass
        class lasts_for(ObjectProperty): pass

        # Causes
        class causes(ObjectProperty): pass
        class caused_by(ObjectProperty): pass

        # Consequences
        class is_consequence_of(ObjectProperty): pass
        class has_consequence(ObjectProperty): pass

        # Employes
        class employes(ObjectProperty): pass
        class is_employed(ObjectProperty): pass

        # Purposes
        class is_purpose_for(ObjectProperty): pass
        class has_purpose(ObjectProperty): pass

        # Basis
        class is_basis_for(ObjectProperty): pass
        class has_basis(ObjectProperty): pass

        # Basis
        class is_scope_for(ObjectProperty): pass
        class has_scope(ObjectProperty): pass

        # Basis
        class is_special_category_for(ObjectProperty): pass
        class has_special_category(ObjectProperty): pass

        # Collects
        class collects_from(ObjectProperty): pass
        class is_collected_by(ObjectProperty): pass

        # Shares
        class shares_with(ObjectProperty): pass
        class is_shared_by(ObjectProperty): pass

        # Shares
        class notifies(ObjectProperty): pass
        class notified_by(ObjectProperty): pass

        # Ordering & Navigation
        class following_activity(ObjectProperty, TransitiveProperty): pass
        class followed_by_activity(ObjectProperty, TransitiveProperty): pass
        class next_activity_is(followed_by_activity, IrreflexiveProperty, FunctionalProperty): pass
        class previous_activity_is(following_activity, IrreflexiveProperty, FunctionalProperty): pass
        class binded_to_activity(ObjectProperty, SymmetricProperty, IrreflexiveProperty): pass
        
        class has_older_version(ObjectProperty): pass
        class has_newer_version(ObjectProperty): pass

        """
        Data properties
        """
        class uuid(DataProperty, FunctionalProperty): pass
        class evidence(DataProperty, FunctionalProperty): pass
        class policyId(DataProperty, FunctionalProperty): pass
        class policyUpdate(DataProperty, FunctionalProperty): pass
        class policyWebsite(DataProperty, FunctionalProperty): pass
        class does(DataProperty, FunctionalProperty): pass

        """
        Class disjoints
        """
        AllDisjoint([PrivacyPolicy, Agent, Activity, Data, Basis, Purpose, Mode, 
                     Cause, Consequence, TimePeriod, PolicyChangeScope, UserSpecialCategory])

        AllDisjoint([User, FirstParty, ThirdParty, Criminal, DataProtectionOfficer])

        AllDisjoint([DataActivity, ControlActivity, Notification, Breach])

        AllDisjoint([Use, Protection, FPCollection, TPCollection, TPSharing, Retention])
        AllDisjoint([FPNotification, UserNotification])
        AllDisjoint([DataControl, PolicyChange])
        AllDisjoint([ProvidedDataControl, PrivacyControl, OptControl])

        AllDisjoint([ServiceEnhancement, ServiceProvision])
        AllDisjoint([Analytics, Marketing, Research, Security])

        AllDisjoint([ByRequest, Permanent])

        AllDisjoint([SecurityMechanism, TPSaCMechanism, DataRetentionMechanism, CommunicationMechanism])

        AllDisjoint([OwnServers, EmployedServers])
        AllDisjoint([Contract, ForFree])
        AllDisjoint([TechnicalMeasure, OrganizationalMeasure])
        AllDisjoint([LockedOffice, SecurityTraining, UserMaintain])
        AllDisjoint([Firewall, PseudoAnonymization, AccessControls, Encryption])
        AllDisjoint([SecureTunnel, SecureStorage])

        AllDisjoint([Mutual, UserSpecific, FPSpecific])
        AllDisjoint([InPrivacyPolicy, OnWebsitePage, OnServiceApp])
        AllDisjoint([Email, SMS, PhoneCall, PostalMail])
        AllDisjoint([Manual, Automatic])
        AllDisjoint([ThroughServiceApp, ThroughWebsite])
        AllDisjoint([PersonalVisit, DataProvision, WebsiteForm, ServiceAppForm])

        AllDisjoint([PolicyChangeCause, BreachCause])
        AllDisjoint([ForceMajeur, Unintentional, Intentional])
        AllDisjoint([MergeAcquisition, NonPrivacyRelated, PrivacyRelated])

        AllDisjoint([PolicyChangeConsequence, BreachConsequence, UserChoiceConsequence])
        AllDisjoint([Compensation, RemoveCompromisedInformation, BreachInvestigation])
        AllDisjoint([PartialServiceRestriction, NoServiceRestriction, FullServiceRestriction])

        AllDisjoint([PolicyAcceptanceTime, DataRetentionTime, NotificationTime, BreachInvestigationTime])

        AllDisjoint([PersonalData, NonPersonalData])
        AllDisjoint([SensitiveData, NonSensitiveData])
        AllDisjoint([FinancialData, ApplicationData, DeviceData, AccountData, TrackingData, ServiceData])
        AllDisjoint([GenericData, CrimeData, HealthData, RacialData, BiometricData, ReligionData])
        
        AllDisjoint([EuropeanResident, RussianFederationResident, CaliforniaResident, Child])

        """
        Class restrictions
        """
        DataActivity.is_a.extend([
            Activity & collects_from.only(ThirdParty | FirstParty),
            Activity & applies_to.only(Data)
        ])

        Protection.is_a.extend([
            DataActivity & has_mechanism.only(SecurityMechanism)
        ])

        FPCollection.is_a.extend([
            DataActivity & collects_from.only(User),
            DataActivity & has_mechanism.only(Mutual | UserSpecific),
            DataActivity & has_mode.only(DataTransmissionMode)
        ])

        TPCollection.is_a.extend([
            DataActivity & collects_from.only(ThirdParty),
            DataActivity & has_mechanism.only(TPSaCMechanism),
            DataActivity & has_mode.only(DataTransmissionMode)
        ])

        TPSharing.is_a.extend([
            DataActivity & shares_with.only(ThirdParty),
            DataActivity & has_mechanism.only(TPSaCMechanism),
            DataActivity & has_mode.only(DataTransmissionMode)
        ])

        Retention.is_a.extend([
            DataActivity & initiated_by.only(FirstParty),
            DataActivity & has_mechanism.only(DataRetentionMechanism),
            DataActivity & lasts_for.only(NotificationTime),
        ])

        Notification.is_a.extend([
            Activity & initiated_by.only(User | FirstParty),
            Activity & has_mechanism.only(CommunicationMechanism),
            Activity & lasts_for.only(NotificationTime),
        ])

        FPNotification.is_a.extend([
            Notification & initiated_by.only(FirstParty),
            Notification & notifies.only(User),
            Notification & has_mechanism.only(FPSpecific | Mutual)
        ])

        UserNotification.is_a.extend([
            Notification & initiated_by.only(User),
            Notification & notifies.only(FirstParty),
            Notification & has_mechanism.only(UserSpecific | Mutual)
        ])

        Breach.is_a.extend([
            Activity & initiated_by.only(Criminal),
            Activity & applies_to.only(Data)
        ])

        ControlActivity.is_a.extend([
            Activity & initiated_by.only(FirstParty | User),
        ])

        PolicyChange.is_a.extend([
            ControlActivity & initiated_by.only(FirstParty),
            ControlActivity & lasts_for.only(PolicyAcceptanceTime),
            ControlActivity & has_scope.only(PolicyChangeScope),
        ])

        DataControl.is_a.extend([
            ControlActivity & initiated_by.only(User),
            ControlActivity & has_mechanism.only(UserSpecific | Mutual),
            ControlActivity & applies_to.only(Data),
        ])

        ProvidedDataControl.is_a.extend([
            DataControl & initiated_by.only(User)
        ])

        PrivacyControl.is_a.extend([
            DataControl & initiated_by.only(User)
        ])

        OptControl.is_a.extend([
            DataControl & initiated_by.only(User)
        ])

        # Agents
        FirstParty.is_a.extend([
            Agent & initiates.only(FPNotification | PolicyChange | DataActivity) 
        ])

        ThirdParty.is_a.extend([
            Agent & is_collected_by.only(TPCollection),
            Agent & is_shared_by.only(TPSharing)
        ])

        DataProtectionOfficer.is_a.extend([
            Agent & is_employed.only(BreachInvestigation)
        ])

        Criminal.is_a.extend([
            Agent & initiates.only(Breach)
        ])

        User.is_a.extend([
            Agent & initiates.only(UserNotification | DataControl),
            Agent & is_collected_by.only(FPCollection),
            Agent & provides.only(Data)
        ])

        # Mechanisms
        DataRetentionMechanism.is_a.extend([
            Mechanism & mechanism_of.only(Retention)
        ])

        SecurityMechanism.is_a.extend([
            Mechanism & mechanism_of.only(Protection),
        ])

        CommunicationMechanism.is_a.extend([
            Mechanism & initiated_by.only(FirstParty | User),
            Mechanism & mechanism_of.only(Notification | FPCollection | DataControl)
        ])

        UserSpecific.is_a.extend([
            CommunicationMechanism & mechanism_of.only(UserNotification | DataControl)
        ])

        FPSpecific.is_a.extend([
            CommunicationMechanism & mechanism_of.only(FPNotification)
        ])

        # Modes
        DataTransmissionMode.is_a.extend([
            Mode & is_mode_for.only(FPCollection | TPCollection | TPSharing)
        ])

        # Causes
        BreachCause.is_a.extend([
            Cause & causes.only(Breach)
        ])

        PolicyChangeCause.is_a.extend([
            Cause & causes.only(PolicyChange)
        ])

        # Consequences
        BreachConsequence.is_a.extend([
            Consequence & is_consequence_of.only(Breach)
        ])

        BreachInvestigation.is_a.extend([
            BreachConsequence & lasts_for.only(BreachInvestigationTime),
            BreachConsequence & employes.only(DataProtectionOfficer),
        ])

        PolicyChangeConsequence.is_a.extend([
            Consequence & is_consequence_of.only(PolicyChange)
        ])

        UserChoiceConsequence.is_a.extend([
            Consequence & is_consequence_of.only(DataControl)
        ])

        # Purposes
        DataActivityPurpose.is_a.extend([
            Purpose & is_purpose_for.only(DataActivity)
        ])

        # Time periods
        DataRetentionTime.is_a.extend([
            TimePeriod & is_period_of.only(Retention)
        ])

        NotificationTime.is_a.extend([
            TimePeriod & is_period_of.only(Notification)
        ])

        BreachInvestigationTime.is_a.extend([
            TimePeriod & is_period_of.only(BreachInvestigation)
        ])

        PolicyAcceptanceTime.is_a.extend([
            TimePeriod & is_period_of.only(PolicyChange)
        ])

        # Basis
        LegalBasis.is_a.extend([
            Basis & is_basis_for.only(DataActivity)
        ])

        """
        Object properties restrictions
        """
        considers.domain = [PrivacyPolicy]
        considers.range = [Agent | Activity | Data]
        considers.inverse_property = considered_by

        applies_to.domain = [DataActivity | Breach | DataControl]
        applies_to.range = [Data]
        applies_to.inverse_property = applied_by

        provides.domain = [Agent]
        provides.range = [Data]
        provides.inverse_property = provided_by

        initiates.domain = [Agent]
        initiates.range = [Activity]
        initiates.inverse_property = initiated_by

        has_mechanism.domain = [Activity]
        has_mechanism.range = [Mechanism]
        has_mechanism.inverse_property = mechanism_of

        collects_from.domain = [TPCollection]
        collects_from.range = [User | ThirdParty]
        collects_from.inverse_property = is_collected_by

        shares_with.domain = [Activity]
        shares_with.range = [ThirdParty]
        shares_with.inverse_property = is_shared_by

        notifies.domain = [Activity]
        notifies.range = [Agent]
        notifies.inverse_property = notified_by

        employes.domain = [BreachInvestigation]
        employes.range = [DataProtectionOfficer]
        employes.inverse_property = is_employed

        has_mode.domain = [Activity]
        has_mode.range = [Mode]
        has_mode.inverse_property = is_mode_for

        lasts_for.domain = [Activity, BreachInvestigation]
        lasts_for.range = [TimePeriod]
        lasts_for.inverse_property = is_period_of

        causes.domain = [Cause]
        causes.range = [Activity]
        causes.inverse_property = caused_by

        has_consequence.domain = [Activity]
        has_consequence.range = [Consequence]
        has_consequence.inverse_property = is_consequence_of

        has_purpose.domain = [DataActivity]
        has_purpose.range = [Purpose]
        has_purpose.inverse_property = is_purpose_for

        has_scope.domain = [PolicyChange]
        has_scope.range = [PolicyChangeScope]
        has_scope.inverse_property = is_scope_for

        has_special_category.domain = [User]
        has_special_category.range = [UserSpecialCategory]
        has_special_category.inverse_property = is_special_category_for

        has_basis.domain = [DataActivity]
        has_basis.range = [Basis]
        has_basis.inverse_property = is_basis_for

        binded_to_activity.domain = [Activity]
        binded_to_activity.range = [Activity]

        followed_by_activity.domain = [Activity]
        followed_by_activity.range = [Activity]
        followed_by_activity.inverse_property = following_activity

        next_activity_is.inverse = previous_activity_is

        has_older_version.domain = [PrivacyPolicy]
        has_older_version.range = [PrivacyPolicy]
        has_older_version.inverse_property = has_newer_version

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

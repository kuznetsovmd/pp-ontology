from owlready2 import *


def construct(onto):
    with onto:
        class PrivacyPolicy(Thing): pass

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

        class Agent(Thing): pass
        class User(Agent): pass
        class FirstParty(Agent): pass
        class ThirdParty(Agent): pass
        class Criminal(Agent): pass

        class Data(Thing): pass
        class PersonalData(Data): pass
        class NonPersonalData(Data): pass
        class ServiceData(PersonalData): pass
        class NonSensitiveData(PersonalData): pass
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
        class SucurityTraining(OrganizationalMeasure): pass
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

        class Mode(Thing): pass
        class DataTransmissionMode(Mode): pass
        class Permanent(DataTransmissionMode): pass
        class ByRequest(DataTransmissionMode): pass

        class Cause(Thing): pass
        class BreachCause(Cause): pass
        class ForceMajeur(BreachCause): pass
        class Intentional(BreachCause): pass
        class Unintentional(BreachCause): pass
        class PolicyChangeCause(Cause): pass
        class PrivacyRelated(PolicyChangeCause): pass
        class NonPrivacyRelated(PolicyChangeCause): pass
        class MergeAcquisition(PolicyChangeCause): pass

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

        class Purpose(Thing): pass
        class DataActivityPurpose(Purpose): pass
        class ServiceProvision(DataActivityPurpose): pass
        class HealthMonitoring(ServiceProvision): pass
        class ServiceEnhancement(DataActivityPurpose): pass
        class Analytics(ServiceEnhancement): pass
        class Security(ServiceEnhancement): pass
        class Research(ServiceEnhancement): pass
        class Marketing(ServiceEnhancement): pass

        class TimePeriod(Thing): pass
        class DataRetentionTime(TimePeriod): pass
        class NotificationTime(TimePeriod): pass
        class BreachInvestigationTime(TimePeriod): pass
        class PolicyAcceptanceTime(TimePeriod): pass

        class Basis(Thing): pass
        class LegalBasis(Basis): pass

        class PolicyChangeScope(Thing): pass

        class UserSpecialCategory(Thing): pass
        class EuropeanResident(UserSpecialCategory): pass
        class CaliforniaResident(UserSpecialCategory): pass
        class RussianFederationResident(UserSpecialCategory): pass
        class Child(UserSpecialCategory): pass

        # Object properties
        class considered_by(ObjectProperty): pass
        class considers(ObjectProperty): pass
        class data_considered_by(considered_by): pass
        class considers_data(considers): pass
        class activity_considered_by(considered_by): pass
        class considers_activity(considers): pass
        class agent_considered_by(considered_by): pass
        class considers_agent(considers): pass
        class applied_by(ObjectProperty): pass
        class applies_to(ObjectProperty): pass
        class provided_by(ObjectProperty): pass
        class provides(ObjectProperty): pass
        class initiated_by(ObjectProperty): pass
        class initiates(ObjectProperty): pass
        class notification_initiated_by(initiated_by): pass
        class initiates_notification(initiates): pass
        class fp_notification_initiated_by(notification_initiated_by): pass
        class initiates_fp_notification(initiates_notification): pass
        class user_notification_initiated_by(notification_initiated_by): pass
        class initiates_user_notification(initiates_notification): pass
        class mechanism_of(ObjectProperty): pass
        class has_mechanism(ObjectProperty): pass
        class retention_mechanism_of(mechanism_of): pass
        class has_retention_mechanism(has_mechanism): pass
        class communication_mechanism_of(mechanism_of): pass
        class has_communication_mechanism(has_mechanism): pass
        class fp_notification_mechanism_of(communication_mechanism_of): pass
        class has_fp_notification_mechanism(has_communication_mechanism): pass
        class user_notification_mechanism_of(communication_mechanism_of): pass
        class has_user_notification_mechanism(has_communication_mechanism): pass
        class data_control_mechanism_of(mechanism_of): pass
        class has_data_control_mechanism(has_mechanism): pass
        class is_mode_for(ObjectProperty): pass
        class has_mode(ObjectProperty): pass
        class is_last_of(ObjectProperty): pass
        class lasts_for(ObjectProperty): pass
        class causes(ObjectProperty): pass
        class caused_by(ObjectProperty): pass
        class is_consequence_of(ObjectProperty): pass
        class has_consequence(ObjectProperty): pass
        class is_purpose_for(ObjectProperty): pass
        class has_purpose(ObjectProperty): pass
        class is_basis_for(ObjectProperty): pass
        class has_basis(ObjectProperty): pass

        class following_activity(ObjectProperty, TransitiveProperty): pass
        class followed_by_activity(ObjectProperty, TransitiveProperty): pass
        class next_activity_is(followed_by_activity, IrreflexiveProperty, FunctionalProperty): pass
        class previous_activity_is(following_activity, IrreflexiveProperty, FunctionalProperty): pass
        class binded_to_activity(ObjectProperty, SymmetricProperty, IrreflexiveProperty): pass

        # Data properties
        class uuid(DataProperty, FunctionalProperty): pass
        class evidence(DataProperty, FunctionalProperty): pass
        class policyId(DataProperty, FunctionalProperty): pass
        class policyUpdate(DataProperty, FunctionalProperty): pass
        class policyWebsite(DataProperty, FunctionalProperty): pass
        class does(DataProperty, FunctionalProperty): pass

        # Class restrictions
        AllDisjoint([User, FirstParty, ThirdParty, Criminal])
        AllDisjoint([SecurityMechanism, TPSaCMechanism, DataRetentionMechanism, CommunicationMechanism])
        AllDisjoint([Mutual, UserSpecific, FPSpecific])

        CommunicationMechanism.equivalent_to = [
            Mechanism 
            & (
                mechanism_of.only(Notification) 
                | mechanism_of.only(FPCollection) 
                | mechanism_of.only(DataControl)
            )
        ]

        Retention.equivalent_to = [
            DataActivity
                & initiated_by.only(FirstParty) 
                & has_mechanism.only(DataRetentionMechanism) 
        ]

        DataRetentionMechanism.equivalent_to = [
            Mechanism
                & mechanism_of.only(Retention)
        ]

        CommunicationMechanism.equivalent_to = [
            Mechanism 
            & (
                mechanism_of.only(Notification) 
                | mechanism_of.only(FPCollection) 
                | mechanism_of.only(DataControl)
            )
        ]

        DataControl.equivalent_to = [
            Activity & initiated_by.only(User)
        ]

        FPNotification.equivalent_to = [
            Notification 
                & initiated_by.only(FirstParty) 
                & (
                    has_mechanism.only(FPSpecific) 
                    | has_mechanism.only(Mutual)
                )
        ]

        UserNotification.equivalent_to = [
            Notification & initiated_by.only(User)
        ]

        # Object properties restrictions
        considers.domain = [PrivacyPolicy]
        considers.range = [Agent | Activity | Data]
        considers.inverse_property = considered_by

        considers_data.domain = [PrivacyPolicy]
        considers_data.range = [Data]
        considers_data.inverse_property = data_considered_by

        considers_activity.domain = [PrivacyPolicy]
        considers_activity.range = [Activity]
        considers_activity.inverse_property = activity_considered_by

        considers_agent.domain = [PrivacyPolicy]
        considers_agent.range = [Agent]
        considers_agent.inverse_property = agent_considered_by

        applies_to.domain = [Activity]
        applies_to.range = [Data]
        applies_to.inverse_property = applied_by

        provides.domain = [Agent]
        provides.range = [Data]
        provides.inverse_property = provided_by

        initiates.domain = [Agent]
        initiates.range = [Activity]
        initiates.inverse_property = initiated_by

        initiates_notification.domain = [Agent]
        initiates_notification.range = [Notification]
        initiates_notification.inverse_property = notification_initiated_by

        initiates_fp_notification.domain = [FirstParty]
        initiates_fp_notification.range = [FPNotification]
        initiates_fp_notification.inverse_property = fp_notification_initiated_by

        initiates_user_notification.domain = [User]
        initiates_user_notification.range = [UserNotification]
        initiates_user_notification.inverse_property = user_notification_initiated_by

        has_mechanism.domain = [Activity]
        has_mechanism.range = [Mechanism]
        has_mechanism.inverse_property = mechanism_of

        has_retention_mechanism.domain = [Retention]
        has_retention_mechanism.range = [DataRetentionMechanism]
        has_retention_mechanism.inverse_property = retention_mechanism_of

        has_communication_mechanism.domain = [Notification]
        has_communication_mechanism.range = [CommunicationMechanism]
        has_communication_mechanism.inverse_property = communication_mechanism_of

        has_fp_notification_mechanism.domain = [FPNotification]
        has_fp_notification_mechanism.range = [FPSpecific | Mutual]
        has_fp_notification_mechanism.inverse_property = fp_notification_mechanism_of

        has_user_notification_mechanism.domain = [UserNotification]
        has_user_notification_mechanism.range = [UserSpecific | Mutual]
        has_user_notification_mechanism.inverse_property = user_notification_mechanism_of

        has_data_control_mechanism.domain = [DataControl]
        has_data_control_mechanism.range = [Mutual | Manual]
        has_data_control_mechanism.inverse_property = data_control_mechanism_of

        has_mode.domain = [Activity]
        has_mode.range = [Mode]
        has_mode.inverse_property = is_mode_for

        lasts_for.domain = [Activity]
        lasts_for.range = [TimePeriod]
        lasts_for.inverse_property = is_last_of

        causes.domain = [Cause]
        causes.range = [Activity]
        causes.inverse_property = caused_by

        has_consequence.domain = [Activity]
        has_consequence.range = [Consequence]
        has_consequence.inverse_property = is_consequence_of

        has_purpose.domain = [DataActivity]
        has_purpose.range = [Purpose]
        has_purpose.inverse_property = is_purpose_for

        has_basis.domain = [DataActivity]
        has_basis.range = [Basis]
        has_basis.inverse_property = is_basis_for

        binded_to_activity.domain = [Activity]
        binded_to_activity.range = [Activity]

        followed_by_activity.domain = [Activity]
        followed_by_activity.range = [Activity]
        followed_by_activity.inverse_property = following_activity

        next_activity_is.inverse = previous_activity_is

        # Data properties restrictions
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

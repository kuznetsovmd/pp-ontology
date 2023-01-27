from owlready2 import *

from config import ontologies


_ID = 0


def construct_ontology(name=None):

    if not name:
        global _ID
        name = _ID
        _ID += 1

    onto_path.append(f"{os.path.abspath(ontologies)}")
    onto = get_ontology(
         f"http://test.org/iot-ontology-{name}.owl")

    # onto = get_ontology(
    #      f"file://{os.path.abspath(ontologies)}/iot-ontology-{name}.owl")

    with onto:
        # Core
        class PrivacyPolicy(Thing): pass

        # Activities
        class Activity(Thing): pass

        class BreachNotificationActivity(Activity): pass

        class ControlActivity(Activity): pass

        class PolicyChangeActivity(ControlActivity): pass

        class ReportBreachActivity(ControlActivity): pass

        class ConsentActivity(ControlActivity): pass

        class GiveConsentActivity(ConsentActivity): pass

        class WithdrawConsentActivity(ConsentActivity): pass

        class DataControlActivity(ControlActivity): pass

        class UserAccessActivity(DataControlActivity): pass

        class UserPrivacyControl(DataControlActivity): pass

        class UserOptControl(DataControlActivity): pass

        class DataActivity(Activity): pass

        class DataUseActivity(DataActivity): pass

        class DataCollectionActivity(DataActivity): pass

        class DataSharingActivity(DataActivity): pass

        class DataRetentionActivity(DataActivity): pass

        # Agents
        class Agent(Thing): pass

        class User(Agent): pass

        class FirstParty(Agent): pass

        class DataProtectionOfficer(Agent): pass

        class ThirdParties(Agent): pass

        # Data
        class Data(Thing): pass

        class PersonalData(Data): pass

        class NonPersonalData(Data): pass

        class ServiceData(PersonalData): pass

        class SensitiveData(PersonalData): pass

        class NonSensitiveData(PersonalData): pass

        class FinancialData(NonSensitiveData): pass

        class DeviceData(NonSensitiveData): pass

        class AppData(NonSensitiveData): pass

        class AccountData(NonSensitiveData): pass

        class TrackingData(NonSensitiveData): pass

        class ReligionData(SensitiveData): pass

        class RacialData(SensitiveData): pass

        class HealthData(SensitiveData): pass

        class GenericData(SensitiveData): pass

        class CrimeData(SensitiveData): pass

        class BiometricData(SensitiveData): pass

        # Causes
        class Cause(Thing): pass

        class BreachCause(Cause): pass

        class ForceMajeur(BreachCause): pass

        class IntentionalCause(BreachCause): pass

        class UnintentionalCause(BreachCause): pass

        class PolicyChangeCause(Cause): pass

        class PrivacyRelatedCause(PolicyChangeCause): pass

        class NonPrivacyRelatedCause(PolicyChangeCause): pass

        class MergeAcquisitionCause(PolicyChangeCause): pass

        class OtherPolicyChangeCause(PolicyChangeCause): pass

        # Consequences
        class Consequence(Thing): pass

        # class BreachConsequence(Consequence): pass
        #
        # class RemoveCompromisedInformation(BreachConsequence): pass
        #
        # class Compensation(BreachConsequence): pass
        #
        # class BreachInvestigation(BreachConsequence): pass

        class PolicyChangeConsequence(Consequence): pass

        class UserChoiceConsequence(Consequence): pass

        class NoServiceRestriction(UserChoiceConsequence): pass

        class PartialServiceRestriction(UserChoiceConsequence): pass

        class FullServiceRestriction(UserChoiceConsequence): pass

        # Mechanisms
        class Mechanism(Thing): pass

        class NotificationMechanism(Mechanism): pass

        class OnWebsitePage(NotificationMechanism): pass

        class ViaPostalMail(NotificationMechanism): pass

        class ViaSMS(NotificationMechanism): pass

        class OnService(NotificationMechanism): pass

        class ViaPhoneCall(NotificationMechanism): pass

        class InPrivacyPolicy(NotificationMechanism): pass

        class ViaEmail(NotificationMechanism): pass

        class DataRetentionMechanism(Mechanism): pass

        class DataSharingMechanism(Mechanism): pass

        class DataCollectionMechanism(Mechanism): pass

        class DataControlMechanism(Mechanism): pass

        class DataActivityForm(DataControlMechanism): pass

        class SecurityMechanism(Mechanism): pass

        class TechnicalMeasure(SecurityMechanism): pass

        class PseudoAnonymization(TechnicalMeasure): pass

        class Encryption(TechnicalMeasure): pass

        class OrganizationalMeasure(SecurityMechanism): pass

        # Mechanism procedures
        class MechanismProcedure(Thing): pass

        class DataCollectionProcedure(MechanismProcedure): pass

        class DataSharingProcedure(MechanismProcedure): pass

        class PolicyChangeNotificationProcedure(MechanismProcedure): pass

        # Mechanism modes
        class MechanismMode(Thing): pass

        class DataSharingMode(MechanismMode): pass

        class DataCollectionMode(MechanismMode): pass

        # Time periods
        class TimePeriod(Thing): pass

        class DataRetentionTime(TimePeriod): pass

        class BreachReportTime(TimePeriod): pass

        # class BreachInvestigationTime(TimePeriod): pass

        class PolicyAcceptanceTime(TimePeriod): pass

        class BreachNotificationTime(TimePeriod): pass

        # Purposes
        class Purpose(Thing): pass

        class DataActivityPurpose(Purpose): pass

        class HealthMonitoring(DataActivityPurpose): pass

        # Basis
        class Basis(Thing): pass

        class LegalBasis(Basis): pass

        # Policy change scope
        class PolicyChangeScope(Thing): pass

        # Evidence
        class Evidence(Thing): pass

        # User special category
        class UserSpecialCategory(Thing): pass

        # Object properties
        # Considers
        class considers(ObjectProperty): pass
        class isConsideredBy(ObjectProperty):
            inverse_property = considers

        # Considers agents
        class agentIsConsideredBy(isConsideredBy): pass
        class considersAgent(considers):
            domain = [PrivacyPolicy]
            range = [Agent]
            inverse_property = agentIsConsideredBy

        # Considers activities
        class activityIsConsideredBy(isConsideredBy): pass
        class considersActivity(considers):
            domain = [PrivacyPolicy]
            range = [Activity]
            inverse_property = activityIsConsideredBy

        # Considers data
        class dataIsConsideredBy(isConsideredBy): pass
        class considersData(considers):
            domain = [PrivacyPolicy]
            range = [Data]
            inverse_property = dataIsConsideredBy

        # Applies
        class isAppliedTo(ObjectProperty): pass
        class isInfluencedBy(ObjectProperty):
            inverse_property = isAppliedTo

        class isInfluencedByActivity(isInfluencedBy): pass
        class isAppliedToData(isAppliedTo):
            domain = [Activity]
            range = [Data]
            inverse_property = isInfluencedByActivity

        # Has
        class has(ObjectProperty): pass
        class isRelatedTo(ObjectProperty):
            inverse_property = has

        class breachCauseIsRelatedTo(isRelatedTo): pass
        class hasBreachCause(has):
            domain = [BreachNotificationActivity]
            range = [BreachCause]
            inverse_property = breachCauseIsRelatedTo

        # class consequenceIsRelatedTo(isRelatedTo): pass
        # class hasBreachConsequence(has):
        #     domain = [BreachActivity]
        #     range = [BreachConsequence]
        #     inverse_property = consequenceIsRelatedTo

        class userChoiceConsequenceIsRelatedTo(isRelatedTo): pass
        class hasUserChoiceConsequence(has):
            domain = [ConsentActivity]
            range = [UserChoiceConsequence]
            inverse_property = userChoiceConsequenceIsRelatedTo

        # class breachInvestigationTimeIsRelatedTo(isRelatedTo): pass
        # class hasBreachInvestigationTime(has):
        #     domain = [BreachInvestigation]
        #     range = [BreachInvestigationTime]
        #     inverse_property = breachInvestigationTimeIsRelatedTo

        class breachNotificationTimeIsRelatedTo(isRelatedTo): pass
        class hasBreachNotificationTime(has):
            domain = [BreachNotificationActivity]
            range = [BreachNotificationTime]
            inverse_property = breachNotificationTimeIsRelatedTo

        class hasBreachReportTime(isRelatedTo): pass
        class breachReportTimeIsRelatedTo(has):
            domain = [ReportBreachActivity]
            range = [BreachReportTime]
            inverse_property = hasBreachReportTime

        class dataActivityPurposeIsRelatedTo(isRelatedTo): pass
        class hasDataActivityPurpose(has):
            domain = [Activity]
            range = [DataActivityPurpose]
            inverse_property = dataActivityPurposeIsRelatedTo

        class dataRetentionTimeIsRelatedTo(isRelatedTo): pass
        class hasDataRetentionTime(has):
            domain = [DataRetentionActivity]
            range = [DataRetentionTime]
            inverse_property = dataRetentionTimeIsRelatedTo

        class hasNewerVersion(has, FunctionalProperty): pass
        class hasOlderVersion(has, FunctionalProperty):
            domain = [PrivacyPolicy]
            range = [PrivacyPolicy]
            inverse_property = hasNewerVersion

        class evidenceIsRelatedTo(isRelatedTo): pass
        class hasEvidence(has):
            domain = [Thing]
            range = [Evidence]
            inverse_property = evidenceIsRelatedTo

        class legalBasisIsRelatedTo(isRelatedTo): pass
        class hasLegalBasis(has):
            domain = [DataActivity]
            range = [LegalBasis]
            inverse_property = legalBasisIsRelatedTo

        class mechanismIsRelatedTo(isRelatedTo): pass
        class hasMechanism(has):
            domain = [Activity]
            range = [Mechanism]
            inverse_property = mechanismIsRelatedTo

        class privacyControlMechanismIsRelatedTo(mechanismIsRelatedTo): pass
        class hasPrivacyControlMechanism(hasMechanism):
            domain = [UserPrivacyControl]
            range = [DataControlMechanism]
            inverse_property = privacyControlMechanismIsRelatedTo

        class notificationMechanismIsRelatedTo(mechanismIsRelatedTo): pass
        class hasNotificationMechanism(hasMechanism):
            domain = [BreachNotificationActivity, PolicyChangeActivity]
            range = [NotificationMechanism]
            inverse_property = notificationMechanismIsRelatedTo

        class securityMechanismIsRelatedTo(mechanismIsRelatedTo): pass
        class hasSecurityMechanism(hasMechanism):
            domain = [Activity]
            range = [SecurityMechanism]
            inverse_property = securityMechanismIsRelatedTo

        class dataCollectionMechanismIsRelatedTo(mechanismIsRelatedTo): pass
        class hasDataCollectionMechanism(hasMechanism):
            domain = [DataCollectionActivity]
            range = [DataCollectionMechanism]
            inverse_property = dataCollectionMechanismIsRelatedTo

        class modeIsRelatedTo(isRelatedTo): pass
        class hasMode(has):
            domain = [Mechanism]
            range = [MechanismMode]
            inverse_property = modeIsRelatedTo

        class dataCollectionModeIsRelatedTo(modeIsRelatedTo): pass
        class hasDataCollectionMode(hasMode):
            domain = [DataCollectionMechanism]
            range = [DataCollectionMode]
            inverse_property = dataCollectionModeIsRelatedTo

        class policyAcceptanceTimeIsRelatedTo(isRelatedTo): pass
        class hasPolicyAcceptanceTime(has):
            domain = [PolicyChangeActivity]
            range = [PolicyAcceptanceTime]
            inverse_property = policyAcceptanceTimeIsRelatedTo

        class policyChangeScopeIsRelatedTo(isRelatedTo): pass
        class hasPolicyChangeScope(has):
            domain = [PolicyChangeActivity]
            range = [PolicyChangeScope]
            inverse_property = policyChangeScopeIsRelatedTo

        class policyChangeCauseIsRelatedTo(isRelatedTo): pass
        class hasPolicyChangeCause(has):
            domain = [PolicyChangeActivity]
            range = [PolicyChangeCause]
            inverse_property = policyChangeCauseIsRelatedTo

        class policyChangeConsequenceIsRelatedTo(isRelatedTo): pass
        class hasPolicyChangeConsequence(has):
            domain = [PolicyChangeActivity]
            range = [PolicyChangeConsequence]
            inverse_property = policyChangeConsequenceIsRelatedTo

        class procedureIsRelatedTo(isRelatedTo): pass
        class hasProcedure(has):
            domain = [Mechanism]
            range = [MechanismProcedure]
            inverse_property = procedureIsRelatedTo

        class specialCategoryIsRelatedTo(isRelatedTo): pass
        class hasSpecialCategory(has):
            domain = [User]
            range = [UserSpecialCategory]
            inverse_property = specialCategoryIsRelatedTo

        # Initiates
        class initiates(ObjectProperty): pass
        class isInitiatedBy(ObjectProperty):
            inverse_property = initiates

        class activityIsInitiatedBy(isInitiatedBy): pass
        class initiatesActivity(initiates):
            domain = [Agent]
            range = [Activity]
            inverse_property = activityIsInitiatedBy

        # Notifies
        class notifies(ObjectProperty): pass
        class isNotifiedBy(ObjectProperty):
            inverse_property = notifies

        class agentIsNotifiedBy(isNotifiedBy): pass
        class notifiesAgent(notifies):
            domain = [ReportBreachActivity]
            range = [Agent]
            inverse_property = agentIsNotifiedBy

        # Provides
        class provides(ObjectProperty): pass
        class isProvidedBy(ObjectProperty):
            inverse_property = provides

        class dataIsProvidedBy(isProvidedBy): pass
        class providesData(provides):
            domain = [Agent]
            range = [Data]
            inverse_property = dataIsProvidedBy

        # Collects
        class collects(ObjectProperty): pass
        class isCollected(ObjectProperty):
            inverse_property = collects

        class isCollectedByActivity(isCollected): pass
        class collectsDataFromAgent(collects):
            domain = [DataCollectionActivity]
            range = [Agent]
            inverse_property = isCollectedByActivity

        # Shares
        class shares(ObjectProperty): pass
        class isShared(ObjectProperty):
            inverse_property = shares

        class isSharedByActivity(isShared): pass
        class sharesDataWithAgent(shares):
            domain = [DataSharingActivity]
            range = [Agent]
            inverse_property = isSharedByActivity

        # Data properties
        class evidenceContent(DataProperty, FunctionalProperty):
            domain = [Evidence]
            range = [str]

        class policyId(DataProperty, FunctionalProperty):
            domain = [PrivacyPolicy]
            range = [int]

        class policyUpdate(DataProperty, FunctionalProperty):
            domain = [PrivacyPolicy]
            range = [str]

        class policyWebsite(DataProperty, FunctionalProperty):
            domain = [PrivacyPolicy]
            range = [str]

        AllDisjoint([DataActivityPurpose, DataCollectionMechanism])

    return onto


def finish(o, reason=True):

    if reason:
        sync_reasoner(infer_property_values=True)

    o.save()

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
        class Breach(Activity): ...
        class DataActivity(Activity): ...
        class PolicyChange(DataActivity): ...
        class Use(DataActivity): ...
        class Protection(DataActivity): ...
        class FPCollection(DataActivity): ...
        class TPCollection(DataActivity): ...
        class TPSharing(DataActivity): ...
        class Retention(DataActivity): ...
        class Notification(Activity): ...
        class FPNotification(Notification): ...
        class UserNotification(Notification): ...
        class DataControl(Activity): ...
        class ProvidedDataControl(DataControl): ...
        class PrivacyControl(DataControl): ...
        class OptControl(DataControl): ...

        # Agents
        class Agent(Thing): ...
        class User(Agent): ...
        class FirstParty(Agent): ...
        class ThirdParty(Agent): ...
        class Criminal(Agent): ...

        # Data
        class Data(Thing): ...
        class PersonalData(Data): ...
        class NonPersonalData(Data): ...
        class NonSensitiveData(PersonalData): ...
        class ServiceData(NonSensitiveData): ...
        class FinancialData(NonSensitiveData): ...
        class DeviceData(NonSensitiveData): ...
        class ApplicationData(NonSensitiveData): ...
        class AccountData(NonSensitiveData): ...
        class TrackingData(NonSensitiveData): ...
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
        class OwnServers(DataRetentionMechanism): ...
        class EmployedServers(DataRetentionMechanism): ...
        class TPSaCMechanism(Mechanism): ...
        class Contract(TPSaCMechanism): ...
        class ForFree(TPSaCMechanism): ...
        class SecurityMechanism(Mechanism): ...
        class TechnicalMeasure(SecurityMechanism): ...
        class PseudoAnonymization(TechnicalMeasure): ...
        class Encryption(TechnicalMeasure): ...
        class SecureStorage(Encryption): ...
        class SecureTunnel(Encryption): ...
        class Firewall(TechnicalMeasure): ...
        class AccessControls(TechnicalMeasure): ...
        class OrganizationalMeasure(SecurityMechanism): ...
        class LockedOffice(OrganizationalMeasure): ...
        class SecurityTraining(OrganizationalMeasure): ...
        class UserMaintain(OrganizationalMeasure): ...
        class CommunicationMechanism(Mechanism): ...
        class UserSpecific(CommunicationMechanism): ...
        class Automatic(UserSpecific): ...
        class ThroughServiceApp(Automatic): ...
        class ThroughWebsite(Automatic): ...
        class Manual(UserSpecific): ...
        class WebsiteForm(Manual): ...
        class ServiceAppForm(Manual): ...
        class DataProvision(Manual): ...
        class PersonalVisit(Manual): ...
        class Mutual(CommunicationMechanism): ...
        class Email(Mutual): ...
        class PostalMail(Mutual): ...
        class PhoneCall(Mutual): ...
        class SMS(Mutual): ...
        class FPSpecific(CommunicationMechanism): ...
        class OnWebsitePage(FPSpecific): ...
        class OnServiceApp(FPSpecific): ...
        class InPrivacyPolicy(FPSpecific): ...

        # Modes
        class Mode(Thing): ...
        class DataTransmissionMode(Mode): ...
        class Permanent(DataTransmissionMode): ...
        class ByRequest(DataTransmissionMode): ...

        # Causes
        class Cause(Thing): ...
        class BreachCause(Cause): ...
        class ForceMajeur(BreachCause): ...
        class Intentional(BreachCause): ...
        class Unintentional(BreachCause): ...
        class PolicyChangeCause(Cause): ...
        class PrivacyRelated(PolicyChangeCause): ...
        class NonPrivacyRelated(PolicyChangeCause): ...
        class MergeAcquisition(PolicyChangeCause): ...

        # Consequences
        class Consequence(Thing): ...
        class BreachConsequence(Consequence): ...
        class RemoveCompromisedInformation(BreachConsequence): ...
        class Compensation(BreachConsequence): ...
        class BreachInvestigation(BreachConsequence): ...
        class PolicyChangeConsequence(Consequence): ...
        class UserChoiceConsequence(Consequence): ...
        class NoServiceRestriction(UserChoiceConsequence): ...
        class PartialServiceRestriction(UserChoiceConsequence): ...
        class FullServiceRestriction(UserChoiceConsequence): ...

        # Purposes
        class Purpose(Thing): ...
        class DataActivityPurpose(Purpose): ...
        class LegalCompliance(DataActivityPurpose): ...
        class ServiceProvision(DataActivityPurpose): ...
        class HealthMonitoring(ServiceProvision): ...
        class ServiceEnhancement(DataActivityPurpose): ...
        class Analytics(ServiceEnhancement): ...
        class Security(ServiceEnhancement): ...
        class Research(ServiceEnhancement): ...
        class Marketing(ServiceEnhancement): ...

        # Time periods
        class TimePeriod(Thing): ...
        class DataRetentionTime(TimePeriod): ...
        class NotificationTime(TimePeriod): ...
        class BreachInvestigationTime(TimePeriod): ...
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
        class Child(UserSpecialCategory): ...

        """
        Class disjoints

        Make classes of same level different (involves subclasses)
        """
        AllDisjoint([PrivacyPolicy, Agent, Activity, Data, Basis, Purpose, Mode, 
                     Cause, Consequence, TimePeriod, PolicyChangeScope, UserSpecialCategory])

        AllDisjoint([User, FirstParty, ThirdParty, Criminal])

        AllDisjoint([Breach, DataActivity, DataControl, Notification])

        AllDisjoint([Use, Protection, FPCollection, TPCollection, TPSharing, Retention, PolicyChange])
        AllDisjoint([FPNotification, UserNotification])
        AllDisjoint([DataControl, PolicyChange])
        AllDisjoint([ProvidedDataControl, PrivacyControl, OptControl])

        AllDisjoint([LegalCompliance, ServiceEnhancement, ServiceProvision])
        AllDisjoint([Analytics, Marketing, Research, Security])

        AllDisjoint([ByRequest, Permanent])

        AllDisjoint([SecurityMechanism, TPSaCMechanism, DataRetentionMechanism, CommunicationMechanism])

        AllDisjoint([OwnServers, EmployedServers])
        AllDisjoint([Contract, ForFree])
        AllDisjoint([TechnicalMeasure, OrganizationalMeasure])
        AllDisjoint([LockedOffice, SecurityTraining, UserMaintain])
        AllDisjoint([Firewall, PseudoAnonymization, AccessControls, Encryption])
        AllDisjoint([SecureTunnel, SecureStorage])

        AllDisjoint([UserSpecific, FPSpecific])

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

        Breach.is_a.extend([
            initiated_by.only(Criminal)
            & applies_to.only(Data)
            & caused_by.only(BreachCause)
            & has_consequence.only(BreachConsequence)
        ])

        DataActivity.is_a.extend([
            initiated_by.only(FirstParty)
            & has_purpose.only(DataActivityPurpose)
            & applies_to.only(Data)
            & has_basis.only(LegalBasis)
        ])

        Use.is_a.extend([
            DataActivity
        ])

        Protection.is_a.extend([
            has_mechanism.only(SecurityMechanism)
        ])

        FPCollection.is_a.extend([
            collects_from.only(User)
            & has_mechanism.only(UserSpecific)
            & has_mode.only(DataTransmissionMode)
        ])

        TPCollection.is_a.extend([
            collects_from.only(ThirdParty)
            & has_mechanism.only(TPSaCMechanism)
            & has_mode.only(DataTransmissionMode)
        ])

        TPSharing.is_a.extend([
            shares_with.only(ThirdParty)
            & has_mechanism.only(TPSaCMechanism)
            & has_mode.only(DataTransmissionMode)
        ])

        Retention.is_a.extend([
            has_mechanism.only(DataRetentionMechanism)
            & lasts_for.only(DataRetentionTime)
        ])

        PolicyChange.is_a.extend([
            has_consequence.only(PolicyChangeConsequence)
            & caused_by.only(PolicyChangeCause)
            & lasts_for.only(PolicyAcceptanceTime)
            & has_scope.only(PolicyChangeScope)
        ])

        Notification.is_a.extend([
            initiated_by.only(Agent)
            & notifies.only(Agent)
            & has_mechanism.only(CommunicationMechanism)
            & lasts_for.only(NotificationTime)
        ])

        FPNotification.is_a.extend([
            initiated_by.only(FirstParty)
            & notifies.only(User)
            & has_mechanism.only(FPSpecific)
        ])

        UserNotification.is_a.extend([
            initiated_by.only(User)
            & notifies.only(FirstParty)
            & has_mechanism.only(Manual)
        ])

        DataControl.is_a.extend([
            initiated_by.only(User)
            & applies_to.only(Data)
            & has_basis.only(LegalBasis)
            & has_mechanism.only(Manual)
        ])

        ProvidedDataControl.is_a.extend([
            
        ])

        PrivacyControl.is_a.extend([
            
        ])

        OptControl.is_a.extend([

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
            initiates.only(DataActivity | FPNotification)
            & notified_by.only(UserNotification)
        ])

        ThirdParty.is_a.extend([
            is_shared_by.only(TPSharing)
            & is_collected_by.only(TPCollection)
        ])

        Criminal.is_a.extend([
            initiates.only(Breach)
        ])


        # Data
        Data.is_a.extend([
            considered_by.only(PrivacyPolicy)
        ])

        PersonalData.is_a.extend([

        ])

        NonPersonalData.is_a.extend([

        ])

        NonSensitiveData.is_a.extend([

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
            mechanism_of.only(Retention)
        ])

        OwnServers.is_a.extend([

        ])

        EmployedServers.is_a.extend([

        ])

        TPSaCMechanism.is_a.extend([
            mechanism_of.only(TPCollection | TPSharing)
        ])

        Contract.is_a.extend([

        ])

        ForFree.is_a.extend([

        ])

        SecurityMechanism.is_a.extend([
            mechanism_of.only(Protection)
        ])

        TechnicalMeasure.is_a.extend([

        ])

        PseudoAnonymization.is_a.extend([

        ])

        Encryption.is_a.extend([

        ])

        SecureStorage.is_a.extend([

        ])

        SecureTunnel.is_a.extend([

        ])

        Firewall.is_a.extend([

        ])

        AccessControls.is_a.extend([

        ])

        OrganizationalMeasure.is_a.extend([

        ])

        LockedOffice.is_a.extend([

        ])

        SecurityTraining.is_a.extend([

        ])

        UserMaintain.is_a.extend([

        ])

        CommunicationMechanism.is_a.extend([
            mechanism_of.only(Notification | DataControl | FPCollection)
        ])

        UserSpecific.is_a.extend([
            mechanism_of.only(Not(FPNotification))
        ])

        Automatic.is_a.extend([

        ])

        ThroughServiceApp.is_a.extend([

        ])

        ThroughWebsite.is_a.extend([

        ])

        Manual.is_a.extend([
            (UserSpecific | Mutual),
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

        Mutual.is_a.extend([
            
        ])

        Email.is_a.extend([

        ])

        PostalMail.is_a.extend([

        ])

        PhoneCall.is_a.extend([

        ])

        SMS.is_a.extend([

        ])

        FPSpecific.is_a.extend([
            (FPSpecific | Mutual),
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

        Permanent.is_a.extend([

        ])

        ByRequest.is_a.extend([

        ])

        # Causes
        Cause.is_a.extend([
            causes.only(Activity)
        ])

        BreachCause.is_a.extend([
            causes.only(Breach)
        ])

        ForceMajeur.is_a.extend([

        ])

        Intentional.is_a.extend([

        ])

        Unintentional.is_a.extend([

        ])

        PolicyChangeCause.is_a.extend([
            causes.only(PolicyChange)
        ])

        PrivacyRelated.is_a.extend([

        ])

        NonPrivacyRelated.is_a.extend([

        ])

        MergeAcquisition.is_a.extend([

        ])


        # Consequences
        Consequence.is_a.extend([
            is_consequence_of.only(Activity)
        ])

        BreachConsequence.is_a.extend([
            is_consequence_of.only(Breach)
        ])

        RemoveCompromisedInformation.is_a.extend([

        ])

        Compensation.is_a.extend([

        ])

        BreachInvestigation.is_a.extend([

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

        ServiceProvision.is_a.extend([

        ])

        HealthMonitoring.is_a.extend([

        ])

        ServiceEnhancement.is_a.extend([

        ])

        Analytics.is_a.extend([

        ])

        Security.is_a.extend([

        ])

        Research.is_a.extend([

        ])

        Marketing.is_a.extend([

        ])


        # Time periods
        TimePeriod.is_a.extend([
            is_period_of.only(Activity)
        ])

        DataRetentionTime.is_a.extend([
            is_period_of.only(Retention)
        ])

        NotificationTime.is_a.extend([
            is_period_of.only(Notification)
        ])

        BreachInvestigationTime.is_a.extend([
            is_period_of.only(BreachInvestigation)
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

        Child.is_a.extend([

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

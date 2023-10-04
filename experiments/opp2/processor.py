from .parsing import *


_ID = -1


def first_party_scenario(o, r, fp, u):
    data = parse_data(o, r, u)
    purpose = parse_purpose(o, r)
    mechanism = parse_mechanism_fp(o, r)
    mode = parse_mode_fp(o, r)
    protection = parse_identifiability(o, r, fp, data)

    collection = None
    use = None

    if r["attributes"]["Choice Scope"]["value"] == "Collection" \
            or r["attributes"]["Choice Scope"]["value"] == "Both" \
            or r["attributes"]["Choice Scope"]["value"] == "not-selected":
        collection = o.individual(
            'FPCollection',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('has_purpose', purpose),
                o.property('has_mode', mode),
                o.property('has_mechanism', mechanism),
                *[o.property('applies_to', d) for d in data],
                o.property('collects_from', u),
                o.property('binded_to', protection),
            ]
        )

    if r["attributes"]["Choice Scope"]["value"] == "Use" \
            or r["attributes"]["Choice Scope"]["value"] == "Both" \
            or r["attributes"]["Choice Scope"]["value"] == "not-selected":
        use = o.individual(
            'Use', 
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('has_purpose', purpose),
                *[o.property('applies_to', d) for d in data],
                o.property('binded_to', protection),
            ]
        )

    if not collection and use:
        o.destroy(mode)
        o.destroy(mechanism)
    elif not collection and not use:
        o.destroy(mode)
        o.destroy(purpose)
        o.destroy(mechanism)


def third_party_scenario(o, r, fp, tp, u):
    data = parse_data(o, r, u)
    purpose = parse_purpose(o, r)
    mechanism = parse_mechanism_tp(o, r)
    protection = parse_identifiability(o, r, fp, data)
    mode = parse_mode_tp(o, r)

    collection = None
    sharing = None

    if r["attributes"]["Choice Scope"]["value"] == "Collection" \
            or r["attributes"]["Choice Scope"]["value"] == "Both" \
            or r["attributes"]["Choice Scope"]["value"] == "not-selected":
        collection = o.individual(
            'TPCollection',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('has_purpose', purpose),
                o.property('has_mode', mode),
                o.property('has_mechanism', mechanism),
                *[o.property('applies_to', d) for d in data],
                o.property('collects_from', tp),
                o.property('binded_to', protection),
            ]
        )

    if r["attributes"]["Choice Scope"]["value"] == "Sharing" \
            or r["attributes"]["Choice Scope"]["value"] == "Both" \
            or r["attributes"]["Choice Scope"]["value"] == "not-selected":
        sharing = o.individual(
            'TPSharing',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('has_purpose', purpose),
                o.property('has_mode', mode),
                o.property('has_mechanism', mechanism),
                *[o.property('applies_to', d) for d in data],
                o.property('shares_with', tp),
                o.property('binded_to', protection),
            ]
        )

    if not collection and sharing:
        o.destroy(mode)
        o.destroy(purpose)
        o.destroy(mechanism)


def user_choice_and_control(o, r, u):
    mechanism = parse_mechanism_choice(o, r)
    data = parse_data(o, r, u)
    
    if r["attributes"]["Choice Type"]["value"] != "null" \
            and "selectedText" in r["attributes"]["Choice Type"].keys():
        o.individual(
            'ProvidedDataControl',
            r["segment_text"],
            [
                o.property('initiated_by', u),
                o.property('has_mechanism', mechanism),
                *[o.property('applies_to', d) for d in data],
            ]
        )


def data_retention(o, r, fp, u):
    data = parse_data(o, r, u)
    purpose = parse_purpose_retention(o, r)
    period = parse_period_retention(o, r)

    o.individual(
        'Retention',
        r["segment_text"],
        [
            o.property('initiated_by', fp),
            o.property('lasts_for', period),
            o.property('has_purpose', purpose),
            *[o.property('applies_to', d) for d in data],
        ]
    )


def user_access(o, r, u):
    data = parse_data_access(o, r, u)

    o.individual(
        'ProvidedDataControl',
        r["segment_text"],
        [
            o.property('initiated_by', u),
            o.property('has_mechanism', o.individual('Manual', r["segment_text"])),
            *[o.property('applies_to', d) for d in data],
        ]
    )


def do_not_track(o, r, u):
    o.individual(
        'OptControl',
        r["segment_text"],
        [
            o.property('initiated_by', u),
        ]
    )


def international_and_specific_audience(o, r, u):
    o.individual(
        'UserSpecialCategory',
        r["segment_text"],
        [
            o.property('is_special_category_for', u),
        ]
    )


def data_security(o, r, fp):
    mechanisms = parse_mechanism_security(o, r)

    o.individual(
        'Protection',
        r["segment_text"],
        [
            o.property('initiated_by', fp),
            *[o.property('has_mechanism', m) for m in mechanisms],
        ]
    )


def policy_change(o, r, u, fp):
    mechanisms = parse_mechanism_policy_change(o, r)
    causes = parse_cause_policy_change(o, r)

    policy_change = o.individual(
        'PolicyChange',
        r["segment_text"],
        [
            o.property('initiated_by', fp),
            *[o.property('has_cause', c) for c in causes],
        ]
    )

    o.individual(
        'FPNotification',
        r["segment_text"],
        [
            o.property('initiated_by', fp),
            o.property('notifies', u),
            o.property('has_mechanism', mechanisms),
            o.property('binded_to', policy_change),
        ]
    )


def process_opp(o, policy):
    """
    mappings = {
        "First Party Collection/Use": "DataCollectionActivity",
        "Third Party Sharing/Collection": "DataSharingActivity",
        "User Choice/Control": "ConsentActivity",
        "User Access, Edit and Deletion": "UserAccessActivity",
        "Data Retention": "DataRetentionActivity",
        "Data Security": "SecurityMechanism",
        "Policy Change": "PolicyChangeActivity",
        "Do Not Track": "UserOptActivity",
        "International and Specific Audiences": "UserSpecialCategory",
    }

    Data Security is needed to be connected with all activities

    Notions:
        Write migration scheme for each category of OPP-115
        DataSecurity & Notification can be binded with Activity to produce more complex activities
        Three of actors are mandatory and unique FP, TP, and User
    """
    global _ID
    _ID += 1

    o.new_policy(policy["name"])

    user = o.individual('User')
    first_party = o.individual('FirstParty')
    third_party = o.individual('ThirdParty')

    for a in policy["annotations"]:
        if a["category"] == "Other":
            continue

        if a["category"] == "First Party Collection/Use":
            first_party_scenario(o, a, first_party, user)

        if a["category"] == "Third Party Sharing/Collection":
            third_party_scenario(o, a, first_party, third_party, user)

        if a["category"] == "User Choice/Control":
            user_choice_and_control(o, a, user)

        if a["category"] == "Data Retention":
            data_retention(o, a, first_party, user)

        if a["category"] == "User Access, Edit and Deletion":
            user_access(o, a, user)

        if a["category"] == "Do Not Track":
            do_not_track(o, a, user)

        if a["category"] == "International and Specific Audiences":
            international_and_specific_audience(o, a, user)

        if a["category"] == "Data Security":
            data_security(o, a, first_party)

        if a["category"] == "Policy Change":
            policy_change(o, a, user, first_party)

    return o


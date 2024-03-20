from .parsing import *


_ID = -1


def construct_first_party_scenario(o, r, fp, u):

    if r["attributes"]["Choice Scope"]["value"] == "Both":
        
        data = parse_data(o, r, u)
        purposes = parse_purpose(o, r)
        mechanisms = parse_mechanism_fp(o, r)
        modes = parse_mode_fp(o, r)
        protection = parse_identifiability(o, r, fp, data)
        
        o.individual(
            'FPCollection',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('collects_from', u),
                *purposes,
                *modes,
                *mechanisms,
                *data,
                *protection,
            ],
            [o.property('does', True if r["attributes"]["Choice Scope"]["value"] == 'Does' else False)]
        )
        
        o.individual(
            'DataUse', 
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                *purposes,
                *data,
                *protection,
            ],
            [o.property('does', True if r["attributes"]["Choice Scope"]["value"] == 'Does' else False)]
        )

    if r["attributes"]["Choice Scope"]["value"] == "Collection":
        
        data = parse_data(o, r, u)
        purposes = parse_purpose(o, r)
        mechanisms = parse_mechanism_fp(o, r)
        modes = parse_mode_fp(o, r)
        protection = parse_identifiability(o, r, fp, data)

        o.individual(
            'FPCollection',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('collects_from', u),
                *purposes,
                *modes,
                *mechanisms,
                *data,
                *protection,
            ],
            [o.property('does', True if r["attributes"]["Choice Scope"]["value"] == 'Does' else False)]
        )

    if r["attributes"]["Choice Scope"]["value"] == "Use":

        data = parse_data(o, r, u)
        purposes = parse_purpose(o, r)
        protection = parse_identifiability(o, r, fp, data)

        o.individual(
            'DataUse', 
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                *purposes,
                *data,
                *protection,
            ],
            [o.property('does', True if r["attributes"]["Choice Scope"]["value"] == 'Does' else False)]
        )


def construct_third_party_scenario(o, r, fp, tp, u):

    if r["attributes"]["Choice Scope"]["value"] == "Both":

        data = parse_data(o, r, u)
        purpose = parse_purpose(o, r)
        mechanism = parse_mechanism_tp(o, r)
        protection = parse_identifiability(o, r, fp, data)
        
        o.individual(
            'TPCollection',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('collects_from', tp),
                *purpose,
                *mechanism,
                *data,
                *protection,
            ],
            [o.property('does', True if r["attributes"]["Choice Scope"]["value"] == 'Does' else False)]
        )

        o.individual(
            'TPSharing',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('shares_with', tp),
                *purpose,
                *mechanism,
                *data,
                *protection,
            ],
            [o.property('does', True if r["attributes"]["Choice Scope"]["value"] == 'Does' else False)]
        )

    if r["attributes"]["Choice Scope"]["value"] == "Collection":
        
        data = parse_data(o, r, u)
        purpose = parse_purpose(o, r)
        mechanism = parse_mechanism_tp(o, r)
        protection = parse_identifiability(o, r, fp, data)

        o.individual(
            'TPCollection',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('collects_from', tp),
                *purpose,
                *mechanism,
                *data,
                *protection,
            ],
            [o.property('does', True if r["attributes"]["Choice Scope"]["value"] == 'Does' else False)]
        )

    if r["attributes"]["Choice Scope"]["value"] == "Sharing":
        
        data = parse_data(o, r, u)
        purpose = parse_purpose(o, r)
        mechanism = parse_mechanism_tp(o, r)
        protection = parse_identifiability(o, r, fp, data)

        o.individual(
            'TPSharing',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('shares_with', tp),
                *purpose,
                *mechanism,
                *data,
                *protection,
            ],
            [o.property('does', True if r["attributes"]["Choice Scope"]["value"] == 'Does' else False)]
        )


def construct_user_choice_and_control(o, r, u):
    if r["attributes"]["Choice Type"]["value"] != "null" and "selectedText" in r["attributes"]["Choice Type"].keys():
        
        o.individual(
            'OptInOptOutControl',
            r["segment_text"],
            [
                o.property('initiated_by', u),
                *parse_mechanism_choice(o, r),
                *parse_data(o, r, u),
            ]
        )


def construct_data_data_retention(o, r, fp, u):
    o.individual(
        'DataRetention',
        r["segment_text"],
        [
            o.property('initiated_by', fp),
            *parse_period_data_retention(o, r),
            *parse_purpose_data_retention(o, r),
            *parse_data(o, r, u)
        ]
    )


def construct_user_access_edit_deletion(o, r, u):
    o.individual(
        'OptInOptOutControl',
        r["segment_text"],
        [
            o.property('initiated_by', u),
            o.property('has_mechanism', o.individual('ManualCommunicationMechanism', r["segment_text"])),
            *parse_data_access(o, r, u),
        ]
    )


def construct_do_not_track(o, r, u):
    o.individual(
        'AdvertisingDataControl',
        r["segment_text"],
        [
            o.property('initiated_by', u),
        ]
    )


def construct_international_and_specific_audience(o, r, u):
    o.individual(
        'UserSpecialCategory',
        r["segment_text"],
        [
            o.property('is_special_category_for', u),
        ]
    )


def construct_data_security(o, r, fp):
    mechanisms = parse_mechanism_security(o, r)

    o.individual(
        'DataProtection',
        r["segment_text"],
        [
            o.property('initiated_by', fp),
            *mechanisms,
        ]
    )


# Connect with privacy control
def construct_policy_change(o, r, u, fp):
    o.individual(
        'FPNotification',
        r["segment_text"],
        [
            o.property('initiated_by', fp),
            o.property('notifies', u),
            *parse_mechanism_policy_change(o, r),
            o.property('binded_to', o.individual(
                'PolicyChange',
                r["segment_text"],
                [
                    o.property('initiated_by', fp),
                    *parse_cause_policy_change(o, r),
                    o.property('binded_to', o.individual(
                        'OptInOptOutControl',
                        r["segment_text"],
                        [
                            o.property('initiated_by', u),
                        ]
                    )),
                ]
            )),
        ]
    )


def process(o, policy):
    """
    mappings = {
        "First Party Collection/Use": "DataCollectionActivity",
        "Third Party Sharing/Collection": "DataSharingActivity",
        "User Choice/Control": "ConsentActivity",
        "User Access, Edit and Deletion": "UserAccessActivity",
        "Data DataRetention": "DataRetentionActivity",
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
            construct_first_party_scenario(o, a, first_party, user)

        if a["category"] == "Third Party Sharing/Collection":
            construct_third_party_scenario(o, a, first_party, third_party, user)

        if a["category"] == "User Choice/Control":
            construct_user_choice_and_control(o, a, user)

        if a["category"] == "Data DataRetention":
            construct_data_data_retention(o, a, first_party, user)

        if a["category"] == "User Access, Edit and Deletion":
            construct_user_access_edit_deletion(o, a, user)

        if a["category"] == "Do Not Track":
            construct_do_not_track(o, a, user)

        if a["category"] == "International and Specific Audiences":
            construct_international_and_specific_audience(o, a, user)

        if a["category"] == "Data Security":
            construct_data_security(o, a, first_party)

        if a["category"] == "Policy Change":
            construct_policy_change(o, a, user, first_party)

    return o


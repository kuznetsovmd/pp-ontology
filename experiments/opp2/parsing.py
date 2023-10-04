def parse_data(o, r, u):
    data = []

    # Data
    if r["attributes"]["Personal Information Type"]["value"] != "Unspecified" and "selectedText" in r["attributes"]["Personal Information Type"].keys():

        if r["attributes"]["Personal Information Type"]["value"] == "Health":
            data.append(o.individual(
                'HealthData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Unspecified":
            data.append(o.individual(
                'Data', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Cookies and tracking elements":
            data.append(o.individual(
                'TrackingData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Personal identifier":
            data.append(o.individual(
                'AccountData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "IP address and device IDs":
            data.append(o.individual(
                'DeviceData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Financial":
            data.append(o.individual(
                'FinancialData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "User online activities":
            data.append(o.individual(
                'AccountData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "User profile":
            data.append(o.individual(
                'SensitiveData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Contact":
            data.append(o.individual(
                'NonSensitiveData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Other":
            data.append(o.individual(
                'Data', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Computer information":
            data.append(o.individual(
                'DeviceData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Survey data":
            data.append(o.individual(
                'SensitiveData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Generic personal information":
            data.append(o.individual(
                'GenericData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Demographic":
            data.append(o.individual(
                'SensitiveData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Social media data":
            data.append(o.individual(
                'NonSensitiveData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Personal Information Type"]["value"] == "Location":
            data.append(o.individual(
                'TrackingData', 
                r["attributes"]["Personal Information Type"]["selectedText"],
                [o.property('provided_by', u)]))
            
    return data


def parse_data_access(o, r, u):
    data = []

    if r["attributes"]["Access Scope"]["value"] != "Unspecified":

        if r["attributes"]["Access Scope"]["value"] == "User account data":
            data.append(o.individual(
                'AccountData', 
                r["segment_text"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Access Scope"]["value"] == "Other data about user":
            data.append(o.individual(
                'NonSensitiveData', 
                r["segment_text"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Access Scope"]["value"] == "Profile data":
            data.append(o.individual(
                'SensitiveData', 
                r["segment_text"],
                [o.property('provided_by', u)]))

        if r["attributes"]["Access Scope"]["value"] == "Transactional data":
            data.append(o.individual(
                'FinancialData', 
                r["segment_text"],
                [o.property('provided_by', u)]))

    return data


def parse_identifiability(o, r, fp, data):
    if r["attributes"]["Identifiability"]["value"] != "Unspecified" and r["attributes"]["Identifiability"]["value"] != "not-selected" and "selectedText" in r["attributes"]["Identifiability"].keys():
        return o.individual(
            'Protection',
            r["segment_text"],
            [
                o.property('initiated_by', fp),
                o.property('has_mechanism', o.individual('PseudoAnonymization', r["attributes"]["Identifiability"]["selectedText"])),
                *[o.property('applies_to', d) for d in data],
            ]
        )


def parse_purpose(o, r):
    if r["attributes"]["Purpose"]["value"] != "null" and "selectedText" in r["attributes"]["Purpose"].keys():
        return o.individual('DataActivityPurpose', r["attributes"]["Purpose"]["selectedText"])


def parse_purpose_retention(o, r):
    if r["attributes"]["Retention Purpose"]["value"] != "null" and "selectedText" in r["attributes"]["Retention Purpose"].keys():
        return o.individual('DataActivityPurpose', r["attributes"]["Retention Purpose"]["selectedText"])


def parse_period_retention(o, r):
    if r["attributes"]["Retention Period"]["value"] != "null" and "selectedText" in r["attributes"]["Retention Period"].keys():
        return o.individual('DataRetentionTime', r["attributes"]["Retention Period"]["selectedText"])


def parse_mechanism_fp(o, r):
    if r["attributes"]["Action First-Party"]["value"] != "null" and "selectedText" in r["attributes"]["Action First-Party"].keys():
        return o.individual('UserSpecific', r["attributes"]["Action First-Party"]["selectedText"])


def parse_mechanism_security(o, r):
    mechanisms = []
    
    if r["attributes"]["Security Measure"]["value"] != "Unspecified":

        if r["attributes"]["Security Measure"]["value"] == "Data access limitation":
            mechanisms.append(o.individual('TechnicalMeasure', r['segment_text']))

        if r["attributes"]["Security Measure"]["value"] == "Generic":
            mechanisms.append(o.individual('TechnicalMeasure', r['segment_text']))

        if r["attributes"]["Security Measure"]["value"] == "Secure user authentication":
            mechanisms.append(o.individual('TechnicalMeasure', r['segment_text']))

        if r["attributes"]["Security Measure"]["value"] == "Secure data storage":
            mechanisms.append(o.individual('Encryption', r['segment_text']))

        if r["attributes"]["Security Measure"]["value"] == "Other":
            mechanisms.append(o.individual('SecurityMechanism', r['segment_text']))

        if r["attributes"]["Security Measure"]["value"] == "Privacy review/audit":
            mechanisms.append(o.individual('OrganizationalMeasure', r['segment_text']))

        if r["attributes"]["Security Measure"]["value"] == "Privacy/Security program":
            mechanisms.append(o.individual('TechnicalMeasure', r['segment_text']))

        if r["attributes"]["Security Measure"]["value"] == "Secure data transfer":
            mechanisms.append(o.individual('Encryption', r['segment_text']))

        if r["attributes"]["Security Measure"]["value"] == "Privacy training":
            mechanisms.append(o.individual('OrganizationalMeasure', r['segment_text']))

    return mechanisms


def parse_mechanism_tp(o, r):
    if r["attributes"]["Action Third Party"]["value"] != "null" and "selectedText" in r["attributes"]["Action Third Party"].keys():
        return o.individual('TPSaCMechanism', r["attributes"]["Action Third Party"]["selectedText"])


def parse_mechanism_choice(o, r):
    if r["attributes"]["Choice Type"]["value"] != "null" and "selectedText" in r["attributes"]["Choice Type"].keys():
        return o.individual('Manual', r["attributes"]["Choice Type"]["selectedText"])


def parse_mechanism_policy_change(o, r):
    mechanisms = []

    if r["attributes"]["Notification Type"]["value"] == "Personal notice":
        mechanisms.append(o.individual('FPSpecific', r['segment_text']))

    if r["attributes"]["Notification Type"]["value"] == "General notice on website":
        mechanisms.append(o.individual('OnWebsitePage', r['segment_text']))

    if r["attributes"]["Notification Type"]["value"] == "General notice in privacy policy":
        mechanisms.append(o.individual('InPrivacyPolicy', r['segment_text']))

    if r["attributes"]["Notification Type"]["value"] == "Other":
        mechanisms.append(o.individual('FPSpecific', r['segment_text']))

    return mechanisms


def parse_mode_fp(o, r):
    if r["attributes"]["Collection Mode"]["value"] != "Unspecified" and "selectedText" in r["attributes"]["Collection Mode"].keys():
        return o.individual('DataTransmissionMode', r["attributes"]["Collection Mode"]["selectedText"])


def parse_mode_tp(o, r):
    if r["attributes"]["Choice Scope"]["value"] != "Unspecified" and "selectedText" in r["attributes"]["Choice Scope"].keys():
        return o.individual('DataTransmissionMode', r["attributes"]["Choice Scope"]["selectedText"])


def parse_cause_policy_change(o, r):
    causes = []

    if r["attributes"]["User Choice"]["value"] != "Unspecified" and "selectedText" in r["attributes"]["User Choice"].keys():

        if r["attributes"]["Change Type"]["value"] == "Privacy relevant change":
            causes.append(o.individual('PrivacyRelated', r['segment_text']))

        if r["attributes"]["Change Type"]["value"] == "Non-privacy relevant change":
            causes.append(o.individual('NonPrivacyRelated', r['segment_text']))

        if r["attributes"]["Change Type"]["value"] == "In case of merger or acquisition":
            causes.append(o.individual('MergeAcquisition', r['segment_text']))

        if r["attributes"]["Change Type"]["value"] == "Other":
            causes.append(o.individual('PolicyChangeCause', r['segment_text']))

    return causes
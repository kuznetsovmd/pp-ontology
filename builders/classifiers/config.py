import os

import torch
from torch import device as get_device
from torch.cuda import current_device, is_available

from builders.classifiers.model import Linear2BERT


def select_device(use_cuda):
    d = current_device() if is_available() and use_cuda else get_device('cpu')
    print(f'Torch version: {torch.__version__}')
    try:
        print(f'Using: {torch.cuda.get_device_name(d)}')
    except ValueError:
        print(f'Using: CPU')
    return d


def make_conf(resources, annotations, russian_pp, tqdm_conf, device='cpu', pretrained=False,
              n_epochs=100, padding=10, density=.2, version=0, module=Linear2BERT, split=.75,
              ontology_class='FPCollection'):
    return {
        'ontology_class': ontology_class,
        'annotations_path': annotations,
        'descriptor_path': f'{russian_pp}/json/plain.json',
        'policies_path': f'{russian_pp}/output_policies',
        'output_path': f'{resources}/classified',
        'sequence_len': 512,
        'split': split,
        'n_epochs': n_epochs,
        'padding': padding,
        'density': density,
        'bert_tokenizer': 'DeepPavlov/rubert-base-cased',
        'tqdm_conf': tqdm_conf,
        'model_conf': {
            'name': f'bert-{ontology_class.lower()}',
            'version': version,
            'path': f'{resources}/models/epochs_{ontology_class.lower()}',
            'pretrained': pretrained,
            'bert_model': 'DeepPavlov/rubert-base-cased',
            'device': device,
            'module': module,
            'module_parameters': {
                'input_size': 768,
                'hidden_size': 1024,
                'dropout': .01, 
            },
            'optimizer': torch.optim.AdamW,
            'optimizer_parameters': {
                'lr':  5e-5,
                'eps': 1e-8,
                'betas': (0.9, 0.999),
            },
            'criterion': torch.nn.BCELoss,
            'criterion_parameters': {},
        }
    }


def train_config(resources, annotations, russian_pp, use_cuda, tqdm_conf, **kwargs):
    conf_args = [
        {'pretrained': False, 'version': 0, 'ontology_class': 'PrivacyPolicy'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'Data'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'PolicyChangeScope'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DataBreachProcessing'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'FirstParty'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DataBreach'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DataActivity'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DataActivityPurpose'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'LegalBasis'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'PolicyChange'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'PolicyAcceptanceTime'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DataUse'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DataProtection'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'SecurityMechanism'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'FPCollection'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'User'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'UserSpecificCommunicationMechanism'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'GeneralCommunicationMechanism'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'TPCollection'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'ThirdParty'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'TPSharing'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DataRetention'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DataRetentionTime'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'NotificationTime'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'FPNotification'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'UserNotification'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'AdvertisingDataControl'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'OptInOptOutControl'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'NonPersonalData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'PersonalData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'ServiceData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'FinancialData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DeviceData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'ApplicationData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'AccountData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'TrackingData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'SensitiveData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'ReligionData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'RacialData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'GenericData'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'StoreOnEmployedServers'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'TechnicalSecurityMeasure'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'OrganizationalSecurityMeasure'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'PseudoAnonymization'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'Encryption'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'Firewall'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'AutomaticCommunicationMechanism'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'ViaServiceApp'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'ViaWebsite'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'WebsiteForm'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'DataProvision'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'PersonalVisit'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'Email'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'PostalMail'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'SMS'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'OnWebsitePage'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'InPrivacyPolicy'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'IntentionalBreach'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'UnintentionalBreach'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'PartialServiceRestriction'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'FullServiceRestriction'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'LegalCompliancePurpose'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'ServiceProvisionPurpose'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'ServiceEnhancementPurpose'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'AnalyticsPurpose'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'SecurityPurpose'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'ResearchPurpose'},
        {'pretrained': False, 'version': 0, 'ontology_class': 'MarketingPurpose'},
    ]

    device = select_device(use_cuda)
    conf = [make_conf(resources, annotations, russian_pp, tqdm_conf, device, **ca) for ca in conf_args]
    list(os.makedirs(c['model_conf']['path'], exist_ok=True) for c in conf)

    return conf


def eval_config(resources, annotations, russian_pp, use_cuda, tqdm_conf, **kwargs):
    conf_args = [
        {'pretrained': True, 'version': 99, 'ontology_class': 'PrivacyPolicy'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'Data'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'PolicyChangeScope'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DataBreachProcessing'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'FirstParty'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DataBreach'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DataActivity'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DataActivityPurpose'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'LegalBasis'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'PolicyChange'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'PolicyAcceptanceTime'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DataUse'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DataProtection'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'SecurityMechanism'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'FPCollection'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'User'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'UserSpecificCommunicationMechanism'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'GeneralCommunicationMechanism'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'TPCollection'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'ThirdParty'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'TPSharing'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DataRetention'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DataRetentionTime'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'NotificationTime'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'FPNotification'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'UserNotification'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'AdvertisingDataControl'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'OptInOptOutControl'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'NonPersonalData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'PersonalData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'ServiceData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'FinancialData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DeviceData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'ApplicationData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'AccountData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'TrackingData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'SensitiveData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'ReligionData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'RacialData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'GenericData'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'StoreOnEmployedServers'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'TechnicalSecurityMeasure'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'OrganizationalSecurityMeasure'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'PseudoAnonymization'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'Encryption'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'Firewall'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'AutomaticCommunicationMechanism'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'ViaServiceApp'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'ViaWebsite'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'WebsiteForm'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'DataProvision'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'PersonalVisit'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'Email'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'PostalMail'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'SMS'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'OnWebsitePage'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'InPrivacyPolicy'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'IntentionalBreach'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'UnintentionalBreach'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'PartialServiceRestriction'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'FullServiceRestriction'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'LegalCompliancePurpose'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'ServiceProvisionPurpose'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'ServiceEnhancementPurpose'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'AnalyticsPurpose'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'SecurityPurpose'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'ResearchPurpose'},
        {'pretrained': True, 'version': 99, 'ontology_class': 'MarketingPurpose'},
    ]

    device = select_device(use_cuda)
    conf = [make_conf(resources, annotations, russian_pp, tqdm_conf, device, **ca) for ca in conf_args]
    list(os.makedirs(c['model_conf']['path'], exist_ok=True) for c in conf)

    return conf

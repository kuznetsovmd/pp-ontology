import os
import shutil
import torch
import contextlib

import numpy as np

from torch import nn
from transformers import AutoModel

from ontology2.classifier_builder.device import DEVICE
from ontology2.classifier_builder.model import Linear2BERT, LinearBERT, RNN_BERT


def model_defaults():
    return {
        'device': DEVICE,
        'module': LinearBERT,
        'module_parameters': {
            'input_size': 768,
            'hidden_size': 2048,
            'dropout': .01, 
            'device': DEVICE,
        },
        'optimizer': torch.optim.Adam,
        'optimizer_parameters': {
            'lr':  5e-5,
            'eps': 1e-9,
            'betas': (0.9, 0.98),
        },
        'criterion': nn.CrossEntropyLoss,
        'criterion_parameters': {
            'label_smoothing': .05,
        },
        'bert_model': 'ai-forever/ruBert-base',
        'name': 'bert',
        'version': 0,
    }


class BaseModel:
    
    def __init__(self, **kwargs):
        self.device = kwargs['device']
        self.bert = AutoModel.from_pretrained(kwargs['bert_model'])
        self.module = kwargs['module'](**kwargs['module_parameters'])
        self.optimizer = kwargs['optimizer'](self.module.parameters(), **kwargs['optimizer_parameters'])
        self.criterion = kwargs['criterion'](**kwargs['criterion_parameters'])

        self.bert.to(self.device)
    
    def train(self, sample):
        input_ids, attention_mask, targets = \
            torch.tensor(sample['input_ids'], device=DEVICE).unsqueeze(0), \
            torch.tensor(sample['attention_mask'], device=DEVICE).unsqueeze(0), \
            torch.tensor(sample['targets'], device=DEVICE)

        # with torch.no_grad():
        embedding = self.bert(input_ids, attention_mask).last_hidden_state[0]

        # self.module.init_hidden()
        total_loss = 0
        for i, trg in enumerate(targets):
            src = torch.mean(embedding[i:i+10, :], dim=0)
            output = self.module(src.unsqueeze(0))
            loss = self.criterion(output, trg.unsqueeze(0))
            total_loss += loss
            yield {
                'predicted': torch.argmax(output, dim=1).item(),
                'output': output.detach().cpu().tolist()[0], 
                'loss': loss.item()
            }
        total_loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
        
    
    def test(self, sample):
        input_ids, attention_mask, targets = \
            torch.tensor(sample['input_ids'], device=DEVICE).unsqueeze(0), \
            torch.tensor(sample['attention_mask'], device=DEVICE).unsqueeze(0), \
            torch.tensor(sample['targets'], device=DEVICE)

        with torch.no_grad():
            embedding = self.bert(input_ids, attention_mask).last_hidden_state[0]

            for i, trg in enumerate(targets):
                src = torch.mean(embedding[i:i+10, :], dim=0)
                output = self.module(src.unsqueeze(0))
                loss = self.criterion(output, trg.unsqueeze(0))
                yield {
                    'predicted': torch.argmax(output, dim=1).item(),
                    'output': output.detach().cpu().tolist()[0], 
                    'loss': loss.item()
                }
    
    def predict(self, sample):
        input_ids, attention_mask = \
            torch.tensor(sample['input_ids'], device=DEVICE).unsqueeze(0), \
            torch.tensor(sample['attention_mask'], device=DEVICE).unsqueeze(0)

        with torch.no_grad():
            embedding = self.bert(input_ids, attention_mask).last_hidden_state[0]

            for i, _ in enumerate(embedding):
                src = torch.mean(embedding[i:i+10, :], dim=0)
                output = self.module(src.unsqueeze(0))
                yield {
                    'predicted': torch.argmax(output, dim=1).item(),
                    'output': output.detach().cpu().tolist()[0], 
                }


class Model(BaseModel):
    
    def __accuracy(self, output, target):
        assert len(output) == len(target), 'outputs & targets not equally on length'
        return np.average(np.array(output) == np.array(target))
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs['name']
        self.version = kwargs['version']

        self.t_outputs = []
        self.t_losses = []
        self.v_outputs = []
        self.v_losses = []

        self.stats_mem = []

    def train(self, sample):
        output = list(super().train(sample))
        self.t_losses.append(np.average([o['loss'] for o in output]))
        self.t_outputs.append(self.__accuracy([o['predicted'] for o in output], sample['target_ids']))
        return output

    def test(self, sample):
        output = list(super().test(sample))
        self.v_losses.append(np.average([o['loss'] for o in output]))
        self.v_outputs.append(self.__accuracy([o['predicted'] for o in output], sample['target_ids']))
        return output

    def predict(self, sample):
        return list(super().predict(sample))

    def stats(self):
        stats = {
            't_loss': np.average(self.t_losses) if self.t_losses else 0,
            'v_loss':  np.average(self.v_losses) if self.v_losses else 0,
            't_accuracy': np.average(self.t_outputs) if self.t_outputs else 0,
            'v_accuracy': np.average(self.v_outputs) if self.v_outputs else 0,
        }

        self.stats_mem.append(stats)

        self.t_losses = []
        self.t_outputs = []
        self.v_losses = []
        self.v_outputs = []

        return stats


def build_model(path=None, **kwargs):
    model = Model(**kwargs)

    if path:
        loaded = torch.load(f'{path}/{kwargs["name"]}{kwargs["version"]}.pt')

        if loaded:
            model.module.load_state_dict(loaded['model_state_dict'])
            model.optimizer.load_state_dict(loaded['optimizer_state_dict'])
            model.stats_mem = loaded['stats_mem']

    else:
        with contextlib.suppress(FileNotFoundError):
            shutil.rmtree(path, ignore_errors=True)
        
    return model


def save_model(model, path):
    os.makedirs(path, exist_ok=True)
    torch.save({
        'model_state_dict': model.module.state_dict(),
        'optimizer_state_dict': model.optimizer.state_dict(),
        'stats_mem': model.stats_mem,
    }, f'{path}/{model.name}{model.version}.pt')

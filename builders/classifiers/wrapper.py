import os
import shutil
import torch

import numpy as np
from sklearn.metrics import average_precision_score, f1_score
from transformers import logging, AutoModel


logging.set_verbosity_error()


class BaseModel:
    def __init__(self, bert_model, device, module, module_parameters, 
                 optimizer, optimizer_parameters, criterion, 
                 criterion_parameters):
        self.device = device
        self.bert = AutoModel.from_pretrained(bert_model)
        self.module = module(**module_parameters)
        self.optimizer = optimizer(self.module.parameters(), **optimizer_parameters)
        self.criterion = criterion(**criterion_parameters)

        self.bert.to(device)
        self.module.to(device)

    def train(self, input_ids, attention_mask, target_ids, **kwargs):
        input_ids, attention_mask, target_ids = \
            torch.tensor(input_ids, device=self.device).unsqueeze(0), \
            torch.tensor(attention_mask, device=self.device).unsqueeze(0), \
            torch.tensor(target_ids, device=self.device, dtype=torch.float)

        with torch.no_grad():
            embedding = self.bert(input_ids, attention_mask).last_hidden_state.squeeze(0)

        output = self.module(embedding)
        loss = self.criterion(output, target_ids.unsqueeze(1))
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

        output = output.detach().cpu().tolist()
        return {
            'predicted': [1 if v[0] > .5 else 0 for v in output],
            'output': [v[0] for v in output], 
            'loss': loss.item()
        }
        
    def test(self, input_ids, attention_mask, target_ids, **kwargs):
        input_ids, attention_mask, target_ids = \
            torch.tensor(input_ids, device=self.device).unsqueeze(0), \
            torch.tensor(attention_mask, device=self.device).unsqueeze(0), \
            torch.tensor(target_ids, device=self.device, dtype=torch.float)

        with torch.no_grad():
            embedding = self.bert(input_ids, attention_mask).last_hidden_state.squeeze(0)

        output = self.module(embedding)
        loss = self.criterion(output, target_ids.unsqueeze(1))
        loss.backward()

        output = output.detach().cpu().tolist()
        return {
            'predicted': [1 if v[0] > .5 else 0 for v in output],
            'output': [v[0] for v in output], 
            'loss': loss.item()
        }

    def predict(self, input_ids, attention_mask, **kwargs):
        input_ids, attention_mask = \
            torch.tensor(input_ids, device=self.device).unsqueeze(0), \
            torch.tensor(attention_mask, device=self.device).unsqueeze(0)

        with torch.no_grad():
            embedding = self.bert(input_ids, attention_mask).last_hidden_state.squeeze(0)
            output = self.module(embedding).detach().cpu().tolist()

            return {
                'predicted': [1 if v[0] > .25 else 0 for v in output],
                'output': [v[0] for v in output], 
            }


class Model(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.t_losses = []
        self.v_losses = []
        self.t_pred = []
        self.v_pred = []
        self.t_output = []
        self.v_output = []
        self.t_target = []
        self.v_target = []

        self.stats_mem = []

    def train(self, sample):
        output = super().train(**sample)
        self.t_losses.append(output['loss'])
        self.t_target.extend(sample['target_ids'])
        self.t_pred.extend(output['predicted'])
        self.t_output.extend(output['output'])
        return output

    def test(self, sample):
        output = super().train(**sample)
        self.v_losses.append(output['loss'])
        self.v_target.extend(sample['target_ids'])
        self.v_pred.extend(output['predicted'])
        self.v_output.extend(output['output'])
        return output

    def predict(self, sample):
        return super().predict(**sample)

    def stats(self):
        stats = {
            't_loss': np.average(self.t_losses) if self.t_losses else 0,
            'v_loss':  np.average(self.v_losses) if self.v_losses else 0,
            't_f1': f1_score(self.t_target, self.t_pred),
            'v_f1': f1_score(self.v_target, self.v_pred),
            't_pr_auc': average_precision_score(self.t_target, self.t_output),
            'v_pr_auc': average_precision_score(self.v_target, self.v_output)
        }
        self.stats_mem.append(stats)

        self.t_losses = []
        self.v_losses = []
        self.t_pred = []
        self.v_pred = []
        self.t_output = []
        self.v_output = []
        self.t_target = []
        self.v_target = []

        return stats


def build_model(name, version, path, pretrained, **kwargs):
    model = Model(**kwargs)
    model.path = path

    if pretrained:
        try:
            loaded = torch.load(f'{path}/{name}.{version:05d}.pt')
        except FileNotFoundError:
            return None

        if loaded:
            model.name = loaded['name']
            model.version = loaded['version']
            model.module.load_state_dict(loaded['model_state_dict'])
            model.optimizer.load_state_dict(loaded['optimizer_state_dict'])
            model.stats_mem = loaded['stats_mem']

    else:
        shutil.rmtree(path, ignore_errors=True)
        model.name = name
        model.version = version
                
    return model


def save_model(model, path):
    os.makedirs(path, exist_ok=True)
    torch.save({
        'name': model.name,
        'version': model.version,
        'model_state_dict': model.module.state_dict(),
        'optimizer_state_dict': model.optimizer.state_dict(),
        'stats_mem': model.stats_mem,
    }, f'{path}/{model.name}.{model.version:05d}.pt')

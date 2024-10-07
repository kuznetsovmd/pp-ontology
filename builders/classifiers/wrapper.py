import os
import shutil
import torch

import numpy as np


class BaseModel:
    def __init__(self, device, module, module_parameters, 
                 optimizer, optimizer_parameters, criterion, 
                 criterion_parameters):
        self.device = device
        self.module = module(**module_parameters)
        self.optimizer = optimizer(self.module.parameters(), **optimizer_parameters)
        self.criterion = criterion(**criterion_parameters)

    def train(self, input_ids, attention_mask, target_ids, **kwargs):
        input_ids, attention_mask, target_ids = \
            torch.tensor(input_ids, device=self.device).unsqueeze(0), \
            torch.tensor(attention_mask, device=self.device).unsqueeze(0), \
            torch.tensor(target_ids, device=self.device, dtype=torch.float)

        output = self.module(input_ids, attention_mask)
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

        output = self.module(input_ids, attention_mask)
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
            output = self.module(input_ids, attention_mask).detach().cpu().tolist()

            return {
                'predicted': [1 if v[0] > .5 else 0 for v in output],
                'output': [v[0] for v in output], 
            }


class Model(BaseModel):
    def __accuracy(self, output, target):
        assert len(output) == len(target), 'outputs & targets not equally on length'
        return np.average(np.array(output) == np.array(target))
    
    def __f1score(self, output, target):
        assert len(output) == len(target), 'outputs & targets not equally on length'
        tp = np.sum((np.array(output) == 1) == (np.array(target) == 1))
        fp = np.sum((np.array(output) == 1) == (np.array(target) == 0))
        fn = np.sum((np.array(output) == 0) == (np.array(target) == 1))
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        return 0 if precision + recall == 0 else (2 * precision * recall) / (precision + recall)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.t_scores = []
        self.t_losses = []
        self.v_scores = []
        self.v_losses = []

        self.stats_mem = []

    def train(self, sample):
        output = super().train(**sample)
        self.t_losses.append(output['loss'])
        self.t_scores.append(self.__f1score(output['predicted'], sample['target_ids']))
        return output

    def test(self, sample):
        output = super().train(**sample)
        self.v_losses.append(output['loss'])
        self.v_scores.append(self.__f1score(output['predicted'], sample['target_ids']))
        return output

    def predict(self, sample):
        return super().predict(**sample)

    def stats(self):
        stats = {
            't_loss': np.average(self.t_losses) if self.t_losses else 0,
            'v_loss':  np.average(self.v_losses) if self.v_losses else 0,
            't_accuracy': np.average(self.t_scores) if self.t_scores else 0,
            'v_accuracy': np.average(self.v_scores) if self.v_scores else 0,
        }

        self.stats_mem.append(stats)

        self.t_losses = []
        self.t_scores = []
        self.v_losses = []
        self.v_scores = []

        return stats


def build_model(name, version, path, pretrained, **kwargs):
    model = Model(**kwargs)
    model.path = path

    if pretrained:
        loaded = torch.load(f'{path}/{name}.{version:05d}.pt')

        if loaded:
            print('OK!')
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

import itertools
import sys
import shutil
import contextlib
import os
import numpy as np
import torch
from tqdm import tqdm


class BaseModel:
    def __init__(self, **kwargs) -> None:
        self.module = kwargs['module'](**kwargs['module_parameters'])
        self.optimizer = kwargs['optimizer'](self.module.parameters(), **kwargs['optimizer_parameters'])
        self.criterion = kwargs['criterion'](**kwargs['criterion_parameters'])
    
    def train(self, source, target):
        loss_sum, outputs = 0, []

        data = list(zip(source, target)) 
        for s, t in tqdm(data, ncols=80, ascii=True):
            self.optimizer.zero_grad()

            s_gpu = torch.tensor(s, device=self.module.device)
            t_gpu = torch.tensor(t, device=self.module.device)
            output = self.module(s_gpu, t_gpu[:, :-1])

            predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)
            expected = t_gpu[:, 1:].contiguous().view(-1)
            loss = self.criterion(predicted, expected)
            loss_sum += loss
            loss.backward()
            self.optimizer.step()

            outputs.append(output.detach().cpu().numpy())

        return outputs, loss_sum / len(data)
    
    def test(self, source, target):
        loss_sum, outputs = 0, []

        data = list(zip(source, target)) 
        with torch.no_grad():
            for s, t in tqdm(data, ncols=80, ascii=True):
                s_gpu = torch.tensor(s, device=self.module.device)
                t_gpu = torch.tensor(t, device=self.module.device)
                output = self.module(s_gpu, t_gpu[:, :-1])

                predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)
                expected = t_gpu[:, 1:].contiguous().view(-1)
                loss = self.criterion(predicted, expected)
                loss_sum += loss

                outputs.append(output.detach().cpu().numpy())

        return outputs, loss_sum / len(source)

    def predict(self, source, target):
        s_gpu = torch.tensor(source, device=self.module.device)
        t_gpu = torch.tensor(target, device=self.module.device)
        t_mask = torch.ones((target.shape[0], 1), dtype=torch.uint8, device=self.module.device)
        sentence = np.empty((target.shape[0], 0), dtype=np.uint8)
        
        with torch.no_grad():
            for _ in itertools.count():
                output = self.module(s_gpu, t_gpu)
                predicted = torch.argmax(output[:, -1], 1).reshape(-1, 1)
                t_mask = torch.where((predicted == self.sep) | (predicted == self.eot), 0, 1) * t_mask
                tokens = predicted * t_mask
                t_gpu = torch.cat((t_gpu[:, 1:], tokens), 1)
                sentence = np.hstack((sentence, tokens.cpu()))
                
                if t_mask.sum() == 0:
                    break

        sentence = sentence.reshape(-1)
        return sentence[sentence > 0]


class Model(BaseModel):
    
    def __asses(self, output, target):
        o = np.argmax(np.vstack((*output,)), -1)[:, -1]
        t = np.vstack((*target,))[:, -1]
        return ((o == t) & np.isin(t, self.ignore_index, invert=True)).sum() / \
               (np.isin(t, self.ignore_index, invert=True)).sum()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sep = kwargs['sep']
        self.eot = kwargs['eot']
        self.name = kwargs['name']
        self.version = kwargs['version']
        self.ignore_index = kwargs['ignore_index']

        self.train_losses = []
        self.validation_losses = []
        self.train_accuracies = []
        self.validation_accuracies = []

    def train(self, source, target):
        output, loss = super().train(source, target)
        self.train_accuracies.append(self.__asses(output, target))
        self.train_losses.append(loss)
        return output, loss

    def test(self, source, target):
        output, loss = super().test(source, target)
        self.validation_accuracies.append(self.__asses(output, target))
        self.validation_losses.append(loss)
        return output, loss

    def predict(self, source, target):
        return super().predict(source, target)


def build_model(path=None, **kwargs):

    model = Model(**kwargs)

    if path:
        loaded = torch.load(f'{path}/{kwargs["name"]}{kwargs["version"]}.pt')

        if loaded:
            model.module.load_state_dict(loaded['model_state_dict'])
            model.optimizer.load_state_dict(loaded['optimizer_state_dict'])
            model.train_losses = loaded['train_losses']
            model.validation_losses = loaded['validation_losses']
            model.train_accuracies = loaded['train_accuracies']
            model.validation_accuracies = loaded['validation_accuracies']

    else:
        with contextlib.suppress(FileNotFoundError):
            os.remove(f'{path}/{kwargs["name"]}{kwargs["version"]}.pt')
        
    return model


def save_model(model, path):
    os.makedirs(path, exist_ok=True)
    torch.save({
        'model_state_dict': model.module.state_dict(),
        'optimizer_state_dict': model.optimizer.state_dict(),
        'train_losses': model.train_losses,
        'validation_losses': model.validation_losses,
        'train_accuracies': model.train_accuracies,
        'validation_accuracies': model.validation_accuracies,
    }, f'{path}/{model.name}{model.version}.pt')

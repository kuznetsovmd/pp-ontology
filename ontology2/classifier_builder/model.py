import itertools
import sys
import shutil
import contextlib
import os
import numpy as np
import torch
from tqdm import tqdm


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        self.module = kwargs['module'](**kwargs['module_parameters'])
        self.optimizer = kwargs['optimizer'](self.module.parameters(), **kwargs['optimizer_parameters'])
        self.criterion = kwargs['criterion'](**kwargs['criterion_parameters'])
        self.eot = kwargs['criterion'](**kwargs['criterion_parameters'])
    
    def train_unsupervised(self, source):
        loss_sum = 0
        outputs = []

        for s in tqdm(source, ncols=80, ascii=True):
            self.optimizer.zero_grad()

            s_gpu = torch.tensor(s, device=self.module.device)
            output = self.module(s_gpu, s_gpu[:, :-1])

            predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)
            expected = s_gpu[:, 1:].contiguous().view(-1)
            loss = self.criterion(predicted, expected)
            loss.backward()
            self.optimizer.step()

            loss_sum += loss
            outputs.append(output.detach().cpu())
        return outputs, loss_sum / len(source)
    
    def train_supervised(self, source, target):
        loss_sum = 0
        outputs = []

        data = list(zip(source, target)) 
        for s, t in tqdm(data, ncols=80, ascii=True):
            self.optimizer.zero_grad()

            s_gpu = torch.tensor(s, device=self.module.device)
            t_gpu = torch.tensor(t, device=self.module.device)
            output = self.module(s_gpu, t_gpu[:, :-1])

            predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)
            expected = t_gpu[:, 1:].contiguous().view(-1)
            loss = self.criterion(predicted, expected)
            loss.backward()
            self.optimizer.step()

            loss_sum += loss
            outputs.append(output.detach().cpu())
        return outputs, loss_sum / len(data)
    
    def test(self, source, target):
        loss_sum = 0
        outputs = []

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
                outputs.append(output.detach().cpu())
        return outputs, loss_sum / len(data)

    def predict(self, source, target, cls, sep, eot):
        sentence = np.empty((0,))
        s_gpu = torch.tensor(source, device=self.module.device)
        t_gpu = torch.tensor(target, device=self.module.device)
        
        i = 0 
        with torch.no_grad():
            for _ in range(300):
            # for _ in itertools.count():
                output = self.module(s_gpu[i, :].reshape(1, -1), t_gpu)
                predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)[-1]
                predicted_tensor = torch.argmax(predicted).unsqueeze(0).unsqueeze(1)
                
                token = predicted_tensor.item()
                if token == sep and i < s_gpu.shape[0] - 1:
                    i += 1 
                    t_gpu = torch.cat((t_gpu[:, 1:], torch.tensor(cls, device=self.module.device).reshape(1, 1)), 1)
                if token == eot:
                    break
                if token != sep:
                    sentence = np.append(sentence, token)
                    t_gpu = torch.cat((t_gpu[:, 1:], predicted_tensor), 1)
        return sentence


class Model(BaseModel):
    
    @staticmethod
    def __asses(output, target):
        l = np.empty((0,))
        r = np.empty((0,))
        for o, t in zip(output, target):
            predicted = np.array(torch.argmax(o[:, -2], 1))
            target = t[:, -2]
            l = np.append(l, (target > 0).sum())
            r = np.append(r, ((predicted == target) & (target > 0)).sum())
        return sum(r) / sum(l)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs['name']
        self.version = kwargs['version']

        self.train_losses = []
        self.validation_losses = []
        self.train_accuracies = []
        self.validation_accuracies = []

    def train_unsupervised(self, source):
        output, loss = super().train_unsupervised(source)
        self.train_accuracies.append(self.__asses(output, source))
        self.train_losses.append(loss)
        return output, loss

    def train_supervised(self, source, target):
        output, loss = super().train_supervised(source, target)
        self.train_accuracies.append(self.__asses(output, target))
        self.train_losses.append(loss)
        return output, loss

    def test(self, source, target):
        output, loss = super().test(source, target)
        self.validation_accuracies.append(self.__asses(output, target))
        self.validation_losses.append(loss)
        return output, loss

    def predict(self, source, target, cls, sep, eot):
        return super().predict(source, target, cls,  sep, eot)


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
        # for name, param in model.module.named_parameters():
        #     if 'weight' in name and param.data.dim() == 2:
        #         torch.nn.init.uniform_(param)

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

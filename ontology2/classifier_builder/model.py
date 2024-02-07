import itertools
import contextlib
import os
import numpy as np
import torch


class BaseModel:
    def __init__(self, **kwargs) -> None:
        self.module = kwargs['module'](**kwargs['module_parameters'])
        self.optimizer = kwargs['optimizer'](self.module.parameters(), **kwargs['optimizer_parameters'])
        self.criterion = kwargs['criterion'](**kwargs['criterion_parameters'])
    
    def train(self, source, target):
        s_gpu = torch.tensor(source, device=self.module.device)
        t_gpu = torch.tensor(target, device=self.module.device)
        output = self.module(s_gpu, t_gpu[:, :-1])

        predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)
        expected = t_gpu[:, 1:].contiguous().view(-1)
        loss = self.criterion(predicted, expected)
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

        return output.detach().cpu().numpy(), loss
    
    def test(self, source, target):
        with torch.no_grad():
            s_gpu = torch.tensor(source, device=self.module.device)
            t_gpu = torch.tensor(target, device=self.module.device)
            output = self.module(s_gpu, t_gpu[:, :-1])

            predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)
            expected = t_gpu[:, 1:].contiguous().view(-1)
            loss = self.criterion(predicted, expected)

        return output.detach().cpu().numpy(), loss

    def predict(self, source, target):
        s_gpu = torch.tensor(source, device=self.module.device)
        t_gpu = torch.tensor(target, device=self.module.device)
        t_mask = torch.ones((target.shape[0], 1), dtype=torch.uint8, device=self.module.device)
        sentence = np.empty((target.shape[0], 0), dtype=np.uint8)
        
        with torch.no_grad():
            # for _ in itertools.count():
            for _ in range(200):
                output = self.module(s_gpu, t_gpu)
                predicted = torch.argmax(output[:, -1], 1).reshape(-1, 1)
                t_mask = torch.where((predicted == self.sep), 0, 1) * t_mask

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
        self.name = kwargs['name']
        self.version = kwargs['version']
        self.ignore_index = kwargs['ignore_index']

        self.t_outputs = []
        self.t_targets = []
        self.t_losses = []
        self.v_outputs = []
        self.v_targets = []
        self.v_losses = []

        self.stats_mem = []

    def train(self, source, target):
        output, loss = super().train(source, target)
        self.t_outputs.append(output)
        self.t_targets.append(target)
        self.t_losses.append(loss.item())
        return output, loss

    def test(self, source, target):
        output, loss = super().test(source, target)
        self.v_outputs.append(output)
        self.v_targets.append(target)
        self.v_losses.append(loss.item())
        return output, loss

    def predict(self, source, target):
        return super().predict(source, target)

    def stats(self):
        stats = {
            't_loss': np.average(self.t_losses) if self.t_losses else 0,
            'v_loss':  np.average(self.v_losses) if self.v_losses else 0,
            't_accuracy': self.__asses(self.t_outputs, self.t_targets) if self.t_outputs else 0,
            'v_accuracy': self.__asses(self.v_outputs, self.v_targets) if self.v_outputs else 0,
        }

        self.stats_mem.append(stats)

        self.t_losses = []
        self.v_losses = []
        self.t_outputs = []
        self.v_outputs = []
        self.t_targets = []
        self.v_targets = []

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
            os.remove(f'{path}/{kwargs["name"]}{kwargs["version"]}.pt')
        
    return model


def save_model(model, path):
    os.makedirs(path, exist_ok=True)
    torch.save({
        'model_state_dict': model.module.state_dict(),
        'optimizer_state_dict': model.optimizer.state_dict(),
        'stats_mem': model.stats_mem,
    }, f'{path}/{model.name}{model.version}.pt')

import shutil
import os
import numpy as np
import torch
from tqdm import tqdm


class BaseModel:
    def train(self, source, target):
        predictions = np.ndarray((0, 2))
        for s, t in tqdm(list(zip(source, target)), ncols=80, ascii=True):
            self.optimizer.zero_grad()

            s_gpu = torch.tensor(s, device=self.module.device)
            t_gpu = torch.tensor(t, device=self.module.device)
            output = self.module(s_gpu, t_gpu[:, :-1])

            predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)
            expected = t_gpu[:, 1:].contiguous().view(-1)
            loss = self.criterion(predicted, expected)
            loss.backward()
            self.optimizer.step()
            
            val_1 = torch.argmax(output[:, -2], 1).cpu().reshape(-1, 1)
            val_2 = t[:, -2].reshape(-1, 1)
            predictions = np.vstack((predictions, np.hstack((val_1, val_2))))
        return predictions, loss

    def test(self, source, target):
        predictions = np.ndarray((0, 2))
        with torch.no_grad():
            for s, t in tqdm(list(zip(source, target)), ncols=80, ascii=True):
                s_gpu = torch.tensor(s, device=self.module.device)
                t_gpu = torch.tensor(t, device=self.module.device)
                output = self.module(s_gpu, t_gpu[:, :-1])

                predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)
                expected = t_gpu[:, 1:].contiguous().view(-1)
                loss = self.criterion(predicted, expected)
                
                val_1 = torch.argmax(output[:, -2], 1).cpu().reshape(-1, 1)
                val_2 = t[:, -2].reshape(-1, 1)
                predictions = np.vstack((predictions, np.hstack((val_1, val_2))))
        return predictions, loss

    def predict(self, source, target, eot):
        sentence = np.empty((0,))
        t_gpu = torch.tensor(target, device=self.module.device)
        with torch.no_grad():
            for _ in range(200):
                s_gpu = torch.tensor(source, device=self.module.device)
                output = self.module(s_gpu, t_gpu)
                predicted = output.contiguous().view(-1, self.module.decoder_embedding.num_embeddings)[-1]
                predicted_word = torch.argmax(predicted).unsqueeze(0).unsqueeze(1)

                sentence = np.append(sentence, predicted_word.item())
                if sentence[-1] == eot:
                    break
                t_gpu = torch.cat((t_gpu[:, 1:], predicted_word), 1)
        return sentence


class Model(BaseModel):
    
    @staticmethod
    def __asses(output):
        res = [o[0] == o[1] for o in output if o[1] != 0]
        return sum(res) / len(res)
    
    def __init__(self):
        super().__init__()
        self.last_epoch = 0
        self.train_iters = 0
        self.validation_iters = 0
        self.train_loss = 0
        self.validation_loss = 0
        self.train_accuracy = []
        self.validation_accuracy = []
        self.train_losses = []
        self.validation_losses = []
        self.train_accuracies = []
        self.validation_accuracies = []

    def train(self, source, target):
        s, t = self.batcher.pack(source, target)
        output, loss = super().train(s, t)
        self.train_accuracy.append(self.__asses(output))
        self.train_loss += loss
        self.train_iters += 1
        return output, loss

    def test(self, source, target):
        s, t = self.batcher.pack(source, target)
        output, loss = super().test(s, t)
        self.validation_accuracy.append(self.__asses(output))
        self.validation_loss += loss
        self.validation_iters += 1
        return output, loss

    def predict(self, sample, eot):
        s, t = self.batcher.pack(sample)
        return super().predict(s, t, eot)
        
    def epoch(self):
        self.train_losses.append(self.train_loss / self.train_iters)
        self.validation_losses.append(self.validation_loss / self.validation_iters)
        self.train_accuracies.append(sum(self.train_accuracy) / len(self.train_accuracy))
        self.validation_accuracies.append(sum(self.validation_accuracy) / len(self.validation_accuracy))

        self.train_iters = 0
        self.validation_iters = 0

        self.train_loss = 0
        self.validation_loss = 0
        self.train_accuracy = []
        self.validation_accuracy = []

        self.last_epoch += 1


def build_model(*args, **kwargs):
    model = Model()
    model.module = kwargs['module'](**kwargs['module_parameters'])
    model.optimizer = kwargs['optimizer'](model.module.parameters(), **kwargs['optimizer_parameters'])
    model.criterion = kwargs['criterion'](**kwargs['criterion_parameters'])
    model.batcher = kwargs['batcher']
    model.path = kwargs['path']

    if kwargs['pretrained']:
        loaded = torch.load(f'{kwargs["path"]}.pt')

        if loaded:
            model.module.load_state_dict(loaded['model_state_dict'])
            model.optimizer.load_state_dict(loaded['optimizer_state_dict'])
            model.last_epoch = loaded['last_epoch']
            model.train_losses = loaded['train_losses']
            model.validation_losses = loaded['validation_losses']
            model.train_accuracies = loaded['train_accuracies']
            model.validation_accuracies = loaded['validation_accuracies']

    else:
        shutil.rmtree(os.path.dirname(model.path), ignore_errors=True)

    return model


def save_model(model, version=''):
    version = f'_{version}' if version else ''
    os.makedirs(os.path.dirname(model.path), exist_ok=True)
    torch.save({
        'last_epoch': model.last_epoch,
        'model_state_dict': model.module.state_dict(),
        'optimizer_state_dict': model.optimizer.state_dict(),
        'train_losses': model.train_losses,
        'validation_losses': model.validation_losses,
        'train_accuracies': model.train_accuracies,
        'validation_accuracies': model.validation_accuracies,
    }, f'{model.path}{version}.pt')

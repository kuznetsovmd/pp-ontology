import torch
from torch import nn
from torch.nn import functional


class LinearBERT(nn.Module):
    def __init__(self, input_size=768, hidden_size=512, output_size=2, dropout=0.1, device='cpu'):
        super(LinearBERT, self).__init__()

        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)
        
        self.to(device)

    def forward(self, embedding):
        output = functional.relu(self.fc1(embedding))
        output = self.dropout(output)
        return self.fc2(output)


class Linear2BERT(nn.Module):
    def __init__(self, input_size=768, hidden_size=512, output_size=2, dropout=0.1, device='cpu'):
        super(Linear2BERT, self).__init__()

        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)
        nn.init.xavier_uniform_(self.fc3.weight)
        
        self.to(device)

    def forward(self, embedding):
        output = functional.relu(self.fc1(embedding))
        output = self.dropout(output)
        output = functional.relu(self.fc2(output))
        output = self.dropout(output)
        return self.fc3(output)


class Linear3BERT(nn.Module):
    def __init__(self, input_size=768, hidden_size=512, output_size=2, dropout=0.1, device='cpu'):
        super(Linear3BERT, self).__init__()

        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, hidden_size)
        self.fc4 = nn.Linear(hidden_size, output_size)
        
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)
        nn.init.xavier_uniform_(self.fc3.weight)
        nn.init.xavier_uniform_(self.fc4.weight)
        
        self.to(device)

    def forward(self, embedding):
        output = functional.relu(self.fc1(embedding))
        output = self.dropout(output)
        output = functional.relu(self.fc2(output))
        output = self.dropout(output)
        output = functional.relu(self.fc3(output))
        output = self.dropout(output)
        return self.fc4(output)
    

class RNN_BERT(nn.Module):
    def __init__(self, input_size=768, hidden_size=512, output_size=2, dropout=0.1, device='cpu'):
        super(RNN_BERT, self).__init__()
        self.hidden_size = hidden_size
        self.device = device

        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(input_size + hidden_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)

        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)
        nn.init.xavier_uniform_(self.fc3.weight)

        self.init_hidden()
        self.to(device)

    def forward(self, embedding):
        self.hidden = torch.cat((embedding, self.hidden), 1)
        self.hidden = self.dropout(self.hidden)
        self.hidden = functional.relu(self.fc1(self.hidden))
        self.hidden = self.dropout(self.hidden)
        self.hidden = functional.relu(self.fc2(self.hidden))
        return self.fc3(self.dropout(self.hidden))

    def init_hidden(self):
        self.hidden = torch.zeros(1, self.hidden_size, device=self.device)
        
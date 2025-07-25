from torch import nn
from torch.nn import functional


class LinearBERT(nn.Module):
    def __init__(self, input_size=768, hidden_size=512, output_size=1, dropout=0.1):
        super(LinearBERT, self).__init__()

        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
        
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)
        
    def forward(self, embedding):
        output = functional.relu(self.fc1(embedding))
        output = self.dropout(output)
        return self.sigmoid(self.fc2(output))


class Linear2BERT(nn.Module):
    def __init__(self, input_size=768, hidden_size=512, output_size=1, dropout=0.1):
        super(Linear2BERT, self).__init__()

        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
        
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)
        nn.init.xavier_uniform_(self.fc3.weight)
        
    def forward(self, embedding):
        output = functional.relu(self.fc1(embedding))
        output = self.dropout(output)
        output = functional.relu(self.fc2(output))
        output = self.dropout(output)
        return self.sigmoid(self.fc3(output))


class Linear3BERT(nn.Module):
    def __init__(self, input_size=768, hidden_size=512, output_size=1, dropout=0.1):
        super(Linear3BERT, self).__init__()

        self.dropout = nn.Dropout(dropout)
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, hidden_size)
        self.fc4 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
        
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)
        nn.init.xavier_uniform_(self.fc3.weight)
        nn.init.xavier_uniform_(self.fc4.weight)
        
    def forward(self, embedding):
        output = functional.relu(self.fc1(embedding))
        output = self.dropout(output)
        output = functional.relu(self.fc2(output))
        output = self.dropout(output)
        output = functional.relu(self.fc3(output))
        output = self.dropout(output)
        return self.sigmoid(self.fc4(output))
        
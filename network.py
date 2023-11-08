import numpy as np
import torch
import torch.nn as nn


class FeedForwardNN(nn.Module):
    def __init__(self, input_dim, out_dim):
        super(FeedForwardNN, self).__init__()

        self.layer1 = nn.Linear(input_dim, 64)
        self.layer2 = nn.Linear(64, 64)
        self.layer3 = nn.Linear(64, out_dim)
        self.relu = nn.ReLU()

    
    def forward(self, obs):
        # convert observation to tensor if it's a numpy array
        if isinstance(obs, np.ndarray):
            obs = torch.tensor(obs, dtype=torch.float)

        activation1 = self.relu(self.layer1(obs))
        activation2 = self.relu(self.layer2(activation1))
        output = self.layer3(activation2)

        return output

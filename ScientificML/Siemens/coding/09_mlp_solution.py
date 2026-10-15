"""09. Small modules — SOLUTION.

nn.Linear registers weight and bias. ReLU has no parameters.
The residual add requires the second linear to emit the same width as x.
""",

import torch
import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, d_in, d_hidden, d_out):
        super().__init__()
        self.fc1 = nn.Linear(d_in, d_hidden)
        self.fc2 = nn.Linear(d_hidden, d_out)

    def forward(self, x):
        return self.fc2(torch.relu(self.fc1(x)))


class ResidualMLP(nn.Module):
    def __init__(self, d, d_hidden):
        super().__init__()
        self.fc1 = nn.Linear(d, d_hidden)
        self.fc2 = nn.Linear(d_hidden, d)

    def forward(self, x):
        return x + self.fc2(torch.relu(self.fc1(x)))


if __name__ == "__main__":
    mlp = MLP(4, 8, 2)
    y = mlp(torch.randn(3, 4))
    assert y.shape == (3, 2)
    assert any(p.requires_grad for p in mlp.parameters())
    block = ResidualMLP(4, 8)
    x = torch.randn(3, 4)
    assert block(x).shape == x.shape
    print("09_mlp_solution: ok")

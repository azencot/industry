"""G. LayerNorm by hand — PROBLEM. Wednesday, after group attention.

No solution file. Do not call nn.LayerNorm inside forward.
You may use nn.LayerNorm only in a test, as the reference.

    x: [..., D]
    return [..., D]

Normalize over the last dimension only.
mean = average of x over D
variance = average of (x - mean)^2 over D
         divide by D, not by D - 1
normalized = (x - mean) / sqrt(variance + eps)
output = normalized * weight + bias

weight and bias are parameters of shape [D].
A new module starts with weight 1 and bias 0, so it matches a new
nn.LayerNorm(D) before any training.
eps defaults to 1e-5.

Write these tests before you trust it:
- output shape equals input shape, including a leading batch and time
- batch size 1, and a single vector of shape [D]
- a fresh module matches nn.LayerNorm on the same input
- after changing weight and bias, the output changes and still matches
  nn.LayerNorm with those same parameters copied in
- gradients reach x, weight, and bias
- D = 1 does not divide by zero

Time box: 25 minutes.
"""

import torch
from torch import nn


class LayerNorm(nn.Module):
    def __init__(self, d, eps=1e-5):
        super().__init__()

        assert d != 0
        
        self.d = d
        self.eps = eps

        self.weight = nn.Parameter(torch.ones(d))
        self.bias = nn.Parameter(torch.zeros(d))

    def forward(self, x):
        # x in [..., d]
        assert x.shape[-1] == self.d

        mean = torch.sum(x, dim=-1, keepdim=True) / self.d            # [..., d] -> [..., 1]
        var = torch.sum((x - mean) ** 2, dim=-1, keepdim=True) / self.d       # [..., d] -> [.... 1]
        normalized = (x - mean) / torch.sqrt(var + self.eps)          # [..., d] - [..., 1] / [..., 1] -> [..., d]

        return normalized * self.weight + self.bias                   # [..., d] * [..., d] + [..., d] -> [..., d]

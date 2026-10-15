"""09. Small modules — PROBLEM.

Do not open 09_mlp_solution.py until this file runs.

MLP: Linear -> ReLU -> Linear. forward(x) with x [..., d_in] -> [..., d_out].

ResidualMLP: same hidden width, but the second Linear maps back to d,
and the block returns x + f(x). d_in must equal d_out or the add fails.

Use nn.Module, super().__init__, and registered submodules.
A tensor you assign as self.w = torch.zeros(...) is NOT a parameter.
""",

import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, d_in, d_hidden, d_out):
        super().__init__()
        raise NotImplementedError

    def forward(self, x):
        raise NotImplementedError


class ResidualMLP(nn.Module):
    def __init__(self, d, d_hidden):
        super().__init__()
        raise NotImplementedError

    def forward(self, x):
        raise NotImplementedError

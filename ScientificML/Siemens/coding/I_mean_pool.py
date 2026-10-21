"""I. Mean-pool classifier — PROBLEM.

No solution file.

    token_ids: [B, T] long
    return logits [B, C]

Embed each id to D, average over T, then a linear map to C classes.
Every position counts. Sequences in a batch have the same T.

Write these tests before you trust it:
- output shape is [B, C], including batch size 1
- swapping two time positions does not change the logits
- gradients reach the embedding weight and the linear weight
- a row of identical ids does not error

Time box: 20 minutes.
"""

import torch
from torch import nn


class MeanPoolClassifier(nn.Module):
    def __init__(self, n_tokens, d, n_classes):
        super().__init__()
        raise NotImplementedError

    def forward(self, token_ids):
        raise NotImplementedError

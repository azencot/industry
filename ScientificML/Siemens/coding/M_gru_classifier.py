"""M. Variable-length GRU classifier — PROBLEM.

No solution file. Thursday 22, after K if the morning is on time.

    x:       [B, T, D]   right-padded
    lengths: [B] long    lengths[i] is the valid prefix of row i
    return logits [B, C]

Use nn.GRU and nn.Linear. Do not softmax.

The vector you classify must be the hidden state at the last valid
step of that row, not a state that has consumed the padding.
For a right-padded sequence, the final hidden state returned by an
unpacked GRU is the state after the padded steps. That is not the
state at lengths[i] - 1 unless the sequence was packed, or you index
the step outputs yourself.

Tests to write before you trust it:
- logits are [B, C], including B = 1
- two different lengths in one batch both run
- gradients reach the GRU and the linear layer
- editing a padded step does not change the logits

Time box: 20–25 minutes. If pack_padded_sequence is unfamiliar, index
the valid step. Do not spend the block memorizing the packing API.
One follow-up after it runs.
"""

import torch
from torch import nn


class GRUClassifier(nn.Module):
    def __init__(self, d, hidden, n_classes):
        super().__init__()
        raise NotImplementedError

    def forward(self, x, lengths):
        raise NotImplementedError

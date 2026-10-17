"""17. Attention across the series axis — PROBLEM.

Do not open 17_group_attention_solution.py until this file runs.

The sequence axis is not time. That is the only new idea.

    x: [B, G, T, D]
        B = batch of groups
        G = series inside the group (variates, or target + covariates)
        T = time (or patches)
        D = channels
    series_mask: [B, G] bool, True = valid series. Optional.
    return [B, G, T, D]

At each time index, independently, attend across G.
Do not attend across T.

Say the reshape out loud before you write it:
[B, G, T, D] -> [B, T, G, D] -> [B*T, G, D], attend, then invert.

Mask invalid series as keys before softmax. Queries still attend.
An all-invalid group comes out as zeros, not NaN.

If every series in a group is the same vector, the output equals the input.
If only series 0 is valid, every series in that group comes out equal
to series 0. The other series are not zeroed. Zero is only for a group
with no valid key.
"""

import torch


def group_attention(x, series_mask=None):
    raise NotImplementedError

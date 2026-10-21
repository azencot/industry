"""17. Attention across the series axis — PROBLEM. Wednesday, part A.

Do not open 17_group_attention_solution.py until this file runs.
After this runs, do 17b (cross-group), then 17c (multi-head). Do not open those first.

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
import math

def group_attention(x, series_mask=None):
    # the idea is the same as standard attention, but on the group dim instead of time dim

    # x in [B, G, T, D]
    B, G, T, D = x.shape

    # transpose/reshape
    x = x.transpose(2, 1).reshape(-1, G, D).contiguous()    # [B, G, T, D] -> [B*T, G, D]
    
    scores = x @ x.transpose(-2, -1) / math.sqrt(D)         # [B*T, G, D] @ [B*T, D, G] -> [B*T, G, G]

    if series_mask is not None:                             # [B, G]
        series_mask = series_mask.repeat_interleave(T, dim=0)   # [B, G] -> [B*T, G]
        scores = scores.masked_fill(~series_mask[:, None, :], float("-inf"))

    a = torch.softmax(scores, dim=-1)                       # [B*T, G, G] -> [B*T, G, G]
    a = torch.nan_to_num(a, nan=0.0)                        # [B*T, G, G] -> [B*T, G, G]
    y = a @ x                                               # [B*T, G, G] @ [B*T, G, D] -> [B*T, G, D]

    # reshape/transpose
    y = y.reshape(B, T, G, D).contiguous().transpose(2,1)   # [B*T, G, D] -> [B, T, G, D] -> [B, G, T, D]

    return y
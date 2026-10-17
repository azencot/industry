"""17c. Multi-head cross-group attention — PROBLEM. Wednesday, after 17b.

Do not open 17c_group_multihead_solution.py until this file runs.

Same task as 17b, with H heads. D must divide H.

    q:        [B, Gq, T, D]
    kv:       [B, Gk, T, D]
    key_mask: [B, Gk] bool, True = valid key. Optional.
    return    [B, Gq, T, D]

Internal shape to say out loud: [B, T, H, G, Dh]
Score shape:                     [B, T, H, Gq, Gk]
Softmax over Gk.
key_mask [B, Gk] has to broadcast onto that score. State the view you use.

Which two axes does transpose hit on the keys? Say it before you write it.
Dh, not D, is the scale.
"""

import torch


def cross_group_multihead(q, kv, n_heads, key_mask=None):
    raise NotImplementedError

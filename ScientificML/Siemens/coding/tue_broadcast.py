"""Tuesday mask / broadcasting micro-drills. About 30 minutes.

Do not open tue_broadcast_solution.py until this file runs.
True = valid in every function. Say that before each one.

A. scores [B, H, Tq, Tk], key_mask [B, Tk] -> same shape, invalid keys -inf
B. x [B, T, D], mask [B, T] -> masked mean over T, [B, D]
C. scores [B, T, Gq, Gk], key_mask [B, Gk] -> same shape, invalid keys -inf
D. scores [B, H, T, T], padding_mask [B, T]
   Combine a causal mask (j > i blocked) with the padding mask.
   A position survives only if it is causal AND the key is valid.
"""

import torch


def mask_attn_keys(scores, key_mask):
    return scores.masked_fill(~key_mask[:, None, None, :], float("-inf"))


def masked_mean_time(x, mask):
    m = mask.unsqueeze(-1)
    lengths = m.sum(dim=1).clamp_min(1)
    
    return x.masked_fill(~m, 0).sum(dim=1) / lengths


def mask_group_keys(scores, key_mask):
    raise NotImplementedError


def mask_causal_and_padding(scores, padding_mask):
    Mp = ~padding_mask[:, None, None, :]
    
    T = scores.shape[-1]
    Mc = torch.triu(torch.ones([T, T], dtype=bool, device=scores.device), diagonal=1)

    return scores.masked_fill(Mp | Mc, float("-inf"))

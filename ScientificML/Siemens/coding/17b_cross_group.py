"""17b. Cross-group attention — PROBLEM. Wednesday follow-up to 17.

Do not open 17b_cross_group_solution.py until this file runs.
Do not start here. Finish 17_group_attention.py first.

    q:        [B, Gq, T, D]
    kv:       [B, Gk, T, D]
    key_mask: [B, Gk] bool, True = valid key. Optional.
    return    [B, Gq, T, D]

At each time independently, queries from Gq attend to keys and values from Gk.
Do not attend across T.

Narrate before coding:
- query axis, key axis
- score shape: [B, T, Gq, Gk] after the rearrange (or [B*T, Gq, Gk] if you flatten time into the batch)
- which axis softmax uses (Gk)
- how key_mask [B, Gk] broadcasts onto that score
- how the result goes back to [B, Gq, T, D]

Same mask rules as 17. An all-invalid key group comes out as zeros, not NaN.
If only key 0 is valid, every query comes out equal to that key's vector.
"""

import torch


def cross_group_attention(q, kv, key_mask=None):
    raise NotImplementedError

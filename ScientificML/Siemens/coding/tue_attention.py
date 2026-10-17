"""Tuesday blank-file attention. 20 minute hard cap.

New empty buffer. No notes. No autocomplete if you can turn it off.
Do not open tue_attention_solution.py until this file runs.

If this is clean in under 15 minutes, do not practice vanilla attention again.

scaled_dot_product_attention(q, k, v, key_padding_mask=None, causal=False)

    q: [B, H, Tq, Dh]
    k: [B, H, Tk, Dh]
    v: [B, H, Tk, Dv]
    key_padding_mask: [B, Tk] bool, True = valid key. Optional.
    return [B, H, Tq, Dv]

Must use k.transpose(-2, -1), scale by sqrt(Dh), masked_fill, softmax(dim=-1).
Invalid logits are -inf, not 0. An all-invalid row comes out as zeros, not NaN.
Causal: query i cannot attend to key j > i. Tq and Tk may differ.

Narrate every shape out loud.
"""

import torch
import math

def scaled_dot_product_attention(q, k, v, key_padding_mask=None, causal=False):
    # mul and normalize
    scores = q @ k.transpose(-2, -1) / math.sqrt(q.shape[-1])       # [B, H, Tq, Dh] @ [B, H, Dh, Tk] -> [B, H, Tq, Tk]

    # prepare masks, note valid vs invalid
    B, Tq, Tk = q.shape[0], q.shape[-2], k.shape[-2]

    Mp = torch.zeros([B, 1, 1, Tk], dtype=bool).to(q.device)
    if key_padding_mask is not None:
        Mp = ~key_padding_mask[:, None, None, :]

    Mc = torch.zeros([1, 1, Tq, Tk], dtype=bool).to(q.device)
    if causal:
        Mc = torch.triu(torch.ones([Tq, Tk], dtype=bool).to(q.device), diagonal=1)                                     # TODO: not sure about the syntax
        Mc = Mc[None, None, :, :]                                   # [1, 1, Tq, Tk]

    scores = scores.masked_fill(Mp | Mc, float("-inf"))

    # apply softmax
    a = torch.softmax(scores, dim=-1)
    a = torch.nan_to_num(a, nan=0.0)

    # scale v and return
    return a @ v                            # [??] @ [B, H, Tk, Dv] -> [B, H, Tq, Dv]
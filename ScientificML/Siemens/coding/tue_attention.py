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


def scaled_dot_product_attention(q, k, v, key_padding_mask=None, causal=False):
    raise NotImplementedError

"""3. Masked cross-attention — PROBLEM.

Single-head cross-attention.

    q:   [B, Tq, D]
    kv:  [B, Tk, D]
    mask [B, Tk] optional, True = valid token, False = pad / missing

    return [B, Tq, D]

Shapes to write down before coding:

    Q, K, V     [B, Tq, D], [B, Tk, D], [B, Tk, D]
    scores      [B, Tq, Tk]   = Q K^T / sqrt(D)
    attn        [B, Tq, Tk]
    out         [B, Tq, D]

Complexity: O(Tq * Tk * D).

Why this vs concat self-attention: text length T_text attending to modality
tokens T_mod is O(T_text * T_mod), not O((T_text + T_mod)^2).

Assumptions:
- One head; linear maps to the same D.
- Name projections self.wq / self.wk / self.wv (tests inspect them).
- mask True means keep, False means fill scores with -inf before softmax.
- All-masked keys: softmax(-inf) is NaN — mention it; a production version
  needs a fallback.

Requires PyTorch. Same interpreter as ../code/day1_attention.py.

Follow-ups:
1. Why divide by sqrt(D)?
2. What changes for multi-head?
3. What if Tk is 100,000?
4. Insert a latent resampler before this.
5. How do you test whether the model is ignoring kv?
"""

from __future__ import annotations

import math

import torch
import torch.nn as nn


class CrossAttention(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        
        self.wq = nn.Linear(d_model, d_model)
        self.wk = nn.Linear(d_model, d_model)
        self.wv = nn.Linear(d_model, d_model)

        self.d_model = d_model

    def forward(self, q, kv, mask=None):
        # q in [B, Tq, d_model], kv in [B, Tk, d_model], mask in [B, Tk]
        
        # obtain Q, K, V
        Q = self.wq(q)      # [B, Tq, d_model]
        K = self.wk(kv)     # [B, Tk, d_model]
        V = self.wv(kv)     # [B, Tk, d_model]

        # compute attention scores
        QKT = (Q @ K.transpose(-2, -1)) / math.sqrt(self.d_model)         # [B, Tq, Tk]
        if mask is not None:
            QKT = QKT.masked_fill(~mask[:, None, :], float("-inf"))   
        A = torch.softmax(QKT, dim=-1)                                  # [B, Tq, Tk]

        # compute weighted sum
        Y = A @ V           # [B, Tq, d_model]

        # return Y
        return Y


if __name__ == "__main__":
    torch.manual_seed(0)
    B, Tq, Tk, D = 2, 3, 5, 8
    attn = CrossAttention(D)
    q = torch.randn(B, Tq, D)
    kv = torch.randn(B, Tk, D)
    out = attn(q, kv)
    assert tuple(out.shape) == (B, Tq, D), tuple(out.shape)

    mask = torch.ones(B, Tk, dtype=torch.bool)
    mask[:, -2:] = False
    out_m = attn(q, kv, mask=mask)
    assert tuple(out_m.shape) == (B, Tq, D)

    # With only the first key valid, output should equal the projected V of that key.
    V = attn.wv(kv)
    one_key = torch.zeros(B, Tk, dtype=torch.bool)
    one_key[:, 0] = True
    out_one = attn(q, kv, mask=one_key)
    torch.testing.assert_close(out_one, V[:, 0:1, :].expand_as(out_one), atol=1e-5, rtol=1e-5)
    print("03_cross_attention: PASS")

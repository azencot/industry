"""3. Masked cross-attention — SOLUTION.

    scores = (Q K^T) / sqrt(D)
    scores = masked_fill(~mask[:, None, :], -inf)
    out    = softmax(scores, last dim) @ V

    Time  O(B * Tq * Tk * D)
    Space O(B * Tq * Tk) for the score matrix

mask is a *validity* mask on keys (pad / missing modality), not causal.

Concatenated self-attention on [text; modality] is
O((T_text + T_mod)^2). Cross-attention from text queries to modality
keys is O(T_text * T_mod). That is why Flamingo-style fusion exists.

All-False mask row -> softmax(-inf) = NaN. Production code should use
a tiny epsilon, or a boolean "any valid key" fallback to zeros.

Follow-ups:
1. sqrt(D): unscaled QK^T has variance ~D if components are O(1);
   softmax saturates to one-hot. Scale keeps the distribution usable.
2. Multi-head: split D into H heads of d = D/H, attn per head, concat,
   output projection. Scores become [B, H, Tq, Tk].
3. Tk = 1e5: materializing Tq*Tk is the bottleneck. Perceiver / Q-Former
   / latent resampler first, or chunked / memory-efficient attention.
4. Resampler: a small set of learned latents cross-attend to kv, then
   the LLM attends to the latents. Tk_eff becomes N_latents.
5. Neglect test: zero / shuffle / dropout kv at eval and watch the
   metric. If it does not move, fusion is a no-op.

Requires PyTorch. Same interpreter as [`../code/day1_attention.py`](../code/day1_attention.py).
"""

from __future__ import annotations

import math

try:
    import torch
    import torch.nn as nn
except ImportError:
    torch = None
    nn = None


if nn is not None:

    class CrossAttention(nn.Module):

        def __init__(self, d_model):
            super().__init__()
            self.wq = nn.Linear(d_model, d_model)
            self.wk = nn.Linear(d_model, d_model)
            self.wv = nn.Linear(d_model, d_model)

        def forward(self, q, kv, mask=None):
            Q = self.wq(q)
            K = self.wk(kv)
            V = self.wv(kv)

            scores = torch.matmul(Q, K.transpose(-2, -1))
            scores = scores / math.sqrt(Q.shape[-1])

            if mask is not None:
                # mask: [B, Tk] -> [B, 1, Tk] broadcasts over Tq
                scores = scores.masked_fill(~mask[:, None, :], float("-inf"))

            attn = torch.softmax(scores, dim=-1)
            return torch.matmul(attn, V)


if __name__ == "__main__":
    if torch is None:
        print("03_cross_attention_solution: SKIP (no torch in this interpreter)")
    else:
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
        assert torch.isfinite(out_m).all()

        V = attn.wv(kv)
        one_key = torch.zeros(B, Tk, dtype=torch.bool)
        one_key[:, 0] = True
        out_one = attn(q, kv, mask=one_key)
        torch.testing.assert_close(
            out_one, V[:, 0:1, :].expand_as(out_one), atol=1e-5, rtol=1e-5
        )

        Q = attn.wq(q)
        K = attn.wk(kv)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(D)
        scores = scores.masked_fill(~mask[:, None, :], float("-inf"))
        weights = torch.softmax(scores, dim=-1)
        torch.testing.assert_close(weights.sum(dim=-1), torch.ones(B, Tq))
        print("03_cross_attention_solution: PASS")

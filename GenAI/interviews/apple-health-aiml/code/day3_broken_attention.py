"""Day 3 — find the bugs. Spoken screen: name the failure, don't golf a patch.

Each attn_* has exactly one defect vs day1 CausalSelfAttention.
sft_* and nan_* are separate objects.

Read the body. Write the bug and the Tuesday symptom under INTERROGATE.
Run only after you have named them:

    python3 day3_broken_attention.py
"""

from __future__ import annotations

import math

import torch
import torch.nn.functional as F


# --- named sizes --------------------------------------------------------------
B, T, C, H = 2, 8, 32, 4
d = C // H  # 8
V = 50
P = 3  # last P tokens are pad in the pad example


def _qkv(x):
    """x [B,T,C] → q,k,v each [B,H,T,d]. Not the bug."""
    B_, T_, C_ = x.shape
    qkv = torch.randn(B_, T_, 3 * C_, device=x.device, dtype=x.dtype)
    q, k, v = qkv.split(C_, dim=-1)
    q = q.view(B_, T_, H, d).transpose(1, 2)
    k = k.view(B_, T_, H, d).transpose(1, 2)
    v = v.view(B_, T_, H, d).transpose(1, 2)
    return q, k, v


def attn_a(x):
    """q,k,v [B,H,T,d] → y [B,T,C]."""
    q, k, v = _qkv(x)
    att = q @ k.transpose(-2, -1)
    causal = torch.triu(torch.ones(T, T, device=x.device), diagonal=1).bool()
    att = att.masked_fill(causal, float("-inf"))
    att = F.softmax(att, dim=-1)
    y = att @ v
    return y.transpose(1, 2).contiguous().view(B, T, C)


def attn_b(x):
    q, k, v = _qkv(x)
    att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(d))
    att = F.softmax(att, dim=-1)
    y = att @ v
    return y.transpose(1, 2).contiguous().view(B, T, C)


def attn_c(x):
    q, k, v = _qkv(x)
    # stay [B,T,C] — no head split
    att = (q.transpose(1, 2).contiguous().view(B, T, C) @ k.transpose(1, 2).contiguous().view(B, T, C).transpose(-2, -1)) * (
        1.0 / math.sqrt(C)
    )
    causal = torch.triu(torch.ones(T, T, device=x.device), diagonal=1).bool()
    att = att.masked_fill(causal, float("-inf"))
    att = F.softmax(att, dim=-1)
    v_flat = v.transpose(1, 2).contiguous().view(B, T, C)
    y = att @ v_flat
    return y


def attn_d(x, pad_mask):
    """pad_mask [B,T]: True = PAD.

    Allowed: attend to earlier non-pad. Forbidden: future, and any pad key.
    """
    q, k, v = _qkv(x)
    att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(d))
    causal = torch.triu(torch.ones(T, T, device=x.device), diagonal=1).bool()
    att = att.masked_fill(causal, float("-inf"))
    # pad_mask True → 1, added onto scores
    att = att + pad_mask[:, None, None, :].to(att.dtype)
    att = F.softmax(att, dim=-1)
    y = att @ v
    return y.transpose(1, 2).contiguous().view(B, T, C)


def attn_e(x, pad_mask):
    """pad_mask [B,T]: True = PAD."""
    q, k, v = _qkv(x)
    att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(d))
    causal = torch.triu(torch.ones(T, T, device=x.device), diagonal=1).bool()
    att = att.masked_fill(causal, float("-inf"))
    att = F.softmax(att, dim=-1)
    att = att.masked_fill(pad_mask[:, None, None, :], 0.0)
    y = att @ v
    return y.transpose(1, 2).contiguous().view(B, T, C)


def ce_shift_a(logits, ids):
    """logits [B,T,V], ids [B,T] → scalar. Next-token LM."""
    return F.cross_entropy(
        logits[:, 1:, :].reshape(-1, V),
        ids[:, 1:].reshape(-1),
    )


def sft_labels_a(ids, answer_from):
    """ids [B,T]. answer_from = first answer *index* (not last prompt).

    Completion-only: loss should include logits[last prompt] → first answer.
    """
    labels = ids.clone()
    labels[:, :answer_from] = -100
    labels[:, -1] = -100
    return labels


def nan_case(scores):
    """scores [T,T]. Row 0 is entirely -inf (a pad query that also cannot
    look at itself). Then softmax."""
    return F.softmax(scores, dim=-1)


# --- INTERROGATE (write here) -------------------------------------------------
# attn_a: line 41 does not divide by sqrt(d); does not have Wo for multihead
# attn_b: line 52 no causal mask; does not have Wo for multihead
# attn_c: line 60 too large denominator; I think inner product q and k is wrong due to view
# attn_d:  (what does +pad_mask do to a True pad key?) it adds one to the value
# attn_e:  (mask after softmax — does the row still sum to 1? can mass sit on pad?)
# ce_shift_a:
# sft_labels_a:  (ids = [p0,p1,p2,a0,a1,eos], answer_from = 3)
# nan_case:  (what is softmax([-inf,-inf,...])? Tuesday first check for attn NaN?)
#
# Frozen vs detach (no code): freeze_encoder vs h_v.detach() after projector —
# who still gets CE grad? Same two sentences as Day 2.


def _demo():
    torch.manual_seed(0)
    x = torch.randn(B, T, C)
    pad_mask = torch.zeros(B, T, dtype=torch.bool)
    pad_mask[:, -P:] = True
    for name, fn in [
        ("a", lambda: attn_a(x)),
        ("b", lambda: attn_b(x)),
        ("c", lambda: attn_c(x)),
        ("d", lambda: attn_d(x, pad_mask)),
        ("e", lambda: attn_e(x, pad_mask)),
    ]:
        y = fn()
        print(name, tuple(y.shape), "finite", bool(torch.isfinite(y).all()))
    logits = torch.randn(B, T, V)
    ids = torch.randint(0, V, (B, T))
    print("ce_shift_a", float(ce_shift_a(logits, ids)))
    print("sft_labels_a[0]", sft_labels_a(ids, answer_from=3)[0].tolist())
    scores = torch.full((T, T), float("-inf"))
    out = nan_case(scores)
    print("nan_case row0", out[0, :3], "has_nan", bool(torch.isnan(out).any()))


if __name__ == "__main__":
    _demo()

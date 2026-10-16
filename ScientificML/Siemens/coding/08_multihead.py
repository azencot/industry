"""08. Multi-head shapes — PROBLEM.

Do not open 08_multihead_solution.py until this file runs.

split_heads: [B, T, D] -> [B, H, T, Dh] with Dh = D / H. D must divide H.
merge_heads: reverse that.

multihead_attention(q, k, v, n_heads):
    q, k, v are [B, T, D] (same T and D here).
    Split, scaled dot-product per head (scale by sqrt(Dh)), merge.
    return [B, T, D]

Say the shape after transpose(-2, -1) on keys: [B, H, Dh, T].
Q @ K^T is [B, H, T, T]. Attention @ V is [B, H, T, Dh].

view/reshape after permute needs contiguous memory.
""",
import torch
import math

def split_heads(x, n_heads):
    B, T, D = x.shape
    Dh = D // n_heads
    
    assert D % n_heads == 0

    return x.reshape([B, T, -1, Dh]).transpose(2, 1).contiguous()


def merge_heads(x):
    B, H, T, Dh = x.shape
    return x.transpose(2, 1).reshape([B, T, H * Dh])


def multihead_attention(q, k, v, n_heads):
    B, T, D = q.shape
    Dh = D // n_heads

    assert D % n_heads == 0

    # [B, T, D] -> [B, H, T, Dh]
    qh, kh, vh = split_heads(q, n_heads), split_heads(k, n_heads), split_heads(v, n_heads)

    scores = qh @ kh.transpose(-2, -1) / math.sqrt(Dh)      # [B, H, T, Dh] @ [B, H, Dh, T] -> [B, H, T, T]

    a = torch.softmax(scores, dim=-1)                        # [B, H, T, T]
    yh = a @ vh                                             # [B, H, T, T] @ [B, H, T, Dh] -> [B, H, T, Dh]

    return merge_heads(yh)                                     # [B, H, T, Dh] -> [B, T, D]

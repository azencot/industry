"""08. Multi-head shapes — SOLUTION.

[B, T, D] -> [B, T, H, Dh] -> permute to [B, H, T, Dh].
Merge is the inverse permute, then view back to [B, T, D].
Scale by Dh, the per-head width, not the full D.
H = 1 must match single-head attention.
""",

import math
import torch


def split_heads(x, n_heads):
    b, t, d = x.shape
    if d % n_heads != 0:
        raise ValueError(f"D={d} is not divisible by n_heads={n_heads}")
    dh = d // n_heads
    return x.view(b, t, n_heads, dh).permute(0, 2, 1, 3).contiguous()


def merge_heads(x):
    b, h, t, dh = x.shape
    return x.permute(0, 2, 1, 3).contiguous().view(b, t, h * dh)


def multihead_attention(q, k, v, n_heads):
    qh = split_heads(q, n_heads)
    kh = split_heads(k, n_heads)
    vh = split_heads(v, n_heads)
    scores = qh @ kh.transpose(-2, -1) / math.sqrt(qh.shape[-1])
    weights = torch.softmax(scores, dim=-1)
    return merge_heads(weights @ vh)


if __name__ == "__main__":
    x = torch.randn(2, 3, 8)
    heads = split_heads(x, 4)
    assert heads.shape == (2, 4, 3, 2)
    assert torch.allclose(merge_heads(heads), x)
    q = torch.randn(2, 5, 8)
    k = torch.randn(2, 5, 8)
    v = torch.randn(2, 5, 8)
    out = multihead_attention(q, k, v, 2)
    assert out.shape == (2, 5, 8)
    single = multihead_attention(q, k, v, 1)
    d = q.shape[-1]
    manual = torch.softmax(q @ k.transpose(-2, -1) / math.sqrt(d), dim=-1) @ v
    assert torch.allclose(single, manual, atol=1e-5)
    print("08_multihead_solution: ok")

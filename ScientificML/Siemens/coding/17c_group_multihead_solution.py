"""17c. Multi-head cross-group attention — SOLUTION.

[B, G, T, D] -> permute to [B, T, G, D] -> [B, T, G, H, Dh] -> [B, T, H, G, Dh].
Scores [B, T, H, Gq, Gk]. Mask broadcasts as [B, 1, 1, 1, Gk].
"""

import math
import torch


def _split(x, n_heads):
    b, g, t, d = x.shape
    dh = d // n_heads
    return (
        x.permute(0, 2, 1, 3)
        .reshape(b, t, g, n_heads, dh)
        .permute(0, 1, 3, 2, 4)
        .contiguous()
    )


def cross_group_multihead(q, kv, n_heads, key_mask=None):
    b, gq, t, d = q.shape
    gk = kv.shape[1]
    if d % n_heads != 0:
        raise ValueError("D must divide n_heads")
    dh = d // n_heads
    qq = _split(q, n_heads)
    kk = _split(kv, n_heads)
    scores = qq @ kk.transpose(-2, -1) / math.sqrt(dh)
    if key_mask is not None:
        scores = scores.masked_fill(~key_mask[:, None, None, None, :], float("-inf"))
    weights = torch.nan_to_num(torch.softmax(scores, dim=-1), nan=0.0)
    out = weights @ kk
    return out.permute(0, 3, 1, 2, 4).reshape(b, gq, t, d)


if __name__ == "__main__":
    torch.manual_seed(0)
    kv = torch.randn(2, 1, 4, 8).expand(2, 3, 4, 8).contiguous()
    q = torch.randn(2, 2, 4, 8)
    out = cross_group_multihead(q, kv, n_heads=4)
    assert out.shape == q.shape
    assert torch.allclose(out, kv[:, :1].expand_as(out), atol=1e-5)

    kv = torch.randn(2, 4, 3, 8)
    q = torch.randn(2, 2, 3, 8)
    mask = torch.zeros(2, 4, dtype=torch.bool)
    mask[:, 0] = True
    out = cross_group_multihead(q, kv, n_heads=4, key_mask=mask)
    assert torch.allclose(out, kv[:, :1].expand_as(out), atol=1e-5)
    print("17c_group_multihead_solution: ok")

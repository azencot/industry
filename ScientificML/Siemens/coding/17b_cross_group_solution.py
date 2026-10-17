"""17b. Cross-group attention — SOLUTION.

[B, G, T, D] -> [B, T, G, D] -> [B*T, G, D].
Scores are [B*T, Gq, Gk]. Softmax over Gk.
key_mask [B, Gk] is repeated once per time index, then [B*T, 1, Gk].
"""

import math
import torch


def cross_group_attention(q, kv, key_mask=None):
    b, gq, t, d = q.shape
    gk = kv.shape[1]
    qq = q.permute(0, 2, 1, 3).reshape(b * t, gq, d)
    kk = kv.permute(0, 2, 1, 3).reshape(b * t, gk, d)
    scores = qq @ kk.transpose(-2, -1) / math.sqrt(d)
    if key_mask is not None:
        m = key_mask[:, None, :].expand(b, t, gk).reshape(b * t, gk)
        scores = scores.masked_fill(~m[:, None, :], float("-inf"))
    weights = torch.nan_to_num(torch.softmax(scores, dim=-1), nan=0.0)
    out = weights @ kk
    return out.reshape(b, t, gq, d).permute(0, 2, 1, 3)


if __name__ == "__main__":
    torch.manual_seed(0)
    kv = torch.randn(2, 1, 5, 4).expand(2, 3, 5, 4).contiguous()
    q = torch.randn(2, 2, 5, 4)
    out = cross_group_attention(q, kv)
    assert out.shape == (2, 2, 5, 4)
    assert torch.allclose(out, kv[:, :1].expand_as(out), atol=1e-5)

    kv = torch.randn(2, 4, 3, 5)
    q = torch.randn(2, 2, 3, 5)
    mask = torch.zeros(2, 4, dtype=torch.bool)
    mask[:, 0] = True
    out = cross_group_attention(q, kv, key_mask=mask)
    assert torch.allclose(out, kv[:, :1].expand_as(out), atol=1e-5)

    dead = torch.zeros(2, 4, dtype=torch.bool)
    assert torch.allclose(cross_group_attention(q, kv, key_mask=dead), torch.zeros_like(out))
    print("17b_cross_group_solution: ok")

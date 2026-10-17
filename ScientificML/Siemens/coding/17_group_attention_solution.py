"""17. Attention across the series axis — SOLUTION.

permute(0, 2, 1, 3) swaps G and T. reshape merges B and T into the batch.
The mask [B, G] has to be repeated once per time index before the merge.
"""

import math
import torch


def group_attention(x, series_mask=None):
    b, g, t, d = x.shape
    h = x.permute(0, 2, 1, 3).reshape(b * t, g, d)
    scores = h @ h.transpose(-2, -1) / math.sqrt(d)
    if series_mask is not None:
        m = series_mask[:, None, :].expand(b, t, g).reshape(b * t, g)
        scores = scores.masked_fill(~m[:, None, :], float("-inf"))
    weights = torch.nan_to_num(torch.softmax(scores, dim=-1), nan=0.0)
    out = weights @ h
    return out.reshape(b, t, g, d).permute(0, 2, 1, 3)


if __name__ == "__main__":
    torch.manual_seed(0)
    x = torch.randn(2, 1, 5, 4).expand(2, 3, 5, 4).contiguous()
    out = group_attention(x)
    assert out.shape == x.shape
    assert torch.allclose(out, x, atol=1e-5)

    x = torch.randn(2, 4, 3, 5)
    mask = torch.zeros(2, 4, dtype=torch.bool)
    mask[:, 0] = True
    out = group_attention(x, series_mask=mask)
    for g in range(4):
        assert torch.allclose(out[:, g], x[:, 0], atol=1e-5)

    dead = torch.zeros(2, 4, dtype=torch.bool)
    assert torch.allclose(group_attention(x, series_mask=dead), torch.zeros_like(x))
    print("17_group_attention_solution: ok")

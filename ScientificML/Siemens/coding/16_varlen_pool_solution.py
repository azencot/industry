"""16. Variable-length self-attention pool — SOLUTION.

Pad by hand so the mask and the copy stay visible.
Key mask [B, T] broadcasts onto scores [B, T, T] as [B, 1, T].
Identical tokens make attention a no-op, so a missed pad shows up
as a change in the length-1 row.
"""

import math
import torch


def pool_variable_sequences(seqs):
    lengths = torch.tensor([s.shape[0] for s in seqs], device=seqs[0].device)
    b = len(seqs)
    d = seqs[0].shape[-1]
    tmax = int(lengths.max())
    x = seqs[0].new_zeros(b, tmax, d)
    for i, s in enumerate(seqs):
        x[i, : s.shape[0]] = s
    mask = torch.arange(tmax, device=x.device)[None, :] < lengths[:, None]
    scores = x @ x.transpose(-2, -1) / math.sqrt(d)
    scores = scores.masked_fill(~mask[:, None, :], float("-inf"))
    weights = torch.nan_to_num(torch.softmax(scores, dim=-1), nan=0.0)
    attended = weights @ x
    m = mask.to(dtype=attended.dtype).unsqueeze(-1)
    return (attended * m).sum(dim=1) / m.sum(dim=1).clamp_min(1.0)


if __name__ == "__main__":
    torch.manual_seed(0)
    a = torch.tensor([[2.0, 3.0], [2.0, 3.0], [2.0, 3.0]])
    b = torch.tensor([[-1.0, 4.0]])
    out = pool_variable_sequences([a, b])
    assert out.shape == (2, 2)
    assert torch.allclose(out[0], torch.tensor([2.0, 3.0]))
    assert torch.allclose(out[1], torch.tensor([-1.0, 4.0]))
    mixed = pool_variable_sequences([torch.randn(4, 3), torch.randn(1, 3), torch.randn(2, 3)])
    assert mixed.shape == (3, 3)
    assert torch.isfinite(mixed).all()
    print("16_varlen_pool_solution: ok")

"""19. Thursday mock — SOLUTION.

Treat each series as its own batch row: [B, G, T, D] -> [B*G, T, D].
lengths [B, G] -> [B*G]. Mask keys, then masked mean, then reshape to [B, G, D].
"""

import math
import torch


def pool_each_series(x, lengths):
    b, g, t, d = x.shape
    h = x.reshape(b * g, t, d)
    lengths = lengths.reshape(b * g).to(device=x.device)
    mask = torch.arange(t, device=x.device)[None, :] < lengths[:, None]
    scores = h @ h.transpose(-2, -1) / math.sqrt(d)
    scores = scores.masked_fill(~mask[:, None, :], float("-inf"))
    weights = torch.nan_to_num(torch.softmax(scores, dim=-1), nan=0.0)
    attended = weights @ h
    m = mask.to(dtype=attended.dtype).unsqueeze(-1)
    pooled = (attended * m).sum(dim=1) / m.sum(dim=1).clamp_min(1.0)
    return pooled.reshape(b, g, d)


if __name__ == "__main__":
    torch.manual_seed(0)
    x = torch.zeros(2, 2, 4, 3)
    x[0, 0, 0] = torch.tensor([1.0, 2.0, 3.0])
    x[0, 1, :2] = torch.tensor([4.0, 0.0, 0.0])
    x[1, 0, :3] = 1.0
    x[1, 1, 0] = torch.tensor([-1.0, 5.0, 2.0])
    lengths = torch.tensor([[1, 2], [3, 1]])
    out = pool_each_series(x, lengths)
    assert out.shape == (2, 2, 3)
    assert torch.allclose(out[0, 0], torch.tensor([1.0, 2.0, 3.0]))
    assert torch.allclose(out[0, 1], torch.tensor([4.0, 0.0, 0.0]))
    assert torch.allclose(out[1, 0], torch.ones(3))
    assert torch.allclose(out[1, 1], torch.tensor([-1.0, 5.0, 2.0]))
    print("19_thu_mock_solution: ok")

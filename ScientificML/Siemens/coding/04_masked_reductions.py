"""04. Masked reductions — PROBLEM.

Do not open 04_masked_reductions_solution.py until this file runs.

x, pred, target: [B, T, D]
mask: [B, T] bool, True = valid.

masked_sum, masked_mean: reduce over T. Return [B, D].
masked_mse: one scalar. Average only over valid positions (and D).

Broadcast the mask with unsqueeze(-1). Do not divide by zero when a row
is all padding: that row's mean is 0.
""",
import torch

def masked_sum(x, mask):
    return torch.sum(x * mask.unsqueeze(-1), dim=1)


def masked_mean(x, mask):
    lengths = torch.sum(mask, dim=1).clamp_min(1)
    return masked_sum(x, mask) / lengths[:, None]


def masked_mse(pred, target, mask):
    err = (pred - target) ** 2                  # [B, T, D]
    valid = mask.unsqueeze(-1).expand_as(err)   # [B, T, D]

    return (err * valid).sum() / valid.sum().clamp_min(1)

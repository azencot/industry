"""J. Gaussian negative log-likelihood — PROBLEM.

No solution file. Thursday 22. Do not open an implementation first.

    mean:    [B, T, D]
    log_var: [B, T, D]
    target:  [B, T, D]
    mask:    [B, T]    True = valid timestamp, False = pad
    return a scalar

Diagonal Gaussian, one variance per feature. For each valid element the
term is

    0.5 * (log(2π) + log_var + (target - mean)^2 * exp(-log_var))

Mean those terms. A term counts only when its timestamp is valid, so a
padded step never enters the sum or the count. Longer sequences
contribute more terms. Features at one valid time all count.

Use the log-variance the model predicted. Do not turn it into a
variance and invert that.

If the mask is all False, do not divide by zero. Return a 0-dimensional
zero on the same device as mean.

Tests to write before you trust it:
- the loss is a scalar, and finite on ordinary inputs
- editing a padded target does not change the loss
- gradients reach mean and log_var
- gradients at padded positions are zero
- a small deterministic example matches the formula above

Time box: 20–25 minutes. One follow-up after it runs.
"""

import torch
import math

def gaussian_nll(mean, log_var, target, mask):
    # mean, log_var, target in [B, T, D]; mask in [B, T]

    # [B, T, D] + [B, T, D] * [B, T, D] -> [B, T, D]
    gnll = .5 * (math.log(2 * math.pi) + log_var + (target - mean) ** 2 * torch.exp(-log_var))

    gnll_count = torch.sum(mask) * mean.shape[-1]
    if gnll_count == 0:
        return torch.zeros(()).to(mean.device)

    return torch.sum(gnll[mask]) / gnll_count

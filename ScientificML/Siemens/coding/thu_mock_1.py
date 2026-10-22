"""Unseen mock. 25 minutes.

    u:  [B, N] real samples of a scalar field on a uniform grid
    dx: positive float, the grid spacing
    return [B, N]

The field is periodic. The value at each point is the second difference

    (u[i + 1] - 2 * u[i] + u[i - 1]) / dx**2

Index 0 wraps around to N - 1. Index N - 1 wraps around to 0.
No loop over the batch.

Write 2–3 tests before you trust it:
- shape [B, N], including a batch of 1
- a constant field returns zeros
- gradients reach u
"""

import torch


def periodic_second_difference(u, dx):
    # u in [B, N]
    B, N = u.shape

    I = torch.arange(N)
    IN, IP = torch.roll(I, 1), torch.roll(I, -1)

    # could also do: torch.roll(u, shifts=-1, dims=1)
    return (u[:, IN] - 2 * u + u[:, IP]) / dx**2
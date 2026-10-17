"""19. Thursday mock — PROBLEM.

Do not open this file before the Thu 22 mock.
Do not open 19_thu_mock_solution.py until your asserts pass.
This is not a repeat of 16–18. No new API.

    x:       [B, G, T, D]   time already padded to T
    lengths: [B, G]        valid timestamps per series
    return   [B, G, D]

For each series independently:
- self-attend over T
- padded timestamps cannot be keys
- masked mean over time

True = valid. Say how you flatten B and G, or how you permute, before you code.
A series with length 1 equals its single valid vector.
"""

import torch


def pool_each_series(x, lengths):
    raise NotImplementedError

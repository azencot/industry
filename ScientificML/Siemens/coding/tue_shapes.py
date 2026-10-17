"""Tuesday shape drills. About 30 minutes. Rapid, from a blank file.

Do not open tue_shapes_solution.py until this file runs.

1. split_heads: [B, T, D] -> [B, H, T, Dh]. D must divide H.
2. merge_heads: reverse that.
3. After a permute, reshape. Use reshape, or contiguous() then view.
4. pairwise_dot(x, y): x [B, N, D], y [B, M, D] -> [B, N, M]. No Python loop.
5. flatten_for_ce(logits [B, T, C], targets [B, T]) -> logits [B*T, C], targets [B*T] long.
"""

import torch


def split_heads(x, n_heads):
    raise NotImplementedError


def merge_heads(x):
    raise NotImplementedError


def pairwise_dot(x, y):
    raise NotImplementedError


def flatten_for_ce(logits, targets):
    raise NotImplementedError

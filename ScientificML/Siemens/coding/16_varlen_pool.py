"""16. Variable-length self-attention pool — PROBLEM.

Do not open 16_varlen_pool_solution.py until this file runs.

One step past a single attention call. Same APIs, one function.

    seqs: list of [Ti, D] float tensors. Same D. Each Ti >= 1.
    return [B, D]

Right-pad to Tmax. True = valid token.
Self-attention (Q = K = V = the padded batch). Mask keys before softmax.
Then masked mean over time. Pad positions must not change the output.

An all-masked row cannot occur here (every sequence is non-empty).
Still use -inf, and nan_to_num after softmax, so the habit is in the code.

Write the asserts before the implementation:
- shape [B, D]
- a sequence of identical rows pools to that row
- a length-1 sequence equals itself (the pad key must not leak)
"""

import torch


def pool_variable_sequences(seqs):
    raise NotImplementedError

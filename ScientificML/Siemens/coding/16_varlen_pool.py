"""16. Padded sequence attention pipeline — PROBLEM.

Do not open 16_varlen_pool_solution.py until this file runs.

Fluency check, not a hard problem. Target 15–20 minutes from a blank file.
If it is clean in under 15 minutes, stop repeating this exact problem.

    seqs: list of [Ti, D] float tensors. Same D. Each Ti >= 1.
    return [B, D]

Steps, in order:
1. Right-pad to x [B, Tmax, D]. Manual pad or pad_sequence.
2. lengths [B]. valid_mask [B, Tmax]. True = valid token.
3. Self-attention over time. Padding keys are masked out.
4. Masked mean over time.

Padding must not leak into the attention or the reduction.
A length-1 sequence equals itself after attention and the masked mean.

Write 3–4 asserts before the implementation:
- shape [B, D]
- a sequence of identical rows pools to that row
- a length-1 sequence equals itself
"""

import torch


def pool_variable_sequences(seqs):
    raise NotImplementedError

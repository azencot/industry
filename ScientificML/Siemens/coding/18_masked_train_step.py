"""18. One masked training step — PROBLEM.

Do not open 18_masked_train_step_solution.py until this file runs.

Two functions. The second calls the first.

masked_cross_entropy(logits, targets, mask) -> scalar
    logits  [B, T, C]   raw scores, not probabilities
    targets [B, T]      class indices
    mask    [B, T]      bool, True = valid position
    Mean over valid positions only. An all-pad batch returns 0.

masked_train_step(model, x, y, mask, optimizer) -> Python float
    x [B, T, D], y [B, T], mask [B, T]
    model(x) -> [B, T, C]
    Order: train mode, zero_grad, forward, masked loss, backward, step.
    Return the loss from this step as a float.

Asserts to write first:
- a wrong label on a pad position does not change the loss
- an all-False mask returns 0
- after several steps on a toy batch, the loss is lower than the first step
"""

import torch


def masked_cross_entropy(logits, targets, mask):
    raise NotImplementedError


def masked_train_step(model, x, y, mask, optimizer):
    raise NotImplementedError

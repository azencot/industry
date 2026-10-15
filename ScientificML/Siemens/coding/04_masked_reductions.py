"""04. Masked reductions — PROBLEM.

Do not open 04_masked_reductions_solution.py until this file runs.

x, pred, target: [B, T, D]
mask: [B, T] bool, True = valid.

masked_sum, masked_mean: reduce over T. Return [B, D].
masked_mse: one scalar. Average only over valid positions (and D).

Broadcast the mask with unsqueeze(-1). Do not divide by zero when a row
is all padding: that row's mean is 0.
""",

def masked_sum(x, mask):
    raise NotImplementedError


def masked_mean(x, mask):
    raise NotImplementedError


def masked_mse(pred, target, mask):
    raise NotImplementedError

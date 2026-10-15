"""15. Masked cross-entropy — PROBLEM.

Do not open 15_masked_ce_solution.py until this file runs.

logits  [B, T, C]   raw scores, not probabilities
targets [B, T]      long class ids
mask    [B, T]      bool, True = count this position

Return one scalar: mean cross-entropy over valid positions only.

CrossEntropyLoss wants logits. Do not softmax first.
ignore_index is the other way, if padding is a class id rather than a mask.
An all-pad batch should return 0, not NaN.
""",

def masked_cross_entropy(logits, targets, mask):
    raise NotImplementedError

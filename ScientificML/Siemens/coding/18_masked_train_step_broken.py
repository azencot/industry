"""18. Masked cross-entropy — BROKEN ON PURPOSE.

Wednesday entry point. Do not open 18_masked_train_step_solution.py.
Run this file. Diagnose out loud. Fix one failure, then run again.

The contract is the same as 18_masked_train_step.py.
True = valid position. Pad labels must not move the loss.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


def masked_cross_entropy(logits, targets, mask):
    return F.cross_entropy(logits, targets)


def masked_train_step(model, x, y, mask, optimizer):
    model.eval()
    loss = masked_cross_entropy(model(x), y.float(), mask)
    loss.backward()
    optimizer.step()
    return float(loss)


if __name__ == "__main__":
    torch.manual_seed(0)
    logits = torch.tensor([[[10.0, 0.0], [0.0, 10.0], [10.0, 0.0]]])
    targets = torch.tensor([[0, 1, 0]])
    mask = torch.tensor([[True, True, False]])
    loss = masked_cross_entropy(logits, targets, mask)
    bad = targets.clone()
    bad[0, 2] = 1
    assert torch.allclose(masked_cross_entropy(logits, bad, mask), loss)

    b, t, d, c = 8, 4, 4, 3
    x = torch.randn(b, t, d)
    y = (x[..., 0] > 0).long()
    step_mask = torch.zeros(b, t, dtype=torch.bool)
    step_mask[:, :2] = True
    model = nn.Linear(d, c)
    opt = torch.optim.SGD(model.parameters(), lr=0.5)
    first = masked_train_step(model, x, y, step_mask, opt)
    last = first
    for _ in range(30):
        last = masked_train_step(model, x, y, step_mask, opt)
    assert last < first
    assert any(p.grad is not None for p in model.parameters())
    print("18 broken: asserts passed — the bugs are gone")

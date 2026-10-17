"""18. One masked training step — SOLUTION.

CrossEntropy wants [N, C] and integer classes. Flatten B and T, then
put the mask back on the per-position loss.
zero_grad before backward: grad accumulates.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


def masked_cross_entropy(logits, targets, mask):
    b, t, c = logits.shape
    per = F.cross_entropy(
        logits.reshape(b * t, c),
        targets.reshape(b * t),
        reduction="none",
    ).view(b, t)
    m = mask.to(dtype=per.dtype)
    return (per * m).sum() / m.sum().clamp_min(1.0)


def masked_train_step(model, x, y, mask, optimizer):
    model.train()
    optimizer.zero_grad()
    loss = masked_cross_entropy(model(x), y, mask)
    loss.backward()
    optimizer.step()
    return float(loss.detach())


if __name__ == "__main__":
    torch.manual_seed(0)
    logits = torch.tensor([[[10.0, 0.0], [0.0, 10.0], [10.0, 0.0]]])
    targets = torch.tensor([[0, 1, 0]])
    mask = torch.tensor([[True, True, False]])
    loss = masked_cross_entropy(logits, targets, mask)
    assert loss.ndim == 0 and loss < 0.01
    bad = targets.clone()
    bad[0, 2] = 1
    assert torch.allclose(masked_cross_entropy(logits, bad, mask), loss)
    none = torch.zeros(1, 3, dtype=torch.bool)
    assert masked_cross_entropy(logits, targets, none).item() == 0.0

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
    print("18_masked_train_step_solution: ok")

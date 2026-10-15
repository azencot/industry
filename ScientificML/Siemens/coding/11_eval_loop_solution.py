"""11. Evaluation loop — SOLUTION.

eval() then no_grad(). The loss tensor is detached by reading .item()
inside no_grad, so the graph is never stored.
""",

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


def evaluate(model, loader, criterion):
    model.eval()
    total = 0.0
    n = 0
    with torch.no_grad():
        for x, y in loader:
            loss = criterion(model(x), y)
            total += float(loss)
            n += 1
    return total / max(n, 1)


if __name__ == "__main__":
    x = torch.randn(16, 3)
    y = torch.randn(16, 1)
    loader = DataLoader(TensorDataset(x, y), batch_size=4)
    model = nn.Linear(3, 1)
    loss = evaluate(model, loader, nn.MSELoss())
    assert loss > 0
    assert not model.training
    print("11_eval_loop_solution: ok")

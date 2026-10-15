"""10. Training loop — SOLUTION.

train() enables dropout. zero_grad clears the previous step.
Mean of batch losses, not a sum, so the number does not depend on
how many batches the loader yielded.
""",

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


def train_one_epoch(model, loader, optimizer, criterion):
    model.train()
    total = 0.0
    n = 0
    for x, y in loader:
        optimizer.zero_grad()
        pred = model(x)
        loss = criterion(pred, y)
        loss.backward()
        optimizer.step()
        total += float(loss.detach())
        n += 1
    return total / max(n, 1)


if __name__ == "__main__":
    torch.manual_seed(0)
    x = torch.randn(32, 3)
    y = x @ torch.tensor([[1.0], [0.0], [-1.0]])
    loader = DataLoader(TensorDataset(x, y), batch_size=8)
    model = nn.Linear(3, 1)
    opt = torch.optim.SGD(model.parameters(), lr=0.1)
    before = train_one_epoch(model, loader, opt, nn.MSELoss())
    after = train_one_epoch(model, loader, opt, nn.MSELoss())
    assert after < before
    print("10_train_loop_solution: ok")

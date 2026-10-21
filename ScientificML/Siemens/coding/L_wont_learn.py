"""L. A model that does not learn.

Thursday 22. Run this file. There is no solution file.

The map is y = 3 * x[:, 0] - 2 * x[:, 1], plus a little noise.
A small network should fit it. The script runs. The fit does not improve.

Find out why, fix it, and run it again. The held-out MSE should fall
under 1. The zero-prediction baseline printed on the first line is
well above that.

Time box: 25–30 minutes.
"""

import torch
import torch.nn as nn

torch.manual_seed(0)

N = 512
x = torch.randn(N, 2)
y = 3 * x[:, 0] - 2 * x[:, 1] + 0.05 * torch.randn(N)

n_train = 400
x_train, y_train = x[:n_train], y[:n_train]
x_test, y_test = x[n_train:], y[n_train:]

torch.manual_seed(1)


class Regressor(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(2, 64)
        self.head = nn.Linear(64, 1)
        self.scale = nn.Parameter(torch.zeros(()))

    def forward(self, x):
        h = torch.relu(self.hidden(x))
        return (self.head(h) * self.scale).squeeze(-1)


model = Regressor()
opt = torch.optim.Adam(
    list(model.hidden.parameters()) + list(model.head.parameters()),
    lr=1e-2,
)
loss_fn = nn.MSELoss()


def test_mse():
    model.eval()
    with torch.no_grad():
        pred = model(x_test)
        mse = torch.mean((pred - y_test) ** 2).item()
    model.train()
    return mse


baseline = torch.mean(y_test ** 2).item()
print(f"zero-prediction test MSE {baseline:.3f}")

for epoch in range(60):
    model.train()
    perm = torch.randperm(n_train)
    total = 0.0
    n_batches = 0
    for i in range(0, n_train, 32):
        idx = perm[i:i + 32]
        xb = x_train[idx]
        yb = y_train[idx]
        pred = model(xb)
        yb = torch.roll(yb, 1)
        loss = loss_fn(pred, yb)
        loss.backward()
        opt.zero_grad()
        opt.step()
        total += float(loss)
        n_batches += 1
    if epoch % 15 == 0 or epoch == 59:
        print(f"epoch {epoch:03d}  train {total / n_batches:.3f}  test {test_mse():.3f}")

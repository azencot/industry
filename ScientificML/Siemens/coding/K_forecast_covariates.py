"""K. Forecasting with covariates — PROBLEM.

No solution file. Thursday 22. Choose the architecture yourself
before writing it. A small module is enough. Not a Transformer.

    past_target: [B, L, Dy]   history of the series
    past_cov:    [B, L, Dc]   covariates over that same history
    future_cov:  [B, H, Dc]   covariates over the horizon
    return forecast [B, H, Dy]

There is no future-target argument. The forward must not take one.

B, L, and H come from the tensors. Do not store a weight whose first
dimension is a fixed horizon or a fixed batch.

The forecast at each horizon step may use the history and the future
covariates. Changing future_cov must be able to change the forecast.
Past covariates and future covariates are different tensors. Do not
read a future target from anywhere.

Tests to write before you trust it:
- forecast shape is [B, H, Dy], including B = 1 and an H different from L
- gradients reach the parameters
- two different future_cov tensors can produce two different forecasts
- the forward signature has no future target

Time box: 25–30 minutes. State the architecture, then code.
One follow-up after it runs.
"""

import torch
from torch import nn


class ForecastWithCovariates(nn.Module):
    def __init__(self, dy, dc, d):
        super().__init__()

        self.d = d
        
        # ARCH: I will go with a simple RNN, i.e., hn = f(W hc + U x), yn = g(V hn)
        # Covariates via a simple concat + add: hn = f(W hc + U x + Q [xc, yc])
        self.W = nn.Linear(d, d)
        self.U = nn.Linear(dy, d)
        self.V = nn.Linear(d, dy)
        self.Q = nn.Linear(dc, d)
        self.P = nn.Linear(dc, d)

        self.relu = nn.ReLU()

    def forward(self, past_target, past_cov, future_cov):
        # past_target in [B, L, Dy], past_cov in [B, L, Dc], future_cov in [B, H, Dc]
        B, L = past_target.shape[:2]
        H = future_cov.shape[1]

        # pre-process history
        hidden = torch.zeros([B, self.d]).to(past_target.device)
        for k in range(L):
            # hidden state
            hidden = self.W(hidden) + self.U(past_target[:, k])

            # use covariates
            hidden = hidden + self.Q(past_cov[:, k])

            hidden = self.relu(hidden)

        pred_target = []
        for j in range(H):
                hidden = hidden + self.P(future_cov[:, j])
                hidden = self.relu(hidden)
            
                # pred
                pred_target.append(self.V(hidden))

        return torch.stack(pred_target, dim=1)                # [B, H, dy]

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
        raise NotImplementedError

    def forward(self, past_target, past_cov, future_cov):
        raise NotImplementedError

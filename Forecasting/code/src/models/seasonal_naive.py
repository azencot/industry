"""Seasonal naive: yhat[t+h] = y[t+h-m] with m known (weekly)."""

from __future__ import annotations

import time

import numpy as np
import pandas as pd

from ..load_panel import SEASONAL_PERIOD


def forecast_seasonal_naive(
    panel: pd.DataFrame,
    horizon: int,
    m: int = SEASONAL_PERIOD,
) -> tuple[pd.DataFrame, float]:
    t0 = time.perf_counter()
    rows: list[dict] = []
    for sid, g in panel.groupby("series_id"):
        g = g.sort_values("ds")
        train = g.loc[g["in_train"]]
        test = g.loc[~g["in_train"]]
        y = train["y"].to_numpy()
        n = len(y)
        if n == 0:
            continue
        if n >= m:
            # tile last season
            season = y[-m:]
            yhat = np.array([season[(h - 1) % m] for h in range(1, len(test) + 1)], dtype=float)
        else:
            # cold start shorter than m: fall back to last value
            yhat = np.full(len(test), float(y[-1]))
        for ds, pred in zip(test["ds"].to_numpy(), yhat):
            rows.append({"series_id": sid, "ds": ds, "yhat": float(pred)})
    elapsed = time.perf_counter() - t0
    return pd.DataFrame(rows), elapsed

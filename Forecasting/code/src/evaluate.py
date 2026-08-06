"""Point-forecast metrics: MAE, RMSE, WAPE, MASE (seasonal period known)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .load_panel import SEASONAL_PERIOD


def _mae(y: np.ndarray, yhat: np.ndarray) -> float:
    return float(np.mean(np.abs(y - yhat)))


def _rmse(y: np.ndarray, yhat: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y - yhat) ** 2)))


def _wape(y: np.ndarray, yhat: np.ndarray) -> float:
    denom = float(np.sum(np.abs(y)))
    if denom < 1e-12:
        return float("nan")
    return float(np.sum(np.abs(y - yhat)) / denom)


def seasonal_naive_scale(train_y: np.ndarray, m: int = SEASONAL_PERIOD) -> float:
    """Mean abs seasonal-naive residual on train (MASE denominator)."""
    if len(train_y) <= m:
        scale = float(np.mean(np.abs(train_y - np.mean(train_y)))) if len(train_y) else 1.0
        return scale if scale > 1e-12 else 1.0
    diff = np.abs(train_y[m:] - train_y[:-m])
    scale = float(np.mean(diff))
    return scale if scale > 1e-12 else 1.0


def score_forecasts(
    forecasts: pd.DataFrame,
    panel: pd.DataFrame,
    model_name: str,
) -> pd.DataFrame:
    """forecasts columns: series_id, ds, yhat — returns overall + per-regime metrics."""
    test = panel.loc[~panel["in_train"], ["series_id", "ds", "y", "regime"]].copy()
    merged = test.merge(forecasts, on=["series_id", "ds"], how="inner")
    train = panel.loc[panel["in_train"], ["series_id", "y"]]

    rows: list[dict] = []

    def add_rows(scope: str, regime: str, sub: pd.DataFrame) -> None:
        if sub.empty:
            return
        mase_num = 0.0
        mase_den = 0.0
        for sid, g in sub.groupby("series_id"):
            ty = train.loc[train["series_id"] == sid, "y"].to_numpy()
            scale = seasonal_naive_scale(ty)
            err = np.abs(g["y"].to_numpy() - g["yhat"].to_numpy())
            mase_num += float(np.sum(err / scale))
            mase_den += float(len(g))
        y = sub["y"].to_numpy()
        yhat = sub["yhat"].to_numpy()
        rows.append(
            {
                "model": model_name,
                "scope": scope,
                "regime": regime,
                "mae": _mae(y, yhat),
                "rmse": _rmse(y, yhat),
                "wape": _wape(y, yhat),
                "mase": mase_num / mase_den if mase_den else float("nan"),
                "n": int(len(sub)),
            }
        )

    add_rows("overall", "all", merged)
    for regime, g in merged.groupby("regime"):
        add_rows("regime", str(regime), g)
    return pd.DataFrame(rows)

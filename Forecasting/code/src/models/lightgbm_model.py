"""Global LightGBM with lags, calendar, and known-future promo/price."""

from __future__ import annotations

import time

import lightgbm as lgb
import numpy as np
import pandas as pd

LAGS = (1, 7, 14, 28)
ROLL_WINDOWS = (7, 28)


def _add_features(df: pd.DataFrame) -> pd.DataFrame:
    parts = []
    for sid, g in df.groupby("series_id", sort=False):
        g = g.sort_values("ds").copy()
        for lag in LAGS:
            g[f"lag_{lag}"] = g["y"].shift(lag)
        for w in ROLL_WINDOWS:
            g[f"roll_mean_{w}"] = g["y"].shift(1).rolling(w, min_periods=1).mean()
        g["dow"] = g["ds"].dt.dayofweek
        g["month"] = g["ds"].dt.month
        g["promo"] = g["promo"].astype(float)
        g["price"] = g["price"].astype(float)
        parts.append(g)
    return pd.concat(parts, ignore_index=True)


def forecast_lightgbm(panel: pd.DataFrame, horizon: int) -> tuple[pd.DataFrame, float]:
    t0 = time.perf_counter()
    feat = _add_features(panel)
    feature_cols = (
        [f"lag_{lag}" for lag in LAGS]
        + [f"roll_mean_{w}" for w in ROLL_WINDOWS]
        + ["dow", "month", "promo", "price"]
    )

    train = feat.loc[feat["in_train"]].dropna(subset=["lag_28"] , how="any")
    # cold-start series may lack lag_28 — allow shorter history with available lags
    if train.empty:
        train = feat.loc[feat["in_train"]].dropna(subset=["lag_1"])
    # drop rows still missing any feature
    train = train.dropna(subset=feature_cols)

    model = lgb.LGBMRegressor(
        n_estimators=200,
        learning_rate=0.05,
        num_leaves=31,
        subsample=0.9,
        colsample_bytree=0.9,
        random_state=42,
        verbosity=-1,
    )
    model.fit(train[feature_cols], train["y"])

    # recursive multi-step within each series for horizon
    rows: list[dict] = []
    for sid, g in feat.groupby("series_id", sort=False):
        g = g.sort_values("ds").reset_index(drop=True)
        y_hist = g.loc[g["in_train"], "y"].astype(float).tolist()
        test = g.loc[~g["in_train"]].copy()
        for _, row in test.iterrows():
            # build feature vector from y_hist + known-future covariates on this row
            feats = {}
            for lag in LAGS:
                feats[f"lag_{lag}"] = y_hist[-lag] if len(y_hist) >= lag else (
                    y_hist[-1] if y_hist else 0.0
                )
            for w in ROLL_WINDOWS:
                window = y_hist[-w:] if y_hist else [0.0]
                feats[f"roll_mean_{w}"] = float(np.mean(window))
            feats["dow"] = float(row["dow"])
            feats["month"] = float(row["month"])
            feats["promo"] = float(row["promo"])
            feats["price"] = float(row["price"])
            x = pd.DataFrame([feats])[feature_cols]
            pred = float(model.predict(x)[0])
            pred = max(pred, 0.0)
            y_hist.append(pred)
            rows.append({"series_id": sid, "ds": row["ds"], "yhat": pred})

    elapsed = time.perf_counter() - t0
    return pd.DataFrame(rows), elapsed

"""Per-series AutoETS (statsforecast) with known weekly seasonality."""

from __future__ import annotations

import time
import warnings

import pandas as pd
from statsforecast import StatsForecast
from statsforecast.models import AutoETS

from ..load_panel import SEASONAL_PERIOD


def forecast_ets(
    panel: pd.DataFrame,
    horizon: int,
    m: int = SEASONAL_PERIOD,
) -> tuple[pd.DataFrame, float]:
    train = panel.loc[panel["in_train"], ["series_id", "ds", "y"]].rename(
        columns={"series_id": "unique_id"}
    )
    t0 = time.perf_counter()
    sf = StatsForecast(
        models=[AutoETS(season_length=m, model="ZZZ")],
        freq="D",
        n_jobs=1,
    )
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fcst = sf.forecast(df=train, h=horizon)
    elapsed = time.perf_counter() - t0

    # columns: unique_id, ds, AutoETS
    out = fcst.reset_index() if "unique_id" not in fcst.columns else fcst.copy()
    if "unique_id" not in out.columns and out.index.name == "unique_id":
        out = out.reset_index()
    # statsforecast versions differ on index layout
    if "unique_id" not in out.columns:
        out = fcst.copy()
        out = out.rename_axis("unique_id").reset_index()

    # find prediction column
    pred_col = [c for c in out.columns if c not in ("unique_id", "ds")][0]
    out = out.rename(columns={"unique_id": "series_id", pred_col: "yhat"})
    out["ds"] = pd.to_datetime(out["ds"]).dt.normalize()
    return out[["series_id", "ds", "yhat"]], elapsed

#!/usr/bin/env python3
"""Generate synthetic multi-regime forecasting panel (Phase 1)."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

SEED = 42
HORIZON = 28
N_PER_REGIME = 10
START_DATE = pd.Timestamp("2022-01-01")
CUTOFF = pd.Timestamp("2024-12-03")  # Tue; leaves room for H=28 into late Dec
LONG_TRAIN_DAYS = (CUTOFF - START_DATE).days + 1  # inclusive


def _dates(start: pd.Timestamp, n_days: int) -> pd.DatetimeIndex:
    return pd.date_range(start, periods=n_days, freq="D")


def _weekly_season(dow: np.ndarray, amp: float) -> np.ndarray:
    # Mon=0 … Sun=6; weekend bump + midweek dip
    pattern = np.array([0.85, 0.9, 1.0, 1.05, 1.1, 1.25, 1.15])
    return amp * (pattern[dow] - 1.0)


def _smooth_path(
    rng: np.random.Generator,
    n: int,
    dates: pd.DatetimeIndex,
    base_level: float,
    season_amp: float,
    noise_scale: float,
) -> np.ndarray:
    dow = dates.dayofweek.to_numpy()
    season = _weekly_season(dow, season_amp)
    # mild annual
    day_of_year = dates.dayofyear.to_numpy()
    annual = 0.08 * base_level * np.sin(2 * np.pi * day_of_year / 365.25)
    noise = rng.normal(0.0, noise_scale, size=n)
    y = base_level + season * base_level + annual + noise
    return np.maximum(y, 0.05)


def _promo_calendar(rng: np.random.Generator, n: int) -> np.ndarray:
    # ~12% promo days in irregular bursts
    promo = np.zeros(n, dtype=int)
    i = 0
    while i < n:
        if rng.random() < 0.08:
            length = int(rng.integers(2, 6))
            promo[i : min(i + length, n)] = 1
            i += length + int(rng.integers(5, 20))
        else:
            i += 1
    return promo


def make_smooth(series_id: str, rng: np.random.Generator, seed_offset: int) -> tuple[pd.DataFrame, dict]:
    base_level = float(rng.uniform(80, 140))
    season_amp = float(rng.uniform(0.25, 0.45))
    noise_scale = float(rng.uniform(3.0, 8.0))
    n = LONG_TRAIN_DAYS + HORIZON
    dates = _dates(START_DATE, n)
    y = _smooth_path(rng, n, dates, base_level, season_amp, noise_scale)
    df = _frame(series_id, "smooth_seasonal", dates, y, promo=np.zeros(n, dtype=int), price=np.full(n, 10.0))
    meta = _meta(
        series_id,
        "smooth_seasonal",
        parent_dgp="smooth",
        base_level=base_level,
        season_amp=season_amp,
        noise_scale=noise_scale,
        seed_offset=seed_offset,
        n_train_days=int(df["in_train"].sum()),
        n_obs=len(df),
    )
    return df, meta


def make_mean_step(series_id: str, rng: np.random.Generator, seed_offset: int) -> tuple[pd.DataFrame, dict]:
    base_level = float(rng.uniform(70, 120))
    season_amp = float(rng.uniform(0.2, 0.4))
    noise_scale = float(rng.uniform(3.0, 7.0))
    step_size = float(rng.uniform(40, 80))
    n = LONG_TRAIN_DAYS + HORIZON
    dates = _dates(START_DATE, n)
    # shift in the second half of train, well before cutoff
    shift_idx = int(LONG_TRAIN_DAYS * rng.uniform(0.45, 0.7))
    shift_date = dates[shift_idx]
    y = _smooth_path(rng, n, dates, base_level, season_amp, noise_scale)
    y[shift_idx:] = y[shift_idx:] + step_size
    df = _frame(series_id, "mean_step", dates, y, promo=np.zeros(n, dtype=int), price=np.full(n, 10.0))
    meta = _meta(
        series_id,
        "mean_step",
        parent_dgp="smooth",
        base_level=base_level,
        season_amp=season_amp,
        noise_scale=noise_scale,
        shift_date=shift_date.strftime("%Y-%m-%d"),
        step_size=step_size,
        seed_offset=seed_offset,
        n_train_days=int(df["in_train"].sum()),
        n_obs=len(df),
    )
    return df, meta


def make_promo(series_id: str, rng: np.random.Generator, seed_offset: int) -> tuple[pd.DataFrame, dict]:
    base_level = float(rng.uniform(60, 110))
    season_amp = float(rng.uniform(0.15, 0.3))
    noise_scale = float(rng.uniform(4.0, 9.0))
    promo_lift = float(rng.uniform(1.8, 2.8))
    n = LONG_TRAIN_DAYS + HORIZON
    dates = _dates(START_DATE, n)
    promo = _promo_calendar(rng, n)
    # ensure some promos in test horizon
    if promo[-HORIZON:].sum() == 0:
        promo[-HORIZON + 3 : -HORIZON + 7] = 1
    price = np.where(promo == 1, 7.5, 10.0).astype(float)
    y = _smooth_path(rng, n, dates, base_level, season_amp, noise_scale)
    y = y * np.where(promo == 1, promo_lift, 1.0)
    df = _frame(series_id, "promo_driven", dates, y, promo=promo, price=price)
    meta = _meta(
        series_id,
        "promo_driven",
        parent_dgp="promo",
        base_level=base_level,
        season_amp=season_amp,
        noise_scale=noise_scale,
        promo_lift=promo_lift,
        seed_offset=seed_offset,
        n_train_days=int(df["in_train"].sum()),
        n_obs=len(df),
    )
    return df, meta


def make_intermittent(series_id: str, rng: np.random.Generator, seed_offset: int) -> tuple[pd.DataFrame, dict]:
    zero_rate_target = float(rng.uniform(0.65, 0.8))
    demand_mean = float(rng.uniform(2.0, 6.0))
    n = LONG_TRAIN_DAYS + HORIZON
    dates = _dates(START_DATE, n)
    active = rng.random(n) > zero_rate_target
    y = np.zeros(n, dtype=float)
    y[active] = rng.poisson(demand_mean, size=int(active.sum())).astype(float)
    # mild weekday effect on active days
    dow = dates.dayofweek.to_numpy()
    y[active & (dow >= 5)] = np.maximum(y[active & (dow >= 5)] + 1, 1)
    df = _frame(
        series_id,
        "intermittent",
        dates,
        y,
        promo=np.zeros(n, dtype=int),
        price=np.full(n, 10.0),
    )
    meta = _meta(
        series_id,
        "intermittent",
        parent_dgp="intermittent",
        base_level=demand_mean,
        season_amp=0.0,
        noise_scale=0.0,
        zero_rate_target=zero_rate_target,
        seed_offset=seed_offset,
        n_train_days=int(df["in_train"].sum()),
        n_obs=len(df),
    )
    return df, meta


def make_cold_start(series_id: str, rng: np.random.Generator, seed_offset: int, idx: int) -> tuple[pd.DataFrame, dict]:
    parent = "promo" if idx % 2 == 0 else "smooth"
    n_train = int(rng.integers(30, 61))
    start = CUTOFF - pd.Timedelta(days=n_train - 1)
    n = n_train + HORIZON
    dates = _dates(start, n)
    base_level = float(rng.uniform(70, 130))
    season_amp = float(rng.uniform(0.2, 0.4))
    noise_scale = float(rng.uniform(4.0, 10.0))
    if parent == "promo":
        promo_lift = float(rng.uniform(1.8, 2.6))
        promo = _promo_calendar(rng, n)
        if promo[-HORIZON:].sum() == 0:
            promo[-HORIZON + 2 : -HORIZON + 5] = 1
        price = np.where(promo == 1, 7.5, 10.0).astype(float)
        y = _smooth_path(rng, n, dates, base_level, season_amp, noise_scale)
        y = y * np.where(promo == 1, promo_lift, 1.0)
    else:
        promo_lift = 0.0
        promo = np.zeros(n, dtype=int)
        price = np.full(n, 10.0)
        y = _smooth_path(rng, n, dates, base_level, season_amp, noise_scale)
    df = _frame(series_id, "cold_start", dates, y, promo=promo, price=price)
    meta = _meta(
        series_id,
        "cold_start",
        parent_dgp=parent,
        base_level=base_level,
        season_amp=season_amp,
        noise_scale=noise_scale,
        promo_lift=promo_lift,
        seed_offset=seed_offset,
        n_train_days=int(df["in_train"].sum()),
        n_obs=len(df),
    )
    return df, meta


def _frame(
    series_id: str,
    regime: str,
    dates: pd.DatetimeIndex,
    y: np.ndarray,
    promo: np.ndarray,
    price: np.ndarray,
) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "series_id": series_id,
            "ds": dates,
            "y": y.astype(float),
            "regime": regime,
            "promo": promo.astype(int),
            "price": price.astype(float),
            "in_train": dates <= CUTOFF,
        }
    )


def _meta(
    series_id: str,
    regime: str,
    *,
    parent_dgp: str,
    base_level: float,
    season_amp: float,
    noise_scale: float,
    seed_offset: int,
    n_train_days: int,
    n_obs: int,
    shift_date: str = "",
    step_size: float = 0.0,
    zero_rate_target: float = 0.0,
    promo_lift: float = 0.0,
) -> dict:
    return {
        "series_id": series_id,
        "regime": regime,
        "parent_dgp": parent_dgp,
        "base_level": base_level,
        "season_amp": season_amp,
        "noise_scale": noise_scale,
        "shift_date": shift_date,
        "step_size": step_size,
        "zero_rate_target": zero_rate_target,
        "promo_lift": promo_lift,
        "n_train_days": n_train_days,
        "n_obs": n_obs,
        "seed_offset": seed_offset,
    }


REGIME_BUILDERS = {
    "smooth_seasonal": ("smooth", make_smooth),
    "mean_step": ("mean_step", make_mean_step),
    "promo_driven": ("promo", make_promo),
    "intermittent": ("intermittent", make_intermittent),
    "cold_start": ("cold", None),  # special-cased
}


def generate() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    frames: list[pd.DataFrame] = []
    metas: list[dict] = []
    offset = 0

    for regime, (prefix, builder) in REGIME_BUILDERS.items():
        for i in range(1, N_PER_REGIME + 1):
            offset += 1
            rng = np.random.default_rng(SEED + offset * 1009)
            series_id = f"{prefix}_{i:03d}"
            if regime == "cold_start":
                df, meta = make_cold_start(series_id, rng, offset, i)
            else:
                assert builder is not None
                df, meta = builder(series_id, rng, offset)
            frames.append(df)
            metas.append(meta)

    panel = pd.concat(frames, ignore_index=True)
    panel["ds"] = pd.to_datetime(panel["ds"]).dt.normalize()
    meta_df = pd.DataFrame(metas)

    panel.to_parquet(OUT / "panel.parquet", index=False)
    panel.to_csv(OUT / "panel.csv", index=False)
    meta_df.to_csv(OUT / "series_meta.csv", index=False)

    cutoff_payload = {
        "cutoff": CUTOFF.strftime("%Y-%m-%d"),
        "horizon": HORIZON,
        "freq": "D",
        "seed": SEED,
        "start_date": START_DATE.strftime("%Y-%m-%d"),
        "n_series_per_regime": N_PER_REGIME,
        "n_series_total": int(meta_df.shape[0]),
        "n_rows": int(panel.shape[0]),
    }
    (OUT / "cutoff.json").write_text(json.dumps(cutoff_payload, indent=2) + "\n")
    print(f"Wrote {OUT / 'panel.parquet'} ({panel.shape[0]} rows, {meta_df.shape[0]} series)")
    print(f"Cutoff={cutoff_payload['cutoff']} horizon={HORIZON} seed={SEED}")


if __name__ == "__main__":
    generate()

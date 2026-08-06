"""Load signed-off synthetic panel artifacts."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

CODE_ROOT = Path(__file__).resolve().parents[1]
DATA_GEN = CODE_ROOT.parent / "data" / "generated"

SEASONAL_PERIOD = 7


def load_cutoff(path: Path | None = None) -> dict:
    p = path or (DATA_GEN / "cutoff.json")
    return json.loads(p.read_text())


def load_panel(path: Path | None = None) -> pd.DataFrame:
    p = path or (DATA_GEN / "panel.parquet")
    df = pd.read_parquet(p)
    df["ds"] = pd.to_datetime(df["ds"]).dt.normalize()
    return df.sort_values(["series_id", "ds"]).reset_index(drop=True)


def load_meta(path: Path | None = None) -> pd.DataFrame:
    p = path or (DATA_GEN / "series_meta.csv")
    return pd.read_csv(p)


def split_train_test(panel: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    train = panel.loc[panel["in_train"]].copy()
    test = panel.loc[~panel["in_train"]].copy()
    return train, test

"""Zero-shot Chronos-Bolt small (no fine-tuning)."""

from __future__ import annotations

import time

import pandas as pd

CHRONOS_MODEL_ID = "amazon/chronos-bolt-small"


def _device() -> str:
    import torch

    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def forecast_chronos_bolt(panel: pd.DataFrame, horizon: int) -> tuple[pd.DataFrame, float]:
    import torch
    from chronos import BaseChronosPipeline

    device = _device()
    t0 = time.perf_counter()
    pipeline = BaseChronosPipeline.from_pretrained(
        CHRONOS_MODEL_ID,
        device_map=device,
        torch_dtype=torch.float32,
    )
    load_elapsed = time.perf_counter() - t0

    rows: list[dict] = []
    t_pred = time.perf_counter()
    for sid, g in panel.groupby("series_id"):
        g = g.sort_values("ds")
        context = torch.tensor(g.loc[g["in_train"], "y"].to_numpy(), dtype=torch.float32)
        test = g.loc[~g["in_train"]]
        h = len(test)
        if len(context) == 0:
            continue
        quantiles, mean = pipeline.predict_quantiles(
            context=context,
            prediction_length=h,
            quantile_levels=[0.5],
        )
        yhat = quantiles[0, :, 0].detach().cpu().numpy().astype(float)
        for ds, pred in zip(test["ds"].to_numpy(), yhat):
            rows.append({"series_id": sid, "ds": ds, "yhat": float(max(pred, 0.0))})
    pred_elapsed = time.perf_counter() - t_pred
    _ = mean
    return pd.DataFrame(rows), load_elapsed + pred_elapsed

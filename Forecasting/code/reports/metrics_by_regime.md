# Bakeoff metrics by regime

Chronos checkpoint: `amazon/chronos-bolt-small` (zero-shot).

## Timings (seconds)

| Model | Wall time |
|-------|-----------|
| `seasonal_naive` | 0.02 |
| `ets` | 16.80 |
| `lightgbm` | 1.76 |
| `chronos_bolt_small` | 3.19 |

## Overall

| Model | MAE | RMSE | WAPE | MASE | n |
|-------|-----|------|------|------|---|
| `lightgbm` | 5.870 | 10.516 | 0.062 | 0.688 | 1400 |
| `chronos_bolt_small` | 9.728 | 24.707 | 0.102 | 0.774 | 1400 |
| `ets` | 14.804 | 29.970 | 0.155 | 0.978 | 1400 |
| `seasonal_naive` | 10.965 | 26.050 | 0.115 | 0.986 | 1400 |

## By regime

### `cold_start` — expected: Chronos-Bolt relative

| Model | MAE | RMSE | WAPE | MASE |
|-------|-----|------|------|------|
| `lightgbm` | 10.943 | 18.878 | 0.096 | 0.635 |
| `chronos_bolt_small` | 17.122 | 38.525 | 0.150 | 0.823 |
| `seasonal_naive` | 19.098 | 41.280 | 0.168 | 0.948 |
| `ets` | 22.175 | 41.960 | 0.195 | 0.954 |

Lowest MASE: **`lightgbm`**

### `intermittent` — expected: messy (use WAPE/MASE)

| Model | MAE | RMSE | WAPE | MASE |
|-------|-----|------|------|------|
| `chronos_bolt_small` | 1.524 | 2.803 | 1.013 | 0.817 |
| `ets` | 1.812 | 2.390 | 1.205 | 0.986 |
| `lightgbm` | 1.915 | 2.411 | 1.273 | 1.057 |
| `seasonal_naive` | 2.196 | 3.279 | 1.461 | 1.198 |

Lowest MASE: **`chronos_bolt_small`**

### `mean_step` — expected: ETS / LightGBM

| Model | MAE | RMSE | WAPE | MASE |
|-------|-----|------|------|------|
| `lightgbm` | 3.722 | 4.861 | 0.025 | 0.704 |
| `chronos_bolt_small` | 4.248 | 5.426 | 0.028 | 0.818 |
| `ets` | 4.288 | 5.469 | 0.028 | 0.830 |
| `seasonal_naive` | 4.878 | 6.350 | 0.032 | 0.936 |

Lowest MASE: **`lightgbm`**

### `promo_driven` — expected: LightGBM

| Model | MAE | RMSE | WAPE | MASE |
|-------|-----|------|------|------|
| `lightgbm` | 8.310 | 11.553 | 0.087 | 0.274 |
| `chronos_bolt_small` | 21.586 | 38.753 | 0.227 | 0.695 |
| `seasonal_naive` | 22.086 | 39.569 | 0.233 | 0.716 |
| `ets` | 40.999 | 51.549 | 0.432 | 1.299 |

Lowest MASE: **`lightgbm`**

### `smooth_seasonal` — expected: SN ≈ ETS

| Model | MAE | RMSE | WAPE | MASE |
|-------|-----|------|------|------|
| `chronos_bolt_small` | 4.160 | 5.367 | 0.036 | 0.718 |
| `lightgbm` | 4.458 | 5.799 | 0.039 | 0.767 |
| `ets` | 4.747 | 6.115 | 0.041 | 0.822 |
| `seasonal_naive` | 6.566 | 8.499 | 0.057 | 1.133 |

Lowest MASE: **`chronos_bolt_small`**


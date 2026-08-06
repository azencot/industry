# Panel schema

Long-format daily panel for forecasting method tradeoff demos.

## `generated/panel.parquet` (also `panel.csv`)

| Column | Type | Notes |
|--------|------|-------|
| `series_id` | str | e.g. `smooth_001`, `mean_step_003` |
| `ds` | date | daily, no gaps within a series |
| `y` | float | target (integer-valued for `intermittent`) |
| `regime` | str | one of: `smooth_seasonal`, `mean_step`, `promo_driven`, `intermittent`, `cold_start` |
| `promo` | int | 0/1; meaningful for promo / cold-promo series; else 0 |
| `price` | float | base or discounted price; constant outside promo regimes |
| `in_train` | bool | `ds <= cutoff` |

## `generated/series_meta.csv`

| Column | Type | Notes |
|--------|------|-------|
| `series_id` | str | PK |
| `regime` | str | regime id |
| `parent_dgp` | str | base process (`smooth` or `promo`) for cold_start |
| `base_level` | float | pre-shift / non-promo mean scale |
| `season_amp` | float | weekly seasonal amplitude |
| `noise_scale` | float | noise std |
| `shift_date` | date or empty | for `mean_step` only |
| `step_size` | float | absolute mean jump (mean_step) |
| `zero_rate_target` | float | for intermittent |
| `promo_lift` | float | multiplicative lift on promo days |
| `n_train_days` | int | count of train rows |
| `n_obs` | int | total rows including horizon |
| `seed_offset` | int | per-series RNG offset |

## `generated/cutoff.json`

| Key | Type | Notes |
|-----|------|-------|
| `cutoff` | str (YYYY-MM-DD) | last train date |
| `horizon` | int | forecast days after cutoff (28) |
| `freq` | str | `D` |
| `seed` | int | global seed |
| `start_date` | str | calendar start for long histories |
| `n_series_per_regime` | int | |

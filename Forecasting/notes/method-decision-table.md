# Method decision table (Day 1)

Interview lens: *when use / why choose / why reject* — not architecture tours.

---

## Tier A — speak fluently

| Method | Pros | Cons | Production use |
|--------|------|------|----------------|
| **Seasonal Naive** | Zero train cost; hard-to-beat baseline on strong seasonality; instant sanity check | No covariates; fails on trends, promos, regime shifts, intermittent zeros | Always ship as baseline + monitoring canary. Reject as sole model when demand is promo/price-driven or sparse. |
| **ETS** | Fast; strong on smooth seasonal series; interpretable; cheap to retrain per series | Weak with rich covariates; struggles with intermittency & related-series pooling; limited cross-learning | Local models for high-volume smooth SKUs / aggregates. Reject when you need price/promo response or catalog-scale transfer. |
| **LightGBM / XGBoost** | Covariates shine (promo, price, holiday, inventory); tabular SOTA; cheap inference; easy feature debugging; wins many M5-style bakeoffs | Needs feature engineering + leakage discipline; point forecast by default (quantiles need care); weak pure zero-shot / cold-start without history features | Default workhorse for retail/marketplace demand with known drivers. Reject when you truly need zero-shot across new series with no features, or trajectory generative paths. |
| **Chronos / Chronos-Bolt** | Strong zero-shot; minimal per-series tuning; Bolt = patch + direct multi-step (faster than AR Chronos-1); good “no feature store yet” path | Cost at millions of series; weaker when rich covariates dominate; may lose to tuned boosting on feature-rich panels; ops/versioning of FM stack | Cold-start, sparse-history, quick coverage across heterogeneous series. Reject as sole system when promo/price is the lever and feature pipeline already exists. |
| **TimesFM** | Decoder-only FM; strong zero-shot / few-shot; long context; Google-backed production narrative | Same FM cost story; covariate story historically thinner than boosting; not automatically calibrated for your business loss | Same niche as Chronos: bootstrap forecasts / heterogeneous catalogs. Reject if latency/cost SLA demands tiny local models and you already have features. |

### Tier A one-liners (memorize)

- **Naive first** — if you can’t beat seasonal naive, you don’t understand the series.
- **ETS** — local statistical strength without covariates.
- **LightGBM** — when the business drivers are columns you can trust.
- **Chronos/TimesFM** — when history is short, series are many, and features are thin or late.

---

## Tier B — niche fluency

| Method | One-liner | Still used when |
|--------|-----------|-----------------|
| **ARIMA** | Classical local linear; heavy per-series fit | Small # series, explainability mandates, legacy stacks |
| **Prophet** | Additive seasonality + holidays; easy API | Analyst/self-serve; marketing calendars; not catalog-scale science |
| **DeepAR** | Autoregressive RNN; probabilistic; early “global neural” | Legacy global models; teaching probabilistic DL; often replaced by TFT/boosting/FMs |
| **TFT** | Attention + known future covariates; interpretable attention | When known-future covariates matter and you want a single DL global model |
| **PatchTST** | Channel-independent patch Transformer | Strong channel-indep baseline in research; production less common than boosting/FMs |

---

## Tier C — name-drop

| Method | Family | Zero-shot? |
|--------|--------|------------|
| **Moirai** | Masked / any-variate FM (Salesforce) | Yes (designed for it) |
| **Moment** | TS foundation (open weights; multi-task) | Fine-tune / embedding heavy; not pure forecast-first |
| **Lag-Llama** | Probabilistic Llama-style for TS | Zero-shot / few-shot probabilistic |
| **TimeGPT** | Commercial API FM | Zero-shot via API |
| **Timer** | Generative / LLM-style TS | Research; interview = “another FM bet” |

---

## Decision tree (spoken ~30s)

```
Strong seasonality, no covariates? → seasonal naive / ETS baseline.
Rich trusted covariates (promo, price, holiday)? → LightGBM (or TFT if DL org).
Many series, short history, thin features? → Chronos-Bolt / TimesFM zero-shot.
Need uncertainty for inventory? → probabilistic path (quantile LGBM, DeepAR/TFT legacy, FM samples/quantiles) + business loss (pinball/CRPS), not MAPE alone.
Always: naive baseline + segment who wins (smooth vs intermittent vs promo-driven).
```

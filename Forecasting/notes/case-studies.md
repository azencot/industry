# Case studies — industry forecasting blogs

Day 6 progress. Look for: data quality, features, eval, ops — models secondary.

---

## 1. Amazon Science — History of Amazon’s forecasting algorithm (read 2026-08-06)

**Link:** https://www.amazon.science/latest-news/the-history-of-amazons-forecasting-algorithm  
**Theme:** decade of production evolution toward a **unified** forecaster for inventory decisions.

### What matters

- **Business stake:** can’t stock everything; need demand estimates that support inventory under huge catalog + uncontrollable spikes (launches, publicity, COVID-like shocks).
- **Era 1 — patchwork:** classical TS OK on stationary series; add-ons for seasonality, price elasticity, cold start; separate **Distribution Engine** for uncertainty on top of point forecasts → **hard to maintain**.
- **Era 2 — pooled tabular ML:** insight that products across categories can share behavior → features (demand, sales, category, page views) + **random forest / SQRF** for **quantiles** at millions of SKUs; still **manual feature engineering**.
- **Era 3 — deep unified model:** train on **multi-horizon quantile loss** (align train metric to inventory asymmetric costs) → retire many local systems; then MQ-RNN/CNN (less hand features); then MQ-Transformer (attention over own error history).
- **Next:** RL to optimize **cost savings**, not only forecast accuracy / inventory levels.

### Interview line

> “Amazon’s arc wasn’t ‘pick a fancier model’ — it was patchwork local systems → pooled quantile ML → unified deep quantile forecasters, because **inventory needs calibrated distributions** and **one maintainable champion** beats a zoo of specialists.”

### Tie to your prep

- Matches Day 1/2: pooling + features before fancy; Day 3: pinball/quantiles > vanity MAPE; Day 4: maintainability; bakeoff: don’t Chronos-everywhere without a production evolution story.

---

## 5. Lyft — Real-Time Spatial Temporal Forecasting (read 2026-08-06)

**Link:** https://eng.lyft.com/real-time-spatial-temporal-forecasting-lyft-fa90b3f3ec24  
**Theme:** marketplace supply/demand forecasts under **latency, refresh cost, and spatial granularity**.

### What matters

- Forecasts feed pricing, incentives, planning — not a leaderboard.
- **Geohash / hierarchical spatial** structure; signal quality varies by granularity and noise.
- **Classical TS vs NN** chosen by horizon + stability of spatial correlations + **engineering cost of refit** — near-term noisy local series often favor simpler/refit-friendly methods; longer horizons may justify heavier models if cost allows.
- Production design (streaming, feature store, serving) is part of the forecasting problem.

### Interview line

> “At Lyft, model choice is a **latency and retrain-cost** decision as much as an accuracy decision — classical vs deep depends on horizon and how stable the spatial structure is, not on what’s trendy.”

### Tie to your prep

- Day 4 “5M requests/day” language; Day 7 system design; contrasts Amazon’s catalog/inventory quantiles with marketplace **real-time spatial** constraints.

---

## Still to read (optional for Day 6 close)

| # | Post | Status |
|---|------|--------|
| 2 | Chronos-2 | skip until after Day 5 FM cards |
| 3 | DoorDash ELITE | recommended next (cost/accuracy ensembles) |
| 4 | Airbnb geography | recommended next (cold/thin history) |

---

## Reusable lines (bank)

1. **Amazon:** patchwork → pooled quantiles → unified deep; inventory needs distributions + one maintainable system.  
2. **Lyft:** classical vs NN = horizon + spatial stability + retrain/latency cost.

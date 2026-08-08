# Day 3 — Metrics cheat sheet

Interview goal: pick a metric that matches **demand shape + decision**, and know when each lies.  
Signed off 2026-08-08: point metrics · pinball/CRPS · intervals · coverage/calibration · business KPIs.

---

## Point metrics (quick map)

| Metric | Idea | Same units as \(y\)? | When it lies / breaks |
|--------|------|----------------------|------------------------|
| **MAE** | Mean \(\|y-\hat{y}\|\) — typical absolute miss | Yes | Hard to compare across scales / series |
| **RMSE** | \(\sqrt{\mathrm{mean}((y-\hat{y})^2)}\) — L2 / spike lens | **Yes** (root restores units; MSE does not) | Rare large errors dominate; bad sole champion metric if you care about typical days |
| **MAPE** | Mean \(\|y-\hat{y}\|/\|y\|\) — per-point % | % | **Unusable** at \(y=0\) / near-zero; overweight tiny days; underweight big SKUs |
| **SMAPE** | % with \((\|y\|+\|\hat{y}\|)/2\) in denom | % | Softer than MAPE on zeros, still noisy near both-zero; weaker than WAPE for retail panels |
| **WAPE** | \(\sum\|e\|/\sum\|y\|\) — portfolio % | % | Needs \(\sum\|y\|>0\); preferred “%” for demand panels |
| **MASE** | MAE / MAE(seasonal naive) — scaled vs baseline | Unitless ratio | Needs a clear seasonal naive; great for intermittent + cross-series compare |

**Default bakeoff stack (this repo):** MAE · RMSE · WAPE · MASE — see [`../code/reports/metrics_by_regime.md`](../code/reports/metrics_by_regime.md).

---

## Probabilistic (one layer)

| Metric | Idea | Interview use |
|--------|------|----------------|
| **Pinball** | Asymmetric quantile loss at level \(\tau\) (over- vs under-forecast weighted by \(\tau\)) | Train/select **q10/q50/q90** for inventory service levels |
| **CRPS** | Integral of pinball over all \(\tau\) — full distribution score | Compare probabilistic forecasts as a whole; better than point MAPE for uncertainty quality |

Point WAPE alone is not enough when the decision needs stock risk / safety stock.

---

## Intervals, coverage, calibration

**Prediction interval (PI)** — band \([L,U]\) claiming that \(y\) falls inside with **nominal** probability \(1-\alpha\) (e.g. 90% PI ⇒ \(\alpha=0.1\)).  
Convention: \(\alpha\) = miss/tail rate (outside); \(1-\alpha\) = claimed coverage (inside).

**Central PI from quantiles:** \(L = q_{\alpha/2}\), \(U = q_{1-\alpha/2}\).

| Nominal PI | \(\alpha\) | Lower | Upper |
|------------|------------|-------|-------|
| 90% | 0.1 | q5 | q95 |
| 95% | 0.05 | q2.5 | q97.5 |

Quantile meaning: \(P(Y \le q_\tau) \approx \tau\). So q95 ≈ “95% of outcomes at or below.” One-sided upper quantiles are fine for “don’t stock out” decisions.

**Coverage** — empirical hit rate of the PI on held-out (time-ordered) data. Claim 90% → observe ~90%. Too low = overconfident (narrow); too high = underconfident (wide). Check **conditional** coverage (horizon, promo, intermittent) — average can lie.

**Calibration** — are stated probabilities honest? Quantile check: ~\(\tau\) of actuals below \(\hat{q}_\tau\). Full CDF: PIT roughly uniform. Interval = object you ship; coverage/calibration = audit that the uncertainty is real.

---

## Business KPIs (above forecast error)

| Layer | Examples |
|-------|----------|
| Forecast quality | WAPE, MASE, pinball, coverage |
| Decision quality | **fill rate** (demand fulfilled / demand — *not* replenishment speed), stockouts, overstock, waste, missed GMV |
| Ops | latency, $/forecast, retrain freshness |

Principal line: optimize/report the **decision KPI**; use WAPE/pinball/coverage as diagnostics. “WAPE −5%” is weak if fill rate didn’t move.

---

## Forced answers (locked)

1. **When is RMSE misleading?**  
   Amplifies sparse large errors so model pick can chase outliers. Units are *not* the issue — RMSE matches \(y\); use it as a **spike lens**, not the only ship metric if business cares about typical miss (MAE/WAPE).

2. **When is MAPE unusable?**  
   True demand zero or near-zero → undefined / explodes. Also a bad portfolio lens (equal weight per timestep, not by volume).

3. **When is WAPE preferred?**  
   Over MAPE: one denom = total demand → stable with zeros, weights big series. Over MAE: same absolute errors, but as an interpretable **portfolio %**.

4. **Intermittent demand — what breaks / what instead?**  
   MAPE/SMAPE break. Lead with **WAPE and/or MASE**. Add pinball/CRPS if decisions need distributions.

---

## One-liners

- *“MAPE is a stakeholder convenience; WAPE/MASE are the selection metrics for sparse retail.”*
- *“RMSE = outlier-sensitive; MAE/WAPE = planning / typical miss.”*
- *“Need inventory risk → quantiles + pinball/CRPS + coverage, not point MAPE.”*
- *“α = outside; 1−α = nominal coverage; 90% central PI = q5–q95.”*
- *“Fill rate = demand fulfilled, not how fast you refill.”*

---

## Spoken: MAPE doubled overnight (playbook)

Practiced 2026-08-08 — keep this order; don’t jump to architecture.

1. **Trust the metric?** Confirm window, filters, new SKUs, more zeros. Pair with **MAE + total demand + WAPE/MASE** (and WAPE / seasonal-naive canary). MAPE can double while MAE flat if scale dropped or intermittency rose.
2. **Data / pipeline before model.** Joins, timezone, holiday calendar, promo flags, backfill, label lag, stockout censorship — fleet-wide demand drops *do* happen (events, outages).
3. **Scope.** Fleet vs category vs SKU; a few outliers vs systemic. Slice by regime (promo / intermittent / smooth).
4. **Model only if data+metric hold.** Champion vs seasonal naive / ETS / prior champion; same features at cutoff?
5. **Next action.** Dashboard: stop leading with MAPE on sparse demand; add WAPE/MASE. Model: fix features/calendar/retrain or regime routing — **not** MoE as first overnight fix.

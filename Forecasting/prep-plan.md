# Forecasting — week prep plan

**Track:** [`INDEX.md`](INDEX.md) · **Skill:** `/forecasting`  
**Window:** one focused week · start date: **2026-08-05**  
**Rule:** industry decision-making > new algorithms. Skip ARIMA/stationarity proofs.

---

## Verdict on the recommended plan (locked)

Keep the skeleton. Cut breadth so the week is finishable:

| Keep | Cut / compress |
|------|----------------|
| Decision questions as the north star | Day 1: don’t deeply read all 15 models — tier them |
| LightGBM pipeline (even if unused in your research) | Day 5: FM survey → 90–120 min competitor framing only |
| Eval + production days (highest gap) | Day 6: 3–4 curated blogs, not a 9-company crawl |
| Daily 30–45 min hands-on thread | Tourism / Favorita as optional; prioritize M4/M5 themes |
| Day 7 mock principal scientist | “One-page summary” = decision table, not encyclopedia |

**Daily non-negotiable:** 30–45 min pipeline work (naive → LightGBM → Chronos-Bolt/TimesFM → multi-metric compare).

---

## Day 1 — Industrial landscape (3h)

**Status (2026-08-06):** Tier A + decision table + bakeoff done. **Part 2 (M4/M5 themes) signed off** ([`notes/2026-08-05_day1-competition-themes.md`](notes/2026-08-05_day1-competition-themes.md)). TimesFM = Tier A one-liner only. Phase 1 data signed off.

### Part 1 — Methods as decision objects (~75 min)

Tier, don’t equalize:

| Tier | Methods | Depth |
|------|---------|-------|
| **A — must speak fluently** | Seasonal Naive, ETS, LightGBM/XGBoost, Chronos / Chronos-Bolt, TimesFM | Use / reject / when |
| **B — know the niche** | ARIMA, Prophet, DeepAR, TFT, PatchTST | One-liner + when companies still use |
| **C — name-drop only** | Moirai, Moment, Lag-Llama, TimeGPT, Timer | What family + zero-shot or not |

For each Tier A (and skim B): *When use? Why choose? Why reject?*

Deep-dives: [`notes/2026-08-05_tierA-deep-dives.md`](notes/2026-08-05_tierA-deep-dives.md) · session debrief: [`notes/2026-08-05_day1-tierA-debrief.md`](notes/2026-08-05_day1-tierA-debrief.md)

### Part 2 — Competition themes (~45 min)

Skim M4 + M5 (+ M3 only if time). Extract themes, not leaderboards:

- hierarchical forecasting
- intermittent demand
- large-scale related series
- what beat fancy models (ensembles, simple baselines, features)

### Part 3 — One-page decision table (~60 min)

Write [`notes/method-decision-table.md`](notes/method-decision-table.md):

| Method | Pros | Cons | Production use |

- [x] Tier A complete — decision table + deep-dives (SN, ETS, LGBM, Chronos); TimesFM = table one-liner only
- [x] M4/M5 themes signed off — [`notes/2026-08-05_day1-competition-themes.md`](notes/2026-08-05_day1-competition-themes.md)
- [x] Decision table drafted — [`notes/method-decision-table.md`](notes/method-decision-table.md)
- [x] Phase 1 data: synthetic panel + gold verify + [`data/review/REVIEW.html`](data/review/REVIEW.html) — **manual review signed off 2026-08-05**
- [x] Pipeline: SN + ETS + LightGBM + Chronos-Bolt bakeoff on signed-off panel ([`code/`](code/) · [`code/reports/metrics_by_regime.md`](code/reports/metrics_by_regime.md))
- [x] Spoken lock-in: Tier A self-checks (SN product-vs-baseline; ETS vs SN; Chronos everywhere) — LGBM vs Chronos corrected once; worth one clean retake
- [ ] Tier B skim (optional)

---

## Day 2 — Features + LightGBM (3h)

Industry forecasting is feature-heavy. Cover enough to *build and defend*:

lags · rolling stats · MA / EWMA · seasonality · holidays · promos · weather · price · inventory · events · categoricals / embeddings · cross-series · time encodings

**Implement:** LightGBM forecasting pipeline (lags + calendar minimum). Goal = *why boosting stays strong*, not a Kaggle medal.

- [x] Feature list with “why it helps / when it leaks” — lenses + v1 set: [`notes/2026-08-06_day2-features.md`](notes/2026-08-06_day2-features.md)
- [x] LightGBM pipeline runs; beats seasonal naive on ≥1 metric (see bakeoff overall WAPE/MASE)
- [x] Spoken 2-min: “Why LightGBM still wins many production bakeoffs” — done 2026-08-06; see corrections in session (baseline framing + inference wording)

---

## Cross-cutting — industry failure modes (light add, 2026-08-06)

Saw in a **peer/industry profile** (Keystone-style vaccine demand work — *not your story*). Treat as a checklist of problems principals expect you to name; fold into Days 3–4 / 7, don’t add a new day or copy their bullets.

| Failure mode | Where it lands in this plan | Interview one-liner |
|--------------|----------------------------|---------------------|
| Historical **stock-outs** (censored demand) | Day 2 features lens #3 · Day 3 intermittent · Day 4 missing/outliers | Model observed sales ≠ demand; unconstrain or censor-aware train |
| **Short history** / cold series | Day 1 M5 related series · Day 4 cold start · Day 6 Airbnb geography | Pool / hierarchy / priors — don’t fit a lonely local model |
| **Sparsity** / intermittent | Day 1 Part 2 · Day 3 metrics | WAPE/MASE (or intermittent-aware), not MAPE |
| **Irregular / multi-scale seasonality** | Day 2 calendar/holidays · Day 5 when FM helps | Separate week-of-year vs season-phase vs launch effects — don’t confound |
| **Probabilistic + hierarchical** | Day 3 pinball/CRPS · Day 1 hierarchy · Day 7 uncertainty | Decisions need quantiles + coherent plans, not leaf point MAPE |
| **Business tuning** / launch timing | Day 4 A/B + impact · Day 7 measure business impact | Forecast exists to change a decision (e.g. pull launch forward) |

- [ ] When doing Day 4 checklist, explicitly cover **stock-out censoring** + **business decision** (not only model ship)
- [ ] Day 7 probe: “Demand history has stock-outs — what do you do?”

---

## Day 3 — Evaluation (3h)

Study until you can answer without notes:

MAPE · SMAPE · WAPE · MAE · RMSE · MASE · pinball · CRPS · intervals · calibration / coverage · business KPIs

Forced answers:

- When is RMSE misleading?
- When is MAPE unusable?
- When is WAPE preferred?
- Intermittent demand — what breaks and what you use instead?

Skim (don’t deep-read everything): Amazon Forecast metrics docs; one Uber/Google forecasting-metrics writeup.

- [ ] [`notes/metrics-cheat-sheet.md`](notes/metrics-cheat-sheet.md) written
- [x] Pipeline: report MAE, RMSE, WAPE, MASE side-by-side ([`code/reports/metrics_by_regime.md`](code/reports/metrics_by_regime.md))
- [ ] Spoken 2-min: “MAPE doubled overnight — debug playbook”

---

## Day 4 — Production forecasting (3h)

Biggest academia → industry gap. Cover:

training pipeline · feature store · backtesting · rolling retrain · data/concept drift · cold start · missing data · outliers · monitoring · deploy · A/B · champion/challenger · online eval · latency · cost

Forced: *If the service gets 5M forecast requests/day, what changes?*

- [ ] [`notes/production-checklist.md`](notes/production-checklist.md)
- [ ] Spoken 3-min: productionize a SKU demand model end-to-end
- [ ] Pipeline: note what you’d monitor in prod for *this* model

---

## Day 5 — Foundation models (90–120 min, not a full day)

You already know this space. Goal = **competitor framing for interviews**, not re-learning.

For Chronos / Chronos-Bolt, TimesFM, (+ skim Moirai or Moment):

pretrain · tokenization / patching · zero-shot · fine-tune · context · probabilistic · failure modes · cost

Forced: *Why not Chronos everywhere? When does LightGBM still win?*

- [ ] [`notes/fm-competitor-cards.md`](notes/fm-competitor-cards.md) — ½ page each for 3 models
- [x] Pipeline: Chronos-Bolt small zero-shot compare (TimesFM still optional)
- [ ] Spoken 3-min: LightGBM vs Chronos decision tree

---

## Day 6 — Case studies (2–3h)

Curated only. Look for: data quality, features, eval, ops — notice models are often secondary.

### Reading list (pick **3–4**; all five are solid)

| # | Post | Why read (interview hook) |
|---|------|---------------------------|
| 1 | [The history of Amazon’s forecasting algorithm](https://www.amazon.science/latest-news/the-history-of-amazons-forecasting-algorithm) (Amazon Science) | Decade of production evolution: point → **quantiles**, many local systems → unified model, inventory decisions need distributions not MAPE flex — **read 2026-08-06** |
| 2 | [Introducing Chronos-2](https://www.amazon.science/blog/introducing-chronos-2-from-univariate-to-universal-forecasting) (Amazon Science, Oct 2025) | Latest FM framing: univariate → **covariate / multivariate** zero-shot; use to sharpen “when FM vs LightGBM,” not to abandon baselines |
| 3 | [How DoorDash built an ensemble for time series](https://careersatdoordash.com/blog/how-doordash-built-an-ensemble-learning-model-for-time-series-forecasting/) (DoorDash, 2023) | **Accuracy vs speed/cost**; ensembles of cheap learners beat grid-search of fancy configs at marketplace scale |
| 4 | [When history fails you, borrow from geography](https://airbnb.tech/data/when-history-fails-you-borrow-from-geography/) (Airbnb) | Cold / thin history: **borrow strength** across related corridors (hierarchical / prior propagation) — M5 “related series” in the wild |
| 5 | [Real-Time Spatial Temporal Forecasting @ Lyft](https://eng.lyft.com/real-time-spatial-temporal-forecasting-lyft-fa90b3f3ec24) (Lyft) | Marketplace forecasts under **latency + retrain cost**; classical vs NN chosen by horizon/granularity, not fashion — **read 2026-08-06** |

**Optional swaps** (if you want a 6th later): [Uber — Forecasting at Uber: An Introduction](https://www.uber.com/us/en/blog/forecasting-introduction/) (platform + backtesting culture); [Amazon Science — correlated products/sellers](https://www.amazon.science/blog/data-on-correlated-products-and-sellers-helps-improve-demand-forecasting) (cross-series / cold start via graphs).

**Today shortcut:** if reading ahead of Day 6, do **1 → 3 → 4** first (ops judgment); save Chronos-2 (#2) for after Day 5 FM cards; Lyft (#5) when you want production latency language.

- [x] 2/3 blogs summarized in [`notes/case-studies.md`](notes/case-studies.md) — Amazon history + Lyft (need one more: DoorDash or Airbnb)
- [x] One reusable line per blog for interviews — Amazon + Lyft locked in note
- [ ] Pipeline: failure analysis — where naive / LGBM / FM each win

---

## Day 7 — Mock principal scientist day

Run `/forecasting` on a subset. Aim for **3–5 min** structured answers:

1. Design forecasting for retail inventory at Amazon scale
2. Millions of series — architecture
3. New products / cold start
4. Holidays that move every year
5. Why not Chronos everywhere?
6. Why is LightGBM still competitive?
7. How do you forecast uncertainty?
8. Detect concept drift
9. Convince leadership to migrate to an FM (or not)
10. Measure business impact

- [ ] ≥6 questions spoken once; ≥3 retaken after feedback
- [ ] Notes in [`notes/`](notes/) with corrections
- [ ] Pipeline wrap: 1-page “what I’d ship” for the public dataset

---

## Hands-on project (every day, 30–45 min)

**Phase 1 data — signed off (2026-08-05):** synthetic multi-regime panel under [`data/`](data/). Human review via [`data/review/REVIEW.html`](data/review/REVIEW.html) complete; gold 19/19.

Then stick to that panel for the bakeoff (M5/Favorita/Electricity optional later):

1. Seasonal naive baseline  
2. LightGBM + lags + calendar  
3. Foundation model (Chronos-Bolt or TimesFM)  
4. Multi-metric eval (MAE, RMSE, WAPE, MASE)  
5. Segment analysis (where each wins/fails)  
6. Deploy/monitor notes (even if not deployed)

Model code will live under [`code/`](code/) (reads [`data/generated/`](data/generated/)).

---

## Progress log

| Day | Date | Done? | Artifact |
|-----|------|-------|----------|
| 1 | 2026-08-05–06 | yes* | Tier A + data + bakeoff v1; Part 2 themes signed off (*Tier B optional still open) |
| 2 | 2026-08-06 | yes | Feature lenses + spoken “why LGBM wins” ([`notes/2026-08-06_day2-features.md`](notes/2026-08-06_day2-features.md)) · debrief [`notes/2026-08-06_day1-part2-day2-debrief.md`](notes/2026-08-06_day1-part2-day2-debrief.md) |
| 3 | | | metrics cheat sheet |
| 4 | | | production checklist |
| 5 | | | FM cards + compare |
| 6 | | | case studies |
| 7 | | | mock answers |

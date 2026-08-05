# Tier A deep dives (Day 1)

Study cards for Seasonal Naive → ETS → LightGBM → Chronos. Interview lens: mechanism enough to sound competent, then **use / choose / reject / failure modes**.

---

## 1. Seasonal Naive

### What it actually does

Forecast = value from the **same season last period**.

- Daily with weekly seasonality: \(\hat{y}_{t+h} = y_{t+h-7}\)
- Monthly with yearly seasonality: \(\hat{y}_{t+h} = y_{t+h-12}\)
- “Seasonal naive” vs plain naive: plain naive uses \(y_t\) (last value); seasonal uses last **aligned** season.

No parameters. No fit. The only modeling choice is **which seasonal period** (and whether you have enough history to look back).

### Why industry still cares

1. **Lower bound of competence.** If your fancy model can’t beat seasonal naive on a strongly seasonal segment, you usually have a bug, leakage, or wrong segment — not a “research opportunity.”
2. **Monitoring canary.** Track WAPE(model) / WAPE(seasonal_naive). When that ratio blows up, something changed (data, holiday calendar, promo regime) before you blame the architecture.
3. **Business-aligned baseline.** Planners already think “same as last year / last week.” You’re speaking their language.

### When you’d actually use it

- Strong, stable seasonality and **weak exogenous drivers** (no big promo/price shocks).
- Aggregate series (category, region, total demand) more often than sparse SKU-day.
- As a **mandatory baseline** in every bakeoff, even when you know LightGBM will win overall.
- Cold debugging: “is the forecast broken or is the world non-seasonal this week?”

### Why a company would choose it

- Zero ML ops cost; explainable to finance/ops.
- Fast to compute for millions of series (lookup).
- Regulatory / audit simplicity in some settings.

### Why they’d reject it (as the *only* model)

- Promotions, price changes, stockouts, new products — seasonality alone is wrong.
- Trend / level shifts (COVID, expansion, competitor entry).
- Intermittent demand: last year’s zero or spike copies nonsense.
- Hierarchy: leaf seasonal naive often incoherent with parent plans unless reconciled.

### Failure modes to name in interview

- Wrong season length (daily series with annual pattern ignored).
- Holiday misalignment (Easter moves; “same DOY last year” ≠ same holiday).
- Stockout in the lookback week → you copy a censored low.
- Double-counting promotions that don’t repeat.

### Spoken 45s

> Seasonal naive copies the value from the same season one cycle ago. I always run it as a baseline and as a monitoring ratio against the champion. I’ll ship it alone only on smooth, strongly seasonal aggregates with no major covariates. I reject it as the system of record when promo, price, or intermittency dominate — and I never trust a model that loses to it on the seasonal segment without a clear reason.

---

## 2. ETS (Error, Trend, Seasonality)

### What it actually does

ETS = family of **exponential smoothing** models. Each series is decomposed into a small set of latent states that update every timestep:

| Component | Role |
|-----------|------|
| **Level** \(\ell\) | Current “typical” value |
| **Trend** \(b\) (optional) | Growth / decline (none, additive, damped) |
| **Season** \(s\) (optional) | Repeating pattern (none, additive, multiplicative) |
| **Error** | Additive or multiplicative noise around the forecast |

Forecast = combination of those states (e.g. level + trend + seasonal factor). Fitting = choose which components + estimate smoothing weights (how fast to adapt to new data). Packages (statsmodels, forecast::ets, Nixtla StatsForecast) usually **auto-select** the ETS variant via AIC/AICc on each series.

You do **not** need to derive the recursions in interview — you need: *local statistical model, state = level/trend/season, adapts via exponential weights, no exogenous features in classical ETS*.

### How it differs from seasonal naive

| | Seasonal naive | ETS |
|--|----------------|-----|
| Memory | Copies one past point | Smooths many past points into level/season |
| Trend | None (unless you hack it) | Can include / damp trend |
| Adaptation | Zero learning | Recent data can outweigh old (via \(\alpha, \beta, \gamma\)) |
| Fit cost | Free | Cheap, but **per series** |

ETS usually **beats** seasonal naive on smooth series with slow level shifts; naive can still win when the season is ultra-stable and ETS overfits noise.

### Why industry still cares

1. **Strong local baseline** after naive — especially weekly/monthly business series with clear seasonality.
2. **Cheap at moderate scale** — fit thousands–hundreds of thousands of series overnight; harder as a sole strategy at tens of millions without heavy engineering.
3. **Interpretable** — “level up, seasonal peak in December” is discussable with ops.
4. **Competition DNA** — exponential smoothing / ETS variants were historically hard to beat (M3/M4 era) before feature-rich global models took retail panels.

### When you’d actually use it

- Smooth, regularly observed series (store total, category, revenue, capacity).
- Few or no trusted exogenous drivers.
- Need a probabilistic interval from a classical model (many ETS implementations give prediction intervals).
- Per-series autonomy: each SKU/region gets its own fit (no pooling required).

### Why a company would choose it

- Mature, boring, debuggable; low ML-platform dependency.
- AutoETS pipelines are a known pattern (Amazon Forecast had ETS among algorithms; many internal “statistical fleet” stacks).
- Good champion for segments where LightGBM features are missing or leaky.

### Why they’d reject it

- **No classical covariates** — can’t natively say “+30% because of this promo tomorrow” (extensions exist; production usually switches to regression/boosting).
- **Intermittent / sparse** — zeros break the smooth-state story; Croston / TSB / intermittent-specific methods instead.
- **Cross-series learning** — ETS doesn’t borrow strength from similar SKUs; cold-start and rare items suffer.
- **Catalog scale** — millions of short series: fit/manage/monitor cost vs one global LightGBM or FM.
- **Rich known-future calendar** — possible with dummies in regression-ETS hybrids, but then you’ve reinvented feature models.

### Failure modes to name

- Multiplicative season on near-zero series → exploded forecasts.
- Undamped trend → runaway long-horizon growth.
- AutoETS picks over-seasonal model on short history.
- Regime break (COVID): states adapt slowly or chase the wrong level.
- Treating censored sales (stockouts) as true demand — same class of problem as naive.

### Spoken 45s

> ETS is exponential smoothing: each series gets a level, optional trend, and optional season, updated with exponential weights. I use it as the strong local statistical model when series are smooth and covariates are weak — often on aggregates. I reject classical ETS when promo/price drivers dominate, when demand is intermittent, or when I need cross-learning across a huge catalog; then I go LightGBM or a foundation model. I still keep ETS in the fleet as a segment champion and as a baseline that doesn’t depend on a feature store.

### Self-check

In one sentence: **why can ETS beat seasonal naive, and when does naive still win?**

---

## 3. LightGBM / XGBoost (tabular forecasting)

### What it actually does

Forecasting is reframed as **supervised learning on a table**, not as a classical TS state model.

Each training row ≈ one `(series_id, timestamp)`:

| Target | Features (examples) |
|--------|---------------------|
| \(y_{t+h}\) or \(y_{t+1}\) | lags \(y_{t}, y_{t-1}, \ldots, y_{t-m}\); rolling mean/std; EWMA |
| | calendar: dow, week, month, holiday flags |
| | exogenous: price, promo, inventory, weather |
| | series identity: category, brand, store (categorical / target encodings) |
| | known-future: scheduled promo tomorrow, planned price |

**LightGBM** builds an additive ensemble of trees that minimize a loss (MSE, MAE, quantile/pinball, …). Inference = fast tree traversal. Same story for XGBoost/CatBoost; LightGBM is the industry shorthand for “gradient-boosted tabular demand model.”

Global by default: **one model (or a few) across many series**, so similar SKUs share statistical strength.

### Direct vs recursive multi-step

| Style | Idea | Tradeoff |
|-------|------|----------|
| **Recursive** | Predict \(t+1\), feed as lag for \(t+2\), … | Error accumulates; one model |
| **Direct** | Separate model (or multi-output) per horizon \(h\) | No feedback error; more models / more compute |
| **Seq2seq-ish hybrids** | Rare in pure LGBM stacks | Usually stick to direct or recursive |

Interview preference: name both; say you pick by horizon length and error accumulation on a backtest.

### Why it dominates many production bakeoffs (esp. M5-like)

1. **Exogenous drivers are first-class** — promo/price/holiday are columns, not afterthoughts.
2. **Cross-series learning** — rare/intermittent items borrow from siblings.
3. **Non-linear interactions** — “promo × weekend × brand” without hand-specified equations.
4. **Cost** — train on billions of rows with CPU; infer in ms; easy to shadow/A/B.
5. **Debuggability** — feature importance, partial dependence, “which promo flag broke?”

### When you’d actually use it

- Retail / marketplace / ads demand with **trusted feature pipelines**.
- Panels: many related series, shared categories, known-future calendar.
- Need a **maintainable champion** that beats naive/ETS on WAPE/WRMSSE-style metrics.
- Quantile forecasts via quantile loss or separate quantile models (P50/P90 for inventory).

### Why a company would choose it

- Wins when the business already invests in a **feature store**.
- Clear ownership: data quality + features often move the needle more than architecture.
- Fits existing ML platforms (Spark, SageMaker, Michelangelo-class stacks).

### Why they’d reject it (or demote it)

- **No / weak features** — then you’re approximating lags with trees; Chronos/TimesFM may win with less plumbing.
- **True cold-start** — brand-new SKU with empty lags; need embeddings, hierarchy priors, or FM zero-shot until history exists.
- **Leakage risk** — using same-day sales, post-hoc adjusted price, or “realized promo lift” that wasn’t known at forecast time.
- **Trajectory / path uncertainty** — trees give point/quantile per step; full generative sample paths are awkward vs DeepAR/FM.
- **Very long pure sequential dependence** with no covariates — sometimes DL/FM edge, if you have the ops appetite.

### Failure modes to name

- **Leakage** (most common “too good to be true” backtest).
- **Distribution shift** in promo policy or price — importance rankings go stale.
- **Target = sales not demand** — stockouts censor labels; model learns “we sell 0 when empty.”
- **Naive time split bugs** — random row split instead of time-based / embargo.
- **Overpowered categoricals** — memorizes SKU id instead of generalizing (need regularization / good encodings).
- MAPE training on intermittent series → pathological.

### vs ETS / Chronos (decision)

```
Trusted promo/price/calendar features + large panel?
  → LightGBM (default production workhorse)

Smooth local series, no feature store?
  → ETS / seasonal naive fleet

Short history, thin features, need coverage tomorrow?
  → Chronos-Bolt / TimesFM zero-shot (then maybe hand off to LGBM as features mature)
```

### Spoken 45s

> I treat forecasting as tabular supervised learning: lags, rolling stats, calendar, and business exogenous features, trained globally with LightGBM so related series share strength. It’s my default when promo, price, and holidays actually drive demand and the feature pipeline is trustworthy. I reject it as the only tool when features are thin or cold-start dominates — then a zero-shot foundation model is a better bootstrap — and I’m paranoid about leakage and sales-vs-demand censorship in the labels. Trees win a lot of bakeoffs because industry forecasting is feature-heavy, not because boosting is magically best for every time series.

---

## 3b. Primer — gradient boosting family (from zero)

*For when LightGBM/XGBoost are unfamiliar. Forecasting use is still “tabular rows → predict y”; this section is the model family underneath.*

### Step 1 — One decision tree

A regression tree partitions the feature space with yes/no rules (“promo=1 AND dow=Sat?”) and predicts a **constant** in each leaf (usually the mean of training rows that fell there).

- **Pros:** nonlinear, handles interactions, mixed feature types  
- **Cons:** one tree underfits or overfits hard; unstable

### Step 2 — Ensemble idea

Combine many weak trees. Two famous recipes:

| Recipe | How trees relate | Intuition |
|--------|------------------|-----------|
| **Bagging / Random Forest** | Trees trained in **parallel** on bootstrap samples; average predictions | Reduce variance |
| **Boosting** | Trees trained **sequentially**; each fixes leftover error of the current ensemble | Reduce bias by chasing residuals |

LightGBM and XGBoost are **boosting**, not random forests.

### Step 3 — Gradient boosting (conceptual)

Start with a simple model \(F_0\) (e.g. predict global mean).

For \(m = 1..M\):

1. Compute how wrong you are — for squared loss, residual \(r_i = y_i - F_{m-1}(x_i)\).  
   In general: residual ≈ **negative gradient** of the loss w.r.t. current prediction.
2. Fit a **small tree** \(h_m\) to those residuals (or gradients).
3. Add it with a learning rate \(\nu\):

\[
F_m(x) = F_{m-1}(x) + \nu\, h_m(x)
\]

Final predictor: \(F_M(x)\). More trees \(M\) + smaller \(\nu\) → slower, usually better generalization if you early-stop.

**Loss can change the “residual”:**
- MSE → ordinary residuals  
- MAE → sign-like gradients  
- **Pinball / quantile** → asymmetric gradients → P50 / P90 forecasts for inventory  

That’s why the same LightGBM engine can do point or probabilistic-ish quantile forecasts.

### Step 4 — What XGBoost added (2010s workhorse)

**XGBoost** = “Extreme Gradient Boosting”: same sequential additive trees, with engineering + objective extras that made it dominate Kaggle/industry:

- **Second-order** approximation of the loss (uses gradient *and* Hessian) → stabler / faster optimization than plain first-order boosting  
- Strong **regularization** on leaf weights and tree complexity  
- System: cache-aware, approximate split finding, sparsity awareness, parallelize *within* tree construction  
- Became the default “boosted trees” brand name

Mental model: *XGBoost popularized production-grade gradient boosting.*

### Step 5 — What LightGBM changed

**LightGBM** (Microsoft) = same family (gradient-boosted trees), different implementation bets for **speed and scale**:

| Topic | XGBoost (classic) | LightGBM |
|-------|-------------------|----------|
| Tree growth | Often **level-wise** (depth by depth) | **Leaf-wise** (grow the leaf that cuts loss most) |
| Split finding | Histogram / approx options; historically heavier | **Histogram-based** binning by default — very fast |
| Categoricals | Often need encoding | Native categorical handling (with caveats) |
| Scale | Excellent | Often **faster / less memory** on huge row counts |

Leaf-wise can reach lower loss with fewer leaves but **overfits easier** on small data → need `num_leaves`, depth caps, min data in leaf.

**CatBoost** (Yandex) = third sibling: ordered target statistics for categoricals, strong out-of-box defaults. In interviews, “LightGBM/XGBoost/CatBoost” = one family.

### Step 6 — Same family, different logo

```
Decision tree
  → Boosted additive ensemble of trees
       → Gradient boosting (fit trees to loss gradients)
            → XGBoost  (GOAT popularizer; L2-approx + reg + systems)
            → LightGBM (histogram + leaf-wise; fast at big tabular scale)
            → CatBoost (categorical-focused variant)
```

For forecasting interviews: saying “I’d use LightGBM” means **gradient-boosted trees on a feature table**, not a different scientific paradigm from XGBoost. Choice is mostly **tooling, speed, categoricals, team standard**.

### Step 7 — Hyperparameters you’ll actually name

| Knob | Role |
|------|------|
| `n_estimators` / rounds | Number of trees \(M\) |
| `learning_rate` | \(\nu\) — shrink each tree’s contribution |
| `num_leaves` / `max_depth` | Tree complexity (LightGBM thinks in leaves) |
| `min_data_in_leaf` | Prevent tiny overfitting leaves |
| `subsample` / `colsample` | Row/feature sampling per tree |
| `early_stopping` | Stop when validation loss stalls |

Train with **time-based validation**, not random CV.

### Step 8 — Tie back to forecasting

You do **not** give LightGBM a raw sequence API like Chronos. You build rows:

\[
x_t = [\text{lags}, \text{rollings}, \text{calendar}, \text{promo}, \text{price}, \ldots], \quad
\hat{y}_{t+h} = F_M(x_t)
\]

Global \(F_M\) over many series ⇒ cross-learning. That’s the whole relationship: **boosting family = how \(F_M\) is built; forecasting quality = whether \(x_t\) and the label are honest.**

---

## 4. Chronos / Chronos-Bolt

### What it is

**Chronos** = Amazon’s **pretrained time-series foundation model** family: train once on a huge corpus of series, then **forecast new series with little or no task-specific training** (zero-shot / light fine-tune).

Different scientific bet from LightGBM:

| | LightGBM | Chronos |
|--|----------|---------|
| Input | Feature table you engineer | Mostly the **history of the series** (values) |
| Learning | Supervised on your panel | **Pretrain** on many datasets, then transfer |
| Cold-start / thin features | Weak unless you invent features | **Stronger** zero-shot story |
| Promo/price | Natural | Historically weaker / not the main path (improving in later variants) |

### Chronos-1 (original) — mechanism worth naming

1. **Scale** the series (e.g. mean scaling) so magnitudes transfer.  
2. **Quantize** real values into a discrete vocabulary (bins) → each timestep ≈ **one token**.  
3. Train a **language-model-style** model (T5-ish) to predict next tokens.  
4. At forecast time: sample many future token paths, **de-quantize** back to values → distribution over futures (often via sample paths).

Inference cost: **autoregressive** over the horizon (token-by-token) × number of sample paths. Accurate enough to matter; **expensive** at catalog scale if you’re careless.

Interview line you already used in FinTech prep: *quantize → 1 token/step → AR; e.g. sample paths × horizon.*

### Chronos-Bolt — what changed

**Bolt** keeps the foundation-model idea but changes representation and decoding for speed:

- **Patching:** group a window of values into a patch embedding (not one token per step).  
- **Direct multi-step / quantile-style heads** instead of slow per-step AR token sampling.  
- Practical punchline: **much faster** forecasts, still zero-shot-friendly — the variant you should default to in “what would you ship?” talk unless someone asks about Chronos-1 sampling.

(Chronos-2 exists in the broader Amazon narrative with richer covariates — mention only if asked; Day 1 Tier A = Chronos / Bolt.)

### Pretraining (what “foundation” means here)

- Trained on large mixtures of public + synthetic / diverse time series.  
- Objective: next-step / future-segment prediction in the tokenized or patched space.  
- After pretrain: given a **context window** of a new series, emit a forecast **without** training a per-SKU model.

Fine-tuning: optional on your domain panel when zero-shot is close but biased; still cheaper than training DeepAR-from-scratch culture for every team.

### When you’d actually use it

- **Many series, short history**, weak shared features.  
- Need **coverage tomorrow** before a feature store is ready.  
- Heterogeneous catalog where per-series ETS is ops-heavy and LGBM has nothing to chew on.  
- Bootstrap / challenger in a champion–challenger setup against LGBM/ETS.  
- Probabilistic paths (Chronos-1 samples) or quantile outputs (Bolt-style) for inventory-aware uncertainty — with calibration checks.

### Why a company would choose it

- Shrinks time-to-forecast for new products and long-tail SKUs.  
- Less feature engineering headcount for v0.  
- Aligns with “foundation model” platform bets (shared backbone, many consumers).

### Why they’d reject it as the *only* system

- **Rich trusted covariates** — tuned LightGBM often wins on WAPE and is cheaper to serve.  
- **Cost / latency at millions of series × frequent refresh** — FM inference bill vs tree lookup.  
- **Maintainability** — GPU/accelerator path, model versioning, drift vs a boring LGBM job.  
- **Business levers** — if planning is “turn promo knobs,” a model that barely sees promo is a hard sell.  
- Not a substitute for **demand vs sales** censorship handling, hierarchy reconciliation, or metric choice.

### Failure modes to name

- Context too short / wrong scaling → garbage zero-shot.  
- Series outside pretrain support (extreme intermittency, exotic seasonality) → confident but wrong.  
- Using Chronos-1 AR sampling naively at full catalog → blow the compute budget.  
- Skipping baseline: lose to seasonal naive on highly seasonal aggregates → you didn’t segment.  
- Treating FM as drop-in replacement without backtest by segment (smooth vs promo-driven vs cold-start).

### vs LightGBM (the money contrast)

```
Have promo/price/holiday features that actually drive the KPI?
  → LightGBM champion; Chronos optional challenger on cold/long-tail

Thin features, new SKUs, need forecasts this week?
  → Chronos-Bolt (or TimesFM) first; graduate segments to LGBM as features mature

Always:
  → seasonal naive / ETS baselines + segment who wins
```

### Spoken 45s

> Chronos is a pretrained time-series foundation model: it learns general forecasting behavior from a huge corpus, then zero-shot forecasts a new series from its history. Chronos-1 tokenizes via value quantization and decodes autoregressively with sample paths; Chronos-Bolt patches values and predicts multi-step more directly so it’s cheaper to serve. I’d use Bolt when history is short and features are thin — especially cold-start and long-tail. I would not replace a strong LightGBM stack when promo and price are the main levers, and I’d never roll it out without beating naive/ETS by segment and watching inference cost.

### Self-check

In one sentence: **Why not Chronos everywhere? What would make you pick Chronos-Bolt over LightGBM anyway?**

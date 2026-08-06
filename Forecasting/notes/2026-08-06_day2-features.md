# Day 2 — Features for LightGBM (lenses, not laundry list)

Signed off framing: 2026-08-06. Interview goal = defend a v1 set + leakage judgment, not memorize every covariate family.

---

## Three decision lenses

### 1. Known-at-cutoff vs leak

Every feature is one of:

| Kind | Examples | Fair? |
|------|----------|-------|
| **History** | lags, rolling/MA/EWMA | Yes if shifted to forecast origin |
| **Known future** | planned promo/price, calendar, holiday **flag** | Yes if ops has it at cutover |
| **Realized future** | final promo that “actually ran,” end-of-day sell-through, observed weather | **Leak** |

**Rule:** available at forecast origin for the full horizon — or it’s cheating.  
**Debug hook:** sudden accuracy jump → check for a same-day realized field.

### 2. Drivers > architecture

Ask: *what would a merchant change to move demand?*  
If promo/price/events dominate → put those in first; boosting often beats pure sequence / FM zero-shot.  
If smooth seasonal, no drivers → lags + calendar may suffice; Chronos can compete.

**Bakeoff pin:** LightGBM crushed `promo_driven` because the lever was in the features — not “trees > FMs.”

### 3. Label problems ≠ feature problems

Stockouts / censorship: adding inventory columns doesn’t fix modeling **observed sales** as if they were demand. May need unconstraining / censoring-aware training.  
Same class of trap: returns, substitutions, store closures.

---

## v1 ship set (defend in 30 sec)

| Feature | Why | When delay / reject |
|---------|-----|---------------------|
| Lags (1, 7, 28) | Autocorr / weekly seasonality | Cold start / very short history; stale lags after level break |
| Calendar (dow, month) | Cheap known-future seasonality | — |
| Planned promo + price | Retail’s real driver | If only *realized* flags exist at cutoff → leak; if ops can’t supply plan → delay |
| Category / store id | Cross-series pooling | Careless **target encoding** (full-sample means) → leak |

**v1.5** (when contracts are clean): holiday event table, weather *forecasts*, inventory with clear censorship story, embeddings.

Moving holidays → reason to add an **event calendar**, not a reason to skip holidays. Reject static day-of-year / lag-365 as a holiday proxy.

---

## Interview hooks

1. “Features are a **contract with operations**, not a Kaggle column dump.”
2. “If covariates drive demand, boosting often beats FMs — M5 and the bakeoff both showed that.”
3. “First debug when accuracy jumps: **did someone leak a same-day realized field?**”

## Spoken Day 2 closer

“Why LightGBM still wins many production bakeoffs”

**Lock (after 2026-08-06 attempt):**
- Lead with **known-future covariates + global pooling**, not “fast/interpretable” alone.
- True baselines = SN/ETS; LGBM = strong **production default** before FM escalation — not “baseline before accuracy.”
- Inference: train once on panel; **score in parallel over series/rows**. Avoid “recursive eval” unless you literally roll lags step-by-step.
- Cite M5 + bakeoff `promo_driven`; DL/FM without promo features can’t see the lever (unless promo is purely seasonal in history).
- Close: maintainable champion + monitoring; still segment (intermittent / smooth may favor other models).


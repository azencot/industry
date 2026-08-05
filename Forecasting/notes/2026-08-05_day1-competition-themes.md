# Competition themes (Day 1 Part 2)

Skim themes from M4 / M5 — not leaderboard memorization.

---

## M4 (2018) — many series, method bakeoff

- **Scale of related series:** thousands of series; global / combination methods competed with local stats.
- **Simple + ensemble wins culture:** pure “fancy DL alone” was not an automatic win; combinations and careful local methods stayed competitive.
- **Takeaway for interviews:** at catalog scale, **pooling + ensembling + strong baselines** beat “one novel architecture.”

## M5 (2020) — Walmart hierarchical retail

- **Hierarchical forecasting:** day × store × department × product; coherence (bottom-up / top-down / MinT-style) matters for planning, not only leaf accuracy.
- **Intermittent / sparse demand:** many zeros at SKU-store-day; MAPE-type metrics misbehave → weighted / scaled / hierarchical metrics.
- **Covariates dominate:** prices, promos, events, SNAP — **feature-rich tabular/boosting** crushed many pure sequence models.
- **Large-scale related series:** cross-learning across items/stores helps cold and sparse series.
- **Takeaway:** retail demand ≈ **features + hierarchy + right metric**, not “best Transformer.”

## M3 (optional)

- Smaller classic bakeoff; reinforced that **simple exponential smoothing / local methods** remain hard to beat on many series.

## Favorita / Tourism (optional)

- Favorita: grocery + oil/holiday covariates → again **external drivers**.
- Tourism: hierarchical visitor series → coherence / aggregation story.

---

## Interview bullets (use these)

1. “M5 taught industry that **promo/price features + LightGBM-class models** often beat sequence DL on retail panels.”
2. “Hierarchical coherence is a **decision-support** constraint — leaf WAPE ≠ usable plan.”
3. “Intermittent demand needs **metrics and models** that don’t explode on zeros — not MAPE.”
4. “Competitions reward **ensembles and process**; production rewards **maintainable champions** with monitoring.”

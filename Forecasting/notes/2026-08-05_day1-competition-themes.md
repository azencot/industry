# Competition themes (Day 1 Part 2) — signed off 2026-08-06

Skim themes from M4 / M5 — not leaderboard memorization. Extracted for interview use.

---

## M4 (2018) — many series, method bakeoff

**What it was:** thousands of heterogeneous series; classical stats, ML, and DL all competed.

- **Large-scale related series:** pooling / global methods and **combinations** competed with pure per-series local models.
- **Simple + ensembles beat “one fancy model”:** strong statistical baselines and ensembles stayed competitive; novel DL alone was not an automatic win.
- **Interview line:** at catalog scale, ship **baselines + pooling/ensembles**, not “latest architecture.”

## M5 (2020) — Walmart hierarchical retail

**What it was:** store × department × product × day demand; lots of zeros; prices/promos/events. Maps closest to industry retail demand.

1. **Hierarchical forecasting**  
   Leaf accuracy ≠ usable plan. Planning needs **coherent** forecasts up the tree (bottom-up / top-down / reconciliation).  
   *Prod:* optimize for the level decisions are made (often higher), then reconcile.

2. **Intermittent / sparse demand**  
   Many SKU-store-days are zero → MAPE blows up or is undefined. Need **weighted/scaled** metrics (WAPE, MASE, hierarchical weights).  
   *Prod:* pick metric by demand shape; don’t default to MAPE.

3. **Large-scale related series**  
   Cross-learning across items/stores helps **cold and sparse** series; pure local models starve.  
   *Prod:* global LightGBM / shared model + category features is the workhorse pattern.

4. **What beat fancy sequence models**  
   **Promo/price/event features + tabular boosting** dominated many pure sequence DL entries. Features and process > architecture flex.  
   *Prod:* if covariates drive demand, LightGBM-class often beats Chronos-everywhere (matches bakeoff `promo_driven`).

## M3 (optional one-liner)

Smaller classic bakeoff: **ETS / simple local methods** remain hard to beat on many “clean” series.

## Favorita / Tourism (optional)

- Favorita: grocery + oil/holiday covariates → again **external drivers**.
- Tourism: hierarchical visitor series → coherence / aggregation story.

---

## Interview bullets (lock these)

1. “M5 taught industry that retail ≈ **features + hierarchy + right metric**, not best Transformer.”
2. “Hierarchical coherence is a **decision-support** constraint — leaf WAPE ≠ usable plan.”
3. “Intermittent demand → **don’t use MAPE**; use WAPE/MASE (or intermittent-aware metrics).”
4. “Competitions reward **ensembles and process**; production rewards a **maintainable champion** with monitoring.”

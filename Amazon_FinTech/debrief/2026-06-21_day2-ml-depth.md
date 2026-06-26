# Debrief — 2026-06-21 — Day 2 ML/LLM depth (interactive)

## Session

- **Type:** ml-deep-dive simulation (Day 2 prep — first three bullets + follow-ups)
- **Duration:** ~60 min interactive Q&A (prior ~30 min reading logged in [`2026-06-21_continual-pretraining-blog.md`](2026-06-21_continual-pretraining-blog.md))
- **Prior context:** Day 1 complete — [`elevator-pitch.md`](../elevator-pitch.md), [`anchor-cheat-sheet.md`](../anchor-cheat-sheet.md); Karan blog read earlier same day
- **Not covered:** prep-plan line 19 — four 3-min spoken drills (end-to-end system; safe deploy; scarce labels; payment doc extraction)

---

## Scores (session)

| Topic | Score | Top gap |
|-------|-------|---------|
| RAG vs FT vs CPT | ~55→70 after blog pushback | Say **limited labels + large unlabeled corpus**, not "data scarce"; not "large data → RAG/FT" |
| Eval gating + corrections | ~60 | IC voice ("I built"), metrics (killed TR mixes, ±0.3 pp pilot), FinTech slice mapping |
| NER/IE + low labels | ~78 | Name **ECG-QALM**; spell out synthetic risks; weak-sup examples |

---

## Recurring corrections (promote to every ML answer)

1. **Two-axis data framing:** labels scarce ≠ corpus scarce. CPT sweet spot = **large unlabeled domain corpus + limited instruction labels + large/unknown task set** (Karan blog quote).
2. **Always separate OCR/parse failures from model errors** — format gates, hard stop on empty compliance fields.
3. **FinTech objective:** precision on compliance-critical **slices**, not headline F1/recall.
4. **IC voice:** "I owned / I built / I killed" + **one number** (TSExam 0.890, TR ~29%, attr-recovery 0.72, pilot ±0.3 pp).
5. **Don't CPT for a single-field regression** — targeted SFT + hard negatives from corrections first; CPT for foundation gaps.
6. **Practice format:** score + gaps → **full reference answer** → optional retake (user preference; now in `ml-deep-dive` skill).

---

## Topic 1 — RAG vs fine-tuning vs continual pre-training

### Decision frame (blog-aligned)

| Method | When | Cost | Limitation |
|--------|------|------|------------|
| **RAG** | Citeable/refreshable facts; narrow task + good retrieval | Inference + index | Doesn't teach finance syntax/style |
| **Instruction FT** | Known task; labeled examples (can be small) | Lowest train cost | Weak broad domain knowledge; task interference |
| **CPT** | Large **unlabeled** domain corpus; **limited labels**; many/unknown downstream tasks | Middle | Needs curation + regression gates on general capability |

**Not either/or in prod:** foundation (CPT or base) + RAG for audit trail + tiered eval + routing.

**Drift:** RAG = stale index; CPT/FT = slice regressions / forgetting → offline gates + shadow.

### Follow-up: 500 invoices + 10M SEC — what first?

- **First:** 500 labeled invoices → baseline + eval harness + instruction FT on extraction slices (amount, vendor, date).
- **Parallel (not sequential):** SEC corpus → **RAG index** (no gold needed) or **CPT pipeline** (curation, dedupe) if errors are domain-language gaps across tasks.
- **One line:** *Labels first for the task; corpus in parallel for domain.*

---

## Topic 2 — Eval gating + corrections loop

### Reference answer (~90s)

```
Problem — full benchmark runs too expensive; headline accuracy hides slice regressions
  (same in FinTech: entity-type slices, parse failures).

What I built — tiered gates, cheap → expensive:
  (1) loss + small gold sanity
  (2) target capability slice (TR on TSExam)
  (3) broader in-domain subset (TSRBench subset)
  (4) full external + in-house regression
  + parse-miss logged separately from accuracy.

Gating — advance only if target slice wins AND prior buckets don't regress.
  Killed TR bucket mixes (~29% vs control) despite gains elsewhere.

FinTech map — precision by entity type; hard block if amount precision drops.

Corrections — pre-ship: corrections → gold/hard-case suite;
  post-ship: shadow mode → override rate by slice → hard-negative mining → retrain;
  promote only when offline gates pass again.

Lesson — eval is a release contract, not a scoreboard.
```

### Follow-up anchors

- **Amount precision down, F1 up → don't ship.** Fix with targeted labels/hard negatives; CPT only if systemic domain gap.
- **Shadow mode:** catches layout/OCR drift, template changes, selective user corrections; track override rate, abstention, latency — not just offline F1.

---

## Topic 3 — NER/IE + low labels

### Reference answer (~90s)

```
Problem — messy PDFs; gold NER expensive; wrong amount/vendor = compliance risk.

Toolkit (layered):
  (1) Weak supervision — rules, gazetteers, distant labels from metadata
  (2) Entity-controlled synthetic — ECG-QALM-style; cheap but template/domain-gap risk
  (3) Human corrections — shadow/prod edits as hard negatives
  (4) Unlabeled domain corpus — RAG index or CPT when labels stay scarce

My project — audited tasks, found ~6–7 missing ops, extended TSExam;
  synthetic TS↔text + CaTS; attr-recovery 0.72; Stage B reasoning still open.

Messy docs — OCR/parse failures separate from model NER; format gates; hard stop if required fields empty.

Eval — precision on compliance slices; synthetic must regress-test on real scanned layouts.

Lesson — instrument tasks before scaling data.
```

### When synthetic NER hurts

Template repetition, layout-blind text, entity combos rare in prod → high offline F1, shadow precision collapse.

---

## Decisions / artifacts updated

- [x] [`prep-plan.md`](../prep-plan.md) — Day 2 bullets 1–3 marked done; spoken drills still open
- [x] [`ml-deep-dive/SKILL.md`](../ml-deep-dive/SKILL.md) — full reference + retake step
- [x] [`Amazon_FinTech/mocks/2026-06-21_ml-deep-dive.md`](../mocks/2026-06-21_ml-deep-dive.md)
- [ ] `stories/` — no LP work this session
- [ ] `omri_azencot_experience.md` — no change

---

## Open questions

- Retake Topic 1 or 2 for scored 90s pass? (optional polish)
- Four spoken drills (prep-plan line 19) — schedule next session or fold into Day 6 mock

---

## Next session (one prompt for session B)

> `@Files Amazon_FinTech/debrief/2026-06-21_day2-ml-depth.md` `@Files Amazon_FinTech/anchor-cheat-sheet.md`  
> Run `/ml-deep-dive` — one spoken drill: **safe deploy of an LLM extraction system** (3 min → score → full reference → retake). Then start Day 3 `/mock-lp` (Customer Obsession + Ownership).

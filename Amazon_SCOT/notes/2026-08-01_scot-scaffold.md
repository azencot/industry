# Debrief — 2026-08-01 — Amazon SCOT scaffold + Mengfei ingest

## Session

- Type: exploration / track setup
- Duration: ~1 session
- Prior context: FinTech loop primary; user opened `Amazon_SCOT/` for Boris call Mon 3 Aug 2026

## Conclusions

- SCOT is a **relationship / contribution** track, not a FinTech-style PS1 machine (no stories/mocks/timed-code bank yet).
- Monday call shape: short NeurIPS paper + workshop update → Mengfei bridge → contribution pitch → ask for openings/intros.
- **Pitch spine (from Feb 19 Mengfei dinner):** generative modeling as **forecasting infrastructure** (synthetic pretrain → cost/latency/leakage; cold-start; rare regimes) on top of already-strong coherence / decision-alignment (CLOVER). Not “replace quantiles everywhere.”
- Quantiles vs trajectories distinction is a strong IC talking point: single-period newsvendor vs path-dependent / lead-time coupled decisions.
- Production-experience and level probes already have ready answers in Mengfei notes.
- Primary thesis for Boris: synthetic/sim as foundation-forecasting infrastructure (aligns with ZSF-by-simulation); backups = coherent hierarchical synthetic, trajectories-where-needed, synthetic stress-test gates.

## Decisions / artifacts updated

- [x] Created `Amazon_SCOT/` lean file set (INDEX, contacts, collaboration, contribution-plan, questions, mengfei-notes, notes/)
- [x] Ingested Mengfei prep + dinner notes (structured + raw archive)
- [x] Wired root `INDEX.md` + `AGENTS.md` for dual-track reading order
- [ ] Paper/workshop exact titles still TODO in `collaboration.md`
- [ ] Pitch not yet rehearsed aloud

## Corrections to promote

| Issue | Where promoted |
|-------|----------------|
| Repo now has two Amazon tracks | `AGENTS.md`, root `INDEX.md` |
| SCOT session debriefs live under `Amazon_SCOT/notes/`, not FinTech debrief/ | debrief skill + `AGENTS.md` reading order (this session) |
| March SCOT group talk read managerial (roadmap / backbone-of-future) | [`talks/README.md`](../talks/README.md); anti-patterns in `contribution-plan.md` |

## Open TODOs before Mon 3 Aug

1. Fill paper/workshop titles + IC contribution slice in [`collaboration.md`](../collaboration.md)
2. Rehearse [`contribution-plan.md`](../contribution-plan.md) once ≤10 min — **IC voice, not March-talk roadmap**
3. After call: dump notes to `notes/2026-08-03_boris-call.md`

## Next session

Rehearse Monday pitch + fill collaboration TODOs.

```
@Files Amazon_SCOT/notes/2026-08-01_scot-scaffold.md Amazon_SCOT/contribution-plan.md Amazon_SCOT/mengfei-notes.md Amazon_SCOT/questions-for-boris.md Amazon_SCOT/collaboration.md
```

Help me rehearse the Boris call: paper/workshop 60s, Mengfei bridge, thesis #1, and closing ask. Fill any remaining TODOs in collaboration.md if I paste titles.

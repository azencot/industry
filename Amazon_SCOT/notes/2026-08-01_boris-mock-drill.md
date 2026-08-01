# Debrief — 2026-08-01 — Boris mock grill (Wedge A)

## Session

- Type: post-mock (Boris role-play)
- Duration: ~afternoon drill after Part 4 rehearsal + ZSF skim
- Prior context: SCOT track scaffold; contribution-plan Wedge A default; conditioning crib

## Conclusions

- **Wedge A is the right default** — upgrade synthetics feeding ZSF/FM, don’t reinvent foundation models.
- First answers were too abstract (“flexibility of generative modeling”). Boris wants **failure modes + first experiment + kill line**.
- **Never use precision/recall/F1** for this pitch — forecasting metrics: **CRPS** (distribution), **NMAE** (point), quantile loss.
- Protocol that landed: freeze backbone/budget/eval; swap only synthetic corpus (SarSim0 vs gen synthetics). Combo/staged = experiment 2.
- Kill line that landed: match/beat SarSim0 on cold-start/rare-regime slice within noise → short debug once → else kill A. Don’t say “no kill for PoC.”
- Train-time: quality first then speed is OK, but charter needs a **generation/pretrain cost** bound, not “efficient sampling later.” Prefer “efficient sampling / one-step,” not “Koopman.”
- If A dies: **ask Boris** B vs C — don’t assume C.
- Loop question: **never** “judged incorrectly.” Fair feedback → two IC bullets (KGO FM + efficient sampling; optional dual-tower).
- Close ask: intro to **Forecasting Science manager**; one-liner = generative modeling for forecasting; wants to strengthen sim→FM with modern generative synthetics (not vague “bridge foundation modeling”).

## What went well

- Recovered after metric mistake; locked CRPS/NMAE language
- IC ownership answer on KGO + dual-tower was strong
- Protocol “change only synthetic corpus” was clean
- Clear ask for Forecasting Science manager intro

## What broke / corrections

| Issue | Fix for Monday |
|-------|----------------|
| Abstract gen-vs-sim | Cold-start + rare regimes; then experiment one-pager |
| F1/precision/recall | CRPS / NMAE / quantile loss |
| Soft kill / “PoC no kill” | Match/beat within noise; one debug; kill A |
| Drop COVID | Keep rare regimes; reweight if needed |
| “Koopman for fast” | Efficient / one-step sampling |
| C over B if A dies | Ask him |
| “Loop judged me wrong” | Fair + IC evidence only |
| Intro wording | Strengthen sim→FM with gen synthetics |

## Decisions / artifacts updated

- [x] This debrief → `Amazon_SCOT/notes/`
- [x] Promote experiment one-pager + intro ask + loop anti-pattern into [`contribution-plan.md`](../contribution-plan.md)
- [x] `Amazon_SCOT/INDEX.md` + `notes/README.md`

## Open questions

- Exact cold-start / rare-regime slice definition once data access is real (Boris decides)
- Whether Forecasting Science manager is Mengfei’s chain or another HM

## Next session (one prompt)

After Monday’s real call: dump notes; update next step / intros.

```
@Files Amazon_SCOT/notes/2026-08-01_boris-mock-drill.md Amazon_SCOT/contribution-plan.md Amazon_SCOT/questions-for-boris.md
```

One more interrupt rehearsal: “Why not just scale SarSim0?” using the experiment one-pager in contribution-plan — then stop drilling.

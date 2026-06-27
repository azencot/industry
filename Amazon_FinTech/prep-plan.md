# Amazon FinTech PS1 — prep plan

**PS1: Tue 30 Jun 2026** · [`INDEX.md`](INDEX.md) · **Story bank:** [`stories/README.md`](stories/README.md)

**Pivot (23 Jun — Imry Kissos):** Karan wants **technical depth on your project**, not managerial LP framing. Prioritize **VLM drill + coding**; skip generic system design and broad ML topics. See [Karan notes in `INDEX.md`](INDEX.md#interviewer--karan-aggarwal).

**Remaining window:** 6 prep days (24–29 Jun). Day 3 (23 Jun) planning + late **Chronos bridge** — carry intro/LP items into 24 Jun.

---

## Completed (Days 1–2 + late 23 Jun)

- [x] Elevator pitch + 3 VLM anchors → [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md)
- [x] Generic ML depth (RAG/FT/eval/low-label) → [debrief](debrief/2026-06-21_day2-ml-depth.md) — **no retake unless bridging from VLM**
- [x] Karan continual pre-training blog skim → [`debrief/2026-06-21_continual-pretraining-blog.md`](debrief/2026-06-21_continual-pretraining-blog.md)
- [x] Intro scripts drafted (TMAY, Why Amazon)
- [x] 4 LP stories drafted (VLM-tied) — **reframe for IC/technical voice, not more drafts**
- [x] **Chronos bridge** (~30 min, 23 Jun late): **v1** (quantize → 1 token/step → AR, 20 sample paths × 64 horizon) → **Bolt** (patch-16 → direct quantile forecast) → **Chronos-2** (covariates). Contrast dual ViT/DINO vs value-space patching; Stage A/B/C (align → MCQ reason → GRPO on CoT) vs Chronos data scale + tiered eval. **Hybrid:** route forecast (Chronos-class) vs explain/QA (VLM); fine-tune Chronos for reasoning = no NL head + task gap; full numeric forecast from VLM out of scope.

---

## Time budget (24–29 Jun)

| Focus | Share | Deliverable |
|-------|-------|-------------|
| VLM project deep-dive (spoken) | ~50% | Grill-ready on A/B/C + Chronos contrast |
| Live coding (narrated) | ~30% | 4 mediums logged |
| LP reframe (2 stories) | ~10% | Ownership + Dive Deep (or Deliver Results) |
| Mock + polish | ~10% | One Karan-format mock; 2 questions |

---

## Wed 24 Jun — VLM drill #1 + intro + 1 code

**VLM (primary)**

- [x] Read aloud [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md) + [`vlm_multimodal_project.md`](../.cursor/skills/debrief/vlm_multimodal_project.md) (architecture section) — via interactive drill
- [x] Spoken drill — **Anchor A** (~15 min): dual encodings, Stage A/B curriculum, training stack, key metrics (stock **0.618/0.402** → **0.905/0.452**); **fold in self-Q&A** (~5 min at end): visual not tokens? Stage A decoupled? what broke? → [`debrief/2026-06-24_anchor-a-spoken-drill.md`](debrief/2026-06-24_anchor-a-spoken-drill.md)
- [x] **Chronos bridge** — done 23 Jun; Imry note = **Bolt** patching (not v1 per-step bins). One-liner: *same problem (efficient TS → model), different bet (forecast quantiles vs VLM reasoning)* → [`INDEX.md` Chronos note](INDEX.md#chronos-team-stack-imry)

**Intro (light)**

- [x] TMAY + elevator pitch once — **IC paragraph only**; trim PI/managerial framing → [`tell-me-about-yourself.md`](stories/tell-me-about-yourself.md)

**Coding**

- [x] 1× `/timed-code` medium — 567 permutation / sliding window (~50 min with debug) → [`debrief/2026-06-24_timed-code-567.md`](debrief/2026-06-24_timed-code-567.md) · root [`INDEX.md`](../INDEX.md)

---

## Thu 25 Jun — VLM drill #2 + LP reframe + 1 code

**VLM**

- [x] Spoken drill — **Anchor B** (~10 min): tiered eval, parse-miss vs accuracy, TR synthetic **kill** (26.9→21.9) → [`debrief/2026-06-25_anchor-bc-lp-debrief.md`](debrief/2026-06-25_anchor-bc-lp-debrief.md)
- [x] Spoken drill — **Anchor C** (~10 min): task coverage audit, missing ops, honest TSRBench/TR gaps
- [x] **Qwen (HF) + PEFT/LoRA** — repo walkthrough: `AutoModelForImageTextToText` + processor, dual visual patch, hybrid Q35 LoRA targets (sparse attention / dense MLP), Stage A→B adapter chain at eval → [`debrief/2026-06-25_qwen-peft-technical.md`](debrief/2026-06-25_qwen-peft-technical.md)
- [ ] Anticipate Karan follow-ups: ablations, config sweeps, what you'd do with proprietary finance TS *(skim if time)*

**LP reframe (technical, not “story”)**

Format: *metric anomaly → what I dug into → code/config change → result*

- [x] Read aloud + reframe → [`ownership_killed-tr-synthetic.md`](stories/ownership_killed-tr-synthetic.md) (~78%; retake optional with exact pp numbers)
- [x] Dive Deep — **covered via Anchor C** (60s handoff only; no separate drill)
- [ ] Backup if asked: [`deliver-results_dual-tower-curriculum.md`](stories/deliver-results_dual-tower-curriculum.md) (verify leaderboard rank)
- [x] **Variety story (non-VLM):** drafted **Learn & Be Curious** (diffusion → 7 papers; ImagenTime/Few) → [`learn-be-curious_diffusion-mastery.md`](stories/learn-be-curious_diffusion-mastery.md) — DOC + ~8 min script; **unrehearsed** (verify 7 papers, add 1 SDE decision, trim managerial voice)
- [x] **Customer Obsession — decided NOT to draft** (repo-usability = open-source hygiene w/o adoption metrics; CO rare in technical screens). **Stop** drafting CO / Earn Trust / etc. unless mock surfaces a gap

**Coding**

- [x] 1× `/timed-code` medium — patterns: hash, sliding window, BFS/DFS → `2026-06-25_200_number_of_islands_practice.py`

---

## Fri 26 Jun — Coding sprint #1

- [x] 3× timed mediums, narrated — `347` heap ~15 min pass; `56` intervals ~19 min pass; `153` binary search ~16 min pass *(all under 25 min)*
- [ ] Patterns: ~~heap~~, ~~intervals~~, trie, ~~binary search~~
- [x] Log results in root [`INDEX.md`](../INDEX.md)
- [ ] Optional 5 min — Karan follow-up drill from [`Qwen/PEFT debrief`](debrief/2026-06-25_qwen-peft-technical.md): ablations, config sweeps, proprietary finance TS
- [x] 10 min — skimmed Karan's [*Efficient Continual Pre-training for Building Domain Specific LLMs*](https://arxiv.org/abs/2311.08545) (FinPythia). **Read:** results modest — mostly vs Pythia base (+10% on 6.9B, +2% on 1B); efficient data selection (ETS/ETA-DACP) matches DACP at ~10% corpus; appears to lose to BloombergGPT. **Unread:** appendix (likely BloombergGPT comparison detail). **Connection point:** same logic as my TR-synthetic kill — domain adaptation only ships if task eval gains hold *without* general-capability regression (paper checks ARC/MMLU/etc.).
- [x] **JD technical mini-mock:** agents (~80%); A/B testing + null hypothesis (~60%→~85% on re-answer). A/B was weak spot — fixed: business metric primary, precision=guardrail, case-level randomize, no peeking, kill on safety. Q3 (agent money-moving failure) **unanswered → next** → [`mocks/2026-06-26_jd-technical-mock.md`](mocks/2026-06-26_jd-technical-mock.md) · [`debrief`](debrief/2026-06-26_coding-and-jd-technical.md)
- [x] **Mock LP — Learn & Be Curious (diffusion, non-VLM):** first rehearsal ~85–90%. Surfaced single-step distillation (NeurIPS'25) as the strong SDE-depth proof → added to story. Fixes: "I owned" not "my group", name a built artifact, drop filler openers, lock distillation numbers → [`mocks/2026-06-26_mock-lp-learn-curious.md`](mocks/2026-06-26_mock-lp-learn-curious.md) · [`debrief`](debrief/2026-06-26_mock-lp-learn-curious.md)
- [x] **JD drill — LLM system choices** (evening, ~70→85%): RAG vs FT vs CPT vs routing + human corrections. Fixed inversions (RAG=default for limited labels not CPT; FT shapes behavior not domain knowledge); corrections → regression tests/taxonomy first, RLHF later. **Recurring:** research-first instinct → must lead with eval/data/guardrails → [`mocks/2026-06-26_jd-llm-system-choices.md`](mocks/2026-06-26_jd-llm-system-choices.md) · [`debrief`](debrief/2026-06-26_llm-system-choices-drill.md)

**Skipped:** system design lite, FinTech scenario templates (Day 5 old plan)

---

## Sat 27 Jun — Karan mock + debrief

- [x] **60-min mock:** TMAY (3 min) → **20 min VLM grill** (he picks anchor) → **1 JD technical probe** — **document intelligence + production eval** (invoice/remittance/contract/ERP → extract/ground/reconcile/escalate; post-ship monitoring, slice regression, kill switches) → **1 LP** (technical) → **1 code** → 2 questions — VLM (arch/why-not-Chronos) strong; JD probe ~70% (precision = guardrail vs primary; deterministic schema validation not LLM-judge); failure-debug Q closed (contain first → 4-layer taxonomy → regression test); Ownership/TR-kill LP strong ("evidence invalidated the hypothesis"); **code:** `19_remove_nth_node` ~18 min pass (2 fix iterations)
- [x] `/debrief` → [`debrief/2026-06-27_karan-full-mock.md`](debrief/2026-06-27_karan-full-mock.md) + [`mocks/2026-06-27_full-mock.md`](mocks/2026-06-27_full-mock.md) + [`ps1-questions-for-karan.md`](ps1-questions-for-karan.md)
- [x] **Bonus drill:** `207_course_schedule` topological sort (Kahn) ~26 min pass (1 fix iteration) — covers ~~graph/topo~~; call it Kahn not DFS
- [x] **Learning block (~40 min):** finance production eval & monitoring teach-and-quiz — fixes the ~70% JD probe gap → [`debrief/2026-06-27_eval-monitoring-lesson.md`](debrief/2026-06-27_eval-monitoring-lesson.md). Crib: gate by slice not headline · business metric ≠ guardrail · schema = deterministic · real citation ≠ supporting citation · shadow mode is diagnostic (withhold automation, don't kill shadow) · corrections → taxonomy → regression tests → component fix → selective FT
- [x] **Bonus drill:** `211_design_add_and_search_words` trie wildcard ~17 min pass (2 fix iterations: `True`/`False`, `word[i+1:]`) — covers ~~trie~~
- [x] **Agent failure retake (spoken):** money-moving auto-approval ~80–85% — contain → 4-layer taxonomy (extraction · reconciliation · policy · guardrail) → deterministic fix + regression slice → selective FT last
- [x] **Learning block (~15 min):** agentic workflows teach-and-quiz (paused at Q2) → [`debrief/2026-06-27_agentic-workflows-lesson.md`](debrief/2026-06-27_agentic-workflows-lesson.md). Crib: agent = plan→tools→state→verify→(maybe)act · reason broadly, act narrowly · narrow typed tools not `approve_payment()` · constrain ReAct in finance · **resume at Q2 (tool design + action boundaries)**
- [ ] Note: rigid interviewer — state approach → complexity → invariants; prefer standard structure

---

## Sun 28 Jun — Coding sprint #2

- [ ] 2× timed mediums (25 min each), narrated
- [ ] Re-do any problem that failed or took >25 min — ~~211 trie wildcard~~ (done Sat 27); hash / sliding window / two pointers if time
- [ ] **JD technical refresh** (30–40 min) from [`job-description.md`](job-description.md):
  - LLM system choices (RAG vs FT/CPT vs routing); parallelism/scaling (data/model/pipeline + inference batching)
  - Eval gates for finance precision; **production monitoring** (dashboards, slice alerts, drift/regression after ship)
  - **User-corrections loop retake** (~10 min): corrections → failure taxonomy → regression tests → component fix → selective training signal
  - **Calibration / abstention / thresholds** (~10 min): confidence routing, human handoff, unsupported-action rate
  - **Retrieval quality** (~10 min): chunking, metadata, reranking, citation precision vs answer precision
- [ ] Light pandas/numpy refresh **only if** coding reps + JD refresh are solid (Imry: rarely tested)

---

## Mon 29 Jun — Polish (no new material)

- [ ] Re-read [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md) — 90s per anchor from memory
- [ ] Review **JD technical crib** (no new papers) — memorize lines from [`job-description.md`](job-description.md):
  - *RAG grounds facts; FT shapes behavior; CPT teaches domain language; routing manages cost-risk*
  - *Corrections → regression tests + failure taxonomy first; only some become training signal*
  - *Thresholds + abstention decide automation; precision = compliance gate*
  - *Document intel: invoice + remittance + contract + ERP → extract, ground, reconcile, escalate*
- [ ] Re-run weakest LP story once (IC voice, timer)
- [ ] Prepare **2 questions** for Karan → [`ps1-questions-for-karan.md`](ps1-questions-for-karan.md) (rehearse once aloud)
- [ ] Why Amazon skim only if intro feels rusty
- [ ] AV test: https://amazon.zoom.us/test

---

## Interview day (30 Jun)

- [ ] Zoom at 21:00 sharp; [Live Code](https://livecode.amazon.jobs/joinsession/e4618c8d-2a90-4c8f-8fb1-b6e875c77bd7) ready
- [ ] Headset; quiet room; phone on backup
- [ ] `/debrief` same night while fresh

---

## Daily default (if short on time)

1. One VLM anchor spoken drill (pick A, B, or C)
2. One `/timed-code` problem
3. Update index or mock log (5 min)

**Deprioritized (do not spend time here):** generic `/ml-deep-dive` retakes, 8-story LP bank, system design scenarios, full Karan paper, ECG-QALM deep read, generic transformers/RLHF theory, Spark/Hadoop internals.

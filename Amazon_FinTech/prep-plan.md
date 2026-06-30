# Amazon FinTech PS1 — prep plan

**PS1: Tue 30 Jun 2026** · [`INDEX.md`](INDEX.md) · **Story bank:** [`stories/README.md`](stories/README.md)

**Pivot (23 Jun — Imry Kissos):** Karan wants **technical depth on your project**, not managerial LP framing. Prioritize **VLM drill + coding**; skip generic system design and broad ML topics. See [Karan notes in `INDEX.md`](INDEX.md#interviewer--karan-aggarwal).

**Recruiter update (29 Jun):** Phone screen is **1 hour on Zoom**: **Science Depth 20 min** + **Coding 20 min** on **Livecode** (no run/compile, no libraries) + **Ownership LP 20 min**. Prepare for a deep end-to-end ML walkthrough, LeetCode-medium algorithmic narration, and one strong Ownership story (gates set before training, kill recommendation when evidence invalidated the hypothesis).

**Science-depth choice:** Lead with **multimodal / VLM time-series reasoning**, not diffusion, for this screen. Diffusion is your deeper theoretical comfort zone, but VLM is the stronger *role-aligned* story: end-to-end model development, multimodal inputs, Qwen integration, LoRA curriculum, eval gates, SLM routing, and finance transfer. Keep diffusion as a reserve if asked for mathematical depth: *"My deepest theory background is diffusion/SDE generative modeling; the end-to-end system most relevant to FinTech is the VLM stack, so I’ll walk through that."*

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
- [x] **Learning block (~25 min total):** agentic workflows teach-and-quiz → [`debrief/2026-06-27_agentic-workflows-lesson.md`](debrief/2026-06-27_agentic-workflows-lesson.md). **Stopped generic track as too high-level for Karan.** Keep crib: reason broadly, act narrowly; typed tools; constrain ReAct. If resumed, make it a low-level engineering-spec drill: tool schemas, verifier checks, logs, action boundaries, and one failure trace.
- [x] **Bonus drill:** `3_longest_substring_without_repeating` sliding window ~15 min pass (2 fix iterations: `last_index[c] >= si`, measure `i-si+1` not `len(s)-si`) — covers ~~sliding window~~
- [ ] Note: rigid interviewer — state approach → complexity → invariants; prefer standard structure

---

## Sun 28 Jun — Coding sprint #2

- [x] **LLM / agentic trends drill** (~40 min, continued from Sat 27): MCP, ReAct, FlashAttention, linear attention, FSDP/DDP, LoRA/RAG/synthetic, serving stack (vLLM → cache → routing → quant), agent observability — low-level decision framing for Karan → [`debrief/2026-06-28_llm-agentic-trends-drill.md`](debrief/2026-06-28_llm-agentic-trends-drill.md) · [`mocks/2026-06-28_ml-deep-dive-agentic-trends.md`](mocks/2026-06-28_ml-deep-dive-agentic-trends.md)
- [x] 2× timed mediums — `2026-06-28_15_3sum_practice.py` (two pointers, ~29 min, pass after 2 fix iterations); `2026-06-28_560_subarray_sum_equals_k_practice.py` (prefix sum + hash, ~18 min, clean pass)
- [x] Bonus drill — `2026-06-28_875_koko_eating_bananas_practice.py` (binary search on answer, ~23 min, pass after fix: bounds `max(piles)`, feasibility `<= h`); `2026-06-28_98_validate_binary_search_tree_practice.py` (tree / BST bounds DFS, pass; paused ~16 min, finished later)
- [ ] Re-do any problem that failed or took >25 min — ~~hash~~ / sliding window / ~~two pointers~~ / ~~binary search~~ / ~~tree~~ if time; **paused:** `2026-06-28_57_insert_interval_practice.py` (three-phase scan); **revisit:** `2026-06-28_322_coin_change_practice.py` (DP — add memo / bottom-up)
- [x] **JD technical refresh** (30–40 min) from [`job-description.md`](job-description.md): 5-block cash-application drill — LLM choices/scaling, eval gates + monitoring, corrections loop, calibration/abstention, retrieval quality. **Locked lines:** *RAG updates facts/rules; FT/LoRA shapes behavior; CPT teaches domain language; routing manages cost-risk.* *Corrections → taxonomy + regression tests first; only some become training signal.* *Deterministic checks first, calibrated thresholds second, automation only on safe slices.* **Watch-outs:** don't say CPT first for changing customer rules; don't use raw p80/p95 confidence without calibration; don't fine-tune generator to fix retrieval.
- [x] Light pandas/numpy refresh **only if** coding reps + JD refresh are solid (Imry: rarely tested): practiced finance-table mismatch query. **Locked pandas pattern:** merge tables by key → vectorized diff/feature column → boolean filter → `groupby(...).sum()` → `sort_values()`. Avoid row loops / `zip` for dataframe work.

---

## Mon 29 Jun — Polish (no new material)

- [ ] Re-read [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md) — 90s per anchor from memory; skim [`vlm-technical-cheat-sheet.md`](vlm-technical-cheat-sheet.md) pull-thread table only (numbers + ablations, no new material)
- [ ] **Answer Q6 FinTech bridge aloud** (carried from 2026-06-28 VLM grill → [`debrief/2026-06-28_vlm-grill.md`](debrief/2026-06-28_vlm-grill.md)): strongest *technical* bridge, not generic motivation — multimodal docs (one view loses info) → dual encoding; Stage A→B = domain align → task FT on invoices/remittance; tiered eval + parse-miss = schema reliability before accuracy; 0.8B≈8B TSExam = SLM routing
- [ ] Review **JD technical crib** (no new papers) — memorize lines from [`job-description.md`](job-description.md):
  - *RAG grounds facts; FT shapes behavior; CPT teaches domain language; routing manages cost-risk*
  - *Corrections → regression tests + failure taxonomy first; only some become training signal*
  - *Thresholds + abstention decide automation; precision = compliance gate*
  - *Document intel: invoice + remittance + contract + ERP → extract, ground, reconcile, escalate*
- [ ] Re-run **Ownership** story once (IC voice, timer) → [`ownership_killed-tr-synthetic.md`](stories/ownership_killed-tr-synthetic.md)
- [ ] Prepare **2 questions** for Karan → [`ps1-questions-for-karan.md`](ps1-questions-for-karan.md) (rehearse once aloud)
- [ ] Why Amazon skim only if intro feels rusty
- [ ] AV test: https://amazon.zoom.us/test

---

## Interview day (30 Jun)

**Goal:** Use ~5 hours to sharpen exactly what the recruiter said will be gated. No broad new material.

### 5-hour final sprint

| Time | Focus | Deliverable |
|------|-------|-------------|
| 0:00–0:15 | Setup + rubric | Rewrite the whiteboard header from memory: Science 20 / Coding 20 / Ownership 20. Open [`anchor-cheat-sheet.md`](anchor-cheat-sheet.md), [`vlm-technical-cheat-sheet.md`](vlm-technical-cheat-sheet.md), [`ownership_killed-tr-synthetic.md`](stories/ownership_killed-tr-synthetic.md), Livecode link. |
| 0:15–1:45 | **Science Depth: VLM mind map** | One spoken end-to-end walkthrough: ideation → data → architecture → training → eval gates → deployment/serving analogy → lessons. Must include exact numbers: **0.618/0.402 → 0.905/0.452**, dual chart+delay, Stage A/B, parse-miss, TR kill, 0.8B routing. |
| 1:45–2:00 | Break | No screens; reset voice. |
| 2:00–3:20 | **Coding: Livecode simulation** | 2 mediums by hand, no execution. Narrate restate → approach → complexity → invariants → edge cases → dry run. Prioritize one DP or graph redo plus one array/hash/window redo. Use plain Python only; no imports unless absolutely standard. |
| 3:20–3:35 | Break | Walk, water, no new content. |
| 3:35–4:30 | **Ownership LP** | Rehearse [`ownership_killed-tr-synthetic.md`](stories/ownership_killed-tr-synthetic.md) once at 8 min, then one 90s version. Lead with **I set the gates / I owned the kill call / I changed the lab process**. Do not drift into team-management framing. |
| 4:30–5:00 | Integration mock | 20 min science + 10 min code approach-only + 10 min Ownership opener + final logistics. Stop if answers get worse; confidence > cramming. |

### Science Depth — answer map

- [x] **Opener (30s):** "I’ll use my multimodal time-series VLM project because it covers the full ML lifecycle: problem framing, data, architecture, training, eval, and deployment-style routing. My deeper theory background is diffusion, but this is the best end-to-end system for the FinTech role."
- [x] **Ideation:** raw numeric tokens and single-view plots underperform; finance analogy = one view of a payment/doc loses information.
- [x] **Data:** TSExam, ChatTS, CaTS, TSRBench; synthetic labels known by construction but distribution can still be wrong.
- [x] **Architecture:** Qwen3-VL chart stream + DINOv3 delay stream; reused visual-token pathway; LoRA adapters; no "hijacked video stream" wording.
- [x] **Training:** Stage A vision alignment with LLM frozen; Stage B LM LoRA for QA/MCQ; explain why not end-to-end from day one.
- [x] **Eval:** loss → TSExam → TSRBench slice → full TSRBench; parse-miss separate from accuracy; gates **−3 pp overall / −5 pp task**.
- [x] **Results:** stock Qwen3-VL-8B **0.618 / 0.402** → stack **0.905 / 0.452**; 0.8B near 8B on TSExam supports SLM routing.
- [x] **Hard question ready:** "Why VLM rather than Chronos?" Forecasting model for values vs VLM for multimodal reasoning/explanations; route by task.

**Science drill done (30 Jun AM, ~75 min):** full 3-min walkthrough strong; probes on delay embeddings, DINO-stream integration, Stage A necessity, eval reliability, synthetic risk, numerical reasoning, routing, production-failure debugging. **Recurring fixes to hold in interview:**

- Add **one FinTech bridge sentence** at the end of the science walkthrough (multimodal docs / one view loses info / SLM routing for cost). Don't leave the lesson research-only.
- Self-bound the headline: **best among open/non-proprietary**; trillion-scale frontier + hard TR slice still ahead.
- Commit to **one** TSRBench task-count number; say it confidently. Say "**Qwen3-VL-8B**, ported to **0.8B Qwen3.5**" decisively (no "or").
- Synthetic risk = lead with **distribution shift even when labels are correct**; anchor with TR kill **26.9→21.9**.
- Numerical reasoning = valid for **visually recoverable** quantities (trend, ranges, ordering, comparisons); **breaks** on exact high-precision values, very long/dense series, poor axis rendering → numeric tools / specialist model / abstain.
- Partial TSRBench = **screening gate**, not winner declaration; full TSRBench + slice gates for promotion. Avoid "promote a model I believe in" phrasing.
- Ablation fairness = matched backbone/data/compute/seed **plus token-budget control** (not "more visual tokens wins"); complementarity repeats across chart-only / delay-only / dual.
- FinTech monitoring = don't assume input correct; **precision = compliance gate**; automation/intervention rate optimized **subject to** safety guardrails; corrections → taxonomy + regression tests first.

### Coding — Livecode rules

- [ ] Say constraints and edge cases before coding; if ambiguous, state a conservative assumption.
- [ ] Write production-clean code without relying on execution: descriptive names, small helper only if it clarifies, no clever one-liners.
- [ ] After code, dry-run one normal case and one edge case manually.
- [ ] Always state runtime and space complexity.
- [ ] Revisit one of: `57_insert_interval` or `322_coin_change` because they were paused/unfinished; then redo a clean pattern from hash/window/two-pointers.

**Coding drill done (30 Jun AM, ~40 min):** 3 mediums, all right approach, each with one end-of-solution slip → all fixed.

| Problem | Pattern | Result | Slip |
|---------|---------|--------|------|
| `2026-06-30_322_coin_change_practice.py` | DP (top-down memo) | near-pass | `return rem[mem]` → `return min_coins` |
| `2026-06-30_3_longest_substring_without_repeating_practice.py` | hash + sliding window | fail → fixed | stale hash update; need `last_seen[c] >= si` guard + `i - si + 1` |
| `2026-06-30_57_insert_interval_practice.py` | intervals 3-phase scan | fail → fixed | `interval` → `intervals[i]` in phase 3 |

**Interview habit to hold:** dry-run the **last 5 lines** before declaring done — every miss today was a tail typo/invariant slip, not a wrong plan. State invariant + O() aloud before coding.

### Ownership — primary story

- [ ] Use [`ownership_killed-tr-synthetic.md`](stories/ownership_killed-tr-synthetic.md) as the primary Ownership answer — already strong in Karan mock ("evidence invalidated the hypothesis").
- [ ] 20-min structure: 7–8 min DOC story, then probes on why kill if average went up, pressure after 8B GPU spend, your role vs student, what you changed in the lab process.
- [ ] Memorize kill line: **TR 26.9 → 21.9 (−5.0 pp)** — gate fired; reasoning avg **+1.8 pp** and AR/IR **~+7 pp** = **still kill**.
- [ ] Ownership proof: pre-declared gates **−3 pp overall / −5 pp per task**; per-task promotion table; kill recommendation in lab review; updated eval template.
- [ ] If pressured on "why you": you owned promotion criteria when the lab had none; you ran 0.8B validation; you remained accountable for the 8B readout and promote/kill call.
- [ ] Backup if they want a second angle: eval adapter-chain bug (**0.469 → 0.601** misleading jump) — you owned debugging and fixed train-time adapter-chain reconstruction at eval.

**Ownership drill done (30 Jun, ~30 min):** full story + 5 probes (why kill if avg up, pressure after 8B spend, your role vs student, gates too conservative, what next). Reframed opener to lead with **"main developer, but the ownership moment was promotion criteria."** Story file updated: stronger 90s version + follow-up answers. **Hold these phrasings:** "killed that **data path**" (not "deleted patterns"); gains "might have been **distribution shift**"; student ran 8B to verify it wasn't a small-model artifact, **accepting compute cost** because verification mattered; gates **block promotion, not learning**; "I would **not start by generating more data** → audit first." Use "I hypothesized/decided/set," not "I felt."

### Logistics

- [ ] Zoom at 21:00 sharp; [Live Code](https://livecode.amazon.jobs/joinsession/e4618c8d-2a90-4c8f-8fb1-b6e875c77bd7) ready.
- [ ] Headset; quiet room; phone on backup.
- [ ] AV test: https://amazon.zoom.us/test
- [ ] `/debrief` same night while fresh.

**Integration mock done (30 Jun PM, ~30 min):** science opener + binary-search approach + Ownership opener, all ~85–90%. **5-hour sprint complete** (setup · science · coding · ownership · integration).

### Interview-day crib (read right before)

- **Science:** TSRBench = multi-task (perception/reasoning/prediction/decision), don't commit to a task count. Chronos = forecasting, not NL reasoning (not "raw tokens"). Eval = TSExam fast gate → partial TSRBench screening → full TSRBench north star. Numbers **0.618/0.402 → 0.905/0.452**. **End with one FinTech bridge sentence** (one view loses info · precision + slice gates · routed SLMs only when eval holds). Self-bound: best among **open/non-proprietary**.
- **Coding:** state invariant + O() before coding; `while left <= right` for exact binary search; `mid = left + (right-left)//2`; **dry-run the last 5 lines** before saying done (every miss today was a tail slip).
- **Ownership:** lead with the **ownership moment** (promotion criteria), not benchmark context. Gates **−3 pp overall / −5 pp per task** set **before** training. **TR 26.9 → 21.9 (−5.0)** = kill despite avg **+1.8** and AR/IR **~+7**. Say "killed that **data path**," "**distribution shift**," gates "block **promotion, not learning**," "I would **not start by generating more data**." Use "I hypothesized/decided/set," not "I felt."

---

## Daily default (if short on time)

1. One VLM anchor spoken drill (pick A, B, or C)
2. One `/timed-code` problem
3. Update index or mock log (5 min)

**Deprioritized (do not spend time here):** generic `/ml-deep-dive` retakes, 8-story LP bank, system design scenarios, full Karan paper, ECG-QALM deep read, generic transformers/RLHF theory, Spark/Hadoop internals.

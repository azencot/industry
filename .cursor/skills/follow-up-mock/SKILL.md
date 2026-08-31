---
name: follow-up-mock
description: >-
  Run a 15-minute hard follow-up mock that starts mid-conversation: skip
  project recap and basic encoder/architecture questions; press on numbers,
  clocks, bottlenecks, diagnosis, and tradeoffs. Use when the user invokes
  /follow-up-mock, asks for a 15-min hard mock, or wants a deeper round for
  Yujie, Chung-Cheng, Haraldur, Jonathan, Vincent, or another on-site
  interviewer after basics are already locked.
---

# Follow-up mock (15 min, hard)

Depth round after the opening is already done. Not a first-pass mock. Not `/ml-deep-dive` (3-min lecture). Not `/mock-lp`.

## When to use

User names an interviewer (or “15 min hard mock”). Default panel: Apple Health AIML on-site sheets under [`GenAI/interviews/apple-health-aiml/`](../../GenAI/interviews/apple-health-aiml/). Hub: [`2026-08-27_onsite-prep.md`](../../GenAI/interviews/apple-health-aiml/2026-08-27_onsite-prep.md).

Works for any person sheet that has spoken misses / later-module questions. Reuse for Chung-Cheng, Haraldur, Jonathan, Vincent without rewriting this skill.

## Load first

1. Hub + that person’s sheet (`2026-08-27_onsite-{slug}.md`).
2. Sheet’s **spoken first-takes / misses / locks** and **Traps**.
3. Profile only if IC evidence is needed: [`.cursor/skills/debrief/omri_azencot_experience.md`](../debrief/omri_azencot_experience.md).

Do not re-teach the sheet. The mock is the product.

## Already covered — do not ask

Treat the first ~15 min as done. **Never** open with:

- “Tell me about your multimodal / VLM project”
- “How would you encode a time series?” (menu of patch / STFT / chart)
- “Concat vs cross-attention?” as a definition
- “What is gradient checkpointing / AdamW / attention?”
- LLaVA / Flamingo recap, vanilla attention derivation
- Paper recap or name-drop (WBM, RelCon, AXLearn, periodicity)

If the user starts reciting that material, interrupt: “We already have that. Stay on this design.”

### Per-person skip → start

| Person | Skip (already said) | Start here |
|--------|----------------------|------------|
| **Yujie** | MM project; TS encoding menu; concat vs xattn named; matplotlib-on-PPG | Module 3–4 + integrated cases: native clocks, token math, hard vs soft alignment, fusion rate, resampler M, neglect tests, bakeoff with one variable. Sheet Q9–Q30, not Q1–Q8. |
| **Chung-Cheng** | Owned-run recap; define checkpointing / Flash / AdamW | Constraint first (P/G/O/A vs comm vs I/O); 8→64; 45% util; sensor+LLM collapse as **infra** (tokens, T², input stall). |
| **Haraldur** | Sensor-FM lecture; “DL will win”; PPV primer | Missingness-as-shortcut; GBDT vs DL under shift; labels; whether you ship. Stay off Yujie’s encoder hour. |
| **Jonathan** | CV walk; pad as the hour | Research depth: hypothesis, control, kill criterion, negative result. Pad only if he pulls it. |
| **Vincent** | Why Apple; 90s story dump | 6-month program, discriminating experiment, judgment cards in [`2026-08-30_behavioral-stories.md`](../../GenAI/interviews/apple-health-aiml/2026-08-30_behavioral-stories.md). |

If the user already did a follow-up with this person in-session, start **one module later** than last time (do not repeat the same case).

## Workflow

1. **Setup (≤4 lines)** — interviewer name, 15 min, “we already covered X; staying on Y.” Then **in character**. No teaching.
2. **Clock** — “15 minutes. Answer as you would on the call.” Prefer spoken; typed is fine if practicing alone.
3. **One evolving problem** — not a quiz list. Open at the sheet’s **hard follow-up** (numbers, a contradiction, a failure). After each answer, change **one** constraint (rate mismatch, missing stream, neglect, budget, scale).
4. **Push, don’t lecture** — demand: token counts, timescales in seconds, what is preserved/lost, which experiment isolates the claim, what you would kill. Interrupt menus and “it depends” with no pick.
5. **Stop at 15** — after ~3–5 exchanges, or when the user says time. Then critique. Do not keep adding questions.
6. **Critique** against that sheet’s **Lock** lines and spoken misses. Score, then one lock rewrite for the worst miss. Do not invent a second mock in the same turn.
7. **Persist** — only if the user asks, or after they want `/debrief`. Apple on-site → `GenAI/interviews/apple-health-aiml/YYYY-MM-DD_follow-up-{person}.md` + row in [`GenAI/INDEX.md`](../../GenAI/INDEX.md).

## Question bar

A follow-up question is valid only if it requires **at least one** of:

- Arithmetic they can do aloud (samples/hour, N = T/P, cost ~ Tq·Tkv)
- A design fork with a stated pick (hard vs soft; what you drop first under a token tax)
- An experiment that would **falsify** their claim (shuffle / drop / time-shift; matched-N bakeoff)
- A failure mode from the sheet they already missed once

Invalid: anything answered by reciting Stage A/B, “I’d use a Transformer,” or naming concat and xattn.

## During the mock (interviewer voice)

- Short. One question. No bullet teaching.
- Stay in **that person’s track** (Yujie ≠ Haraldur PPV; Chung-Cheng ≠ health paper).
- IC: “I”, owned gate, owned kill. Cut PI/students/roadmap.
- Hard rules from the hub still apply (no name-drop, no matplotlib on PPG, etc.).

## Critique format

```markdown
## Follow-up mock — {Person} ({N} min)

### Already treated as covered
- …

### Exchanges
- Q: …
- You: {one-line gist}
- Miss / lock: …

### Score
- [ ] Numbers (samples, tokens, cost) without being prompted twice
- [ ] Native clocks / no illegal resample (or infra analog for Chung-Cheng)
- [ ] One explicit bottleneck (P, M, fusion rate, memory term)
- [ ] Falsification test, not architecture preference
- [ ] Stayed on this hour’s track

### Worst miss → spoken lock
{4–8 sentences they can reuse}

### Next
One follow-up topic for the next 15 min (do not run it now).
```

## Do not

- Restart from “tell me about the project” or the encoding menu
- Teach Module 1–2 during the 15 min
- Turn Yujie into Haraldur (ship / PPV) or Chung-Cheng into a library list
- Name-drop team papers
- Write a debrief file unless asked

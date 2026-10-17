# Siemens technical screen — Huzefa Rangwala — Fri 23 Oct 2026

**When:** Friday 23 October, **22:00–23:00 Thailand** (ICT). That is **08:00–09:00 Pacific**.
**Length:** 1 hour.
**Interviewer:** **Huzefa Rangwala**, Staff Scientist, Physical AI, Siemens. This books the technical screen. He is not confirmed as the hiring manager.
**Prep window:** Tuesday 20, Wednesday 21, Thursday 22. About 2.5–3 hours each. Friday is a 20-minute pre-call, not a fourth day.
**Prep split (revised 2026-10-17):** **~65–70% coding, ~30–35% resume / ML breadth.** The hour itself is still about half methodology and half one PyTorch question. Practice spends more time on coding, because the weakness is syntax under pressure, not algorithms.

Private note from **Danielle Robinson** (she worked with him at AWS). Do not quote it on the call. **Danielle Chandler** is the recruiter who owns the process. Two different people.

> He will probably target it around your resume, so explain anything on your resume in detail and go into the methodology. About half should be ML breadth, then the PyTorch coding question. She worked with him on time series and AI4Science. He also does a lot of PPO/GRPO.

Chandler’s earlier line still stands: STAR is in this screen. Here that means the resume half is told as a story with a decision, a test, and a result. The dedicated behavioral hour is the later virtual on-site.

---

## What this hour is

| Half | About | What “good” sounds like |
|------|--------|-------------------------|
| **~30 min ML breadth** | He picks lines on the resume and asks how the method works, what you ablated, and what failed | Shapes, loss, the control that could have killed your claim, one number, the limit of the claim |
| **~30 min PyTorch** | One live function, then a unit test | Shapes first, tensor ops, mask before softmax, asserts, run, fix the failure out loud |

He has shipped time-series foundation models, physical constraints, and reinforcement fine-tuning. He will recognize a hand-wavy method. He will also recognize a lecture about his own papers. Explain **your** method.

---

## Who he is (public)

Use this to anticipate the probe. Do not recite his biography back to him.

- Siemens since early 2026, Physical AI in Data & AI. Before that, Senior Manager of Applied Science at AWS (2022–2026), a ~70-person org on Bedrock and SageMaker post-training.
- His org shipped **Chronos-2** (he is a coauthor, not the lead author): a 120M encoder-only forecasting model. The piece that matters for you is **group attention** — at each time/patch, series inside a group share information (related series, variates, or target plus covariates), instead of concatenating covariates onto the time axis.
- **Reinforcement fine-tuning** on Bedrock, launched around re:Invent 2025. Amazon’s public docs train that product with **GRPO**: several samples per prompt, a reward function, group-relative advantages. His site also lists RL for GPU kernels. Robinson’s “PPO/GRPO” matches that, not a claim that he will ask you to derive PPO.
- **AI4Science** with Robinson: recent public work on when to trust a surrogate versus call the solver, and on enforcing constraints at inference time. A plausible breadth question. Not a paper to summarize.
- Before AWS: tenured CS faculty at George Mason (bioinformatics, data mining, fairness), NSF CAREER, many PhD students, a stint as department chair. “My students” will sound like a lab lead to him. Name the technical decision you made and the evidence that moved it.

---

## Resume half — what he is likely to ask

He will not run the full story-bank table. Have three stories hot. Source text stays in [`2026-10-15_behavioral-story-bank.md`](2026-10-15_behavioral-story-bank.md). The 16 Oct mock log is [`mocks.md`](mocks.md).

| Hot | Story | Why him |
|-----|--------|---------|
| **A** | ImagenTime | Direction and disagreement. He will ask why a representation, which candidates died, and what the number actually measures. |
| **B** | Dual-tower | Center of the resume. Matched Plot+Plot / Delay+Delay controls. Where delay collapses (ChatTS numerical). Where the dual view does not help (TSExam flat). |
| **C** | TR synthetic kill | Failure and a pre-committed gate. Use this if he asks what you stopped. |

Bosch (story E) only if he asks how a physical measurement changed the model. Leave D and F cold this week.

### Questions to be ready to answer out loud

1. Pick a resume line. Why that method, and what was the obvious alternative?
2. What did you measure before the expensive run, and what result would have killed the idea?
3. Which ablation shows the gain is not just more capacity or more data?
4. Where does the method fail, and what did you narrow the claim to?
5. Tell me about a result that looked good on the average and was still a no.
6. Walk the tensor path: what is the shape in, what is trained, what is frozen, what is the loss?
7. If GRPO or RL is on the resume: what was the reward, what was the group, why did the letter reward do nothing?

### Fixes already owed from the 16 Oct mock (story A)

- A Gramian angular field is a **dense** pairwise field. Off-diagonal is not zero. The sparse, weakly 2D image is the **line plot**.
- Delay embeddings and STFT stayed because the series could be reconstructed at high fidelity. Do not say “numerically exact.”
- One number in the retell: short-series discriminative score about **58%** over prior diffusion models, or the long-series classification figure about **133%**. One, not a list.
- The drop from about 1,000 model evaluations to about **35** is the **EDM sampler**, separate from the image transform.
- Say who owned the 1D stack and what evidence changed the decision. Drop “my students.”

### GRPO card — only if that line is on the resume, or he asks

He ships this. Two minutes, then stop.

- What I ran: SFT on gold temporal-relation traces, then GRPO (TRL). An earlier **letter-level** GRPO on an already-saturated SFT was a no-op.
- Why that no-op is the result to lead with: once the letter was already correct, a letter reward had nothing left to teach. The reward had to sit on the **trace**.
- What moved: 9B TSExam to **0.9316** after the trace stage. TSRBench barely moved. Say that limit.
- PPO in two sentences, only if he asks the difference: PPO usually learns a value function and clips the probability ratio. GRPO drops the value head and uses the advantage inside a group of samples for the same prompt (reward minus the group mean, often divided by the group std), with a similar clip and a KL to the reference.
- If you do not remember group size, KL coefficient, or the exact reward code, say so. Do not invent them in front of him.

### Breadth notes, if he asks

Wednesday's spoken block is the question list in the day plan below, not these notes. Use these only when that list is already fluent and he opens the topic.

**Time series.** A foundation model is the right first try when many related series share structure and the target history is short. A model trained on the task wins when the sampling is irregular, the covariate set is specific, or the decision needs a calibrated error you have measured. Multivariate structure does not have to be “concatenate channels in time.” Sharing across the series axis at each time index keeps a variable number of variates and covariates from blowing up the context. That is a method you can defend from your own representations work. You do not need his Chronos-2 talk track.

**Physical constraint.** A soft penalty can be small while a conservation law or a boundary is still violated. A hard constraint (architecture, projection, or a correction after the network) is the one that still holds on a new initial condition. The average error is the wrong gate for a surrogate: name the decision the surrogate feeds, and the slice where you still call the numerical solver. Bosch is the concrete story if he wants a sensor, not a PDE slogan.

**When the metric lies.** Story C. Gates written before the run. Kill the lever, keep the objective.

---

## Coding — harder axes and bugs, same APIs

The weakness is PyTorch syntax under pressure: mask semantics, transpose axes, reshape after permute, broadcasting, flattening for cross-entropy, `zero_grad`. Make the drills harder through tensor-axis ambiguity, masking, realistic bugs, unit tests, and live debugging.

The coding goal: implement ordinary ML tensor ops from a blank editor, narrate shapes, and fix mistakes. Mask convention in every file: **True = valid**. State it before you code.

| Problem | What | File |
|---------|------|------|
| Tue attention | `q,k` are `[B, H, T, Dh]`, optional key mask and causal mask. 20 min cap. Under 15 min clean: stop repeating vanilla attention. | [`coding/tue_attention.py`](coding/tue_attention.py) |
| **16** | Pad `[Ti, D]` → self-attend over time → masked mean → `[B, D]`. Fluency. 15–20 min. Under 15 min clean: stop repeating it. | [`coding/16_varlen_pool.py`](coding/16_varlen_pool.py) |
| **17** | `[B, G, T, D]`, attend across **G** at each time. Highest-value base problem. | [`coding/17_group_attention.py`](coding/17_group_attention.py) |
| **17b** | Cross-group: `q [B, Gq, T, D]`, `kv [B, Gk, T, D]`, `key_mask [B, Gk]`. Scores `[B, T, Gq, Gk]`. | [`coding/17b_cross_group.py`](coding/17b_cross_group.py) |
| **17c** | Same as 17b with heads. Internal `[B, T, H, G, Dh]`. Scores `[B, T, H, Gq, Gk]`. | [`coding/17c_group_multihead.py`](coding/17c_group_multihead.py) |
| **18** | Masked CE + one optimizer step. **Start from the broken file.** | [`coding/18_masked_train_step_broken.py`](coding/18_masked_train_step_broken.py) |
| Thu mock | `[B, G, T, D]` and `lengths [B, G]`: each series attends over **T**, then masked mean → `[B, G, D]`. Not a repeat of 16–18. | [`coding/19_thu_mock.py`](coding/19_thu_mock.py) — do not open before Thursday |

Tuesday micro-drills: [`coding/tue_broadcast.py`](coding/tue_broadcast.py), [`coding/tue_shapes.py`](coding/tue_shapes.py).

### Out of scope

Hard LeetCode, DP, trees, graphs, an MLP, a CNN, pairwise distance except as a tiny shape drill, a sliding-window `Dataset`, a PPO or GRPO implementation, distributed training APIs, obscure PyTorch functions.

### Failure modes to clear before Friday

- [ ] `k.transpose(-2, -1)`
- [ ] `softmax(dim=-1)`
- [ ] Mask convention said out loud: True = valid
- [ ] `[B, T]` → `[B, 1, 1, T]`
- [ ] Causal mask combined with a padding mask
- [ ] `[B, T, D]` ↔ `[B, H, T, Dh]`
- [ ] `reshape` after `permute`; `contiguous()` when `view` would throw
- [ ] CE: logits `[N, C]`, targets `[N]` long
- [ ] Pad labels ignored (`ignore_index`, or `reduction="none"` then mask)
- [ ] `zero_grad` before `backward`
- [ ] `model.train` vs `model.eval`
- [ ] `no_grad` vs `eval` (`eval` does not turn gradients off)
- [ ] Masked-mean denominator

---

## Three days

No solution file until the asserts pass. Spoken blocks are short answers to the questions, not rehearsed speeches.

### Tuesday 20 — attention fluency + problem 16 (~2.5–3 h)

| | |
|--|--|
| 20 min cap | [`tue_attention.py`](coding/tue_attention.py) from an empty editor. Narrate every shape. No notes, no autocomplete. Under 15 min clean: do not practice vanilla attention again. |
| 20 min | [`16_varlen_pool.py`](coding/16_varlen_pool.py). 3–4 asserts. Padding, mask, attention, masked mean. |
| 30 min | [`tue_broadcast.py`](coding/tue_broadcast.py). Key mask on `[B, H, Tq, Tk]`, masked mean, group-key mask on `[B, T, Gq, Gk]`, causal + padding into `[B, H, T, T]`. |
| 30 min | [`tue_shapes.py`](coding/tue_shapes.py). Heads, permute-then-reshape, pairwise dot with no loop, flatten for CE. |
| 45–60 min | Stories **A** and **B** only, as answers to the questions below. Apply the 16 Oct mock fixes before retelling A. |

Tuesday questions:

- Why image representations at all?
- Why delay embeddings? Why not patches?
- What does the representation preserve? What does it throw away?
- How do you know the gain is not capacity?
- What did the same-view controls establish? What do they **not** establish?
- Why does delay-only fail numerically?
- Why does a second view help on some tasks and not others?

### Wednesday 21 — hardest coding day (~3 h)

| | |
|--|--|
| 35–45 min | [`17_group_attention.py`](coding/17_group_attention.py), blank. Then [`17b_cross_group.py`](coding/17b_cross_group.py): permute, scores, mask keys, softmax over `Gk`, multiply values, restore shape. Shape asserts. No lookup. |
| 25 min | [`17c_group_multihead.py`](coding/17c_group_multihead.py). Say which axes `transpose` hits. |
| 25 min | [`18_masked_train_step_broken.py`](coding/18_masked_train_step_broken.py). Diagnose before editing. CE layout, pad labels, target dtype, `zero_grad`, `train` vs `eval`. |
| 30 min | Debugging sprint. One broken snippet at a time, from the session, not from a file. Diagnose aloud, then a small hint. Bugs to cover if they have not already appeared: wrong softmax axis, inverted key mask, pad filled with 0 instead of `-inf`, wrong transpose, reshape after permute, CE on `[B, T, C]` directly, float targets, missing `zero_grad`, `eval` with gradients still on, pad included in the mean, device mismatch, causal mask off by one. |
| 45 min | Breadth, rapid questions only. See the list below. |

Wednesday questions:

- Time-series foundation model vs a model trained on the task: when the FM helps, when the specialized model wins, transfer, zero/few-shot, heterogeneity, data scale.
- Multivariate / covariates: independent channels vs cross-variate modeling, concatenation vs cross/group attention, known-future covariates, static covariates, leakage, missing variates, scaling with `G`.
- Why diffusion for forecasting? Flexible distributions, multimodality, joint sampling, uncertainty, sampling cost, when diffusion is overkill.
- Koopman: what problem the representation solves, why linear latent dynamics can help, limitations, stability / identifiability, how it differs from a generic latent-state model.
- GRPO only if that line is on the resume. Use the card above. Do not implement PPO or GRPO.

### Thursday 22 — mock + repair (~2.5 h)

| | |
|--|--|
| 50–55 min | Full mock. 20–25 min resume methodology / breadth (assumptions, alternatives, ablations, what the result does not prove, what would make you drop the method). 25–30 min coding: [`19_thu_mock.py`](coding/19_thu_mock.py), opened then, not before. Log breaks in [`mocks.md`](mocks.md). |
| 45–60 min | Repair only what broke. Mask bugs → three mask drills. Reshape bugs → five shape transforms. CE bugs → two masked-loss exercises. `zero_grad` bugs → two training-step snippets. Do not add a new topic. |
| 25 min | A **new** tensor problem, given in the session, using only matmul, transpose/permute, reshape, masking, softmax, reductions, CE. Not 16–18 and not 19. |
| 30 min | Breadth rapid fire. Resume-specific. No story polishing. |

### Friday 23 — 20 minutes, around 20:30

No heavy coding.

| | |
|--|--|
| 5 min | From memory: `scores = q @ k.transpose(-2, -1)`, scale by `sqrt(d)`, `masked_fill`, `softmax(dim=-1)`, `attn @ v`. |
| 5 min | Mask shapes: `[B, T]` → `[B, 1, 1, T]`. `[B, G]` → `[B, T, 1, G]` or the equivalent you actually use for group attention. |
| 5 min | `zero_grad`, forward, loss, backward, step. |
| 5 min | Three anchors. ImagenTime: representation hypothesis + a cheap test that could kill it. Dual tower: matched controls, where it helps, where it does not. TR kill: the slice gate written before the run. |

Then stop. Call at 22:00.

---

## How the drills are run

The session acts as the live screen. It does not reveal the solution up front.

For every coding question: prompt only; you state input and output shapes; you name the axis the op uses; you code; you write 2–3 unit tests; run them; a miss gets a small hint, not the solution; then one follow-up that changes the axis, the mask, the number of groups, the query/key lengths, or the padding convention.

Resume questions push on assumptions, the alternative method, the ablation, what the result does not prove, and what would make you abandon the method.

---

## On the call

- Restate the coding problem and the shapes before typing.
- If his test fails, read the assert and fix that case. Narrate the mask and the axis.
- If he asks a paper of his, answer the scientific question from your work.
- IC verbs. One metric. The claim you will not make.

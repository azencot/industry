# Siemens technical screen — Huzefa Rangwala — Fri 23 Oct 2026

**When:** Friday 23 October, **22:00–23:00 Thailand** (ICT). That is **08:00–09:00 Pacific**.
**Length:** 1 hour.
**Interviewer:** **Huzefa Rangwala**, Staff Scientist, Physical AI, Siemens. This books the technical screen. He is not confirmed as the hiring manager.
**Prep window:** Tuesday 20, Wednesday 21, Thursday 22. Mornings. About three hours each. Friday is a 20-minute pre-call, not a fourth day.

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

### Breadth he can ask without picking a paper

Speak from a project. Two minutes each.

**Time series.** A foundation model is the right first try when many related series share structure and the target history is short. A model trained on the task wins when the sampling is irregular, the covariate set is specific, or the decision needs a calibrated error you have measured. Multivariate structure does not have to be “concatenate channels in time.” Sharing across the series axis at each time index keeps a variable number of variates and covariates from blowing up the context. That is a method you can defend from your own representations work. You do not need his Chronos-2 talk track.

**Physical constraint.** A soft penalty can be small while a conservation law or a boundary is still violated. A hard constraint (architecture, projection, or a correction after the network) is the one that still holds on a new initial condition. The average error is the wrong gate for a surrogate: name the decision the surrogate feeds, and the slice where you still call the numerical solver. Bosch is the concrete story if he wants a sensor, not a PDE slogan.

**When the metric lies.** Story C. Gates written before the run. Kill the lever, keep the objective.

---

## Coding half — slightly harder, same skills

Robinson’s examples are still the floor: `DataLoader`, padding, an attention matrix, and a unit test that has to run. The question is one function, not a puzzle.

The miss last time was **syntax under a live editor**, on problems that were short. Harder algorithms would practice a different failure. The step up is **longer functions on the same APIs**, plus one case where the attention axis is not time.

| Do this week | Leave |
|--------------|--------|
| Blank redo of attention + mask (05, 06), 25 minutes | Rereading the drafts already in 05–08. They pass core asserts. That does not make them retrievable. |
| **16** variable-length pool. This is the realistic “now put it together” question. | 09–15 as a checklist. One train step is covered by **18**. |
| **17** once. Attend across series, not time. | A GRPO / PPO implementation. That is spoken. |
| **18** once. Masked cross-entropy and one optimizer step. | Sliding-window, pairwise, MLP, unless Thursday’s mock shows a hole in `nn.Module`. |

Syntax to say while you type, because this is where time went:

- `transpose(-2, -1)` is the last two axes. After a head or a group appears, `transpose(1, 2)` is a different pair.
- Key mask `[B, Tk]` becomes `[B, 1, Tk]` against scores `[B, Tq, Tk]`. `masked_fill` needs a bool. Invalid logits get `-inf`, not `0`.
- Softmax of an all-`-inf` row is NaN. `nan_to_num(..., nan=0.0)` makes that row contribute nothing.
- `reshape` after `permute`. `view` on non-contiguous memory throws.
- `F.cross_entropy` wants `[N, C]` and class indices. Flatten `B` and `T`, then put the mask back on the per-position loss. Divide by the count of valid positions, with `clamp_min(1)`.
- `zero_grad` before `backward`. `model.train()` does not zero gradients. `eval()` does not turn gradients off.

Mask convention in every file: **True = valid**.

---

## Three days

Each block is spoken or typed. No solution file until the asserts pass. Stop at the end of the block.

### Tuesday 20 — methods, then attention from a blank file

| | |
|--|--|
| 40 min | Story A, no notes. Then check the mock fixes above and say it once more. |
| 40 min | Story B. Include the matched-tower control, the ChatTS numerical collapse for delay-only, and one place the dual view does not help. |
| 25 min | New empty file. Scaled dot-product attention, then the same function with a key mask and a causal mask. Three asserts. Run. |
| 45 min | [`coding/16_varlen_pool.py`](coding/16_varlen_pool.py). Write the asserts first. |
| Stop | | 

### Wednesday 21 — the breadth he can actually push, then the two harder functions

| | |
|--|--|
| 35 min | Time-series card above, out loud, tied to one resume project. |
| 30 min | Constraint card, or story C if you want the failure fresh. |
| 25 min | GRPO card **only if it is on the resume**. Otherwise retell story C’s gate and the kill. |
| 50 min | [`coding/17_group_attention.py`](coding/17_group_attention.py). Say the permute before writing it. |
| 40 min | [`coding/18_masked_train_step.py`](coding/18_masked_train_step.py). |
| Stop | | 

### Thursday 22 — one mock, then stop

| | |
|--|--|
| 50 min | Mock the hour at half length. 20 minutes: he names a resume line, you do method, ablation, failure. 25 minutes: problem 16 or 18 from a blank file, asserts, run. No solution file. Log breaks in [`mocks.md`](mocks.md). |
| 30 min | Repair only what broke. |
| 20 min | Shapes card in [`coding/README.md`](coding/README.md) and the syntax list above, once, from memory. |
| Stop | No new story. No new algorithm. |

### Friday 23 — 20 minutes, around 20:30

Story A in 90 seconds with one number. Story B’s control in four sentences. Then write the attention score shape and the key-mask broadcast from memory. Open the call at 22:00.

---

## On the call

- Restate the coding problem and the shapes before typing.
- If his test fails, read the assert and fix that case. Narrate the mask and the axis.
- If he asks a paper of his, answer the scientific question (when a surrogate is trusted, how covariates enter, what the reward was) from your work.
- IC verbs. One metric. The claim you will not make.

# Recap — Day 2 multimodal (read this to recall)

**For:** Apple Health AIML tech screen (Feng Zhu, Tue 8/25). Spoken. No pad.  
**Worksheet:** [`../interviews/apple-health-aiml/code/day2_multimodal.py`](../interviews/apple-health-aiml/code/day2_multimodal.py)  
**Sat lock-in (tables):** [`2026-08-22_multimodal-fusion-lockin.md`](2026-08-22_multimodal-fusion-lockin.md)

Day 2 is *how a second stream meets the LM*. Shirley already heard **encoding** (text / images / native TS). Feng can go one layer down: fusion, alignment, labels, missingness. Your VLM run is evidence at the end of a block, not the lecture.

There are two axes. Do not mix them.

| Axis | Question | Your HM answer |
|------|----------|----------------|
| **Encoding** | What is the series *as*? | Text dump / patched native encoder / images (two views). |
| **Fusion** | Once you have vectors, how do they enter the LM? | Concat (your stack), cross-attn, or unified tokens. |

---

## 1. The drawing

```
signal/image → modality encoder → projector → modality tokens ─┐
text → tokenizer → embeddings ─────────────────────────────────┴→ LLM → out
```

Encoder sees the raw stream (ViT, 1D TS encoder, speech FM, …). Projector is a learned map into the LM’s width **and basis**. The LM is still a causal next-token model. Everything below is a choice about that join.

---

## 2. Projector

\[
z\in\mathbb{R}^{d_v}\mapsto Wz\in\mathbb{R}^{d_{\mathrm{LLM}}}
\]

It exists because the **spaces** differ, not only the widths. If \(d_v=d_{\mathrm{LLM}}\) you still need \(W\): the vision basis is not the LM basis. Skip it and you either crash or stuff the LM with pad-junk.

The projector is **not** fusion. Fusion is what you do *after* you have LM-width vectors: put them in the sequence, or use them as K/V in extra layers.

Stage A (LLaVA-style): freeze the LM, train the projector (sometimes the encoder) so the spaces meet. Stage B: LoRA / unfreeze the LM so it *uses* those tokens. Your run was this shape.

---

## 3. Three families

### Concat (LLaVA) — your stack

Projected patches become **tokens in the LM sequence**. Self-attention over the fused string. Cost \(\mathcal{O}((T+T_{\mathrm{mod}})^2)\). Dual visual views = this family **twice** (chart block, delay block, then text).

Two *implementations* of the same family — do not call the second one xattn:

| Code name | What happens | Length |
|-----------|--------------|--------|
| **concat** | `cat(h_v, h_t)` — prepend the patch block | \(T_{\mathrm{mod}}+T\) |
| **scatter** | Prompt already reserved \(T_{\mathrm{mod}}\) `<image>` ids; **replace** those embedding rows with \(h_v\) | stays \(T\) (placeholders already counted) |

Tuesday, say **concat** or **insert tokens**. “Scatter” is a write-into-reserved-indices verb.

Use concat when \(T_{\mathrm{mod}}\) is small (your charts: ~114 + delay 64) and you want to reuse the pretrained LM as-is. Failure: the sequence gets long, \(T^2\) hurts, or the LM **ignores** the patches and answers from text.

### Cross-attention (Flamingo)

Text is the only sequence. \(Q\) from text, \(K,V\) from the modality. Length stays text-\(T\). Cost \(\mathcal{O}(T\cdot T_{\mathrm{mod}})\) per layer. A **Perceiver / resample** to a fixed set of latents is a bottleneck on purpose.

Use this when the second stream is long (video, hours of IMU/PPG) or you want that bottleneck. Failure: extra params; a learned gate \(\gamma\sim 0\) so the modality is unused.

### Unified tokens

Patch or quantize the signal so the **same** Transformer sees it. Honest if you have the data — you **train** that encoder. Expanding the vocab with a few special ids is plumbing, not the fusion site.

A native TS encoder + projector + concat into Mistral is **family 1 with an honest encoder**, not a third religion. That is her TS-LLM shape. Your images were a stolen visual prior, not the true object of a series.

---

## 4. CLIP — align two spaces, no decoder

Two encoders, a batch of \(N\) **paired** examples. L2-normalize. Score:

\[
s_{ij}=\frac{z_i^{\mathrm{img}}\cdot z_j^{\mathrm{txt}}}{\tau}
\]

\(N\times N\) matrix. **Diagonal = pair. Off-diagonal = in-batch negatives.** You do not need a separate negative miner for the basic recipe. Symmetric CE (image→text and text→image). \(\tau\) is temperature: small \(\tau\) sharpens, large \(\tau\) flattens the batch.

**What it teaches:** matching. Retrieval, zero-shot classify-by-prompt, a joint embedding.

**What it cannot teach:** generation. No LM head, no causal CE, no “describe the slope,” no CoT. Do **not** say “CLIP cannot solve a downstream task” — it does retrieval. Do **not** say “CLIP is how I add images to a pretrained LM.” Adding images is projector + insert + completion-only SFT.

| Stage | Objective | What moves |
|--------|-----------|------------|
| CLIP-style | \(s_{ij}\) + in-batch CE | Two encoders into one space |
| LLaVA Stage A | Next-token on captions, LM frozen | Projector |
| Stage B | Completion-only SFT | LoRA / LM |

Unpaired streams have no diagonal — pick another recipe or do not contrastive. Tiny batch → few negatives → weak alignment.

---

## 5. Toy concat forward (scatter path)

Named sizes in the file: \(B=2\), \(T_v=4\) vision tokens, \(T=10\) **including** those 4 placeholders, \(d_v=8\), \(C=16\), \(V=32\).

```
z_v   [B, T_v, d_v]   encoder (stub)
h_v   [B, T_v, C]     projector
input_ids [B, T]      placeholders already in the string
h_t   [B, T, C]       embed every id
h     [B, T, C]       scatter: write h_v into reserved rows
S = T
m     [S, S]          causal, upper triangle −∞
A     [B, T, T]       one head
Y=AV  [B, T, C]
logits [B, T, V]
labels [B, T]         vision + prompt = −100
```

**The slip that kept happening:** collapsing \(T\) and \(T_v\). `input_ids` and `h_t` are **long**. `z_v` / `h_v` are **short**. Scatter writes the short block into the long sequence. After scatter, length is still \(T\), not \(T_v\). Concat (the other implementation) grows to \(T_v+T\).

**RoPE.** On **Q and K of the fused sequence**, by **index in that sequence** (`0..S-1`). Score \(q_i^\top R_{j-i} k_j\). Text does **not** restart at 0; first text is position \(T_v\).

**Causal \(M\).** Early vision **cannot** attend to later text. Later text **can** attend to vision. `vis[0]` cannot see the question. The first answer token **can** look at `vis[-1]`.

The vision **encoder** may be bidirectional on the image. Once patches sit in the LM, they obey \(M\).

---

## 6. Two masks — this is the Day 2 lock

| Object | Job | Lives in |
|--------|-----|----------|
| Causal \(M\) (and pad mask) | Who **attends** to whom | Attention |
| `labels == -100` | Who **contributes to CE** | `CrossEntropyLoss(ignore_index=-100)` |

`-100` is a **code convention**, not a token the Transformer understands and not a softer landscape. Positions with that target are **dropped from the average**. Hidden states at those indices still exist. Later tokens can still attend to them and send gradient **through** those positions into whatever produced them.

**Do not say `A→B attention`.** Say **who attends to whom**.

- Last vision **cannot attend to** first text. That is causal. `-100` is irrelevant.
- First text **can attend to** last vision. `-100` does **not** cut that. Text is supposed to look at patches.

If you **forget** `-100` on vision, the distinctive **CE** leak is \(\mathrm{vis}_i\rightarrow\mathrm{vis}_{i+1}\) (or “predict the repeated `<image>` id again”). That is not the same bug as “prompt in the loss” (\(\mathrm{text}_i\rightarrow\mathrm{text}_{i+1}\) on the question).

A separator token (`<imu>`, `<ppg>`) marks **which stream is present**. It is not a loss wall. If you leave the separator id **on**, you train “predict `<ppg>`.”

**Completion-only:** loss on **answer** tokens. Vision and prompt are `-100`. Otherwise the question owns CE. Scaffold slip: `answer_from` should be the **last prompt index** (\(T_v+2\) for three prompt tokens) so `logits[last prompt] → first answer` stays in the loss.

---

## 7. Where gradient goes

| Flag | Meaning | Grad from CE |
|------|---------|----------------|
| `freeze_encoder` (`z_v.detach()`) | Encoder output is a leaf | Projector + embed + `lm_head`. Not the encoder. |
| `detach_vision` (after projector) | \(h_v\) is a leaf | Embed + `lm_head` only. Projector dead too. Silent “vision unused.” |

In the toy, `z_v` is `randn` without `requires_grad`, so the first detach is a no-op until you set that.

---

## 8. Text shortcut / Q9 — modality ignored

Neither concat nor xattn **prevents** a text shortcut. Concat makes patches first-class tokens (they are *available*). It is not a stronger constraint. Do **not** pick concat “because it stops the shortcut.”

**Why** the second stream is ignored (mechanisms of the failure):

1. **Text shortcut** — the LM can answer from the prompt; patches unused.
2. **No grad into the stream** — detach, dead projector, or xattn gate \(\gamma\sim 0\).

**What you do about it** (not the same sentence): change the **task/eval**. Require the modality. Do not leak the answer in the text. That is the fix. Q9 asked for the *why*.

---

## 9. Wearables Q12

ECG, PPG, IMU, sleep, text. Most examples are a **subset**. Streams are async. Days go missing. This is the data, not a bug.

**Window, not a shared clock.** Align on a sample / window (this workout, this night). Each variate keeps its own Hz. Do not resample IMU@100 Hz and nightly sleep onto one timestep grid.

**Binning summaries ≠ that resample.** HealthKit-style **events** (a bpm, a step count) can be collapsed to one scalar per hour/day: **mean** on rates, **sum** on counts, empty = missing. That is a *chosen summary representation* (periodicity paper). Q12’s kill is forcing **native-rate** IMU and nightly sleep onto one timestep. If you already decided “hourly HR / daily steps,” binning is the representation — say so, and keep empty bins.

**Encode what is present.** One encoder per stream (or a family you bake off) → projector → tokens only for sensors that exist. Do **not** synthesize a fake complete tensor. Do **not drop** incomplete rows — that keeps the compliant / healthier cohort. **Mix on purpose:** IMU-only, PPG+text, sleep+HR, full set. Same loss: task / answer tokens, not “reconstruct the absent PPG.”

**Concat vs bottleneck.** Concat if \(T_{\mathrm{mod}}\) is small (summary / resampled latents). Hours of IMU/PPG → cross-attn or a fixed latent set, or you buy \((T+T_{\mathrm{mod}})^2\).

**Charts.** Not “not my first choice.” **Do not reprint matplotlib on PPG.** Images were a stolen visual prior for public series. Pulse morphology is not a line chart.

**Gate.** One eval across encoder families, on *their* missingness. Public ECG-QA ≠ Watch. Abstain when the observed subset cannot support the claim. Fluency on a missing PPG is a failure.

**CLIP here:** fine for alignment when you have pairs. It does not handle missing streams or teach a health answer.

Bakeoff, 20s:

> Text dumps lose structure. A patched native encoder is the honest bias if you have the data — I’d bake that off against a stolen visual prior and against a pretrained encoder probe. I would not port charts onto PPG. Year one: same gate, their IMU/PPG/longitudinal, including the examples that are a subset.

Do not name RelCon, Feng’s mood paper, or Workout Buddy.

---

## 10. Spoken pockets (say these, then stop)

**CLIP.** Normalized cosine over \(\tau\); diagonal is the pair; off-diagonal is the batch; no decoder. SFT is LM head + completion CE.

**Insert.** Encoder to \(d_v\), projector to \(C\), scatter onto reserved slots. RoPE is fused-sequence position. Causal: vision cannot see the later question; text can see patches. Loss on the answer; vision and prompt are `-100`.

**Q12.** Keep subset rows and mix them. No charts on PPG. Concat if short; bottleneck if hours. `-100` on sensor/prompt, not a separator.

**Q9.** Shortcut, or no grad into the stream. Then, if asked what you’d change: the task and the eval.

---

## Corrections that bit you (keep)

- Equal width still needs a projector.
- Unified ≠ “fusion at the dictionary.”
- Scatter ≠ xattn. Both insert recipes are the concat family.
- \(T\) includes placeholders. \(T_v\) is only the vision block.
- `-100` ≠ attention block. Last-vis looking **forward** is already illegal. First-text looking **back** stays.
- Do not pick concat to “stop a text shortcut.”
- CLIP still does retrieval; it does not generate.
- Q12: “don’t impute” is not “drop the row.” Charts are a kill, not a preference.
- Hourly/daily **binning** of HealthKit events ≠ resampling 100 Hz IMU onto sleep’s grid.
- Q9: name the failure, then the fix.

---

## What is done vs Tuesday

Day 2 taught: families, CLIP, scatter forward, two masks, Q12 (on paper), Q9. Day 3 taught SFT + mock Q1–Q11. **Q12 still not spoken.**

**Next:** Speak Q12 from §9 (include binning ≠ resample if it comes up). Then Tue AM retrieval only. Periodicity pocket: [`../interviews/apple-health-aiml/papers/README.md`](../interviews/apple-health-aiml/papers/README.md). Day 3 lock-in: [`2026-08-24_day3-sft-mock.md`](2026-08-24_day3-sft-mock.md). Do not open RelCon or Bosch.

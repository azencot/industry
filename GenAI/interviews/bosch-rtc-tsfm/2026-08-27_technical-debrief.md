# Debrief — 2026-08-27 — Bosch 1h technical (talk + Q&A + coding)

**Type:** 1h technical — conference talk + previous-work Q&A + take-home walkthrough  
**When:** Thu 2026-08-27, 10:00–11:00 AM PT (Teams)  
**Role:** AI Research Scientist — Multimodal Foundational Models (Sunnyvale)  
**Prior:** [`2026-08-20_technical-agenda.md`](2026-08-20_technical-agenda.md) · [`2026-08-26_previous-work-qa.md`](2026-08-26_previous-work-qa.md) · [`2026-08-26_take-home-submit.md`](2026-08-26_take-home-submit.md) · HM: [`2026-08-13_hm-screen-debrief.md`](2026-08-13_hm-screen-debrief.md)  
**Memory:** captured same morning after the call.

**Do not email Shabnam/Joy** unless they write first (thanks / process). Reloc still in-play. Don’t fight the title. Don’t mix Apple.

---

## Flow (as reported)

1. **Teams failed** (app would not sign in). Switched to **browser**. Lost clock.
2. **Talk:** presented through **slide 21**. Did **not** finish 22 (transfer) or 23 (close). Time, not a content skip-21 plan.
3. **Q&A (previous work / talk follow-ups):**
   - Signals at **various frequencies** — asked on **this VLM**, not a general FM. Answer: **multiple views**.
   - **TSRBench** — data and task types; some discussion.
   - **Synthetic data** — how far can synthetic go; for Bosch, spend on **domain data**; **generative modeling** as a middle ground.
   - **Image → tokens** and **how DINO is trained**. Said DINO **starts zero-shot**; tried to adapt it to delay-embedding images. **Did not remember DINO’s SSL objective.**
4. **Coding:**
   - Data module; **why blocks**. They noted: split **text then encode**, so text can be broken. Answer given: only the **last** block, and a short one is **discarded**.
   - **Line 58** (`labels[:, 1:] != -100`) — leftover from the padded line-wise path. How the model is told about padding → **collate**.
   - How to **improve** — some of the logged NTP vs gen / ROUGE list.

Outcome of the loop: **unknown**. They confer. Wait.

---

## What they probed

| Topic | What they wanted | What you said | Read |
|-------|------------------|---------------|------|
| Freq on *this* stack | Chart vs delay (or STFT) as the dual-view bet | Multiple views | Right *for this VLM*. Do not upgrade it to STFT-in-the-checkpoint. |
| TSRBench | What’s hard / what the data is | Discussed types | Fine if you named reasoning/TR as the weak slice. |
| Synthetic | Domain vs fake data | Synthetic to explore; Bosch should fund **real domain** data; gen as middle | Strong RTC line (business/transfer). Maps to ImagenTime/Synth-FAR without dumping papers. |
| Tokens + DINO | Patch/projector + SSL | Zero-shot init + adapt DE; objective blank | Init story is ok. Objective is the miss (pocket below). |
| Blocks | Why not lines; does encode-after-split break words | Last block only / drop remainder | **Incomplete.** Cuts at **every** 256-token boundary, plus the two text-split points. |
| Pad / line 58 | Do you know mask vs labels | Leftover; collate | Honest. Current collate has **no pad**. |
| Improve | Scientist judgment | (your list) | Keep NTP vs ROUGE; loops + shorter continuation. |

---

## What landed / gaps

| | |
|--|--|
| **Landed** | Browser recovery instead of dying on the app. Dual-view answer scoped to **this system**. Synthetic vs domain vs generative is the right Bosch bar. Coding: knew line 58 was padding leftover; pointed at collate; had an improve story. |
| **Gap** | Teams tax ate the **close** (22–23) — transfer + four takeaways never spoken. Prep said **drop 21 if late**; you kept 21 and lost the landing. DINO SSL objective not recalled. Block answer understated mid-sequence cuts. |
| **Unknown** | Who else was on the call; whether they still want a loop; how much the Teams mess counted. |

---

## Corrections (lock)

### 1. Talk clock when logistics eat time

If share/login burns 5+ min: **skip 21 (scale)**, land **22 then 23**. Do not “almost finish the results.” Transfer is the Bosch close.

### 2. DINO objective (say this next time)

DINO is **self-distillation**, not contrastive SimCLR.

> Two views of the image. Student and teacher ViTs. Teacher is an **EMA** of the student. Train the student so its softmax matches the teacher’s (teacher is centered/sharpened). No class labels. **DINOv3** is that family (plus later extras). I do **not** train DINO from scratch. I load the pretrained tower, then **Stage A LoRA** on delay images so it sees that geometry. “Zero-shot” = ImageNet/web SSL weights as init, not “I never train the tower.”

Image → tokens (if they ask again): ViT **patches** → transformer tokens → **merger/projector** into LLM dim → interleaved with the question. Chart uses Qwen’s native ViT (frozen). Delay uses DINO + merger.

### 3. Blocks vs “only the last cut”

Karpathy packing:

- **80/10/10 is on raw text**, then encode. The 80% and 90% **character** cuts can split a word. That is two places, not one.
- Then **non-overlapping 256-token blocks**. **Every** block boundary can split a word/sentence. That is the point of the packing (context across verse), not a bug you only get at EOF.
- `n // 256` **drops** the leftover `n % 256` tokens. There is no padded short last **sequence**. A short last **batch** is fewer *rows*, still length 256.

If they push “so you break Shakespeare”: yes, at token-block edges, like nanoGPT. Alternative is stride/overlap or encode-then-split on a tokenizer-aware boundary. I chose simple non-overlap.

### 4. Padding (line 58)

Current collate: `labels = input_ids.clone()`, `attention_mask` all ones. **No pad, no `-100`.** Line 58 is the general “count shifted non-pad tokens” form (`block_size - 1` times `B`). How you *would* tell the model: `attention_mask=0` on pad so those positions don’t attend; `labels=-100` so CE ignores them.

### 5. Teams

Corporate loops: **open the browser join link first**. Don’t debug the desktop app on the hour. Have the HTML deck on disk, not only Drive.

---

## Signal (honest)

Not a disaster: they got a real talk, real Q&A on freq / TSRBench / data, and a code review of the datamodule. The miss that you can still own is **DINO’s loss** and **block boundaries**. The miss that was partly luck is **Teams + no 22/23**. Wait for Joy. Don’t write a recap email unless they ask.

---

## Immediate next

1. Wait. No chase email same day.  
2. Apple virtual on-site **Wed 9/2** — DINO pocket above is reusable there too.  
3. If Bosch advances: one-pager of 22–23 unsaid (image renderer transfer + four takeaways) only if they offer another slot.

```
@GenAI/interviews/bosch-rtc-tsfm/2026-08-27_technical-debrief.md
Bosch 1h technical done 2026-08-27. Teams app failed → browser. Talk through slide 21; 22–23 unsaid. Q: freq→dual views on this VLM; TSRBench; synthetic vs domain vs gen; DINO init but not SSL objective. Code: blocks (answer understated every-256 cuts); line 58 leftover; collate for pad. Wait for Joy. DINO pocket: self-distillation, EMA teacher, Stage A LoRA on DE. Don’t mix Apple into Bosch follow-up.
```

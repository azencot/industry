# On-site — Jonathan Bourim (Wed 2:05 PDT)

**Assume:** [Jonathan (Jamie) Bourim](https://www.linkedin.com/in/jonathan-bourim) — Applied Research Engineer, **Health AI**, **Seattle**. Self-describes as a **software engineer**.  
**Leftover Tyler theme:** research rigor — but treat a **pad / engineering debug** as the base case.  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md)

Do **not** email. Do not ask if he is Bourim.

Guillermo (private): loop includes SWEs who assess programming. This is the **most plausible real CoderPad**. Don’t grind LeetCode — be ready to **read/write a short training or data-pipeline snippet** from **your** stack (packing/`-100`, collator, freeze vs LoRA).

---

## How to open (first two minutes)

| They open with | You run |
|----------------|---------|
| A pad, a function, “implement / debug” | Narrate, test, complexity. Your collator / labels / packing — not Two-Sum |
| Systems-in-code (“how do you ship a model?”) | Eval harness → gate → kill → merge A→B. IC verbs |
| A paper / project / “walk me through a result” | Rigor defense below |

---

## Rigor (if spoken)

Two projects. Numbers: [`.cursor/skills/debrief/vlm_multimodal_project.md`](../../../.cursor/skills/debrief/vlm_multimodal_project.md)

| | Project |
|--|---------|
| **A** | Dual-tower VLM. Delay-only ChatTS num **~0.17** vs chart **~0.71** vs dual **~0.79**. TR **26.9 → 21.9** kill |
| **B** | ImagenFew / irregular. Shirley already heard it. Bosch noisy → this stack, **not** a Watch feature |

For each: question, hypothesis, why not the obvious alternative, falsifying baseline, which piece moves the number, where it loses, what you’d conclude if X flipped.

Prefer: *“This ablation separated A from B.”* Avoid SOTA lists / students / RelCon name-drop.

---

## Predicted questions

1. (Pad) Labels after inserting vision tokens.  
2. (Pad) Pack two docs; where does CE leak?  
3. How do you know a training bug isn’t an eval bug?  
4. You didn’t ship a Watch feature — what engineering did you **own**? (collator, dual routing, DDP, vLLM plugin)  
5. Walk one result until it breaks.  
6. +2% average — why believe it? Does modality B get used?  
7. What experiment disproves you?  
8. Participant leakage in a health split.

**Mock (Tue, 30 min):** 15 min “debug this collator” + 15 min one ablation / TR kill. Tight slot between Chung-Cheng and Haraldur.

# Group papers (local PDFs)

PDFs of Shirley’s Health AI / Health & Fitness public papers. **Read to understand the stack. Do not name-drop on the tech screen** unless Feng goes there.

Spoken briefing (no paper quiz): [`../2026-08-20_shirley-group-briefing.md`](../2026-08-20_shirley-group-briefing.md).

| File | Paper | Authors (Apple-relevant) | Why it is here |
|------|--------|--------------------------|----------------|
| [`2411.18822v5.pdf`](2411.18822v5.pdf) | **RelCon** — relative contrastive motion FM for wearable accel (ICLR 2025) | Xu, **Narain**, Darnell, Hallgrímsson, … **Ren** | Sensor / motion layer. 1B **segments**, encoder **~3.9M** params. Not Feng. |
| [`2509.00221v3.pdf`](2509.00221v3.pdf) | **Speech FMs** generalize to wearable TS tasks | **Narain**, Aldeneh, **Ren** | Steal a pretrained encoder under scarcity (HuBERT / wav2vec 2.0 probes). |
| [`2409.11376v2.pdf`](2409.11376v2.pdf) | **Towards Time-Series Reasoning with LLMs** | Chow, Gardiner, Hallgrímsson, Xu, **Ren** (thanks: Vincent Chan, **Feng Zhu**) | Closest to your bet: patch TS encoder → Mistral, two-stage, perception first. |
| [`25_Leveraging_Periodicity_for_.pdf`](25_Leveraging_Periodicity_for_.pdf) | **Leveraging Periodicity** — multi-modal mood pattern models | **Narain**, Sun, Elachqar, Hallgrímsson, **Zhu**, **Ren** | **Feng’s paper.** 12 wearable streams, naturalistic **missingness**, periodicity + GBDT beat a deep TS model. |

## How to use before Tue (Feng)

1. **Skim Feng’s PDF first** (periodicity / missingness). If he says your benches aren’t Watch data, land here: longitudinal, missing days, multi-stream — not UCR plots, not matplotlib on PPG.
2. **TS-LLM PDF** only if you need the bakeoff: native encoder vs images; don’t recite Mistral-7B unprompted.
3. RelCon / speech-FM: already in the briefing. Don’t recap 1B segments.

Not in this folder (optional, not required for Feng): 2023 npj heart-rate (Ren + **Sapiro**); ICLR 2025 instruction-following (Ren / Narain / Miller; thanks Sapiro).

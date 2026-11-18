# Apple interview prep for Ozan Sener

Updated November 18, 2026. Continue Ozan prep in this industry repo.

## Confirmed interviews

- Monday, November 23, 2026, **9:00–9:45 and 9:45–10:30 a.m. Pacific** via Webex and CoderPad. Use the original links in the scheduling email.
- Neil Hutchison named **Luca Moschella and David Hafner** and wrote, “Typically, you will work together on an LLM challenge which includes coding.” He did not specify the interviewer order or distinct topics. Earlier guidance included Python/PyTorch, mathematical and GPU concepts, diffusion training/modeling, and LLMs. The first round has two interviews and the second has three. [Neil’s reply](https://mail.google.com/mail/u/?authuser=aizencot%40gmail.com#all/1a1eb333fbe99daa)
- Neil’s subject line identifies the opportunity as Research Scientist - LLM Efficiency. Full JD and role ID are unverified. Keep this process separate from Nick Foti / Chelsea Elwood, Health AIML, and other Apple tracks.

## Start here in Cursor

Open the industry repo so its existing instructions apply. Read [the repo instructions](../../AGENTS.md), [the research track index](../INDEX.md), and [the October 20 call recap](2026-10-20_ozan-call.md). Keep using the existing [mock log](mocks.md) and [paper notes](papers/). The recap records Ozan naming efficient LLMs and physics-based world models, and probing the assumptions behind KDM and how it differs from other distillation methods.

**Next action:** If the causal-attention diagnostic is pending, use the first 45 minutes today to do it. If it is complete, spend those minutes repairing the biggest issue and start cached decoding. No November drill completions were recorded at handoff.

> Act as my interviewer for a 45-minute Python/PyTorch drill. Give one prompt and let me write and run the code. Let me talk through shapes, assumptions, and tests. Ask follow-up questions as I go and give hints only if I ask. Review the implementation after the timer. Start with causal attention from Q, K, and V tensors shaped [B, H, T, D], or KV-cached decoding if I have already completed attention.

Use 5 minutes for clarification, 25 for implementation, 10 for testing and debugging, and 5 for complexity and a follow-up. Keep AI completions off during timed attempts. For LLM efficiency, retrieve from memory first, check a source, then explain the answer again with the source closed.

## Remaining schedule

Budget **3h 30m Wednesday through Saturday** (2h 30m coding or mocks, 45m recall, 15m review) and **3h Sunday** (2h coding, 45m recall, 15m review). This is **17h** from November 18 to 22, including **12h** coding and mocks.

- **Wed Nov 18 — Attention and KV cache.** Build or revisit causal attention, then implement prompt prefill and a one-token decode step. Check cached outputs against full-prefix recomputation over multiple steps. Explain why KV memory scales with context and KV heads. [PyTorch SDPA](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html) · [KV cache explanation](https://huggingface.co/docs/transformers/v4.57.0/en/cache_explanation)
- **Thu Nov 19 — Stable softmax and GPU efficiency.** Implement blockwise softmax, test extreme logits and uneven chunks, then explain how FlashAttention reduces GPU memory traffic. Diagnose slow time to first token versus slow token generation. [FlashAttention](https://arxiv.org/abs/2205.14135)
- **Fri Nov 20 — Serving.** Write a toy request scheduler with a KV-block budget. Test full capacity, oversized requests, and block reuse. Recall the differences among continuous batching, paged KV allocation, grouped-query attention, and quantization. [PagedAttention](https://arxiv.org/abs/2309.06180)
- **Sat Nov 21 — Two back-to-back 45-minute mocks.** Use a plain editor or CoderPad practice with completions off. First prompt is batched causal attention with variable valid lengths. Second is cached chunk decoding with a mask or position-offset bug. Redo the weaker one and explain how to measure time to first token, inter-token latency, throughput, and peak memory.
- **Sun Nov 22 — Rework.** Repeat the two drills that cost the most time. Re-derive KV cache sizing and explain prefill versus decode. Reserve 20 minutes for mixed precision, activation checkpointing, and the basic diffusion training objective and sampling loop. [PyTorch checkpointing](https://docs.pytorch.org/docs/stable/checkpoint.html) · [DDPM](https://arxiv.org/abs/2006.11239)
- **Mon Nov 23, 8:15–8:45 a.m. Pacific — Warm-up.** Write one familiar tensor operation, recall the KV formula and serving metrics, and check the Webex/CoderPad details from the invitation.

After a drill, log the result and the main sticking point in [mocks.md](mocks.md). Historical correspondence and the earlier prep handoff are available in the separate [Codex workspace](</Users/omriazencot/Omri/workspace/Job hunt/Apple Scientist - Ozan Sener/HANDOFF.md>).

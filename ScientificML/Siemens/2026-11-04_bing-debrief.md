# Debrief — 2026-11-04 — Bing Xiang

**Type:** Loop hour 1. Research depth, with breadth and behavioral mixed in.  
**Interviewer:** Bing Xiang. He leads the applied-science team.  
**When:** Wed 4 Nov 2026, 4:00–5:00 AM Thailand (Tue 3 Nov, 1:00–2:00 PM Pacific).  
**Outcome:** Completed. No score. His reaction was not recorded. Few follow-ups is not a signal either way.  
**Sheet:** [`2026-11-04_bing-cheat-sheet.md`](2026-11-04_bing-cheat-sheet.md).

The hour was mostly the multimodal time-series project. He wanted examples of reasoning. He also asked about a deadline, the Bosch collaboration, and whether that work reached a product. Breadth was short: Transformers versus RNNs, why Transformers scale, point clouds versus meshes, why diffusion.

## What Omri said

**Deadline.** The multimodal project, about a month out. The results had to get substantially stronger. He described the urgency, the work, and what he owned in that push. The experimental changes, the numbers, and whether Bing asked about a tradeoff were not written down. Add them only from memory. Do not fill them from story C.

**Bosch.** The prepared story about a difference in the data. Bing asked if Bosch put it in a product. Omri said he did not know. That is the right answer. The method he told was not written down. The bank version is interpolation plus an observation mask. It is not the EM paper.

**Multimodal.** Charts, delay embeddings, a vision-language model, reasoning that depends on the representation, training and eval. Bing asked for examples of reasoning and did not press the implementation. Concrete cases to have ready, and not yet logged as spoken: a numerical read off a chart, a temporal question the delay view answers and the chart does not, how that slice is scored, and a shortcut the control killed. If a number is required: TSRBench plot-only 45.2, plot plus delay 53.2. Prediction 38.0 to 61.7. TSExam flat at 89.9. One, then stop.

**Breadth.** Whether the Transformer-versus-RNN answer, the point-cloud answer, and the diffusion answer landed was not recorded. He stumbled on why Transformers scale.

**Questions he asked.** Current bottlenecks. Bing talked about Siemens projects. The projects were not written down. First six months. Bing said a pod. Who is in it, and what it owns, were not written down. Huzefa’s earlier description of a PM, two scientists, and engineers is a different conversation. Do not paste it onto this pod.

## Why Transformers scale

Say this if it comes up again. Training steps on tokens in parallel, as matrix multiplies, on the accelerators. Residuals and normalization keep that trainable. Empirically, data, width, and compute have moved the loss in many settings. Scaling is not only a Transformer fact, and a larger model without data does not win. Standard attention is quadratic in length. An RNN trains step by step and can be the better streaming model.

## Point clouds, meshes, diffusion

A point cloud is coordinates, and maybe features. It has no faces. A mesh is vertices, edges, and faces, so the surface is explicit. Simulation and CAD want the mesh.

Diffusion is a stable way to learn a distribution with more than one plausible output. The cost is the sampler. A deterministic baseline still has to lose on the decision.

## Still open

Ramesh is logged in [`2026-11-04_ramesh-debrief.md`](2026-11-04_ramesh-debrief.md). Vivek was the design hour at 5:00–6:00 and may have moved. Check the invitation. Sheet: [`2026-11-04_vivek-cheat-sheet.md`](2026-11-04_vivek-cheat-sheet.md).

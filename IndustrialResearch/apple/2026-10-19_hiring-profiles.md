# Who Ozan is likely hiring — first pass (2026-10-19)

**Question:** What are the three most plausible profiles of researchers Ozan might currently want to hire, and which should Omri prepare for?

Grades: **VERIFIED**, **LIKELY**, **SPECULATIVE**, **UNKNOWN**. Coauthors are not reports. Academic rank is not an Apple level.

---

## What can actually be seen

**One person states that she works with Ozan.** Laura Manduchi, research scientist, Apple Zurich, since March 2025. PhD ETH Zürich, 2024, with Julia Vogt and Gunnar Rätsch. Internship at Apple Zurich, April–September 2024, with Jörn-Henrik Jacobsen on simulation-based inference. Her own site says she works with Ozan Sener and Vladlen Koltun. Thesis work: deep generative models, VAEs, clustering, probabilistic modeling, representation learning. Apple paper with Ozan: *Learning to Evict from Key-Value Cache*, ICML 2026, with Luca Moschella. Earlier Apple-adjacent paper: cardiovascular simulation with Ozan, Cuturi, Sapiro, and Jacobsen (arXiv 2024).

**One Zurich peer is likely in the same group and does not say so.** Luca Moschella, Machine Learning Researcher, Apple Zurich, since August 2024. ELLIS PhD, Sapienza, on latent communication and representation learning. NVIDIA intern on diffusion for 3D generation. Third author slot is Ozan’s on the same ICML 2026 paper. He does not name Ozan or Koltun on his site.

**One person states that he works with Koltun, not with Ozan.** Aleksei Petrenko, research scientist at Apple. PhD USC 2022, robotics, Gaurav Sukhatme. Eight years of industry software, graphics, and vision before the PhD. NVIDIA and Intel during the PhD, on high-throughput simulation and RL. His site: “currently working with Vladlen Koltun on RLVR post-training for interactive LLM agents.”

**Two people state that they used to be in Koltun’s org.** Erik Wijmans (PhD Georgia Tech 2022, embodied AI) is now at Thinking Machines. Marco Cusumano-Towner (PhD MIT, probabilistic programming and generative models) is now at Databricks. Both were on the self-play driving paper and the LLM-agent RL line. Ozan was a coauthor on the driving paper only.

**Not current staff.** Raja Giryes is a collaborator on sabbatical. Jörn-Henrik Jacobsen founded Health AI in Zurich, managed there, and is now at Isomorphic Labs. Manduchi’s internship was with him. That is a past Zurich overlap, not Ozan’s current roster.

**Ozan’s own public title** remains “research scientist.” “Head of the ML group” is Raja’s email. **LIKELY** he is in Zurich, because the person who says she works with him is in Zurich. His site does not name a city.

No public page lists his reports, open reqs, or a senior seat.

---

## Hiring signals that are not a roster

Three Apple postings, role numbers 200631342 (LLM Efficiency, Santa Clara), 200631299 (Photorealism, Santa Clara), and 200631338 (Agentic Workflows, Santa Clara and Seattle), showed up on 12 October 2026. Apple’s own pages did not render their bodies here. The Muse, Yabot, and Nexxt agree on the LLM-efficiency text. Other mirrors agree on the other two. Treat the qualification text as **LIKELY**, not as a copy taken from jobs.apple.com.

Shared boilerplate: an organization of researchers and engineers, work that ships across Apple products, and work that is published in selective venues. The three topics are Koltun’s three public 2025–2026 threads: frontier-model efficiency including diffusion, photorealistic view synthesis, and agentic multimodal models. **LIKELY** these are his organization’s reqs. They do not name him or Ozan. They might be a different Santa Clara group with the same themes.

What those postings actually require, where the mirrors agree:

- Title is Research Scientist/Engineer. Not Principal. Not manager.
- LLM Efficiency minimums: SOTA prototypes you built; papers at NeurIPS, ICML, ICLR, or COLM; comfort from low-level systems programming to algorithms; complex-systems software engineering; Python; PyTorch and JAX.
- LLM Efficiency responsibilities: design, train, and adapt frontier models for efficiency; empirical studies; prototypes; publish; collaborate with product teams to ship.
- Stated interest explicitly includes **diffusion models**, not only LLMs.
- Photorealism adds CVPR/ECCV/ICCV/SIGGRAPH and prefers 3D reconstruction, neural rendering, and view synthesis.
- Agentic Workflows, in the mirrors checked, stresses prototypes, multi-language systems, and clean tested code. Those copies do not list a publication minimum. Do not treat that omission as verified.
- Preferred education on the LLM req is a BS, MS, or PhD. No year count. No “define your own agenda.” No mentoring requirement.
- Base-pay mirror for LLM Efficiency: $184,700–$324,800. Wide enough to cover a new PhD and an experienced individual contributor. It is not evidence of a principal opening.

Koltun’s homepage still says the organization is hiring and to email a CV. In November 2024 he posted an AIML **resident** role in robotics, one year. That is an early-career seat.

Values written into the LLM-efficiency description: the right answer over being right, time constraints, phenomenal decisions. The posted job is a builder on a team agenda.

---

## Observable pattern, small sample

The only recent hires tied to Ozan by name or by a three-author paper are Manduchi (2025) and, likely, Moschella (2024). Both came straight from a PhD. Both already worked on generative models or representation learning. Both had industrial internships. Their Apple paper is about KV-cache eviction, which is not what either thesis was about. Ozan hired generative-model depth and pointed it at an efficiency problem the organization already had.

Petrenko shows the other shape Koltun keeps: a person who has written high-throughput training systems and is now doing RL post-training for LLM agents. He is not evidence of what Ozan hires.

Nobody in this public sample is an assistant professor, a research manager, or someone hired to import their own academic program. Two strong RL/systems researchers left. That can mean a gap. It does not say the replacement is a senior academic.

---

## Profile A — Research scientist/engineer for frontier-model efficiency

**This is the profile to prepare for.**

1. **Technical expertise.** Training and adapting large models so they cost less memory or less time. The posting names LLMs and diffusion models. Ozan’s 2026 paper is a learned KV-cache eviction policy. Nearby work in the org includes Cut Cross-Entropy and single-copy RL. Generative modeling and representation learning are useful inputs. They are not the job.
2. **Research background.** A real publication record at NeurIPS, ICML, ICLR, or COLM, plus at least one prototype that reached a state-of-the-art number the candidate can defend. The recent Ozan-linked hires had that record as new PhDs, in generative models and representation learning, and then changed problems.
3. **Engineering expectations.** The minimum qualification is the whole stack: low-level systems through the algorithm, Python, PyTorch or JAX, complex systems, code the candidate wrote. “I supervised the implementation” does not match the sentence in the posting.
4. **Seniority.** The posted title and the last two hires are individual-contributor research scientists, including people hired at graduation. A senior or principal title is not what this req advertises. The top of the pay band does not establish a principal seat.
5. **Likely responsibilities.** Pick an efficiency bottleneck in a frontier model, train or adapt the model, run the ablation, publish, and work with a product team toward a shippable version. The agenda is the team’s. Manduchi’s move from VAEs to KV eviction is the existence proof.
6. **Evidence.** The LLM-efficiency posting; Ozan’s ICML 2026 paper; Manduchi’s self-description; Moschella’s role, city, and coauthorship. **Against:** the posting does not name Ozan, and it is in Santa Clara while his visible juniors are in Zurich. **Already on the team:** Manduchi and likely Moschella. Hiring another person is still what the posting says, if it is this org.
7. **Match.** Partial. Diffusion, representation choice, and measured compute cuts are real, and so is hands-on adaptation of Qwen-class models: LoRA and DDP on Qwen3-VL-8B and Qwen3.5 from 0.8B through 27B, a vLLM serving path, and DeepSpeed ZeRO-3 stood up for 122B as infrastructure rather than as a result. About 44 papers clears the publication line. The remaining hole is the posting’s other minimum: low-level systems, and training a frontier model rather than adapting one.
8. **Biggest weakness.** The posting’s minimum is a complete SOTA prototype across the stack, including systems programming, and responsibility for training frontier models. A stronger mathematical paper does not fill that line.
9. **Emphasize.** One system you personally built, the simple baseline it had to beat, and the measured cost. Then say how that method would be retargeted if the problem were diffusion sampling cost or memory during long-context inference. Do not open with a research program you want to import.
10. **Still missing.** Whether Ozan is the hiring manager for role 200631342. Whether Zurich can host the seat. Whether “frontier model” here means Apple’s models or open models of the size they already publish (Qwen-class, Gemma-class, a 32B agent).

---

## Profile B — Research scientist/engineer for agentic models and RL post-training

1. **Technical expertise.** Policy-gradient post-training, long-horizon tool-using agents, entropy and stability of RL on language models, and the simulators that make that training cheap. Multimodal models are named in the posting.
2. **Research background.** Someone who has already trained agents in an environment, not someone who has written a forecasting paper that could be redescribed as sequential decision-making. Petrenko, Wijmans, and Cusumano-Towner are the templates. The first is still there. The other two left.
3. **Engineering expectations.** High-throughput RL, one copy of a large model in memory, numerical precision, clean multi-language code. The agentic mirrors stress tested code in complex systems.
4. **Seniority.** Same posted band as Profile A. Petrenko had a PhD plus a long pre-PhD engineering career. That combination matters more than faculty rank.
5. **Likely responsibilities.** Improve RL post-training for interactive agents, or the simulator under it, and publish the scaling result. Koltun and Petrenko already describe this as current work.
6. **Evidence.** Petrenko’s site; LOOP; Entropy-Preserving RL (ICLR 2026); the agentic-workflows posting; the two departures. **Against as an Ozan hire:** Ozan is not an author on LOOP or the entropy paper. He is one author among many on the 2025 driving paper. This looks like Koltun’s agent group. Raja called Ozan head of the ML group, which may be a different slice.
7. **Match.** Weak. Sequential modeling and uncertainty are not a substitute for policy-gradient systems or for a 32B agent run.
8. **Biggest weakness.** No public work on RL post-training, self-play, or the systems those papers are built on.
9. **Emphasize.** Only if he raises agents: you know how to evaluate a sequential predictor under shift, and you can tell him what you have not trained. Do not study into a fake expertise in two days.
10. **Still missing.** Whether Ozan has any hiring say over role 200631338. Why Wijmans and Cusumano-Towner left, and whether those seats are open.

---

## Profile C — Independent senior scientist who brings a direction

1. **Technical expertise.** Broad, original ML. Generative models, representation learning, and the judgment to pick a problem the org does not already have a paper on.
2. **Research background.** An established record, students or collaborators, and a direction the candidate can defend as theirs. This is the profile the intro assumes.
3. **Engineering expectations.** Unknown. The posted reqs still want the candidate to have built the prototype. A senior person who only directs students fails Profile A’s minimum even if Profile C exists.
4. **Seniority.** Senior or principal individual contributor. Not a manager. Nothing public advertises this level.
5. **Likely responsibilities.** If this seat exists: choose a problem at the intersection of the org’s agenda and the candidate’s depth, run it, publish, and eventually have junior people on it. The November 2024 robotics resident and the 2024–2025 PhD hires show how the org grows the bottom. They do not show a search for someone to lead them.
6. **Evidence for.** Koltun still solicits CVs directly, which is how a senior person can enter outside a posted req. Ozan himself arrived as an established Intel researcher, not as a new PhD. Raja introduced an assistant professor, which is a strange email if the only open seats are new-graduate reqs. **Evidence against.** No posting asks for independent agenda-setting, mentoring, or a principal. The only recent people near Ozan were hired at graduation and pointed at his existing problem. The written team values favor executing under constraints over arriving with a program.
7. **Match.** This is the best match to rank, grants, and supervision, and the worst match to the evidence of what they are advertising. Publishing independence is real. Industrial seniority is not established by a faculty title.
8. **Biggest weakness.** He may hear a principal candidate who wants to define a direction, while the evidence says he has been hiring people who will implement his. Leading with “I start research programs” answers a question the posting does not ask.
9. **Emphasize.** Nothing from this profile in the first five minutes. If he asks what you would start, give one problem that serves an existing bottleneck, with the baseline and the experiment, and stop.
10. **Still missing.** Whether any senior seat is open. Whether Raja’s intro was a courtesy or a hiring conversation. How Ozan treats faculty candidates. This is the question the meeting has to answer, and it cannot be answered from the web.

Photorealism (role 200631299) is a real posting and a Koltun theme. It is not a plausible Ozan hire on the publication record, and it is not one of the three above. Do not prepare for it unless he raises geometry and you can still defend that work.

---

## Locked strategy (2026-10-19)

Omri agreed. Lead with Profile A when the conversation shows they want those skills. Keep Profile C as a short second beat, not the opening.

**Lead with A if he mentions any of these:** efficiency, memory, latency, KV cache, or sampling cost; diffusion; training or adapting large models; prototypes and the stack; what you have built yourself.

**The A skills, in the order the posting lists them:**

1. A complete prototype that reached a state-of-the-art number, built by the candidate.
2. Training and adapting frontier models, with diffusion named alongside LLMs.
3. The stack from systems programming to the algorithm. Python, PyTorch or JAX.
4. An empirical study, then a publication.
5. Work with a product team toward shipping. This last one is a responsibility on the posting and the weakest of the five for Omri. Do not invent it.

**Evidence that can carry the opening.** Adapting Qwen3-VL-8B and Qwen3.5 (0.8B–27B) with LoRA and DDP, eval gated before the expensive run, vLLM on the 9B path. One-step diffusion distillation: fewer sampling steps because the reverse process was represented differently. Use the irregular-series compute cut only if he asks for another measured saving. Do not describe the 122B ZeRO-3 setup as a result.

**C, briefly.** The version of C that fits this organization is Ozan’s own arrival: an established researcher who then worked on the lab’s problems, not a professor imported to install a program. The only direction worth having ready is the one that serves a bottleneck they already have: a representation that makes generation or long-context memory cheaper, scored against their KV policy or a standard sampler. Use it only if he asks what you would start, or if he says they want someone to open a direction. One experiment, then stop. Grants, students, and “I define agendas” stay out unless he asks how you work with other researchers.

Do not spend the remaining hours on self-play, robotics, or neural rendering.

**Single strongest reason he might stay interested.** Manduchi shows that he will hire a generative-model researcher. You are a much more developed one, if you can show that you still build the method and that you will aim it at a model-efficiency problem.

**Single biggest concern.** The last people he added are new PhDs who write the code and changed topics. An assistant professor with a forecasting identity and no frontier-model training record can lose to that profile on the requirements that the posting lists first.

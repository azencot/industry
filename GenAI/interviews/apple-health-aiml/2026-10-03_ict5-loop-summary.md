# Apple Health AIML — ICT5 loop, written so a friend can use it

This is my loop for **Machine Learning Research Scientist, Health AIML** (Seattle, virtual on-site expected), which I went through at **ICT5**. A friend interviewing at **ICT6** can treat the shape as real and the bar as one notch higher: same kinds of questions, less tolerance for a project tour, more weight on judgment, scope, and influence.

The notes stop at the on-site. I am not recording a final decision here.

**Role.** Research on multimodal and representation models over health and fitness data. In practice the team is applied ML aimed at a product, not an open-ended foundation-model lab. Shirley described the work as breaking a large problem into concrete tasks of about three months. Feng said they were early, roughly 80/20 research, and that the mix could move toward 50/50.

**People.** Recruiter Tyler. Hiring manager Shirley Ren (Senior ML Manager / Principal Engineer, Health & Fitness). Tech screen Feng Zhu (applied research, multimodal sensors). On-site: Jonathan (applied research engineer), Yujie Li (senior MLE), Chung-Cheng Chiu (principal research engineer, Apple AI/ML, not Health), Haraldur Hallgrímsson (senior applied research scientist), Vincent Chan (engineering manager, Health AIML).

**Clock.** About four weeks once it started.

| Date | Round | Length |
|------|--------|--------|
| 2026-08-12 | Recruiter, Tyler | ~10 min |
| 2026-08-21 | Hiring manager, Shirley Ren | 45 min |
| 2026-08-25 | Tech screen, Feng Zhu | 45 min |
| 2026-09-08 | Virtual on-site, five people | 5 × 45 min, one day |

I was sick the week they first booked, and they moved the whole on-site to one Tuesday without changing the panel. Webex. Join a few minutes early, not ten.

---

## How the loop is actually run

Tyler’s official map, which matched the calendar and then only partly matched the hours:

1. Hiring manager — interest in health AI, interest in Apple, most impactful LLM training run. Briefed as fit. **No coding.**
2. Tech screen — LLM training and multimodality fundamentals. Spoken. **No coding.**
3. Virtual on-site, five themes: LLM training and infrastructure; multimodal architecture and time-series encoding; research depth and scientific rigor; technical leadership and system thinking; health domain and applied ML judgment.

What actually happened:

- Shirley’s “fit” hour was a technical paper-and-training conversation.
- Feng’s hour really was fundamentals, and it felt basic on purpose. Clearing it still mattered.
- On the on-site, the theme printed on the invite was a hint, not a contract. Jonathan did run scientific rigor. Yujie did **not** run an encoding hour; she ran how I work with people and ambiguous problems. Haraldur stayed on time-series representations rather than a clinical-metrics exam. Vincent mixed background, team infrastructure, and a product prediction problem.
- Every invite had a CoderPad link. It was template noise on this loop. I never opened a pad. Programming still shows up when the seat is engineering-heavy. An ICT6 loop, or a more SWE-shaped seat, can get a live coding round even if mine did not. I would be ready to write small wearable primitives (align two irregular streams, patch a multivariate series, a masked cross-attention, merge event intervals) and talk while doing it. I would not grind generic LeetCode as the main prep.

Comp for the posted research-scientist req, public: base about **$175K–$308.5K**, plus RSUs, ESPP, benefits. Tyler said the number depends on experience, interview performance, and what people already on the team make. I did not negotiate on these calls.

Work authorization came up once, on the recruiter call. The job expects Seattle on-site.

---

## What they were scoring

Across rounds, the same few habits kept mattering:

- **Own one object.** They would rather spend 40 minutes on one paper or one training decision than hear a CV. I used ImagenTime (time series as images, generative), ImagenFew (the scarce / irregular follow-on), and a dual-tower VLM (charts plus delay embeddings into Qwen).
- **Separate claim, mechanism, and result.** “We used EDM” is not a contribution if EDM was an implementation choice.
- **A bakeoff with a number beats a preference.** Delay-only 0.17 vs chart 0.71 vs dual 0.79 is an answer. “Images are a natural representation” is not.
- **Pre-declare the kill.** A synthetic mix that lifted the average and dropped the target slice got killed. That story did more work than any architecture diagram.
- **IC verbs.** I design, train, gate, and kill. Opening with a professor title reads managerial. If it comes up, one sentence: the title is the university job; on the work I run the experiments.
- **Do not name their papers back to them.** I had read the group’s public work. Saying the titles in the room sounded like I had reverse-engineered the interviewer. Ask about the problem, not the PDF.
- **Honesty about product.** I have not shipped a Watch feature. The industry pressure I have actually felt is a collaborator’s irregular, noisy sensors changing the model. That was enough. Inventing a ship story would not have been.

For ICT6 I would add one layer they only sampled with me: you are expected to set the question, not only answer it. Decompose a fuzzy product into a three-month scientific slice, say what you would not build, and show you can move people who do not report to you.

---

## 1. Recruiter — Tyler, ~10 minutes

This was logistics, not an interview. He walked the loop, named Shirley, confirmed Seattle on-site, asked about work authorization, and talked about how comp is set. I treated it as a process handoff and did not try to deliver a research talk.

Useful only as a map of the five on-site themes above.

---

## 2. Hiring manager — Shirley Ren, 45 minutes

Scheduled as culture and motivation. She ran science. Same day, Tyler said she had given strong feedback and moved me to the tech screen.

### What she asked, and what I answered

**Background.** I said I am a research scientist and an associate professor, then spent two or three minutes on the multimodal project: represent a time series so a language model can use it, with two visual encodings, a two-stage curriculum, and eval gates.

The stronger open, which I would use at ICT6, drops the title:

> I work on how to represent a time series so a model can actually use it. Most recently I owned a multimodal training stack: two visual encodings into an LLM, a two-stage curriculum, and gates that decide what we keep.

**How do you represent time series for an LLM?** I gave three families and defended a bet.

- **Text.** Dumping numbers into the prompt burns context and throws away temporal structure.
- **A native encoder.** Patch the series, encode it, project into the LLM. This is the more honest inductive bias when you have the data and the encoder has seen signals like yours.
- **Images.** A line chart for trend and amplitude, and a delay-embedding image for dynamical structure. I used images to borrow a visual prior from a model that otherwise could not see the series. I did not claim plots are the true object, and I would not reprint charts on PPG.

I used two views because one view loses information. On numerical questions, delay-only was about 0.17, chart-only about 0.71, and both together about 0.79. Delay stayed useful on anomaly and causality. The chart made scale and trend readable.

**How do you evaluate?** Three benchmarks, with different jobs: TSExam, ChatTS, and TSRBench. TSRBench was the multi-task reasoning north star (on the order of 4,000 problems, many tasks, many domains). She asked whether TSRBench is mainly financial. I described tasks and series and did not cleanly say that finance is one domain among many, and that the decision-making slice includes ECG question-answering. That is the fact. It is still not a wearable evaluation, and I would not pretend it is.

**How was training organized?** Two stages, with gates set before the run. Stage A aligns the visual side while the language model stays frozen. Stage B teaches the language model to answer, typically with LoRA. I do not promote on training loss.

The decision I am proudest of, which I should have said in this hour and did say in substance elsewhere: a synthetic mix aimed at temporal reasoning looked like a win on the average (reasoning about 29.5 to 31.2, a couple of other slices up ~7 points) and dropped the slice it was built to fix, temporal relations, from **26.9 to 21.9**. The gates were −3 points overall and −5 on any reasoning subtask. I killed that mix and went back to an item-level audit. The average going up is the failure mode when the intervention was targeted.

Headline recipe numbers, if they want scale rather than the kill: stock Qwen3-VL-8B from about **0.62 to 0.90** on TSExam; TSRBench from about **0.40 to 0.45**; a 27B fine-tune around **0.92** on TSExam, near the 8B champion. The 27B number is not the point. The point is that a larger model did not rescue a bad mix.

**Product experience.** I was honest: collaboration with industry, not a consumer feature I shipped. Bosch gave irregular, noisy series. I did not pretend a regular-grid generative model would transfer. The adaptation was to generate under scarcity and irregular sampling (ImagenFew), so the observation process is part of the model rather than something you interpolate away.

**Why industry?** I said impact at scale. That answer is true and too generic; it works at any company. The version I would give now:

> The scientific question is the same one I already work on: perception first, then language. The setting is different. The series already live on the device, they are longitudinal and specific to one person, and on-device privacy changes the representation itself, not only the compliance appendix. I am not a clinician, and I will not paste charts onto PPG. In the first year I would learn the signals and the eval, then compare encoder families under those constraints.

**Location.** I am based in Seattle. That matched the req.

**What I asked her.** What the hard technical problems on the team are, and what makes someone successful. She said two things I kept: successful people are **curious and broad**, and a real challenge is **cutting a large problem into concrete three-month tasks**. I forgot her second challenge. I did not invent one later.

---

## 3. Tech screen — Feng Zhu, 45 minutes

He introduced himself as working on multimodal models for sensors. I said I work on multimodal models for time-series reasoning. He then stayed on fundamentals. I advanced after this round.

One early ML question did not stick in memory. Everything below did.

### Self-attention, then decoding cost

I walked Q, K, V, why attention exists (content-based mixing, no fixed window), and the quadratic cost in sequence length. He asked what greedy decoding costs without help. I went to the KV cache: you pay the quadratic prefill once, store past keys and values, and each new token attends to the cache instead of recomputing the whole prefix. Training and inference are different FLOP stories, and he was checking that I knew which one I was in.

### How do you add a modality to an LLM?

I spent two or three minutes on the project, then the design.

Standard recipe, then the evidence:

1. A specialist encoder for the new stream.
2. A projector, because the encoder space and the LLM space are not the same.
3. Fusion by concatenation or by cross-attention. Concatenation is simple and lets every layer mix the streams; it is expensive if the new stream is long, and a weak modality can be drowned. Cross-attention costs query-length times key-length, so you do not dump ten thousand sensor tokens into self-attention. The failure mode is that the model ignores the new stream. The test is to shuffle or drop it and see whether the task moves.
4. Training in stages. Stage A trains the projector and maybe the encoder, **language model frozen**, and you look at generations (does it recover slope and period, not whether the caption is fluent). Stage B updates the language model with LoRA. The encoder can stay frozen or not; that is a choice, not a default. You promote on the **task** against a frozen baseline, not because caption cross-entropy fell. ROUGE is n-gram overlap. It is a weak proxy for whether a time-series caption is right.

On which encoder, I gave the bakeoff rather than a religion. On a UCR-style comparison, several encoders against DINO, **DINO won**. On the Qwen stack, PatchTST versus chart versus chart plus delay embedding, **chart plus delay embedding won**. If the language model has never seen that kind of data, a specialist encoder is the more reasonable prior. I also said a native encoder is the right thing to compare when the stream is a raw sensor. I would not start from a chart.

### Multivariate series

I said I concatenate the streams and mark the boundaries with separator tokens. That is a fair layout when the channels are aligned and all present. It is incomplete for a watch: streams are asynchronous, and a user often has only a subset. The better statement, which I would lead with next time, is: encode what is actually there, train on mixed subsets (motion only, heart rate plus sleep, the full set), and do not drop a person because one channel is missing. Separators mark presence. They are not a substitute for a missingness model.

### What I asked him

What is hard on the project, and how research and product split. He said three problems: **finding the multimodal architecture, not having data, and the encoder**. On the mix: **about 80/20 research now**, possibly **50/50 later**, and they are **early**. I treated that as the team’s own description of the seat: research first, in order to pick a representation that later has to land.

The “no data” point is the one to prepare. Labels are scarce, wear is incomplete, and complete-case academic benchmarks hide that. I would keep incomplete rows, mix the subsets the product will actually see, and put one gate on the team’s own signals.

---

## 4. On-site — Jonathan, scientific rigor

Applied research engineer, Seattle. He opened the day. No coding. He picked **one paper, ImagenFew**, and stayed there. This was the cleanest hour of the on-site. He sounded satisfied once we got to the evaluation.

**Describe the paper.** The problem is data scarcity: you want a generative model of a time series when you do not have a large sample. The method is to lift the series into a 2D representation and train a diffusion model in that image, so a small dataset can reuse a strong visual prior.

**Why 1D to 2D, specifically.** Not “vision models are strong.” Delay embedding is a lagged-coordinate map. Under a smooth enough deterministic flow, the classical reconstruction story says the map is a diffeomorphism onto the attractor, so local geometry survives. I can still draw a delay embedding of a nonstationary or switching series; I should not then claim I recovered one attractor. Smoothness makes the image a useful object. It is not a license, and delay embedding does **not** assume ARIMA-style stationarity. I would also be ready to say why not the alternatives I actually dropped: line plots are mostly empty pixels, Gramian angular fields scale badly on long series, and a spectrogram is the right object when the structure is periodic rather than dynamical. The representation has to be invertible enough that you can get the series back. I checked reconstruction before spending a diffusion run.

**What is the loss?** I sketched DDPM and EDM, and said I trained with the **EDM formulation because it was an implementation choice, not a claim of the paper**. That sentence is the whole rigor test. Same pattern for any sampler, encoder, or optimizer: say what the paper is actually claiming, and what you picked because it trained well.

**Are the results fair?** He wanted the eval setting, whether the comparison is fair, what the numbers mean, and a description of the tests. I walked the protocol. Scarcity has to be the unit you claim: fewer series, shorter series, or irregular observations are different claims. A method for scarce data should be plotted against the degree of scarcity, not reported at one convenient operating point. He was happy with this part.

**Can you add constraints?** I described conditioning the generator (the practical version is to concatenate the condition and use adaptive normalization to scale and shift features). I blanked the name, then recovered it in the same meeting. Name the method first, then the mechanism.

**What I asked.** What is most important to work on in healthcare from his seat, and how research and engineering split the work. Both were the right height for an engineer on a research team. I did not write down his answers.

I had a second project ready (the dual tower, the kill). He never asked. I did not force it.

---

## 5. On-site — Yujie Li, system thinking

Senior MLE, Seattle. The invite implied architecture. She ran **how research actually gets done**: adoption, collaboration, people who do not report to you, decomposition, and ambiguity. She used the full 45 minutes. I did not get a question in.

**An evaluation or a method you developed that other people used.** I used ImagenTime and the 1D-as-images bet, and we stayed there for most of the hour. The shape that worked was not a paper recap. It was: there was a gap (one generative framework from short series to more than 17,000 steps), I bet on a structured 2D representation plus a mature image-diffusion stack, collaborators objected that 2D expands the representation and may destroy numerical access, and I answered with three tests that could kill my own idea before a large run — reconstruction, small-scale generative quality, and whether the quality was worth the compute. Line plots and Gramian fields failed the screen. Delay embeddings and an STFT-style map survived. Only then did we scale. The same framework covered lengths from 24 to 17,544. On short unconditional generation the discriminative score improved about 58% on average versus prior diffusion models; on long and ultra-long benchmarks the classification score improved about 133%. On MuJoCo, discriminative error was 0.007 versus 0.059 for a prior diffusion baseline. I kept the claim narrow: those numbers show the image-space system worked across lengths. They do not prove that every 2D map beats every 1D model, and they do not prove that each point of gain is “the representation” rather than capacity.

**How do you collaborate?** I used the Bosch Center for AI collaboration. Benchmarks looked good. Their real sensors did not. My first instinct was a stronger model. Their account of the data changed the diagnosis: irregular sampling, noise, partial observation, and imperfect alignment across modalities. I stopped trying to resample everything onto a clean grid, because that hides the fact that a measurement was never taken, and I put the observation process into the generative model. They were collaborators, not people who reported to me.

**People who do not report to you.** I said I write down the uncertainties, take them to that person’s manager, and agree on a mitigation, with concrete examples rather than “I aligned stakeholders.” For ICT6 this question is central. The answer has to be a technical artifact (a risk, a gate, an experiment), not a relationship story.

**How do you decompose a problem for students?** Gap, then the bet, then a short proof of concept, then four streams: data, modeling, training, evaluation. When steps depend on each other, each step has a deliverable and a gate before the next expensive stage starts. Stage A freezes the language model. A representation has to survive a cheap screen before anyone trains the full stack.

She said “students,” so I answered in that frame. At ICT6 I would still answer, and I would spend one sentence moving it off the university: the same split is how I would scope a three-month slice with engineers who do not report to me. They keep ownership of their piece. I unblock the interface.

**An ambiguous project.** The charter was only “sample in fewer steps.” I had to learn how the sampler actually worked. While doing that I saw that the reverse process can be represented differently, and that alternative representation is what made few-step sampling realistic. I would not have gotten there from a library recipe. I do not open this story with a method brand name.

---

## 6. On-site — Chung-Cheng, training infrastructure

Principal research engineer on Apple’s foundation-model stack, brought in as the cross-org training person. I did not write this hour up afterward, so I will not invent the transcript.

What this seat is for, and what I was ready to say: **diagnose the bottleneck before naming a tool.** Profile first. Then decide whether you are bound by compute, by the all-reduce, or by memory. FSDP, FlashAttention, and “more GPUs” are answers to different profiles.

A trap I had already missed in practice and would not miss again: if you take microbatch 8 on 8 GPUs and “scale to 64,” you have to say whether 64 is the microbatch or the global batch. Global batch is microbatch times world size times gradient accumulation. Changing 8 to 64 without saying which one silently multiplies the optimizer’s batch by eight, changes the noise scale, and makes a later “the run diverged” conversation uninterpretable. Match the batch you mean, or the comparison is not about the parallel strategy.

Other things worth having cold for an ICT6 version of this hour: activation memory versus parameter memory, when sequence length (sensor tokens) blows up before parameter count does, why you would not put raw 100 Hz into an LLM, and what you freeze so the next ablation is cheap.

---

## 7. On-site — Haraldur, time-series representations

Senior applied research scientist on the health team, and a natural person to go deep on representation. The hour felt good. The topic was **time-series representations**. I did not recover the question list that evening, so what follows is the position I hold and was prepared to defend, not a claim that every sentence was said.

- A representation that is right for 5-second activity recognition can be the wrong one for a health outcome a week or a month out. Name the horizon before the architecture.
- Raw 100 Hz is 360,000 samples an hour. Those are not tokens. The stack is signal, then a local encoder, then a coarser latent, then a model at the horizon of the label.
- For a week-ahead outcome I start from daily behavioral aggregates, simple periodic features, a wear indicator, and a gradient-boosted tree. I do not open with a transformer on raw IMU. The tree is the baseline that has to lose, on the slices that matter, before a hierarchical encoder earns its keep.
- Absolute level sometimes is the signal (resting heart rate). Per-window normalization can delete it. Say what you threw away.
- Unlabeled sensor data dwarfs labeled outcomes, so self-supervision is attractive, but the objective has to preserve the structure the downstream label actually needs. A reconstruction loss can be excellent and still discard the one statistic the product uses.
- Evaluation is by person, not by overlapping windows from the same person. A random split of windows leaks tomorrow into today.

If this hour tilts clinical, which it can: a probability is not a decision. AUROC does not make an “80%” mean 80 out of 100. At low prevalence a sensitive detector still has a poor positive predictive value, and that number is what the user feels as false alarms. Threshold, then model, then whether the product should exist. I would not pick the label window because it maximizes sensitivity.

---

## 8. On-site — Vincent Chan, judgment

Engineering manager. Last slot of five. He ran long, about fifteen minutes past the block, which I read as interest. Two technical threads after a long background conversation.

**Infrastructure for the fitness team.** We talked through data, encoding, modeling, training, and evaluation. I answered it as a research plan. The stronger answer, and the one I would give at ICT6, is the system that makes the next experiment cheap and honest:

- What data you are allowed to train on, and what has to stay on device.
- How labels are produced (self-report, a detector, a clinician) and how wrong each source is.
- A participant-disjoint eval harness that already exists before the first model, so a new idea is comparable to the last one.
- Train versus serve, and which pieces must run on the watch.
- Who owns the metric when research and the product disagree.

**Predict onset of menses.** He wanted the whole applied loop: what data, what the label actually is, the first proof of concept, the metrics, and the train/test split. I stayed inside that skeleton. The useful instincts, which match the problem:

- The label is a self-report, not a lab timestamp. Noise in the label is part of the problem, and a model that fits the reporting habit is not a model of physiology.
- The first model should be boring. Cycle history plus a few wearable aggregates, a simple model, a split by person and by time. A foundation model is what you earn if that baseline fails for a reason you can name.
- Metrics follow the decision. A false negative and a false positive are not the same cost on a consumer notification. Report the operating point the product will ship, plus how many alerts a person sees, not only an average rank metric.
- Cold start is the product. Day one has no personal history, so you need an explicit population fallback and a story for when the personal model takes over.

I did not discuss anyone’s patents or shipped cycle-tracking features. I would not.

---

## Stories worth having verbatim

Each of these is about ninety seconds. Stop. If they lean in, answer the follow-up; do not restart the plot. I, not we, for the action. One story per question. Do not tell the kill and the post-kill audit as if they were the same anecdote.

**1. Disagreement — ImagenTime.** Collaborators wanted to stay in 1D because 2D is larger, slower, and can hide the numbers. I agreed the objection was real and proposed three tests that could kill my idea cheaply: reconstruction, small-scale quality, compute. I dropped line plots and Gramian fields myself. We scaled only after the proof of concept survived. The result is the length range and the discriminative-score gains above. The lesson is not that 2D is better than 1D. It is that I design the experiment so my preferred architecture can lose.

**2. I was wrong — delay embeddings.** ImagenTime made delay embeddings look like a general representation. On numerical question answering they were not: about 0.17 delay-only, 0.71 chart-only, 0.79 together. I narrowed the claim. Delay stayed for dynamics; the chart carried scale. A related control: adapting Qwen’s own vision tower to delay embeddings was about 0.60, versus about 0.83 with DINO, so the representation and the pretrained encoder are not separable. I do not say delay “does not contain” the numbers. I say this model did not access them.

**3. Ambiguous failure — reasoning audit.** After the kill below, “reasoning is weak” still had five explanations (missing operators, compositions that are too deep, unfamiliar formats, missing domain knowledge, a representation limit). I labeled benchmark items by hand, mapped each bucket to a different fix, and screened on a 0.8B model before spending 8B. Overall moved only from about 0.382 to 0.405. The point was which error class moved, not the two points. I should have done the audit before the first synthetic mix.

**4. The kill — synthetic temporal-reasoning mix.** This is the one to know cold. Target slice 26.9 to 21.9 against a pre-written floor of −5, while the average improved. I killed the mix, not the goal. I would not “just train longer” or quietly down-weight the synthetic data and call it the same experiment. That would be a new hypothesis.

**5. Collaboration — Bosch sensors.** Benchmarks worked, field sensors did not, and the fix was the problem statement (irregular, noisy, partial, misaligned), not a bigger backbone.

---

## Questions I asked, and ones I wish I had

Leave three to five minutes. One question, then stop. Ask about their problem. Do not cite their papers.

Ones I actually asked:

- Shirley: what is technically hard here, and who succeeds?
- Feng: what is hard on the current project, and how do research and product split?
- Jonathan: what is most worth working on in healthcare, and how do engineers and researchers split a new representation?

Ones that fit the seats, if there is time:

- What is underestimated until you open the pipeline, something that looks like modeling and is actually data or eval?
- When do you trust a simple model over a foundation model on these signals?
- For a new encoder, what do you want decided before it hits the training stack?
- What does a real eval look like here: held-out people, a pre-declared kill, or a metric that moved once?
- What would you want this person to have decided, alone, in the first three months?

---

## What I would do differently at ICT6

The technical content does not get replaced. Attention, a fusion recipe, a training gate, and a representation bakeoff are still the price of entry. The difference is what they do after you answer.

- **Scope.** ICT5 can be “I owned this run.” ICT6 is “I would cut your problem into the slice we can settle in a quarter, and here is what I would explicitly not start.”
- **Influence.** Have one story about people who do not report to you, with a technical decision at the center. Yujie asked it directly.
- **Product judgment.** Be ready to design a small health or fitness predictor end to end: label noise, prevalence, operating point, person-level split, on-device constraint, and the baseline you hope to beat. Vincent’s second question was that exam.
- **Infrastructure.** Be ready to diagnose a slow or unstable run in terms of batch, memory, and communication, including the global-batch arithmetic. That hour was staffed by someone outside the health team, which means it can happen on a research loop.
- **Coding.** My loop had none. I would still be able to write, narrating, a short function on irregular time. State assumptions and the representation choice before the loops.
- **Motivation.** “Impact at scale” and “I love the Watch” are both weak. The setting (on-device, longitudinal, one user, privacy as a modeling constraint) is the answer. Name the cost: slower publication, less freedom to pick the benchmark.
- **Papers.** Read the group if you can. Do not recite them. If they bring a paper up, engage with the assumption, not the author list.
- **Title and students.** If you manage, mentor, or are faculty, say so when asked and then get back to the experiment you personally ran. Do not lead with the org chart.
- **One object, full depth.** They will pick a paper or a run and stay there. Know the assumption behind the representation, the loss versus the claim, whether the comparison is fair, and what you would add next. Jonathan’s hour is the template.
- **Energy.** Five rounds in one day, and the last interviewer may run over. Eat in the gap. Do not spend the last hour replaying the first paper.

---

## Pocket numbers

| Fact | Number |
|------|--------|
| TSExam, 8B, stock to trained | ~0.62 → ~0.90 |
| TSRBench, 8B | ~0.40 → ~0.45; a later small-model probe ~0.382 → ~0.405 |
| 27B fine-tune, TSExam | ~0.92 |
| ChatTS numerical: delay / chart / dual | ~0.17 / ~0.71 / ~0.79 |
| Delay encoder: Qwen tower vs DINO | ~0.60 vs ~0.83 |
| Temporal relations, the killed mix | 26.9 → 21.9 |
| Reasoning average on that same run | ~29.5 → ~31.2 (this is why the kill was hard) |
| Gates, written first | −3 pp overall, −5 pp on any reasoning slice |
| ImagenTime lengths | 24 to 17,544 steps |
| MuJoCo discriminative error | 0.007 vs 0.059 (DiffTime) |

Say “about.” Do not invent a digit you do not remember under pressure. A forgotten number is better than a sharp wrong one.

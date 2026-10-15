# Siemens Principal Applied Scientist — Behavioral Interview Story Bank

## Purpose

This document maps existing STAR stories to behavioral questions likely for a Siemens Principal Applied Scientist interview. It deliberately does **not** invent metrics, collaborators, production deployments, or outcomes.

The Principal-level framing throughout should be:

**Define the scientific problem → create decision criteria → personally go deep enough to resolve ambiguity → influence technical direction with evidence → create a reusable mechanism/process → remain honest about limits.**

Do not over-index on academic status, publication prestige, or student supervision. Translate faculty experience into senior-IC language: technical direction, scientific judgment, influence without authority, reusable mechanisms, and raising the quality of decisions made by the broader team.

Source stories, with the original numbers and bounds: [`2026-10-15_prior-loop-star-stories.md`](2026-10-15_prior-loop-star-stories.md).

---

# 1. Siemens Question-to-Story Map

| Likely Siemens question | Primary story | Backup | Principal-level signal |
|---|---|---|---|
| Tell me about an ambiguous problem you took from definition to outcome. | Dual-tower VLM | TSRBench audit | Defines north star, architecture, gates, and operating mechanism |
| Tell me about a major technical direction you set. | ImagenTime | Dual-tower VLM | Changes abstraction rather than incrementally optimizing |
| Tell me about a difficult technical disagreement. | ImagenTime disagreement | Bosch diagnosis difference | Makes disagreement falsifiable; evidence beats authority |
| Tell me about a hypothesis you got wrong. | Delay-only numerical collapse | TR synthetic kill | Updates beliefs quickly and narrows claims |
| Tell me about a project that failed / did not work. | TR synthetic kill | Delay-only collapse | Protects objective despite sunk cost |
| Tell me about a difficult technical decision with incomplete information. | ImagenTime | TR kill | Predefines evidence and decision criteria |
| Tell me about a time you had to stop or redirect work. | TR synthetic kill | ImagenTime deadline cut | Kills lever, not objective; reallocates attention |
| Tell me about a time you dove deeply into an unexpected failure. | TSRBench reasoning audit | Bosch | Turns ambiguity into competing hypotheses and tests |
| Tell me about influencing people without authority. | ImagenTime disagreement | Bosch | Changes direction through evidence and shared technical language |
| Tell me about cross-functional collaboration. | Bosch Haifa | ImagenTime disagreement | Domain expertise changes the technical formulation |
| Tell me about working with domain experts. | Bosch Haifa | — | Treats measurement process as part of ML problem |
| Tell me about balancing rigor with speed. | TR kill + tiered gates | ImagenTime deadline cut | Cheap falsification before expensive scaling |
| Tell me about delivering under constrained compute/time. | Dual-tower VLM | ImagenTime deadline cut | Builds tiered evaluation and kills non-informative work |
| Tell me about creating a process others adopted. | Dual-tower eval gates | TR promotion gates | Converts personal judgment into repeatable mechanism |
| Tell me about raising the technical bar for a team. | Diffusion learning program | Dual-tower protocol | Builds capability and reusable infrastructure |
| Tell me about learning a new technical area quickly. | Diffusion from SDEs up | — | Builds deep competency, not surface familiarity |
| Tell me about mentoring/developing someone. | Collator invariant backup | Diffusion learning program | Transfers ownership and leaves a test/invariant behind |
| Tell me about a time you communicated complex technical issues across disciplines. | Bosch Haifa | ImagenTime disagreement | Translates physical/data constraints into model assumptions |
| Tell me about real-world / industrial constraints changing your model. | Bosch Haifa | — | Best Siemens-specific applied-science story |
| Tell me about research-to-practice impact. | Bosch Haifa, carefully | Dual-tower reusable stack | Be explicit: research baseline, not product deployment |
| Tell me about your most technically challenging project. | ImagenTime or Dual-tower | — | Choose based on interviewer interest |
| How do you decide which research direction to pursue? | Synthesize ImagenTime + TR gates | — | Impact, falsifiability, feasibility, differentiation, path to use |
| How do you decide whether to scale an experiment? | Dual-tower tiered eval | TR kill | Cheap probe → slice evidence → expensive run |
| Tell me about a decision where the aggregate metric was misleading. | TR synthetic kill | TSRBench audit | Principal scientific judgment |
| Tell me about a time results contradicted your expectations. | Delay-only collapse | TR kill | Strong scientific maturity |
| Tell me about a deadline where you had to cut scope. | ImagenTime deadline cut | — | Kills work that cannot discriminate the bet |

---

# 2. The Six Stories to Have Fully Ready

Do not try to memorize all prior-loop cards. For Siemens, have these six as the main bank.

## Story A — ImagenTime: Setting a Non-Obvious Scientific Direction

### Best for

- Technical disagreement
- Setting research direction
- Innovation / simplification
- Decision with incomplete information
- Influence without authority
- Most technically challenging project

### Principal-level headline

**I reframed a fragmented modeling problem as a representation problem, created cheap experiments that could falsify my own proposal, and used the evidence to redirect the research line toward a reusable architecture.**

### Siemens-ready 90-second version

We were working on generative modeling for time series ranging from very short sequences to more than 17,000 steps. The conventional next move after our VAE baseline was to build a stronger native 1D generative model. I proposed a more fundamental change: transform the series into structured 2D representations and reuse mature image-diffusion machinery.

There was legitimate technical pushback. The representation could be much larger, every diffusion step could cost more, and numerical fidelity could suffer. At my seniority, I did not want the decision to become an argument based on whose intuition carried more weight. I defined three tests that could kill my proposal cheaply: reconstruction fidelity, small-scale modeling value, and compute cost.

I screened representations before expensive training. Line plots were too sparse; Gramian angular fields scaled poorly; delay embeddings and STFT-like representations survived. I then built a small proof of concept rather than asking the group to maintain two full stacks.

The evidence justified the pivot. The resulting framework handled sequences from 24 to over 17,000 steps, improved short-series discriminative score over prior diffusion models by about 58% on average, and improved long/ultra-long classification score by about 133% on average. It became ImagenTime at NeurIPS 2024.

The Principal-level lesson for me is not that 2D is universally better than 1D. It is that when I propose a non-obvious direction, I want to make the strongest objections measurable, design the cheapest experiment where my own idea can lose, and only then commit the team to the expensive path.

### Seniority upgrades

Emphasize:

- You changed the **abstraction**, not merely the architecture.
- You made the strongest objection to your idea part of the decision framework.
- You killed your own candidate representations.
- The insight became a reusable research line, later informing multimodal work.

Avoid:

- "I convinced my students."
- Publication prestige as the main impact.
- Universal claims that image representations are superior.
- Implying every downstream gain was caused only by representation.

---

## Story B — Dual-Tower VLM: End-to-End Scientific Ownership and Delivery

### Best for

- Ambiguous problem → outcome
- Major project leadership
- Delivering results
- Compute/resource constraints
- Creating mechanisms/processes
- Balancing research with execution

### Principal-level headline

**I converted a broad research ambition into a north-star metric, a unified architecture, staged investment gates, and a repeatable evaluation mechanism that let the group make better decisions under limited compute.**

### Siemens-ready 90-second version

I lead a project on making general-purpose vision-language models reason over time series. The starting point was broad and ambiguous: many papers could perform one time-series task, but there was no unified system that transferred well across perception, reasoning, forecasting, and decision-making.

I made TSRBench our north star and defined the problem around a stock Qwen3-VL-8B baseline: 0.618 on TSExam and 0.402 on TSRBench. I chose a dual representation — charts plus delay embeddings — and personally owned the core integration, including model patches, the collator, curriculum logic, and evaluation protocol.

The bigger Principal-level decision was how we would spend experiments. With eight GPUs and many hypotheses, full-scale evaluation could not be the inner loop. I created a staged process: perception alignment first, then language fine-tuning; and loss sanity → small benchmark subsets → full north-star evaluation. We tracked parse failures separately and refused to promote a feature that won one headline metric while regressing important slices.

That system delivered TSExam from 0.618 to about 0.905 and TSRBench from 0.402 to about 0.452 on one architecture. But the more durable result was the operating mechanism: staged training, config-first experiments, and tiered evaluation became how the project decided what deserved the next expensive run.

At Principal level, I think the job is not only to produce a strong experiment. It is to create a technical system in which the broader team can repeatedly make high-quality scientific decisions.

### Seniority upgrades

Emphasize:

- North-star selection.
- Architecture + operating mechanism.
- Investment gates under constrained compute.
- Your hands-on role despite leading the project.
- Reusable protocol adopted by others.

Avoid:

- Presenting 162 configs / 125 scripts as the achievement.
- Calling academic work "shipping to production."
- Overclaiming downstream users.
- Making it sound like you simply supervised jobs.

---

## Story C — TR Synthetic Mix: Scientific Judgment Under Sunk Cost

### Best for

- Failure
- Kill/redirect decision
- Rigor vs speed
- Results contradicting expectations
- Difficult decision
- Aggregate metric misleading
- Protecting quality

### Principal-level headline

**I defined success before seeing an expensive result, then refused to redefine the hypothesis when attractive secondary metrics improved but the targeted capability failed.**

### Siemens-ready 90-second version

On TSRBench, overall performance had plateaued around 46%, while reasoning remained around 29%. I chose temporal relations as a targeted intervention because the failures appeared decomposable into segmentation, ordering, and multi-hop composition. I designed a synthetic curriculum around those operations.

Before the expensive 8B run, I set the decision rule. We would not promote a recipe with more than a three-point overall regression or a five-point regression on any reasoning subtask. I also required every reasoning task to appear explicitly in the readout rather than disappear inside an average.

The result created exactly the situation those gates were meant for. Reasoning average improved from about 29.5 to 31.2, and two other reasoning tasks gained roughly seven points. After spending the compute, it was easy to interpret that as progress.

But temporal relations — the capability the intervention was designed to improve — dropped from 26.9 to 21.9, exactly five points. Numeric reasoning also fell 3.4 points. I recommended killing that mix.

The key judgment was separating three questions: was the run scientifically interesting? Yes. Did it validate the intended hypothesis? No. Should we abandon temporal reasoning as an objective? Also no. We killed the lever, not the objective, and redirected into an item-level diagnosis.

The lesson I carry forward is that for heterogeneous systems, success criteria need to be declared before the expensive result arrives. Otherwise sunk cost and favorable secondary metrics can quietly redefine what success means.

### Seniority upgrades

This is one of the strongest Siemens Principal stories because it demonstrates:

- scientific rigor
- resource judgment
- pre-commitment
- willingness to stop
- ability to distinguish objective from intervention
- next-step redirection

Avoid:

- Claiming someone else aggressively wanted to keep it if that did not happen.
- Treating thresholds as statistical laws.
- Saying synthetic data broadly failed.
- Claiming distribution shift as proven mechanism.

---

## Story D — TSRBench Audit: Turning Ambiguity into a Scientific Program

### Best for

- Dive deep
- Ambiguous failure
- Root-cause analysis
- Technical ownership
- Deciding what experiment to run next
- Scientific method

### Principal-level headline

**After a failed intervention, I decomposed a vague "reasoning problem" into competing failure hypotheses, tied each hypothesis to a different intervention, and used a cheap model as an instrument before scaling.**

### Siemens-ready 90-second version

After I killed the first synthetic reasoning mix, the important question was not what data to add next; it was why reasoning was weak in the first place.

There were several plausible explanations: missing temporal operations, insufficient composition depth, unfamiliar benchmark formats, missing domain knowledge, or a representation limitation. Those explanations imply different investments, so another large training run would have been poorly identified.

I went back to the benchmark and audited failures item by item. For each problem I asked what operation was required, whether that operation and format existed in training, and whether the model appeared to have parsed the relevant signal correctly.

That produced three working regimes: knowledge gaps, operator/composition gaps, and format/convention gaps. I deliberately treated the taxonomy as a hypothesis, not ground truth. Each category implied a different intervention and a predicted pattern of improvement.

I then generated targeted operator and format examples and used the 0.8B model as a fast experimental probe before spending on 8B. The first controlled run moved overall TSRBench from roughly 0.382 to 0.405 and reasoning from 0.245 to 0.255. More importantly, several missing-operation failures improved while a residual class remained where the input appeared correctly parsed but reasoning still failed.

That gave us a much cleaner basis for the next large experiment. The lesson was that a Principal scientist should not merely choose among plausible fixes. When the problem is ambiguous, the first job is often to design an experiment that makes the ambiguity smaller.

### Seniority upgrades

Emphasize:

- Competing hypotheses.
- Experiment identifiability.
- Cheap model as diagnostic instrument.
- You changed the question from "what should we train?" to "what evidence distinguishes the explanations?"
- This followed the TR kill; do not retell the kill.

Avoid:

- Claiming the taxonomy is objectively correct.
- Treating +2.3 pp as the main success.
- Claiming 0.8B guarantees 8B behavior.

---

## Story E — Bosch Haifa: Cross-Functional Scientific ML with Real Sensor Constraints

### Best for

- Cross-functional collaboration
- Industrial / real-world constraints
- Domain experts
- Translating research toward practice
- Communication across disciplines
- Changing your technical view based on external evidence

### Principal-level headline

**I used domain expertise from the physical measurement system to change the ML problem formulation itself, rather than treating real-world failure as generic domain shift or preprocessing noise.**

### Siemens-ready 90-second version

One of my most relevant cross-functional examples is a research collaboration with the Bosch Center for AI in Haifa on modality translation — generating one sensor modality from another.

I brought much of the generative-modeling perspective, and the method worked well on standard research benchmarks. Bosch brought something I did not have: detailed knowledge of how the physical sensor and measurement process behaved in practice.

When we moved to their real data, performance degraded substantially. My initial instinct was to think in terms of model generalization: perhaps more capacity, regularization, or different training. But working through the failures with Bosch changed my diagnosis. The real measurements violated assumptions hidden by the benchmark: irregular sampling, missing observations, noise, and imperfect temporal alignment.

I worked with them to translate each operational observation into a model assumption and then into a testable intervention. The important shift was that I stopped treating preprocessing as a way to force the industrial data to resemble the clean benchmark. The observation process itself became part of the modeling problem.

The robustness extensions substantially improved the approach in the Bosch setting and made it a strong internal research baseline for subsequent work. I would not claim a product deployment I did not observe.

The lasting lesson is especially relevant to scientific ML: domain experts should not enter only after the model is designed. Their understanding of the physical data-generating process can change the mathematical problem you should be solving.

### Seniority upgrades

For Siemens, this story is unusually valuable. Emphasize:

- Physical measurement process.
- Model assumptions vs actual system behavior.
- Translation between domain and ML abstractions.
- Intellectual humility.
- Honest impact boundaries.

Avoid:

- Calling it a product ship.
- Generic "we collaborated well" language.
- Claiming you knew the sensor domain better than Bosch.

---

## Story F — Diffusion from the SDE Up: Building Organizational Technical Capability

### Best for

- Learning new area
- Raising technical bar
- Mentoring / capability building
- Long-term technical investment
- Entering a rapidly changing field

### Principal-level headline

**I identified a capability the group would need before it became table stakes, personally developed enough depth to make original decisions, and converted that learning into reusable infrastructure and a multi-project research capability.**

### Siemens-ready 90-second version

A few years into my faculty role, diffusion models were becoming foundational, but I had to be honest that my group — including me — did not understand them deeply enough to make original modeling decisions.

I could have delegated the topic to students or treated existing libraries as black boxes. Instead, I decided diffusion needed to become a core technical capability. I set a high bar: understand the SDE and score formulation, own a clean implementation, and reach the point where we could make original design decisions.

I ran weekly deep technical sessions combining theory, implementation, and research ideation, and I worked through the mathematics and code myself. When the SDE formulation exposed a differential-equations gap, I slowed the process down and filled that foundation rather than papering over it. When public implementations proved fragile, I rewrote key components into a cleaner experimental framework.

That investment eventually supported seven diffusion papers at ICML, ICLR, and NeurIPS and became reusable infrastructure behind ImagenTime, ImagenFew, and later projects. It also made it much faster for new researchers to ramp up.

The Principal-level lesson for me is that technical leadership sometimes means recognizing a capability gap before there is an immediate deliverable, then building enough personal depth and reusable infrastructure that the capability compounds across projects.

### Seniority upgrades

Emphasize:

- Strategic capability identification.
- You remained hands-on.
- Reusable infrastructure and faster ramp-up.
- Multi-project leverage.

Avoid:

- "I organized a reading group."
- Seven papers as the only outcome.
- Making it sound like curiosity without delivery.

---

# 3. Two Backup Stories

## Backup 1 — Helping Someone Succeed: Collator Invariant

### Best for

- Mentorship
- Helping a colleague
- Raising engineering quality
- Delegation / ownership

### Siemens-ready version

A collaborator on our multimodal stack was debugging corrupted delay-embedding features for multivariate series. The loader was flattening a `[C, T]` array into one long univariate sequence, destroying the geometry.

The fastest fix would have been for me to patch the collator. Instead, I showed the failure on one concrete example and wrote down the invariant the data path needed to preserve: N series → N markers → N chart plus N delay; channels remain channels.

I asked the collaborator to own both the patch and a unit test that would fail on the flattening behavior. They landed the fix and test, and multivariate delay stopped being a hidden confound in later experiments.

The lesson for me is that at senior IC level, helping is often not taking the difficult file away from someone. It is making the technical invariant explicit and leaving them with the ownership and mechanism to prevent recurrence.

### Important limitation

Do not inflate this into a broad people-management story. It is a concise technical coaching example.

---

## Backup 2 — Deadline / Scope Cut: ImagenTime

### Best for

- Difficult deadline
- Prioritization
- Resource constraints
- What did you choose not to do?

### Siemens-ready version

During the ImagenTime NeurIPS cycle, we had two plausible directions: build a full stronger native 1D diffusion stack and pursue the unconventional 2D representation approach. We did not have the time or compute to do both with enough rigor.

I decided the highest-value question was not "can we build both?" but "what evidence would discriminate the bet?" I cut the full 1D campaign. We kept a VAE baseline, a cheap representation screen, and one small 2D proof of concept. Full training happened only after the representation passed reconstruction and small-scale quality gates.

The 2D path survived and became the paper. We did not produce a polished 1D state-of-the-art system in that cycle; that was the explicit cut.

The lesson is that under deadline pressure I prefer to remove work that cannot change the decision, rather than do every branch superficially.

---

# 4. Questions That Need a Synthesized Answer, Not a Single STAR Story

## "How do you choose which scientific problems are worth pursuing?"

Use a Principal-level framework:

1. **Impact:** If solved, does it change an important capability or decision?
2. **Scientific uncertainty:** Is there a real hypothesis to resolve rather than just engineering volume?
3. **Falsifiability:** Can I design an inexpensive experiment that could tell me I am wrong?
4. **Differentiation:** Is there a reason our expertise/data/system position gives us an advantage?
5. **Feasibility:** Do we have the data, compute, domain access, and evaluation needed?
6. **Path to use:** For applied research, can the result plausibly become a capability used by engineers/products rather than only a benchmark result?
7. **Leverage:** Will solving it create a reusable representation, method, dataset, evaluation system, or infrastructure?

Use ImagenTime as the concrete example: representation-level bet + cheap falsification + reusable leverage.

---

## "How do you balance scientific rigor and delivery speed?"

Suggested structure:

- Rigor does not mean running every possible experiment.
- Identify the decision the experiment must support.
- Define the smallest evidence that can invalidate the approach.
- Use cheap probes and tiered evaluation before expensive runs.
- Predeclare important regression floors.
- Scale only when the cheap experiment answers the intended question.
- Keep mechanism claims narrower than empirical claims.

Concrete evidence:

- ImagenTime representation screening.
- Dual-tower 0.8B / subset gates.
- TR predeclared kill criteria.

---

## "How would you move research toward production?"

Do not pretend you have owned production deployment if you have not.

Principal-level answer should include:

- Start with the operational objective and constraints, not just benchmark quality.
- Involve domain/engineering experts early.
- Define relevant failure slices and OOD conditions.
- Separate offline quality from latency, memory, robustness, calibration, and maintainability.
- Make the input/measurement process explicit.
- Establish reproducible evaluation and regression gates.
- Define when the model should abstain/escalate.
- Instrument behavior after deployment.
- Create ownership boundaries between research prototype and production system.

Use Bosch as evidence that real measurement conditions can invalidate benchmark assumptions.

---

## "How do you lead without direct authority?"

Use this model:

**Make the technical question explicit → expose assumptions → create shared decision criteria → build the cheapest discriminating evidence → let the evidence change your own view too → encode the result in a reusable process.**

Primary evidence:

- ImagenTime disagreement.
- Bosch cross-functional work.
- TR promotion gates.

Do not say "I convince people." Say "I try to make the disagreement testable."

---

# 5. Principal-Level Language Upgrades

Prefer these formulations:

Instead of: "I supervised the project."

Say: "I owned the technical direction and remained hands-on in the critical implementation and evaluation decisions."

Instead of: "My students ran experiments."

Say: "I used smaller experiments to resolve uncertainty, then collaborators reproduced the selected recipe at scale while I remained accountable for the evaluation and promote/kill decision."

Instead of: "I convinced the team."

Say: "I turned the disagreement into a test where either hypothesis, including mine, could fail cheaply."

Instead of: "We got a paper."

Say: "The result validated the direction externally, but the more durable impact was the reusable representation / evaluation mechanism / infrastructure that carried into later projects."

Instead of: "I came up with an idea."

Say: "I reframed the problem at the representation/modeling level and defined the evidence required before committing to it."

Instead of: "The model failed."

Say: "The result falsified the hypothesis we had actually designed the experiment to test."

Instead of: "We tried more data."

Say: "I decomposed the aggregate failure into competing hypotheses and designed interventions whose slice-level effects could distinguish them."

Instead of: "I collaborated with Bosch."

Say: "I used Bosch's knowledge of the physical measurement process to revise the assumptions in our ML formulation."

Instead of: "I mentored someone."

Say: "I made the technical invariant explicit, gave them ownership of the fix and regression test, and left the system less dependent on my intervention."

---

# 6. What Siemens Is Likely Looking for at Principal Level

Across answers, make sure the interviewer repeatedly sees these signals without you explicitly labeling them:

### Scientific direction

You can decide what problem should be solved, not merely optimize a predefined objective.

### Hands-on depth

You still inspect examples, write critical code, reason about tensor/data/model behavior, and debug mechanisms.

### Judgment under ambiguity

You distinguish competing explanations and design evidence that resolves them.

### Resource judgment

You know when to use a cheap probe, when to scale, and when to stop.

### Influence

You establish shared technical criteria rather than relying on hierarchy.

### Rigor

You distinguish empirical results from causal/mechanistic claims and resist post-hoc success definitions.

### Applied mindset

You care about the data-generating/physical system, operational constraints, failure modes, and path to real use.

### Multiplication

You leave behind evaluation protocols, invariants, infrastructure, or technical capability that improves other researchers' work.

---

# 7. Recommended Story Selection by Interview Question

## "Tell me about yourself as a technical leader."

Do not use a full STAR. Summarize: Koopman/dynamical systems → generative/probabilistic modeling → multimodal foundation models, with the common theme of representing and modeling complex dynamics. Then say that your role has evolved from solving individual modeling problems to defining research directions, creating evaluation mechanisms, and leading ambiguous work while staying hands-on.

## "Most impactful project?"

Use **ImagenTime** if they mean scientific impact/direction. Use **Dual-tower VLM** if they mean execution/ownership/current work.

## "Failure?"

Use **TR synthetic kill** if they want judgment. Use **Delay-only collapse** if they want a wrong personal hypothesis.

## "Conflict/disagreement?"

Use **ImagenTime disagreement**.

## "Ambiguity?"

Use **TSRBench audit**.

## "Cross-functional?"

Use **Bosch**.

## "Mentoring?"

Use **Collator invariant** first if they want a concise example. Use **Diffusion capability-building** if they want broader technical development of others.

## "Learned something new?"

Use **Diffusion from SDEs up**.

## "Deadline?"

Use **ImagenTime scope cut**.

## "Real-world constraints?"

Use **Bosch**.

## "Created a process?"

Use **Dual-tower tiered evaluation** or **TR promotion gates**.

---

# 8. Do Not Overuse the VLM Project

The VLM work provides several excellent stories, but do not make every answer sound like one long project.

Keep these distinctions:

- **Dual-tower delivery:** architecture + curriculum + evaluation operating mechanism.
- **TR kill:** decision discipline under sunk cost.
- **TSRBench audit:** diagnosis after the kill.
- **Delay-only collapse:** a separate representation hypothesis that you personally got wrong.

If the interviewer asks multiple behavioral questions, deliberately mix in:

- ImagenTime
- Bosch
- diffusion capability-building

This makes your Principal-level range much clearer.

---

# 9. Final Six-Line Memory Strip

1. **ImagenTime:** Changed abstraction; made my own unconventional idea falsifiable; evidence drove pivot.
2. **Dual tower:** Defined north star + architecture + staged evaluation mechanism; 0.618→0.905 / 0.402→0.452.
3. **TR kill:** Attractive aggregate result, target 26.9→21.9; predeclared gate; killed lever, not objective.
4. **Reasoning audit:** Replaced vague "reasoning failure" with three competing regimes and targeted tests.
5. **Bosch:** Real sensors violated benchmark assumptions; domain expertise changed the ML formulation.
6. **Diffusion:** Identified future capability gap; learned theory/code deeply; built reusable capability across projects.

Backups:

- **Collator:** invariant + ownership + regression test.
- **Deadline:** cut full 1D stack; fund only work that could discriminate the bet.

---

# 10. Practice prompt

Act as an interviewer for a Siemens Principal Applied Scientist role focused on scientific machine learning.

Use the story bank above as factual source material. Do not invent outcomes, collaborators, metrics, product deployments, or responsibilities.

Ask one behavioral question at a time. Favor questions about:

- ambiguous scientific problems
- technical direction
- failed hypotheses
- difficult technical decisions
- disagreement
- influence without authority
- scientific rigor
- resource prioritization
- cross-functional/domain collaboration
- translating research toward real-world systems
- mentoring and raising technical quality

After each answer, evaluate on:

1. **Principal scope:** Did I define direction or only execute?
2. **Personal ownership:** Is it clear what I personally did?
3. **Hands-on depth:** Did I demonstrate enough technical involvement?
4. **Judgment:** Did I explain why I made the decision?
5. **Influence:** Did I move others through evidence/process rather than authority?
6. **Applied relevance:** Did I connect scientific choices to real constraints?
7. **Rigor:** Did I avoid claims stronger than the evidence?
8. **Mechanism:** Did I leave behind a reusable process, invariant, or capability?
9. **Conciseness:** Could the core answer be delivered in 90–120 seconds?
10. **Follow-up resilience:** Are there obvious weak points an interviewer could challenge?

Then ask 2–4 realistic follow-up questions as a skeptical senior scientist would.

Do not rewrite the answer immediately. First identify the highest-impact improvements. Only after the follow-ups should you propose a stronger version.

# On-site — Jonathan Bourim (Wed 2:05 PDT)

Assume: [Jonathan (Jamie) Bourim](https://www.linkedin.com/in/jonathan-bourim) — Applied Research Engineer, Health AI, Seattle. Self-describes as a software engineer.

Assumed focus: Tyler #3 — RESEARCH DEPTH & SCIENTIFIC RIGOR.

This person assignment is a working hypothesis, not an official mapping. CoderPad appears on every invite, so it is weak evidence of a coding interview. Keep a 5–10 minute code/debug contingency, but do not center preparation on the collator.

Hub: 2026-08-27_onsite-prep.md

Do not email. Do not ask if he is Bourim. Use IC verbs. Do not name-drop Apple papers. Do not claim ImagenFew or Bosch was an Apple / Watch product.

One sentence to remember: Don't defend the method; defend exactly what the evidence allows you to conclude.

---

## Primary projects

### Project A — Dual-tower multimodal time-series model

Core idea: represent time series through complementary visual and numerical / temporal representations and integrate them with a multimodal language model.

Important empirical observations:

- Chart representation is substantially stronger than delay-only representation on numerical / time-series reasoning.
- Dual representation improves further.
- Staged training separates learning to "see" the time series from learning to answer questions about it.
- Synthetic-data experiments showed that improving the average metric can hide severe degradation on an important slice.

Useful numbers from the current run: delay-only ChatTS numerical ~0.17, chart ~0.71, dual ~0.79. A temporal-relation mix moved an important slice from 26.9 to 21.9, so I killed the additive mix. Do not merge numbers from different model sizes or protocols.

This project is useful for discussing multimodal representation, ablations, complementarity claims, staged training, evaluation slices, failure analysis, and whether an experiment supports the proposed mechanism.

### Project B — ImagenFew

NeurIPS 2025 work on generative modeling when training data are scarce.

Core research question: can a reusable visual generative prior make time-series generation more data-efficient when trajectories are scarce or irregular?

Broader hypothesis: representation choice changes the data-efficiency problem. Mapping trajectories into an image-like space may expose geometric structure and allow reuse of mature vision-diffusion machinery.

Alternative explanations include pretrained visual features, additional model capacity, easier optimization, rendering artifacts, favorable preprocessing, and leakage from data construction.

Reported result: roughly 55% improvement with 5% of the data in the paper's CV setting. Do not rely on this percentage alone; know the metric, baseline, and absolute numbers before quoting it. If those details are not recalled, say so rather than guessing.

The scientific claim must be defended using matched baselines, scarcity curves, held-out real-data evaluation, irregular-sampling experiments, and representation controls. Only claim experiments the paper actually ran; label additional tests as what I would run today.

Do not frame ImagenFew as a deployed Apple / Watch-like system. It is research evidence about representation and data efficiency. Bosch's irregular, noisy signals motivated analogous reasoning; they do not make ImagenFew a shipped Bosch product either.

---

## What this interview is probably testing

This is not primarily "Do you know technique X?"

It is closer to: "Can you make a research claim that survives skeptical scrutiny?"

Central framework:

CLAIM -> EVIDENCE -> ALTERNATIVE EXPLANATION -> DISCRIMINATING EXPERIMENT -> LIMITATION -> NEXT EXPERIMENT

Jonathan should be able to interrupt at any arrow.

Your job is not to defend every decision. Your job is to distinguish WHAT THE EVIDENCE ESTABLISHES from WHAT YOU BELIEVE BUT HAVE NOT YET ESTABLISHED.

That distinction is one of the strongest signals of scientific maturity.

---

## Module 1 — Defend the research question and hypothesis

Core question: Why was this research worth doing, and what exactly were you trying to establish?

Before discussing architecture, clearly separate PROBLEM, HYPOTHESIS, METHOD, and RESULT. These are not interchangeable.

### 1.1 The problem

A good research problem describes a limitation without assuming your solution.

ImagenFew, weak: "Existing methods don't use image diffusion."

Better: "Modern generative models can perform well with abundant training trajectories, but their behavior in severely data-scarce and irregular regimes is much weaker. We wanted to understand whether representation and reusable generative priors could improve that regime."

Dual tower, weak: "LLMs cannot understand time series."

Better: "General-purpose multimodal models have strong pretrained visual and language representations, but continuous numerical trajectories do not naturally live in either representation space. We wanted to understand which representation makes temporal information accessible to these models and whether complementary representations help."

### 1.2 The hypothesis

Force yourself to state one falsifiable hypothesis.

ImagenFew: "A visual representation combined with a reusable diffusion prior can improve generative modeling of time series in low-data regimes relative to approaches that must learn the relevant temporal representation primarily from scarce task-specific trajectories."

Dual tower: "Chart and delay encodings expose complementary information to a multimodal model, so combining them should improve tasks requiring both global shape understanding and temporal / dynamical structure."

Do not call the delay tower a precise numerical representation without evidence. Its delay image exposes dynamical / topological structure; the chart branch currently dominates numerical reasoning.

These hypotheses are stronger than "our method will get better accuracy."

### 1.3 Why should it work?

If asked why converting a time series to an image might help, do not answer "because vision models are powerful."

Give a mechanism. The transformation may expose global geometry, convert temporal shape into spatial structure, provide compatibility with a mature pretrained prior, and reduce how much structure must be learned from scarce target data.

Immediately acknowledge that rendering can destroy information. This is a hypothesis requiring empirical validation.

For dual tower, a chart may expose amplitude, trend, extrema, periodicity, and relative relationships. A delay representation may expose dynamics / state geometry that the chart branch does not learn easily. This motivates complementarity; it does not prove it.

### 1.4 Novelty vs performance

Be ready for "What is actually new here?"

Separate TECHNICAL NOVELTY from EMPIRICAL FINDING from RESEARCH INSIGHT.

ImagenFew may contribute a methodological extension, while the broader insight concerns representation choice under data scarcity.

Dual tower may contribute an architecture, while the broader question is what representations let pretrained multimodal models reason about time series.

Do not inflate novelty. Precisely defining the contribution is stronger.

### 1.5 What would falsify the hypothesis?

ImagenFew's hypothesis becomes weaker if matched native TS methods perform equally well in low-data regimes; benefit disappears after controlling pretraining; gains occur on one dataset only; rendering choices explain the result; gains disappear under irregular sampling; or generated data fail held-out real-data evaluation.

Dual complementarity becomes weaker if gains disappear under parameter / token matching; shuffling the second representation changes nothing; chart-only matches dual; or gains occur only on tasks solvable by the chart branch.

Being able to state this quickly signals rigor.

### Module 1 practice

For each project answer in <= 2 minutes:

1. What problem were you solving?
2. What was your hypothesis?
3. Why was it plausible?
4. What was genuinely new?
5. What observation would have convinced you that the hypothesis was wrong?

Pass condition: explain the research without mentioning architecture for the first 30–45 seconds.

---

## Module 2 — Defend the method and mechanistic claim

Core question: Why does your method work, and does your evidence actually establish that explanation?

This is probably where Jonathan can push hardest.

### 2.1 Method != explanation

Observation: dual > chart.

Possible explanation: the delay representation provides complementary information.

Other explanations: more parameters, more tokens, different optimization, a regularization effect, or an extra pathway that makes training easier.

Therefore dual > chart does not itself prove complementarity.

### 2.2 Build the alternative-explanation tree

For every major result ask: "What else could explain this?"

ImagenFew central alternatives:

A. PRETRAINING — better pretrained initialization.

B. CAPACITY — more effective model capacity.

C. OPTIMIZATION — image diffusion architecture is easier to optimize.

D. REPRESENTATION — image representation genuinely exposes useful structure.

E. PREPROCESSING — rendering / smoothing changes the problem.

F. LEAKAGE — data construction accidentally shares information.

G. BENCHMARK ARTIFACT — the evaluation metric favors the generated trajectories ImagenFew produces.

Experiments should progressively eliminate these explanations.

### 2.3 Discriminating experiments

This is the central skill for this panel.

Given explanations A and B, ask: "What is the cheapest experiment that separates them?"

Pretraining vs representation: compare the same representation with pretrained vs random initialization. Then compare different representations while matching architecture and training as practically as possible.

Do not change multiple variables simultaneously.

### 2.4 Parameter-matched controls

Suppose dual tower = 8B plus an extra encoder, while single tower = 8B. Maybe it wins because it has more capacity.

Possible controls: parameter-match; add an equivalent-capacity irrelevant branch; compare frozen encoders; test whether interventions on the second modality change predictions.

The exact control depends on the architecture. The principle is to control the competing explanation.

### 2.5 Pretraining controls

If the claim is that a reusable prior matters, compare pretrained vs random initialization under the same representation.

If the claim is that representation matters, compare representations while controlling pretraining as well as practical.

An acceptable conclusion is: "It may be the combination of representation and pretrained prior." Do not force decomposition beyond what experiments establish.

### 2.6 Information interventions

For the dual tower: REMOVE a branch; SHUFFLE it across examples; TIME-SHIFT it; CORRUPT it.

Then observe prediction changes. If the model supposedly uses dynamics from delay images, construct tasks / slices where those dynamics matter.

This is stronger than attention visualization.

### 2.7 Rendering as an information bottleneck

Rendering is not neutral. Choices include resolution, axis scaling, line width, normalization, range, interpolation, labels, color, and cropping.

Each can alter information.

Ask whether gains are robust to reasonable rendering choices and characterize which information rendering preserves or loses.

Do not say "images preserve the time series." They do not necessarily.

### 2.8 Irregular sampling

Separate the representation mechanism from the missing-data mechanism.

Ask: how are timestamps represented? Are missing samples interpolated? Does interpolation create artifacts? Is the model learning actual dynamics or interpolation structure? Does performance degrade as irregularity increases?

A scarcity method should be evaluated over scarcity levels. An irregular-data method should be evaluated over irregularity levels.

Do not imply one ImagenFew experiment established both unless the paper did so.

### 2.9 Mechanistic claim strength

Level 1 — observation: "Dual representation improves accuracy."

Level 2 — supported interpretation: "The gain is concentrated on tasks where the delay representation is useful, and disrupting that representation removes the gain."

Level 3 — strong mechanistic claim: "The delay tower causes the model to learn representation X."

Level 3 requires much stronger evidence. Avoid jumping from Level 1 to Level 3.

### Module 2 practice

For each major result write:

CLAIM

ALTERNATIVE 1 / 2 / 3

EXPERIMENT separating each alternative

Do this for three ImagenFew results and three dual-tower results.

Pass condition: when challenged, first identify the competing explanation rather than reflexively defending the method.

---

## Module 3 — Defend the experimental evidence

Core question: Assume the method is interesting. Why should I believe the empirical result?

### 3.1 Baseline ladder

A baseline should test a hypothesis, not merely add another model name.

ImagenFew needs conceptually: a simple TS generative baseline; a strong native TS generative model; a strong diffusion / generative baseline; a data-scarce adaptation baseline; representation-matched controls where possible.

For each baseline ask: what alternative explanation does it test?

Dual tower: stock multimodal model; chart-only; delay-only; dual; parameter / token controls where possible.

The ladder should isolate what each component contributes.

### 3.2 Data-scarcity curves

Do not rely on "At 5% data we improve 55%."

Evaluate performance as a function of data fraction: 1%, 5%, 10%, 25%, 50%, 100%.

The shape matters. If ImagenFew wins only at 5%, the result is interesting but narrow. If its advantage systematically grows as data decreases, that is stronger evidence for data efficiency.

If the method converges toward the baseline with abundant data, that may strengthen the interpretation.

### 3.3 Absolute vs relative improvement

When saying "55% improvement," know 55% of what: metric, direction, baseline value, method value, absolute change, and relative change.

Never rely only on percentage improvement. If you do not recall the absolute numbers, do not invent them.

### 3.4 Held-out real-data evaluation

Generative models are difficult to evaluate.

Possible dimensions: distributional similarity; downstream utility; temporal statistics; spectral statistics; cross-channel relationships; diversity; coverage; memorization.

No single metric establishes generative quality.

Especially under scarcity, check memorization.

### 3.5 Memorization

Possible checks: nearest-neighbor analysis; train / generated similarity; held-out likelihood or proxy metrics; diversity / coverage; downstream evaluation on held-out real examples.

Think carefully about which checks the actual paper performed.

Strong answer: "We tested X. A stronger additional test would be Y."

### 3.6 Irregularity curves

Vary missing fraction, observation density, sampling pattern, and gap length, then measure degradation.

A claim of robustness under irregular sampling requires more than one irregular benchmark.

### 3.7 Ablations should answer questions

Weak: "We ablated A, B, C."

Strong: "We suspected the pretrained prior caused the low-data gain, so we removed transfer while holding the representation fixed."

Every ablation should correspond to a scientific question.

### 3.8 Seeds and uncertainty

Variance may increase substantially when training data are scarce.

Know the number of runs / seeds if applicable, variability, confidence intervals if reported, and whether differences are large relative to variation.

Do not overclaim tiny differences.

### 3.9 Hyperparameter fairness

Be ready for "Did you tune your method more than the baselines?"

Discuss search budget, baseline hyperparameters, separate tuning, validation protocol, and early stopping. Perfect equality is often impossible; be transparent.

### 3.10 Leakage audit

For both projects walk raw data -> preprocessing -> split -> augmentation -> training -> evaluation.

At every stage ask whether test information can influence training.

Inspect overlapping windows, participant / entity overlap, normalization using the full dataset, synthetic construction, preprocessing before splitting, and duplicate sequences.

### 3.11 Distribution of gains

Average improvement is insufficient. Ask where the method wins and where it loses.

Dual tower: numerical tasks, shape tasks, temporal reasoning, difficult / easy slices.

ImagenFew: scarcity level, dataset type, regularity, sequence length, dimensionality.

A mature scientist knows the failure region.

### Module 3 practice

For each project prepare:

CLAIM

BEST EVIDENCE

STRONGEST BASELINE

MAIN ABLATION

POTENTIAL CONFOUND

WEAKEST PART OF EVIDENCE

Then answer: What is the weakest experiment? Which result are you least confident about? What baseline would you add today? What one control would most strengthen the claim?

Pass condition: identify weaknesses in your own evidence faster than the interviewer can.

---

## Module 4 — Survive the research deep dive

Core question: Can you remain scientifically precise when someone keeps pushing?

This module should contain most of the actual practice time.

### 4.1 The 90-second project opening

Prepare a 90-second opening for each project:

PROBLEM -> HYPOTHESIS -> KEY IDEA -> KEY RESULT -> WHY IT MATTERS

Then stop. Do not give a seven-minute paper presentation. Let Jonathan choose where to drill.

### 4.2 The depth ladder

For every important component prepare four levels:

Level 1 — intuition: why?

Level 2 — mechanism: how exactly?

Level 3 — evidence: how do you know?

Level 4 — limitation: where does the explanation break?

Example:

Why image representation? It exposes trajectory geometry and allows reuse of a visual prior.

How? The trajectory is transformed into spatial structure consumed by the vision-diffusion architecture.

How do you know that caused the gain? State the actual comparison.

Could pretraining explain it instead? "Yes, representation and prior are partly coupled in our experiment. We controlled X, but experiment Y would isolate them more cleanly."

That final answer is stronger than pretending the experiment proved everything.

### 4.3 Failure stories

Prepare at least one meaningful failure from each project.

Structure: HYPOTHESIS -> WHAT I TRIED -> WHAT HAPPENED -> DIAGNOSIS -> EXPERIMENT -> WHAT CHANGED.

Avoid "we tried hyperparameter X and it didn't work." Prefer failures that changed scientific understanding.

Dual-tower failure lock: the temporal-relation mix improved an average while the important slice moved 26.9 -> 21.9, so I killed the additive mix and changed the evaluation gate / data hypothesis.

For ImagenFew, use only a failure that actually occurred. Do not manufacture one from the suggested limitation list.

### 4.4 Surprising results

Prepare "What result surprised you most?"

Strong structure: I expected X because Y. Instead I observed Z. My first explanation was A. I tested it with B. That changed my interpretation to C.

### 4.5 Limitations

Real ImagenFew limitations may include rendering as an information bottleneck; visual prior not fitting every TS domain; representation and pretraining being difficult to disentangle; memorization risk under extreme scarcity; irregularity handling depending on preprocessing assumptions. Claim only those supported by your knowledge of the work.

Dual-tower limitations: rendering dependence; dual-path compute; complementarity varying by task; delay-only branch being much weaker alone than chart; image representations not being natural for high-rate raw signals.

For each limitation, name the experiment that addresses it.

### 4.6 What would you do differently today?

Do not say "use a bigger model."

Possible dimensions: cleaner causal ablations; stronger modern baseline; better matched compute; broader representation comparison; intervention-based modality tests; robustness tests; a scaling study after the representation is validated.

Show that your scientific standards evolved.

### 4.7 What is the next paper?

Derive the next question from the unresolved mechanism.

ImagenFew: if representation changes sample efficiency, which properties of a representation predict data efficiency? Can those properties be measured independently of downstream score?

Dual tower: if representations are complementary, can representation / token budget be allocated dynamically based on the query rather than always supplying both?

### 4.8 Know when to say "we don't know"

Useful structure:

"We don't establish that directly. What we show is X. That is consistent with Y. To distinguish Y from Z, I would run E."

This is stronger than overclaiming.

### Module 4 practice

Do two 20–25 minute hostile deep dives: dual tower, then ImagenFew.

Start: "Tell me about the project."

Then: Why? How do you know? What else could explain it? Why is that baseline fair? What happens if I remove X? What falsifies the hypothesis? Why trust the metric? Could this be leakage or capacity? What failed? What would you change today?

Do not practice these as isolated flashcards. Sustain interrogation of one research story.

---

## Project-specific attack questions — Dual tower

1. Why should chart and delay representations be complementary?
2. Delay-only is much weaker than chart-only. Why doesn't that show the delay representation is bad?
3. If chart is strong, why not improve that encoder rather than add a tower?
4. How do you know the dual gain is not additional capacity?
5. What evidence shows the model uses the second tower?
6. What information exists in delay representation that chart cannot recover?
7. What information does rendering destroy?
8. Why use a pretrained VLM instead of a native TS foundation model?
9. How sensitive are results to rendering?
10. Why does Stage A freeze the language model?
11. How do you know Stage A learns alignment rather than dataset artifacts?
12. Why does Stage B use LoRA?
13. Could end-to-end training outperform the staged procedure?
14. Why did the average hide the temporal-relation slice collapse?
15. How did that failure change the evaluation methodology?
16. What experiment would most strongly establish complementarity?
17. With 10x more native TS data, would chart still win?
18. Which part of the interpretation is least established?

---

## Project-specific attack questions — ImagenFew

1. Why should an image representation improve data efficiency?
2. How do you separate representation from a pretrained vision-diffusion prior?
3. Could the 55% improvement reflect a weak baseline?
4. 55% improvement in what metric?
5. What are the absolute numbers?
6. Why is 5% the important regime?
7. What does the full scarcity curve look like?
8. Does the advantage shrink with more data? Why?
9. How do you know the generator is not memorizing?
10. What does good generated time series mean?
11. Why should the metric correlate with generative quality?
12. What held-out real-data evaluation did you perform?
13. How do you handle irregular sampling?
14. Could interpolation create the structure the image model learns?
15. What happens as irregularity becomes more severe?
16. How sensitive is the method to rendering?
17. Would it work for high-dimensional multivariate signals?
18. What kind of series is a bad fit for an image prior?
19. Why not pretrain a native TS diffusion model?
20. How would you test that?
21. How did you control capacity?
22. How did you control optimization budget?
23. Were baselines tuned equally?
24. What is the strongest evidence for the central claim?
25. What is the weakest evidence?
26. What surprised you?
27. What failed?
28. What would you do differently today?
29. What alternative explanation can you not rule out?
30. What single experiment would most increase confidence?

---

## Cross-project questions

1. Both projects transform time series. What is your general representation principle?
2. When does representation engineering help more than scaling?
3. Both use pretrained priors. How do you separate representation from pretraining?
4. When does an image prior harm time series?
5. What did these projects teach you about inductive bias?
6. If native TS foundation models become dramatically better, does this research become obsolete?
7. How did ImagenFew change the dual-tower design?
8. What scientific mistake from the earlier project did you avoid later?

Do not defend images dogmatically. The durable question is which representation / prior gives the best transfer and sample efficiency under the problem's constraints.

---

## Practice schedule

Target: ~20% review, ~80% active defense.

Session 1 — build two research stories, ~60 min. For each: problem, hypothesis, why plausible, method, central result, central claim, best evidence, strongest alternative, limitation, next experiment. Give a 90-second opening.

Session 2 — claim / alternative / experiment, ~90 min. Take three major claims from each project. For each: three alternatives and one discriminating experiment per alternative. Speak aloud.

Session 3 — evidence audit, ~60 min. Inspect baselines, splits, preprocessing, leakage, ablations, uncertainty, slices, and metrics. Identify the three weakest points and prepare honest answers.

Session 4 — ImagenFew hostile deep dive, ~30 min.

Session 5 — dual-tower hostile deep dive, ~30 min.

Session 6 — failure / limitation practice, ~45 min. For each: biggest failure, surprise, weakest evidence, strongest limitation, initially misinterpreted result, experiment I would run today.

Session 7 — final Jonathan mock, 45 min. Do not decide which project beforehand. Start: "Tell me about a research project you're proud of." Expect technical depth, experimental skepticism, scientific interpretation, limitations, and next research question.

Tuesday live-order mock: Jonathan gets 30 minutes between Chung-Cheng and Haraldur. Use one project deep dive, not a collator-first mock.

Coding contingency: if he opens a pad, narrate, test, and state complexity. Be ready for a short collator / evaluation bug from your own stack, but do not spend the main prep block on it.

---

## What to memorize

Only:

CLAIM -> EVIDENCE -> ALTERNATIVE EXPLANATION -> DISCRIMINATING EXPERIMENT -> LIMITATION -> NEXT EXPERIMENT

Three useful sentences:

1. "What we establish experimentally is X; Y is our interpretation of that result."

2. "An alternative explanation is Z. The clean experiment I would use to distinguish them is..."

3. "We didn't establish that directly in this work. The experiment I would run now is..."

These are not escape phrases. They are scientific precision.

---

## Final pass condition

You are ready when Jonathan can interrupt anywhere and you can answer:

1. What exactly is the claim?
2. What evidence supports it?
3. What is the strongest competing explanation?
4. Which experiment distinguishes them?
5. Is the comparison fair?
6. Could there be leakage?
7. Could capacity explain it?
8. Could optimization explain it?
9. Could pretraining explain it?
10. Does the metric measure the desired property?
11. Where does the method fail?
12. Which claim is weakest?
13. What did you learn from a failed experiment?
14. What would falsify your preferred explanation?
15. What would you do differently today?
16. What is the next scientific question?

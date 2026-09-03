# Behavioral stories — Apple Health AIML on-site

**Status:** Speakable cards for Vincent (leadership) and anyone who pulls judgment / disagreement / failure. Not Amazon LP scripts.  
**Hub:** [`2026-08-27_onsite-prep.md`](2026-08-27_onsite-prep.md) · **Vincent:** [`2026-08-27_onsite-vincent.md`](2026-08-27_onsite-vincent.md)

Default length: **~90 seconds**. Stop. If they lean in, add WHY + REFLECTION only — do not restart the plot. Do not memorize as STAR. The card is the memory; the spoken block is the delivery.

---

## How to use

| Card | Demonstrates | Project | Distinct object |
|------|----------------|---------|-----------------|
| **1** | Disagreement — influence without authority | ImagenTime | Representation bet vs “1D→2D is too expensive” |
| **2** | Wrong hypothesis — changed my own mind | Dual-tower VLM | Delay-only as a numerical channel |
| **3** | Leadership under ambiguity | VLM, after the kill | Three-regime reasoning audit → sequenced plan |
| **4** | Kill / tradeoff | VLM synthetic TR mix | Average up, target slice down → do not promote |
| **5** | Collaboration / impact | Bosch Haifa · LDDBM | Cross-org modality translation, not a student run |
| **A** | Mentorship (60s backup) | VLM collator / multivariate | Technical unblock; they keep ownership. Not “my student.” |
| **B** | Deadline (60s backup) | ImagenTime NeurIPS | Scope cut; representation screen before full 2D stack |

**Do not tell #3 and #4 as the same anecdote.** #4 is the kill. #3 starts *after* it (one sentence handoff).

**Do not tell #1 as a professor-overruled-students story.** The object is a compute/representation disagreement. Collaborators who would train the 2D stack thought the cost would not pay. You answered with a discriminating experiment.

---

## Hard rules

- **I** + named technical action. Not “my lab,” not “I aligned stakeholders,” not associate professor.
- Technical decision at the center: believed X → evidence → I did Y → Z.
- Never “images keep all information.” Never reprint matplotlib on PPG.
- Do not name-drop RelCon / WBM / Workout Buddy / AXLearn.
- Bosch = **BCAI Haifa**, collaborators not reports. Do not claim a BU / Watch ship.
- If asked “what would the other person say?”: give their view in their language, then the evidence that moved the decision.

**Interviewer pull (if the theme holds):**

| Person | Most likely cards |
|--------|-------------------|
| **Vincent** | 1, 3, 4 (leadership = discriminating experiment + kill). **A/B** if mentorship or deadline |
| **Jonathan** | 2, 4 (claim vs evidence) |
| **Haraldur** | 4, 5 (slice gates; messy sensors; don’t assume DL) |
| **Yujie** | 2 (encoding bakeoff) |
| **Chung-Cheng** | usually none — stay on infra |

---

1. Technical disagreement — ImagenTime, native 1D vs image-space modeling

What it should demonstrate: Technical disagreement resolved through hands-on experimentation. I proposed a non-obvious direction, took the strongest objections seriously, tested them directly, and let evidence—not seniority—decide.

Card

CONTEXT. In ImagenTime, we wanted one generative framework that could handle time series ranging from short benchmark sequences to more than 17,000 time steps. After establishing a strong VAE baseline, the conventional next step was to build a stronger native 1D generative model. I proposed a less obvious direction: transform the series into a structured 2D representation and reuse mature image-diffusion machinery.

TENSION. Several collaborators preferred staying in 1D, and their objection was technically strong. Mapping a sequence into 2D expands the representation, increases the cost of every diffusion step, and can make numerical information harder to recover. Their concern was that we might pay substantially more compute just to force a time series into an image architecture.

My hypothesis was that the additional representation cost might be worth it because the transformation would expose useful structure and let us reuse a much stronger and more mature generative stack. But at that point, both positions were hypotheses.

MY ACTION. Rather than argue that the image prior would compensate, I proposed three tests that could kill my own idea early:

1. Reconstruction fidelity: can we recover the original time series accurately enough from the representation?
2. Modeling value: does the representation actually improve generative quality at small scale?
3. Compute: is the quality improvement large enough to justify the expanded representation and additional cost?

I screened candidate representations before committing to expensive diffusion training. Simple line plots were extremely sparse as images. Gramian angular fields had unattractive scaling properties for long sequences, so I dropped those directions. Delay embeddings and STFT-like representations survived the reconstruction tests.

I then built a small proof-of-concept comparison rather than asking us to maintain two complete research stacks. I looked at whether the representation remained faithful, whether the image-space model actually gained quality at small scale, and whether the additional spatial cost was defensible.

The important part was that this was an experiment where my preferred 2D hypothesis could fail cheaply. Only after it survived those tests did we commit to the larger training campaign.

WHY. The real question wasn't "Are images better than sequences?" It was whether the representation exposed enough useful structure, and let us reuse enough mature diffusion machinery, to compensate for its larger footprint.

I wasn't trying to convince the collaborators that 2D was right. I was trying to design an experiment where either their hypothesis or mine could lose cheaply.

RESULT. It didn't fail. The evidence was strong enough that we committed to the image-space route.

What was particularly convincing was that the approach generalized across almost three orders of magnitude in sequence length. The same basic framework handled sequences from 24 to 17,544 time steps. On short-series unconditional generation, we improved the discriminative score over prior diffusion models by about 58% on average. On the long and ultra-long benchmarks, the classification score improved by about 133% on average.

There were also concrete cases where the gains were quite large. For example, on MuJoCo the discriminative error was 0.007 compared with 0.059 for DiffTime. On the 17,544-step Traffic dataset, classification was 0.684 versus 0.630 for LS4, while prediction error was 0.138 versus 0.170.

The work became ImagenTime at NeurIPS 2024.

I keep the scientific claims separate, though. Those results show that the overall image-space approach worked very well across very different sequence lengths. They do not prove that 2D representations are intrinsically superior to every possible 1D model.

REFLECTION. The collaborators' compute objection actually improved the work. It forced me to treat representation size, reconstruction fidelity, and computational cost as first-class technical constraints rather than focusing only on downstream quality. It also caused me to reject some of my own candidate representations before expensive training.

Today I would go one step further and quantify that Pareto tradeoff upfront: reconstruction error, representation size, training FLOPs, sampling cost, and downstream quality before committing the full run.


Spoken (~90 sec)

One technical disagreement that changed how I make architecture decisions happened during ImagenTime.

We were building a generative model for time series ranging from very short sequences to more than seventeen thousand steps. The conventional direction after our VAE baseline was a stronger native 1D model. I proposed something less obvious: map the time series into a structured 2D representation and reuse mature image-diffusion machinery.

Several collaborators pushed back, and I thought their objection was valid. The 2D representation could be much larger, every diffusion step would cost more, and the transformation could make numerical information harder to recover.

So rather than argue that the image prior would compensate, I proposed three tests that could kill my idea early: can we reconstruct the signal faithfully, does it actually improve generative quality at small scale, and is the compute tradeoff acceptable?

I screened the representations first. Line plots were mostly empty pixels. Gramian angular fields scaled poorly to long sequences, so I dropped them. Delay embeddings and STFT-like representations survived the reconstruction checks.

Then I built a small proof of concept rather than having us build two complete stacks. The important thing was that my own 2D hypothesis could fail cheaply.

It didn't. The evidence was strong enough that we committed to the image-space route. What convinced me was that the approach generalized across almost three orders of magnitude in sequence length. The same basic framework handled sequences from 24 to over 17,000 steps. On short-generation benchmarks we improved the discriminative score over prior diffusion models by about 58% on average, and on long and ultra-long benchmarks the classification score improved by about 133%.

That became ImagenTime at NeurIPS.

The lesson wasn't that 2D is universally better than 1D. It was that representation determines which modeling priors become available—and when there's a genuine architecture disagreement, I try to design the cheapest experiment where my own idea can lose.


If they lean in

Keep three technical questions separate:

1. REPRESENTATION
Does the mapping preserve the information needed for the task?

2. GENERATIVE PRIOR
Does putting the signal into that representation expose useful structure or allow the model to exploit machinery that would otherwise be unavailable?

3. END-TO-END EFFICIENCY
Is the resulting quality improvement worth the representation expansion and computational cost?

Do not use a later sampling-efficiency improvement as evidence for the representation hypothesis. Sampling efficiency is primarily question #3.


Follow-ups

What exactly was the disagreement?

Whether the benefits of image-space modeling could justify the representation expansion, additional compute, and potential loss of numerical accessibility compared with staying native in 1D.


What did you personally do?

I proposed the image-space hypothesis, screened the candidate representations, defined the reconstruction/quality/cost tests, and built and analyzed the small proof of concept before we committed to the larger experiments.


Why did collaborators prefer 1D?

It preserved the native structure, avoided representation expansion, and was computationally lower-risk. Their objection was legitimate.


Did you convince them?

I would say the experiment did. My contribution was designing a test where either hypothesis—including mine—could lose before we made the expensive commitment.


Did their disagreement actually change what you did?

Yes. It made reconstruction fidelity, representation size, and compute explicit decision criteria. More importantly, I dropped some of my own candidate representations because they failed those tests.


So were you right and they were wrong?

I wouldn't frame it that way. Their concern identified a real cost that remained in the successful system. What the experiments showed was that, in the regimes we tested, the modeling benefits outweighed that cost.


What evidence made you comfortable scaling it?

It wasn't one final benchmark number. First the representation survived the reconstruction test. Then the small-scale generative experiment showed enough benefit to justify further investment. The final evidence was that essentially the same framework worked from 24 to 17,544 steps and performed strongly across both short and ultra-long benchmarks.


Give me one concrete result.

On MuJoCo, for example, the discriminative error was 0.007 compared with 0.059 for DiffTime. At the other extreme, Traffic has 17,544 time steps, and we achieved classification of 0.684 versus 0.630 for LS4, with prediction error of 0.138 versus 0.170.


Could the gains simply come from architecture or capacity rather than the representation?

Partly, yes. The experiments establish the effectiveness of the overall approach, not that every improvement is causally attributable to the representation itself. A cleaner mechanistic experiment would control representation, architecture capacity, and initialization separately.


Then how do you know the representation mattered?

We have evidence from reconstruction behavior, representation screening, and downstream comparisons, but I distinguish that from a strong causal claim. Today I would run a representation × architecture × initialization factorial experiment if identifying the mechanism itself were the objective.


Why not just build the strongest possible 1D model?

That's the natural counterfactual. We compared against native time-series approaches, but I wouldn't claim we exhausted every possible 1D architecture. The decision we needed to make was whether there was enough evidence to invest in the image-space direction, not whether we had proved a universal superiority theorem.


Why not line plots?

They are intuitive for humans, but they are extremely sparse as images. For this generative formulation, most pixels contain no signal, so they were unattractive from both representation and computational perspectives.


What would have made you abandon the 2D approach?

Poor reconstruction, no small-scale quality advantage, or a compute increase large enough that the end-to-end Pareto point was worse than the native alternative.


What would you do differently today?

I would formalize the Pareto analysis earlier: reconstruction error, representation size, FLOPs, sampling cost, and downstream quality. And if resources allowed, I would run a more controlled representation-versus-architecture study to separate the mechanism from the overall system result.


The strongest sentence

"I wasn't trying to convince them that 2D was right. I was trying to design an experiment where either their hypothesis or mine could lose cheaply."


Do not

- Say "my students disagreed with me."
- Say "I set the research vision and convinced them."
- Say "2D is better than 1D."
- Say the representation preserves all information.
- Treat the final paper result as proof that the original mechanistic explanation was correct.
- Claim that every gain came specifically from the representation.
- Make the story primarily about leadership or resource allocation.

IC framing

"I proposed a non-obvious technical direction, personally tested the strongest objections, dropped parts of my own proposal that failed, and only scaled the idea after a cheap experiment showed that the tradeoff was worth pursuing."

---

2. Wrong hypothesis — delay-only numerical collapse

What it should demonstrate: Scientific maturity. Updating a research hypothesis that was motivated by your own previous success rather than defending it after the evidence changed.

Card

CONTEXT. ImagenTime had given me strong evidence that delay embeddings are useful representations for time-series generation. When I moved to multimodal reasoning, I hypothesized that the same representation would transfer more broadly—that a delay-based tower could expose both dynamical structure and enough numerical information for an LLM to reason about amplitude and values.

TENSION. This mattered architecturally. If delay alone captured both, the chart tower was unnecessary complexity. But there was a scientific risk in my reasoning: I was taking an inductive bias validated for generation and assuming it would transfer to a very different objective—numerical question answering.

MY ACTION. I turned that assumption into a matched representation bakeoff: delay-only, chart-only, and dual, with the same data and evaluation protocol. The numerical slice was deliberately useful because it could falsify the strongest version of my hypothesis. When delay failed badly, I did not try to explain away the result or discard the representation entirely. I narrowed the hypothesis and asked where its information was actually useful, then examined task-level failure modes and representation/encoder controls.

WHY. Representation quality is task-conditional. A representation can preserve structure that is excellent for generative modeling while making another property—such as absolute scale—difficult for a pretrained model to recover. The relevant question became not “Is delay a good representation?” but “Which information does each representation make accessible to this model for this task?”

RESULT. On ChatTS numerical reasoning, delay-only was roughly 0.17, chart-only roughly 0.71, and dual roughly 0.79. So the strong version of my hypothesis was clearly wrong: delay was not functioning as a general numerical interface. At the same time, delay remained useful on tasks where dynamical/topological structure mattered, including anomaly and causality slices on TSExam. We also found that simply adapting the native Qwen vision encoder was insufficient for the delay representation: qwendelay was about 0.60 versus 0.83 with DINO. Taken together, the results are consistent with complementary representations, but I would not claim that dual > chart alone proves complementarity.

REFLECTION. The mistake was not using delay embeddings. It was generalizing too aggressively from one objective to another. Today I would formulate the hypothesis from the beginning as task-conditional and design the falsifying slices earlier: absolute-value questions for numerical accessibility, and anomaly/dynamics tasks for structural information. More broadly, a representation that succeeds on one objective becomes a hypothesis—not a prior fact—when the objective changes.

Spoken (~90s)

One hypothesis I got wrong came directly from my own previous success.

In ImagenTime, delay embeddings worked very well as a representation for time-series generation. When I moved to multimodal reasoning, I generalized that result too aggressively. I expected a delay-based tower to expose not only dynamical structure but also enough numerical information for the language model to answer questions about values and amplitudes.

That mattered architecturally. If delay could do both, adding a chart representation was probably unnecessary complexity.

So rather than keep reasoning from ImagenTime, I set up a matched representation bakeoff: delay-only, chart-only, and dual, with the same data and evaluation protocol. Numerical reasoning was a particularly useful falsifier because the hypothesis made a very clear prediction there.

And it failed badly. On ChatTS numerical questions, delay-only was around 0.17, compared with roughly 0.71 for chart-only and 0.79 for dual.

At that point I changed the hypothesis rather than trying to rescue it. The useful question wasn’t “Is delay a good time-series representation?” It was “What information does this representation make accessible for this objective?” Delay remained useful on slices involving dynamical or topological structure, such as anomaly and causality, while the chart representation made scale, amplitude, and trend much more accessible.

We also found an encoder interaction: simply adapting Qwen’s native vision encoder to delay representations was substantially weaker than using DINO—about 0.60 versus 0.83. So representation and pretrained encoder prior weren’t separable in the simplistic way I initially imagined.

The lesson I took is that an inductive bias validated on one objective doesn’t automatically transfer to another. A successful representation becomes a new hypothesis when the task changes. Today I’d design the task-specific falsifiers much earlier.

If they lean in

Keep three claims separate:

1. Delay-only is poor for numerical QA in our setting.
    Strongly supported by the bakeoff.
2. Delay preserves/exposes information useful for dynamics/topology.
    Supported by its behavior on relevant task slices.
3. Delay and chart are genuinely complementary.
    Dual > chart is evidence consistent with this, but not sufficient by itself to establish the mechanism.

A stronger complementarity experiment would intervene on each representation and evaluate tasks constructed to require information uniquely accessible from each view, ideally with capacity/token-budget controls.

Also separate representation from encoder prior: the Qwen-vs-DINO result says the encoder matters substantially; it does not prove that one representation is intrinsically superior.

Follow-ups

They ask	You say
What exactly did you get wrong?	I generalized an inductive bias from generation to numerical reasoning. Delay was useful, but not as a general-purpose numerical interface to the LLM.
What evidence changed your mind?	The cleanest falsifier was ChatTS numerical: roughly 0.17 delay-only versus 0.71 chart-only. That gap was too large to explain away as noise.
Why keep delay after that?	Because the failure was task-specific rather than universal. It remained useful on tasks emphasizing dynamical/topological structure, and dual improved over chart alone. That justified investigating complementarity rather than simply deleting it.
Does 0.79 vs 0.71 prove complementarity?	No. It establishes an empirical gain from the combined system. Complementarity is an interpretation supported by the different slice behavior; a stronger causal test would control capacity and intervene on each representation.
Couldn’t dual simply win because it has more tokens or capacity?	Yes—that is an alternative explanation that the basic ablation doesn’t completely eliminate. I would capacity/token-match the control and then use representation shuffling or corruption on tasks where each view should matter.
Why didn’t you see this earlier?	I had evidence that delay was effective for generation and let that prior become too strong. I should have asked earlier which properties the new objective required the representation to expose.
What does the Qwen-vs-DINO experiment tell you?	That representation and encoder prior interact. A representation being information-rich does not mean an arbitrary pretrained encoder can readily extract that information.
Could a better delay encoder eventually match the chart?	Absolutely. Our result is about accessibility under the tested architecture and training regime, not an information-theoretic statement that delay cannot encode numerical values.
What’s the general lesson?	Representation quality isn’t absolute. I now ask: what information is preserved, what information is readily accessible to the chosen encoder, and what information does the downstream objective actually require?
How would this affect a new sensor problem?	I wouldn’t assume either charts or delay embeddings transfer. I’d define the information the task requires, propose several encodings, and run an early representation bakeoff before committing the larger model.

Do not

Say “delay doesn’t contain numerical information.” It may contain it; the model failed to access/use it effectively.

Say “dual proves complementarity.” Say the evidence is consistent with complementary failure modes.

Say “DINO proves delay is better.” The experiment shows an important representation × encoder interaction.

Say “ImagenTime proved delay is the right TS representation.”

Say images preserve all information.

Use the synthetic-TR kill story here.

Senior-IC framing:
“I let a successful result from my previous work become too strong a prior. When a task-specific falsifier contradicted it, I narrowed the claim, investigated where the representation was actually useful, and changed the architectural interpretation rather than defending the original hypothesis.”

---

3. Technical ownership under ambiguity — TSRBench reasoning audit

What it should demonstrate: Taking an ambiguous model failure and turning it into a concrete technical diagnosis and experiment sequence. Hands-on error analysis before scaling.

Card

CONTEXT. After the first synthetic reasoning mix failed its temporal-relations gate, reasoning was still the weakest part of TSRBench. We knew that simply adding plausible synthetic data could move the average while hurting the capability we were actually targeting.

TENSION. The failure was ambiguous. There were several technically plausible explanations: insufficient coverage of reusable temporal operations, compositions that were too deep, unfamiliar benchmark formats, missing domain knowledge, or even a representation limitation. Those explanations require different fixes. Another large training run without distinguishing them would tell us very little even if the score moved.

MY ACTION. I went back to the benchmark itself and audited the reasoning failures item by item. For each one, I looked at what operation the question required, whether that operation or format appeared in our training distribution, and whether the model appeared to have parsed the relevant time-series information correctly.

That gave me three useful working categories:

1. Knowledge gap: the task requires domain information the model does not have—for example specialized seismology concepts.
2. Operator/composition gap: the relevant primitives are present, but the model fails when it has to combine them into a longer reasoning chain.
3. Format gap: the underlying operation is within scope, but the benchmark expresses it through notation or conventions absent from training.

I then mapped those categories back to training interventions. Rather than mix everything together again, I generated targeted examples for the operator/composition and format gaps and used the 0.8B model as a fast experimental probe before repeating the experiment at 8B.

I also changed my evaluation from reasoning-average-only to failure-type and task-level readouts, including distinctions such as missing operation versus correctly parsed input followed by incorrect reasoning.

WHY. I wanted the next experiment to answer a diagnostic question, not just produce another score. If targeted operator data improved the failures I had classified as operator gaps but not the knowledge cases, that would support the diagnosis. If the predicted slices did not move, I would revise the taxonomy rather than immediately scale the intervention.

RESULT. On the first controlled 0.8B experiment, TSRBench overall moved from roughly 0.382 to 0.405, and reasoning from 0.245 to 0.255. I would not treat those aggregate gains as the main result. More useful was that several errors associated with missing operation coverage improved, while a residual class remained where the model appeared to parse the item correctly but still failed the reasoning.

That gave us a more specific next experiment and enough evidence to test the targeted recipe at 8B rather than use the large model for exploratory search.

REFLECTION. I should have done the item-level audit before generating the original synthetic mix. The benchmark already contained evidence that “reasoning” was not one failure mode. I spent compute learning something that careful error analysis could have exposed earlier. Now, when a heterogeneous benchmark stalls, I try to inspect failures first, formulate competing explanations, and make the next training run discriminate between them.

Spoken (~90s)

After I killed the first synthetic reasoning mix, the harder question was why reasoning was still weak.

There were several plausible explanations. Maybe we did not have enough examples of the temporal operations. Maybe the model knew the primitives but failed on longer compositions. Maybe it lacked domain knowledge. Maybe some benchmark formats were simply unfamiliar. Or maybe the representation itself was still limiting us.

Rather than generate another mixture, I went back to the benchmark and audited the failures item by item.

For each question, I looked at what operation it required, whether that operation and format existed in our training data, and whether the model appeared to have parsed the relevant time-series information correctly.

That separated the failures into three useful regimes. Some were knowledge gaps, like specialized domain concepts I wouldn’t expect a 0.8B model to infer from a few plots. Some were operator-depth failures: the primitives were familiar, but the model broke when it had to compose them. And some were format failures: the reasoning itself was within scope, but the notation or convention was absent from training.

I then turned those diagnoses into targeted training interventions rather than mixing them together. I used the 0.8B model as a fast probe and changed the evaluation so I could see whether the specific failure class I was targeting actually moved.

The first controlled run moved overall TSRBench from about 0.382 to 0.405 and reasoning from 0.245 to 0.255. But the more useful result was qualitative: several missing-operation failures improved, while another class remained where the model seemed to parse the input correctly but still reasoned incorrectly.

That made the next experiment much more specific.

What I learned is that when a benchmark stalls, I shouldn’t immediately ask “what should I train next?” I should first ask “what different failures are hiding inside this average, and what experiment would distinguish them?”

If they lean in

The story is a diagnostic loop:

failure → inspect examples → competing explanations → targeted intervention → predicted slice movement → revise or scale

The taxonomy is a working hypothesis, not ground truth.

The 0.8B model is a screening instrument, not evidence that 8B must behave identically.

Keep these failure types distinct:

Knowledge gap
The necessary external/domain information is absent.

Operator/composition gap
The ingredients are available, but the reasoning procedure fails.

Format gap
The capability may exist, but the input convention does not expose it in a familiar way.

Follow-ups

They ask	You say
What did you personally do?	I audited the benchmark failures, compared them with our training distribution, built the working taxonomy, designed the targeted interventions, and ran/analyzed the 0.8B screening experiments.
Why not just generate more reasoning data?	Because the previous experiment showed that more plausible data could improve the average while hurting the target capability. I wanted to know which failure I was treating before generating more.
Why not just scale to 8B?	Scaling would make the experiment more expensive without resolving the ambiguity. I used 0.8B to test whether an intervention moved the predicted failure class before repeating it at scale.
How did you know something was a format failure rather than reasoning?	I looked for cases where the underlying operation was represented in training and the model could handle analogous questions, but failed when the same operation appeared through an unfamiliar convention or notation.
How did you distinguish perception from reasoning?	Where possible, I checked whether the model correctly identified the relevant series structure or intermediate quantities before the final reasoning step. If it could parse the evidence but still produced the wrong relation, that pointed downstream of representation.
Could your taxonomy be wrong?	Absolutely. It was a hypothesis about the errors. That’s why I tied each category to an intervention with a predicted effect. If the intended slice didn’t move, I would revise the diagnosis.
Why 0.8B?	Fast iteration. I was testing whether the intervention had the expected directional effect, not trying to establish the final model quality.
What did the +2.3 points establish?	Very little mechanistically by itself. The useful evidence was which error classes moved. The aggregate gain told me the intervention wasn’t obviously destructive; the slice behavior told me whether my diagnosis had predictive value.
Why defer domain knowledge?	It was a qualitatively different intervention. I first wanted to test failures we could directly connect to missing operators or formats rather than mix broad knowledge augmentation into the same experiment.
What happened next?	The targeted small-model result justified testing the recipe at 8B. I would keep the 8B result separate until it is complete.
What would you do differently?	Audit first. I would sample and classify benchmark failures before designing the first synthetic-data generator.

If they ask where the leadership is

Don’t force it into a management story:

“For me the ownership was technical. We had several plausible directions, and rather than choose one based on intuition, I went into the failures myself, turned the explanations into testable interventions, and gave us a much cleaner basis for the next large experiment.”

If there was no interpersonal disagreement, say so. The ambiguity itself is enough.

Do not

Say “I allocated the 8B budget.”

Say “I aligned the team around my taxonomy.”

Say the taxonomy was objectively correct.

Say 0.8B predicts 8B.

Claim the representation was ruled out unless you actually established that.

Make 0.382 → 0.405 the success of the story.

Retell the TR kill. One sentence of context is enough.

IC framing

“After a failed intervention, I went into the benchmark myself, decomposed the aggregate failure into testable hypotheses, built targeted interventions, and used a cheap model to determine which diagnosis deserved a larger experiment.”

---

4. Kill decision — synthetic TR mix

What it should demonstrate: Senior-IC judgment under sunk cost. Pre-committed decision criteria. Protecting the hypothesis from being redefined by a favorable aggregate metric.

This is probably the strongest card. Vincent already expects it.

Card

CONTEXT. On TSRBench, overall performance had plateaued around 46%, while reasoning remained much weaker, around 29%. I chose temporal relations as a targeted intervention because the failure looked decomposable into teachable operations: segmentation, ordering, and multi-hop composition. I built a tiered synthetic training mix specifically around those operations.

TENSION. The expensive 8B run produced a result that was easy to misread. Aggregate reasoning improved from roughly 29.5% to 31.2%, and two other reasoning tasks gained about 7 points each. The compute was already spent, several metrics looked better, and the natural temptation was to call the experiment promising and scale the same recipe.

MY ACTION. Before launching the run, I had written promotion gates tied to the risks I cared about: no more than −3 pp overall and no more than −5 pp on any reasoning subtask. I also changed the evaluation readout so every reasoning task appeared explicitly rather than being hidden inside an average. The result that mattered was immediate: temporal relations—the task the synthetic data was designed to improve—fell from 26.9% to 21.9%, exactly −5.0 pp. Numeric reasoning also fell 3.4 pp. I recommended that we kill that training mix and stop spending compute on that direction.

WHY. The experiment was testing a specific hypothesis: this synthetic curriculum improves temporal-relation reasoning without materially damaging the rest of the system. Once the target task regressed substantially, gains elsewhere could not be used to redefine success after the fact. They might reflect redistribution of capacity or training-distribution shift, but they did not validate the hypothesis we had actually tested.

RESULT. We did not promote the mix. More importantly, the failure changed how I ran the next reasoning experiments: aggregate reasoning, overall score, and every reasoning slice became first-class promotion criteria. Temporal relations remained an open research problem; what we killed was the lever, not the objective. That directly led to the item-level reasoning audit in the next story.

REFLECTION. I would make one change upstream: perform the failure taxonomy before generating the first synthetic curriculum. The decision gate did exactly what it was supposed to do; the avoidable mistake was spending compute before we had decomposed the benchmark carefully enough. I still use predeclared slice-level floors when optimizing heterogeneous systems because aggregate metrics are especially dangerous when an intervention is targeted.

Spoken (~90s)

This is a case where the aggregate metric told us to keep going, but the experiment we had actually designed told us to stop.

On TSRBench, overall performance had plateaued around forty-six percent, and reasoning was much weaker, around twenty-nine. I picked temporal relations as the first targeted intervention because the failures looked teachable: segment the series, order events, then compose those operations into multi-hop questions. We built a tiered synthetic curriculum around exactly that.

Before launching the expensive run, I wrote the promotion criteria down. No more than a three-point regression overall, and no more than a five-point regression on any reasoning subtask. I also required the readout to show every reasoning task individually, because I did not want an average to hide a localized failure.

The 8B result was actually quite tempting. Reasoning average moved from about 29.5 to 31.2, and two other reasoning tasks improved by roughly seven points. After spending the GPU budget, that is exactly the kind of result you can rationalize into “let’s scale it further.”

But temporal relations—the task the data was specifically designed to improve—went from 26.9 to 21.9. Minus five points. Numeric reasoning also regressed.

So I recommended killing that mix.

The important part for me was that I did not let the favorable aggregate result redefine the hypothesis after seeing the data. The experiment was supposed to improve temporal relations without damaging the rest of the system, and it failed that test. The other gains might have been useful signals, but they belonged to a different hypothesis.

We stopped that recipe and moved to an item-level reasoning audit to understand the failure modes before generating more data.

What I would change today is upstream, not the kill decision: I would do the taxonomy before the first synthetic run. The predeclared gates worked exactly as intended.

If they lean in

Keep three decisions separate:

1. Was the run interesting? Yes. It changed several behaviors.
2. Did it validate the intended hypothesis? No. The target task regressed materially.
3. Should the entire research direction be abandoned? No. Kill the intervention, not the objective.

The senior-IC point is not “I was strict about metrics.”

It is:

I defined the decision rule before seeing the result, so sunk cost and attractive secondary metrics could not silently change what counted as success.

Follow-ups

They ask	You say
Why kill it if reasoning average improved?	Because the intervention targeted temporal relations, and temporal relations regressed from 26.9 to 21.9. The average improvement was scientifically interesting, but it did not validate the hypothesis we had tested.
Could the gains on the other tasks still make the mix useful?	Potentially, but that would be a new experiment. I would isolate the components responsible for those gains rather than promote a mixture that materially damaged its intended target.
Who wanted to keep it?	There wasn’t necessarily a person arguing aggressively for promotion; the result itself created that pressure. After an expensive run, positive averages and seven-point gains make continuation very easy to rationalize. The predeclared gate removed that discretion.
Why were the gates set at −3 and −5?	They were large relative to the improvements we were trying to earn and to the baseline level of those tasks. A five-point drop on a task in the mid-twenties is not noise I was willing to trade away for a modest average gain.
How do you know −5 wasn’t noise?	I would distinguish the promotion decision from a statistical-mechanism claim. The gate was a risk-control criterion: a regression that large was enough to prevent automatic promotion. If we wanted to understand whether it was systematic, that justified a targeted follow-up rather than another large run.
Why not just reduce the synthetic-data weight?	That’s a reasonable next experiment, but it would be a new hypothesis: that the direction is useful but the mixture coefficient is wrong. I did not want to continue scaling the original recipe after it failed its own gate.
Why not train longer?	Same issue. More compute does not repair a failed causal interpretation. First I wanted to know whether we had the wrong mixture, wrong task decomposition, or wrong data generator.
What did you personally own?	I defined the intervention, ran the small-model experiments, set the promotion gates, structured the per-task evaluation, and made the promote/kill recommendation. A collaborator reproduced the recipe at 8B.
How did you get buy-in?	The criteria were agreed before we had the result, and the per-task readout made the regression explicit. I did not need to argue that my interpretation was preferable after the fact.
What happened next?	I stopped treating “reasoning” as one failure mode and audited the benchmark item by item. That produced the operator-depth / format / domain-knowledge decomposition.
Was the synthetic-data idea itself wrong?	No. The specific curriculum and mixture were wrong for the target we had defined. Some of the positive secondary movement suggested synthetic data could still be useful if designed against a better failure taxonomy.
What would you do differently?	Error taxonomy first, generation second. The kill criterion worked; the expensive part was learning too late what categories of failure the benchmark actually contained.

Do not

Say “the average was misleading, so averages are bad.” Aggregate metrics are useful; they are just insufficient for targeted interventions.

Say “TR dropped, therefore the synthetic data caused distribution shift.” Distribution shift is a plausible explanation, not established fact.

Say “I killed synthetic data.” You killed that mix/recipe.

Turn this into a generic “ownership” story.

Present the thresholds as universal statistical truths. They were predeclared engineering/research risk criteria.

Retell the delay-only failure here.

Senior-IC framing:
“I defined success before seeing the expensive result. When the aggregate metric improved but the targeted capability crossed the predeclared failure floor, I refused to redefine the experiment post hoc, killed the intervention, and used the failure to redesign the next scientific question.”

---

5. Cross-functional collaboration — Bosch Haifa / real-world modality translation

WHAT THIS SHOULD DEMONSTRATE
Cross-functional collaboration across different technical expertise. I brought the
generative-modeling perspective; Bosch brought deep knowledge of the sensor system
and its real-world failure modes. I listened when their evidence challenged my
modeling assumptions, translated their operational constraints into an ML problem,
and worked with them toward a solution neither side would have reached independently.


CARD

CONTEXT.
I had an ongoing research collaboration with the Bosch Center for AI in Haifa around
modality translation: given observations in one modality, generate the corresponding
signal in another modality.

I was responsible for much of the generative-modeling side. We developed a latent
diffusion bridge framework with modality-specific representations and a shared
generative translation mechanism. On standard research benchmarks, the approach
worked very well.

The Bosch researchers had a different kind of expertise. They understood the actual
sensor systems, how the measurements were collected, and the failure modes that
appear in industrial data.


TENSION.
When we moved from the clean research benchmarks to Bosch's real sensor data,
performance degraded substantially.

My initial instinct was to view this mainly as a model-generalization problem:
perhaps we needed a stronger model, different regularization, or better training.

But discussions with the Bosch researchers changed that diagnosis.

They helped us understand that the real data violated assumptions that were almost
invisible in the benchmarks. Measurements could be irregularly sampled, noisy,
partially observed, and only imperfectly aligned across modalities.

That meant our abstraction itself was incomplete.

We had been thinking approximately:

    clean modality A -> modality B

whereas the actual problem was closer to:

    partial + noisy + irregular observations of A
                    ->
             useful estimate of B

That distinction changed what I thought we needed to solve.


MY ACTION.
I worked with the Bosch researchers to translate what they were observing in the
sensor pipeline into concrete modeling assumptions.

Rather than treating "the Bosch data is harder" as one generic domain-shift problem,
I tried to separate the sources of mismatch:

- irregular sampling,
- missing observations,
- measurement noise,
- and imperfect temporal correspondence.

On my side, I connected those constraints to our work on generative modeling of
irregular, noisy, and partially observed time series.

The important technical shift was that I stopped treating preprocessing as something
that should simply clean the industrial data until it looked like the benchmark.

For example, forcing irregular observations onto a clean regular grid can hide the
fact that some measurements were never observed and can create artificial temporal
precision.

Instead, we adapted the modeling formulation so that the observation process itself
was part of the problem: what was observed, when it was observed, and what information
was actually missing.

Throughout this process, I kept going back to the Bosch researchers with a concrete
translation:

    "If this is what the sensor is doing, then this is the assumption our model is
     currently making, and this is the experiment that should tell us whether that
     mismatch matters."

That gave us a shared technical language despite coming from different sides of the
problem.


WHY.
The key realization was that neither group had the complete diagnosis independently.

I understood the generative model and knew which assumptions it relied on.

The Bosch researchers understood the physical data-generation and measurement
process much better than I did.

If I had treated their observations merely as noisy data that needed preprocessing,
I would have optimized the wrong abstraction.

And if we had only described the sensor problems operationally, without translating
them into model assumptions, it would have been difficult to know what to change.

The collaboration worked because we connected those two views.


RESULT.
The robustness extensions substantially improved performance in the Bosch setting,
and the approach became a strong internal research baseline for subsequent work.

The collaboration also influenced my broader research direction. It helped motivate
work on modality translation and on generative modeling when time-series observations
are irregular, noisy, or incomplete.

I am careful about how I describe the impact: this was a research collaboration, so
I would not claim a Bosch product deployment that I did not observe. The concrete
impact I can defend is that we turned a method that looked strong on clean benchmarks
but struggled on their real data into a substantially more useful approach for their
setting.


REFLECTION.
The biggest thing I took from that collaboration is that benchmark generalization and
deployment generalization are different claims.

It also changed how I work with domain experts.

When someone who understands the data-generating process tells me that a model is
failing in a particular way, I don't treat that as an implementation detail outside
the ML problem. I try to translate it into:

    What assumption is my model making?
    Which real-world constraint violates it?
    What experiment would distinguish that explanation?

For me, that is the value of cross-functional work: not simply dividing tasks between
people with different expertise, but allowing expertise from another function to
change the technical problem I think I am solving.


======================================================================
SPOKEN VERSION — ~90 SECONDS
======================================================================

"One of my best examples of cross-functional collaboration is a long-running project
with researchers at the Bosch Center for AI in Haifa.

We were working on modality translation: generating one sensor modality from another.
I brought much of the generative-modeling perspective, and we developed a latent
diffusion approach that performed very well on standard research benchmarks. The
Bosch researchers, though, understood the actual sensor systems and industrial data
far better than I did.

When we moved to their real data, performance degraded substantially. My initial
instinct was to think of it as a model-generalization problem. But working through the
failures with Bosch changed my diagnosis. Their data violated assumptions that were
almost invisible in our benchmarks: sampling was irregular, measurements could be
missing or noisy, and modalities weren't always perfectly synchronized.

So I reformulated the problem. Instead of asking how to make their data look like our
clean benchmark, I started treating the observation process itself as part of the
modeling problem. I connected what Bosch was seeing to our work on irregular and
partially observed time series, and we translated each operational issue into a
modeling assumption and a testable intervention.

That substantially improved the approach on the Bosch setting and made it a strong
internal research baseline for subsequent work.

The part I value most is that neither side could have reached the same diagnosis
alone. I understood the model assumptions; Bosch understood what the sensors were
actually doing. The solution came from translating between those two views.

That experience changed how I approach cross-functional work. Domain expertise isn't
something I collect after designing the model. I want it early enough that it can
change the problem I think I'm solving."


======================================================================
IF THEY ASK: "WHAT DID YOU PERSONALLY DO?"
======================================================================

"My contribution was primarily on the modeling side. I helped design the generative
translation framework, and when it struggled on the Bosch data, I worked directly
through the mismatch between the assumptions in our model and the properties Bosch
was seeing in the sensor pipeline.

The important part wasn't simply tuning the model. I translated issues like irregular
sampling, missing observations, noise, and imperfect alignment into changes in the
generative formulation and into experiments we could use to test those explanations."


======================================================================
IF THEY ASK: "WHAT DID BOSCH CONTRIBUTE THAT YOU COULDN'T?"
======================================================================

"They had knowledge I simply didn't have: how the sensors and data-collection process
behaved in practice.

Looking only at the ML benchmark, I could see that performance had degraded. They
could explain why certain assumptions behind the benchmark didn't correspond to the
real measurement process.

That distinction mattered because otherwise I might have spent time increasing model
capacity or tuning optimization when the more fundamental problem was that our
observation model was wrong."


======================================================================
IF THEY ASK: "WHAT WAS DIFFICULT ABOUT THE CROSS-FUNCTIONAL PART?"
======================================================================

"The difficulty was that initially we described the same failure at different levels.

From my side, I was thinking in terms of distribution shift, representation, and
generative-model assumptions. From their side, the issues were concrete properties
of the sensor pipeline: this measurement arrives irregularly, this channel can
disappear, these two signals aren't actually synchronized as cleanly as the benchmark
assumes.

The useful step was translating between those descriptions. Once we could say,
'This sensor behavior violates this particular modeling assumption,' we could design
an experiment rather than just discuss the failure qualitatively."


======================================================================
IF THEY ASK: "WAS THERE A DISAGREEMENT?"
======================================================================

"I wouldn't characterize it as a major interpersonal disagreement. It was more an
initial difference in diagnosis.

My first instinct was to approach the degradation as a modeling/generalization
problem. Their knowledge of the sensor system made it clear that some of the problem
was more fundamental: the clean observation assumptions in our research setup did
not hold.

The important thing was that I changed my technical view based on their evidence
rather than trying to force the real data into the abstraction I had started with."


======================================================================
IF THEY ASK: "HOW DID YOU BUILD TRUST WITH THE OTHER GROUP?"
======================================================================

"I think the most useful thing was not pretending to know their domain better than
they did.

When they described a sensor issue, my job wasn't to immediately prescribe an ML
solution. I tried to understand the constraint precisely and then translate it back
into the assumptions of our model.

And in the other direction, I tried to make our modeling choices concrete enough
that they could challenge them. That created a much better loop than each group
working independently and exchanging results at the end."


======================================================================
IF THEY ASK: "WHAT WOULD YOU DO DIFFERENTLY?"
======================================================================

"I would involve the real observation process earlier.

We initially had strong benchmark results before fully stress-testing assumptions
like missingness, irregular sampling, noise, and imperfect alignment.

Today, especially for sensor or health data, I would define those deployment
conditions alongside the benchmark from the beginning and make them part of the
evaluation matrix.

That would expose assumption failures much earlier."


======================================================================
IF THEY ASK: "WHAT WAS THE IMPACT?"
======================================================================

"The robustness work substantially improved the approach in the Bosch setting, and
the resulting method became a strong internal research baseline for subsequent work.

I wouldn't claim downstream product impact that I didn't directly observe. The impact
I can defend is that Bosch brought us a real-data failure that our benchmark did not
capture, and together we turned that failure into a better modeling formulation and
a substantially stronger approach for their setting."


======================================================================
ONE-LINE L5 CROSS-FUNCTIONAL TAKEAWAY
======================================================================

"The strongest cross-functional collaborations I've had are not ones where different
groups simply divide the work. They're ones where another group's expertise changes
my technical understanding of the problem."

---

## 90-second cheat strip (memory only)

| # | One line |
|---|----------|
| 1 | 2D cost objection → invertibility + small POC → +58% / +132%; they bought the evidence |
| 2 | Delay should carry numbers → ChatTS 0.17 vs 0.71 vs 0.79 → delay is dynamics, not scale |
| 3 | After the kill, fog → three regimes → formats before domain; +2.3 pp 0.8B, 8B WIP |
| 4 | Average + AR/IR up; TR 26.9→21.9; pre-declared −5 pp; killed |
| 5 | Haifa, not Sunnyvale; latent bridge + contrastive/predictive; NeurIPS 2025; no ship claim |
| A | Ravel killed delay geometry → invariant + they own the test |
| B | NeurIPS: cut full 1D stack; screen then one 2D POC |

Practice: read each spoken block aloud once. Vincent mock: 1 or 4 first; keep 3 as the sequel to 4 if they ask “what happened after.” Sunday 9/6: speak A and B once (60s). Do not polish them into fifth and sixth 90s cards.

---

## Backup A — 60s — helping someone succeed (not a student-supervision story)

Use if asked: “Tell me about helping a colleague grow” / “coaching” / “mentorship.”  
**Hard rule:** do **not** open with PI, lab, or “my student.” The plot is a **technical block** you identified, a method you changed, ownership you left with them, and a result they produced.

**CONTEXT.** On the multimodal VLM stack, a collaborator was debugging why delay-embedding features looked wrong on multivariate series. Their loader flattened a `[C, T]` array into one long univariate. Delay geometry became garbage; dual-tower numbers on those tasks were noise.

**TENSION.** The obvious move was for me to take the collator and “just fix it.” That would have been faster for the next run and would have taught them nothing about the invariant.

**ACTION.** I showed the failure with one example: ravel concatenates channels in time, so the delay image is not a trajectory in R^C. I wrote the invariant we needed — *N series → N markers → N chart + N delay, channels stay channels* — and asked them to own the loader patch and a unit test that fails on ravel. I did not merge a silent fix.

**RESULT.** They landed the collator test. Multivariate delay stopped being a hidden confound. Later bakeoffs on those tasks became interpretable.

**REFLECTION.** Helping was changing the representation contract and giving them the test, not taking the file.

If they push “were they your student?”: *They were a collaborator on the codebase. The same move would apply to anyone stuck on a silent data bug. I do not treat this as management.*

---

## Backup B — 60s — deadline / execution under pressure

Use if asked: “difficult deadline” / “too much to do” / “how do you cut scope.”

**CONTEXT.** ImagenTime, NeurIPS cycle. We wanted one generative framework from short series to 17k steps. The conventional path was a stronger native 1D diffusion stack *and* the 2D image-space bet. There was not time or compute to do both at full fidelity.

**TENSION.** Shipping two incomplete stacks would have produced two weak papers’ worth of evidence and no discriminating comparison. The quality bar I cared about was: can we recover the series, and does 2D win at small scale?

**ACTION.** I cut the full 1D diffusion campaign. I kept a VAE baseline, a cheap representation screen (line plots and GAF died; delay/STFT-like survived invertibility), and one small 2D proof-of-concept. Full training only after those gates.

**RESULT.** The 2D path survived and became the paper. We did not get a polished 1D SOTA in that cycle. That was the cut.

**REFLECTION.** The deadline was met by **killing work that could not falsify the bet**, not by working longer on everything. If I redid it, I would pre-declare the screen as a kill criterion in writing even earlier.

Do not merge this with card 1. Card 1 is the disagreement. This card is **what you did not build** so the deadline held.

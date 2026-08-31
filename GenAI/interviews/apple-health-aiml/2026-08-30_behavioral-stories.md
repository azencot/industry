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
| **Vincent** | 1, 3, 4 (leadership = discriminating experiment + kill) |
| **Jonathan** | 2, 4 (claim vs evidence) |
| **Haraldur** | 4, 5 (slice gates; messy sensors; don’t assume DL) |
| **Yujie** | 2 (encoding bakeoff) |
| **Chung-Cheng** | usually none — stay on infra |

---

1. Technical disagreement — ImagenTime, native 1D vs image-space modeling

What it should demonstrate: Senior-IC influence without authority. Taking a legitimate technical disagreement and converting it into a decision process in which either hypothesis could lose.

Card

CONTEXT. In ImagenTime, we wanted one generative framework that could handle time series ranging from short benchmark sequences to roughly 17,000 time steps. After establishing a strong VAE baseline, the conventional next step was to build a stronger native 1D generative model. I proposed a less obvious direction: transform the series into a structured 2D representation and reuse mature image-diffusion machinery.

TENSION. Several collaborators preferred staying in 1D, and their objection was technically strong. Mapping a sequence into 2D expands the representation, increases the cost of every diffusion step, and can distort or discard numerical information. From their perspective, we risked paying substantially more compute just to force a time series into an image architecture. My argument was that the additional representation cost might be amortized by access to a much stronger, reusable vision-diffusion prior—but at that point both positions were hypotheses.

MY ACTION. Rather than push the 2D direction because it was my research idea, I turned the disagreement into three decision gates:

1. Information: can we reconstruct the original series accurately enough from the representation?
2. Modeling value: at small scale, does the representation actually improve generative quality relative to native alternatives?
3. Cost: is the end-to-end quality/compute tradeoff good enough to justify the larger representation?

That immediately changed my own proposal. I screened several image representations before committing to expensive diffusion training. Simple line plots were extremely sparse. Gramian angular fields had unattractive scaling properties. I dropped those directions. Delay embeddings and STFT-like representations survived the information/reconstruction gate.

Then, instead of building two full research stacks, I proposed a small matched POC where the 2D hypothesis could fail cheaply. Only after that evidence favored the image-space direction did we commit the larger training campaign. We also reused established vision-diffusion components rather than building a bespoke 2D system around the hypothesis.

WHY. The disagreement was not really “Are images better than sequences?” It was a Pareto question: does the representation expose enough useful structure, and let us reuse enough mature generative machinery, to compensate for its additional cost? I wanted an experiment where my preferred direction could lose before we invested heavily in it.

RESULT. The POC gave the group enough evidence to converge on the image-space direction. The final framework handled sequences from roughly 24 to 17,000 time steps in a common modeling approach. On the short-series discriminative evaluation we saw roughly 58% improvement relative to the time-series diffusion comparison, and on the ultra-long classification evaluation roughly 132%. Later, moving to EDM reduced sampling from around 1,000 model evaluations to about 35. The work became ImagenTime, NeurIPS 2024.

I would keep the claims separate: those results establish that the overall approach worked well; they do not prove that 2D representations are intrinsically superior to 1D models. EDM addressed sampling efficiency and should not be treated as evidence for the representation hypothesis.

REFLECTION. The collaborators’ compute objection was useful—it made the eventual work stronger because it forced me to treat representation size and reconstruction quality as first-class constraints rather than only looking at downstream accuracy. Today I would go further and define the Pareto analysis upfront: reconstruction error, representation size, training FLOPs, sampling cost, and downstream quality before committing the full run.

Spoken (~90s)

One technical disagreement that changed how I make architecture decisions happened during ImagenTime.

We were building a generative model for time series ranging from short sequences to around seventeen thousand steps. The conventional direction after our VAE baseline was a stronger native 1D model. I proposed something less obvious: map the time series into a structured 2D representation and reuse mature image-diffusion machinery.

Several collaborators pushed back, for good reasons. A 2D representation can be much larger, every diffusion step becomes more expensive, and the transformation can make numerical information harder to recover. My argument was that the extra representation cost might be worth it if we could expose useful structure and reuse a much stronger generative stack. But at that point, neither side actually knew.

So instead of debating architectures, I turned the disagreement into three gates: does the representation preserve the information we need, does it improve modeling quality at small scale, and is the quality/compute tradeoff worth it?

That changed my own proposal. We screened representations before expensive training. Line plots were too sparse. Gramian angular fields scaled poorly. I dropped them. Delay embeddings and STFT-style representations survived the reconstruction gate.

Then I proposed a small matched POC rather than having us build competing full stacks. The important thing was that it was an experiment where my own 2D hypothesis could fail cheaply.

The evidence was strong enough that the group converged on the image-space direction. The final framework handled sequences from roughly 24 to 17,000 steps, with large gains on both short and ultra-long evaluations, and became ImagenTime at NeurIPS.

The lesson wasn’t that 2D is better than 1D. It was that representation determines which modeling priors and infrastructure become available—and when people disagree on architecture, I try to define the cheapest experiment where either side can be proven wrong.

If they lean in

The story has three distinct technical questions. Do not collapse them:

1. Representation
Does the mapping preserve the information needed for the task?

2. Generative prior
Does putting the data into that representation let the model exploit useful architecture/prior machinery?

3. End-to-end efficiency
Is any quality improvement worth the representation expansion and sampling cost?

EDM primarily improves #3. It does not establish #1 or #2.

Follow-ups

They ask	You say
What exactly was the disagreement?	Whether the benefit of reusing a mature image-diffusion stack could justify the representation expansion and potential information loss versus staying native in 1D.
Why did collaborators prefer 1D?	It preserved the native structure, avoided representation expansion, and was the lower-risk architecture. Their compute and information-loss objections were legitimate.
What did you personally contribute?	I proposed the image-space hypothesis, but more importantly I structured the decision: representation screening, reconstruction gate, small-scale quality comparison, then expensive training only if those survived.
Did you convince them?	I would say the experiment did. My contribution was designing a test where either hypothesis—including mine—could lose cheaply.
Did their disagreement change your thinking?	Yes. It forced representation size, reconstruction fidelity, and compute into the decision criteria. It also led me to reject some of my own candidate representations before full training.
So were you right and they were wrong?	I wouldn’t frame it that way. Their objection identified a real cost that remained even in the successful system. The experiment showed that, for the settings we tested, the benefits outweighed that cost.
Why not simply build the strongest 1D baseline too?	That’s the natural counterfactual. We compared against native time-series approaches, but I would not claim we exhausted every possible 1D architecture. The decision was whether the evidence justified investing in this direction, not whether we had proven a universal superiority theorem.
Could the gains just come from more capacity?	Yes, that’s an alternative explanation for part of the gain. The overall experiment establishes the effectiveness of the approach, not that every gain is causally attributable to the representation. A stronger mechanistic test would control architecture capacity and initialization separately.
How do you know the image representation mattered?	We have reconstruction/scaling behavior and downstream comparisons supporting it, but I distinguish that evidence from the stronger causal claim. Today I would run a representation × architecture × initialization factorial experiment.
Why not use line plots?	They are intuitive for humans but extremely sparse as images and therefore inefficient for this generative formulation. They failed an early representation screen.
What would have made you abandon 2D?	Poor reconstruction, no small-scale quality advantage, or a compute increase large enough that the end-to-end Pareto point was worse than the native alternative.
What’s the senior-leadership lesson?	I don’t try to win architecture disagreements by having the strongest intuition. I try to make the disagreement falsifiable and make sure my preferred solution can fail before the expensive commitment.

The strongest sentence

“I wasn’t trying to convince them that 2D was right. I was trying to design an experiment where either their hypothesis or mine could lose cheaply.”

Do not

Say “my students disagreed with me.” Use collaborators/team/research collaborators.

Say “I set the research vision and convinced them.”

Say “2D is better than 1D.”

Say the transformation preserves all information.

Treat the final paper result as proof that your original mechanistic explanation was correct.

Use the EDM sampling improvement as evidence that the 2D representation was better.

Pretend the collaborators’ concern disappeared. Their compute objection remained valid; the result showed the tradeoff was worthwhile in the tested regime.

Senior-IC framing:

“I proposed a non-obvious architecture, took the strongest objection seriously enough to change how I evaluated my own idea, eliminated parts of my proposal that failed those gates, and created a cheap experiment where either technical position could lose before we committed the expensive resources.”
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

3. Leadership under ambiguity — TSRBench reasoning audit

What it should demonstrate: Turning an ambiguous technical failure into competing hypotheses and an experiment sequence. Leadership through problem decomposition and resource allocation, not authority.

Card

CONTEXT. After the first synthetic reasoning mix failed its temporal-relations gate, reasoning was still the weakest part of TSRBench. We had already shown that simply adding plausible synthetic data could improve the average while hurting the capability we were targeting.

TENSION. The failure did not tell us what to do next. There were several reasonable explanations, and they implied different investments. We could generate more examples of the same temporal operators, scale the model and assume this was a capacity problem, add domain-specific knowledge, teach benchmark-specific formats, or revisit the architecture. We could eventually try all of them, but doing that at 8B would be an expensive search with very little scientific information per run.

MY ACTION. I stopped the next generation cycle and changed the question from “What should we train next?” to “What kind of failure are we actually observing?”

I audited the reasoning items individually and mapped each failure against what the model had seen during training. That produced three working hypotheses:

1. Knowledge gap: the required domain concept was absent—for example specialized seismology knowledge.
2. Operator/composition gap: the primitives were present, but the model failed when several operations had to be composed.
3. Format gap: the underlying reasoning was within scope, but the task expressed it using a convention or representation absent from training.

Then I tied each hypothesis to a different intervention and predicted which error slices should move if it was correct. Instead of immediately spending another 8B run, I used 0.8B as the experimental probe: cheap enough to reject weak interventions, with the larger model reserved for ideas that moved the intended failure class.

I also changed the evaluation from a single reasoning score to per-item tags such as missing operation versus correctly parsed but incorrect reasoning, so the next run would tell us why it moved rather than only whether the average moved.

WHY. At that point the scarce resource was not just GPU time; it was experimental clarity. An 8B run that moved the benchmark two points but mixed three causal explanations would leave us almost as uncertain as before. I wanted each training run to eliminate a hypothesis or strengthen one.

RESULT. The first controlled 0.8B intervention moved TSRBench overall from roughly 0.382 to 0.405 and reasoning from 0.245 to 0.255. I would not present that as a product-level win. The more useful result was that several errors associated with missing operator coverage improved, while another residual class remained where the model appeared to parse the task but failed the reasoning itself. That gave us a much more specific next experiment and justified testing the recipe at 8B rather than blindly scaling every candidate intervention.

REFLECTION. I should have done this decomposition before generating the original synthetic mix. The benchmark already contained evidence about the failure modes. I spent compute to learn that aggregate “reasoning” was too coarse a unit of analysis. Since then, when a system fails heterogeneously, I try to decompose first, attach interventions to competing hypotheses, and only then spend the expensive experimental budget.

Spoken (~90s)

After I killed the first synthetic reasoning mix, we had a more difficult problem: there were too many reasonable explanations for why reasoning was still weak.

We could generate more temporal-relation data. We could scale the model and call it capacity. We could add domain knowledge. We could teach missing task formats. Or maybe the representation itself was still wrong.

Eventually you can try all of those, but at 8B that’s an expensive search, and even if the score moves you may not learn why.

So I stopped the next generation cycle and changed the question from “what should we train?” to “what kind of failure do we actually have?”

I audited the reasoning items individually and compared each failure with the training distribution. Three regimes emerged.

Some were genuine knowledge gaps—specialized domain concepts like seismology that I would not expect a 0.8B model to infer from a few plots.

Some were operator-depth failures: the model had seen the primitives but broke when they were composed into longer chains.

And some were format failures: the required reasoning was actually simple, but the benchmark expressed it using a convention the model had never seen.

Those imply completely different interventions. So I mapped each category to an experiment and used the 0.8B model as a cheap discriminator before spending the 8B budget. I also changed the evaluation so we tracked failure type, not just reasoning average.

The first controlled run moved overall TSRBench from about 0.382 to 0.405 and reasoning from 0.245 to 0.255. That’s not the important claim. What mattered was that some missing-operation failures moved while a residual class of correctly parsed but incorrectly reasoned items remained.

So the next expensive experiment was no longer a guess.

The lesson for me was that under ambiguity, leadership isn’t necessarily choosing the answer. Sometimes it’s structuring the problem so the next experiment can tell the team which answer deserves investment.

The line I would anchor the story around

“The scarce resource wasn’t only GPU time; it was experimental clarity. I wanted each expensive run to eliminate a hypothesis, not just move an average.”

If Vincent pushes on leadership

“Where is the leadership here?”

I wasn’t resolving ambiguity by authority. I changed how we made the decision. Instead of allowing several plausible directions to compete through intuition, I turned them into hypotheses with predicted failure patterns, chose the cheapest experiments that could distinguish them, and reserved the expensive run for the hypothesis that survived.

“Why couldn’t everyone just try their idea?”

Eventually we could test several ideas, but running all of them at full scale would be expensive and scientifically weak. The small model gave us a screening layer. I wanted the 8B budget to test something for which we already had evidence, not serve as the exploratory search itself.

“How did you get people aligned?”

The useful part was that people did not have to agree that my diagnosis was correct. We agreed on what each diagnosis predicted. Once the experiments were tied to those predictions, the evidence determined which direction earned the next run.

“Did anyone actually disagree?”

Only claim disagreement if there really was one. You do not need interpersonal conflict for this story to work. If there wasn’t one:

There wasn’t a major interpersonal conflict. The ambiguity came from several technically defensible directions. My contribution was preventing us from choosing among them based on whoever had the strongest intuition.

That’s actually a strong senior answer.

Do not overclaim

Don’t say the taxonomy was “the answer.” It was a working decomposition.

Don’t say 0.8B proved what would happen at 8B. It was a screening instrument.

Don’t say the architecture had been ruled out unless you really had evidence for that.

Don’t imply the +2.3 pp was the success of the story. The decision process is the success.

Don’t manufacture a team disagreement. Technical ambiguity is enough.

Senior-IC framing:

“We had several plausible explanations, each implying a different expensive intervention. I converted them into hypotheses with different observable predictions, used the cheapest model to discriminate among them, and only then committed the larger experimental budget.”

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

5. Collaboration / impact — Bosch, benchmark success to real sensor data

What it should demonstrate: Cross-functional technical collaboration. Responding when a research result does not survive contact with real data. Using domain expertise from collaborators to change the modeling assumptions, not just tune the existing solution.

Card

CONTEXT. In a collaboration with Bosch Center for AI, we were working on modality translation: learn to generate one modality from another even when the source and target have different representations. I designed much of the modeling framework around a latent diffusion bridge, with modality-specific encoders and a shared generative translation mechanism.

TENSION. On standard research benchmarks, the approach worked very well. But when we moved toward real Bosch sensor data, the behavior degraded. The benchmark formulation implicitly assumed much cleaner paired observations than Bosch actually sees. Their data could be irregularly sampled, noisy, partially observed, and imperfectly aligned. So we had a method that looked strong scientifically but was not yet robust to the distribution the industrial collaborators actually cared about.

MY ACTION. Instead of treating this as a hyperparameter problem, I worked with the Bosch side to understand how the deployment distribution differed from our benchmark assumptions. That changed the modeling question. We needed the generative model to represent not only modality translation, but also the corruption and observation process around the signal.

I extended the approach using ideas from our work on irregular, noisy, and missing time-series generation: explicitly train under incomplete and corrupted observations, preserve timing information rather than assuming a clean common grid, and evaluate under controlled levels of missingness/noise that reflected the failure modes Bosch was seeing.

The important collaboration point was that I could not infer those failure modes from the benchmark. Bosch understood the sensor/data distribution; I understood how to turn those constraints into changes in the generative formulation. The resulting solution came from combining those two views.

WHY. The original model had optimized the wrong abstraction boundary. We had treated modality translation as A → B under clean paired observations. The real problem was closer to partial/noisy/irregular observations of A → a useful estimate of B. Once we changed the problem statement, the modeling changes became much more natural.

RESULT. The robustness extensions substantially improved behavior on the real Bosch setting, and the resulting approach became a strong internal baseline for the company. I would distinguish that from claiming a shipped product: what I observed was that the method became useful enough to serve as a reference point for subsequent internal work. The research direction also produced the modality-translation and irregular-time-series work we published around this collaboration.

REFLECTION. The lesson was that benchmark generalization and deployment generalization are different claims. Today, when I start an industry-facing research problem, I ask much earlier: what assumptions in the benchmark are violated by the actual data-generating process? I would build those stress distributions into evaluation before optimizing the architecture.

Spoken (~90s)

One collaboration that changed how I think about applied research was with Bosch Center for AI.

We were working on modality translation—generating one modality from another when the source and target may have very different representations. I designed much of the modeling framework around a latent diffusion bridge, and on standard research benchmarks it worked very well.

Then we tried to move closer to real Bosch sensor data, and the behavior degraded.

That was actually the useful part of the collaboration. The benchmark assumed much cleaner paired observations than Bosch sees in practice. Their signals could be irregularly sampled, noisy, partially missing, and imperfectly aligned. So technically we had solved clean A-to-B translation, while their actual problem was closer to corrupted, partially observed A-to-B translation.

I worked with the Bosch researchers to characterize that gap rather than just tune the existing model. They had the domain knowledge about how the sensor distribution failed; I could translate those failure modes into modeling assumptions.

I brought in ideas from our work on irregular and missing time-series generation: train explicitly under incomplete observations, preserve timing information instead of forcing everything onto a clean common grid, and stress-test the model under controlled missingness and noise.

That materially improved behavior on the Bosch setting, and the resulting method became a strong internal baseline for subsequent work.

What I like about this example is that neither side had the complete answer. I had a generative framework that looked strong on benchmarks; Bosch had the evidence showing where its assumptions broke. The useful solution came from combining those two.

The lesson I took is that benchmark generalization and deployment generalization are different claims. Now, in an applied collaboration, one of my first questions is: which assumptions in our benchmark are violated by the actual data-generating process?

If they lean in

The central technical transition is:

Initial problem
clean paired source → target

Actual Bosch problem
irregular / missing / noisy / imperfectly observed source → target

The collaboration changed the problem formulation, not merely the hyperparameters.

Keep three claims distinct:

1. LDDBM/general translation framework worked on research benchmarks.
2. Real Bosch data exposed assumptions that those benchmarks did not stress.
3. Robustness work targeting those assumptions improved the industrial setting.

Do not imply that LDDBM itself automatically solved irregular sampling unless that is literally what the experiments showed.

Follow-ups

They ask	You say
What did you personally contribute?	I designed much of the generative translation framework, and when transfer broke, I helped reformulate the problem around the actual observation process and connected it to our work on irregular/missing/noisy generation.
What did Bosch contribute?	They exposed the gap I could not see from academic benchmarks: the actual sensor distribution and which assumptions failed in practice. That changed the modeling problem.
Why didn’t your original model work?	It had been validated under cleaner pairing and observation assumptions. The real data violated those assumptions through irregular sampling, missingness, noise, and alignment issues.
How did you diagnose that rather than just guessing?	Compare performance as we introduce the real-data characteristics separately—missingness, irregularity, noise/alignment—and identify which perturbations reproduce the degradation.
Why not just preprocess everything onto a regular grid?	That’s a baseline, but interpolation can erase information, create artificial certainty, or distort event timing. I wanted the model to represent observation time and missingness rather than hide them entirely in preprocessing.
What was the impact?	The robustness work improved behavior on the Bosch setting and became a strong internal baseline for subsequent work. I would call that internal research impact rather than claim a product deployment I didn’t observe.
What did you learn about collaboration?	Domain experts often know where the assumptions break before they know what model should replace them. My role was to convert those deployment failures into testable modeling changes.
What would you do differently now?	Build a deployment-style stress suite at the beginning: missingness, irregularity, noise, alignment shift, and held-out real distributions—not after the benchmark model is already optimized.

Senior-IC framing

“I brought a general modeling framework that looked strong on benchmarks. Bosch exposed where its assumptions broke on real sensor distributions. Rather than treating that as tuning, I worked backward from those deployment failures, changed the problem formulation, and incorporated irregularity, missingness, and noise into the generative model. The resulting approach improved the real-data behavior and became a strong internal baseline.”

---

## 90-second cheat strip (memory only)

| # | One line |
|---|----------|
| 1 | 2D cost objection → invertibility + small POC → +58% / +132%; they bought the evidence |
| 2 | Delay should carry numbers → ChatTS 0.17 vs 0.71 vs 0.79 → delay is dynamics, not scale |
| 3 | After the kill, fog → three regimes → formats before domain; +2.3 pp 0.8B, 8B WIP |
| 4 | Average + AR/IR up; TR 26.9→21.9; pre-declared −5 pp; killed |
| 5 | Haifa, not Sunnyvale; latent bridge + contrastive/predictive; NeurIPS 2025; no ship claim |

Practice: read each spoken block aloud once. Vincent mock: 1 or 4 first; keep 3 as the sequel to 4 if they ask “what happened after.”

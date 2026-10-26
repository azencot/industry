# Technical deep dive — briefing

45 minutes with **Yochai Pagi** and **Matan Pagi**. **Tue 27 Oct 2026, 00:15 Thailand** (Mon 26 Oct, 20:15 Israel), unless the invite differs.

This is the meeting, not a second reconstruction of the company. Background lives in [`2026-10-27_one-to-many.md`](2026-10-27_one-to-many.md), the call in [`2026-10-20_founders-call.md`](2026-10-20_founders-call.md), the shorter card in [`2026-10-27_contribution-and-call.md`](2026-10-27_contribution-and-call.md), and the control reading log in [`2026-10-26_koopman-control-prep.md`](2026-10-26_koopman-control-prep.md).

The role frame is already in the email. Part-time **Principal Researcher at 40%–60%** (your letter: Principal Research Scientist, 2–3 days a week, remote from Seattle). Agenda plus hands-on, on time series, generative models, and representation learning. They asked for technical leadership and a hands-on approach as they scale. Do not reopen the fraction. Seattle was not restated; leave it unless they do.

Paper: *Bilinear Mamba-Koopman Neural MPC for Varying Dynamics*, Matan Pagi and Zohar Sorek, [arXiv:2605.04793](https://arxiv.org/abs/2605.04793). The zero-shot resampler is from the 20 Oct summary. It is not in this manuscript, and it was not public as of 25 Oct.

---

## 1. Their problem

One-to-many, as they said it on 20 Oct, is an operations ratio: infrastructure is multiplying, the people who can run it are leaving, and one expert capacity has to cover many facilities. Under that sentence sit three different technical problems. The meeting has to say which one is binding for the next six months.

| Reading | What has to be true | What you would own |
|---------|---------------------|--------------------|
| One operator, many sites | A signed twin of this site’s plans, plus a forecast good enough to point at a procedure. | The gate between forecast and procedure. The twin itself is their vision model. |
| One model, many plants | A representation trained somewhere else still steps this plant forward, with a small local correction. | The lift. This is the open scientific claim. |
| Autonomous optimization | The same model stays accurate when the action is the optimizer’s, not the action in the historian, and the write is allowed. | The shift from the data policy to the optimized policy, and the refusal when the forecast splits. |

They decided on 20 Oct that the product is predictive operations: forecast a future state, then optimize. Reaction to the current state is the smaller problem. The public stack that matches the call is a time-series foundation model, a vision model that builds an operational twin from the plans, and an optimization on the learned dynamics. Website names, if they use them: Rosetta, Horizon / PsiFM, Maverick.

Timescales, as far as the paper and the September post go. A chemical benchmark in the paper samples every 18 seconds, and five convex steps cost about 0.9 seconds, so the inner loop fits that plant. A control room decision — which procedure, whether to touch a setpoint — is slower than a sample and has to survive a stale plan. The operator’s constraint is an envelope and a page, not a quadratic tracking cost. None of those operational objects are in the experiments.

Research, as opposed to engineering: a lift that is shared, a local operator that is small enough to audit, a definition of success that is the procedure an engineer would have named, and a measurement of what happens when the optimized action leaves the training support. Engineering, which this seat should not absorb: ingesting drawings, mapping tags at a customer, air-gap deployment, and the on-call path from a pilot.

---

## 2. The paper, critically

### Formulation

Controlled step \(x_{k+1} = f(x_k, u_k)\). A learned lift \(z = \psi(x)\), with a linear decode. MamKO emits \(\bar A_k\) and \(\bar B_k\) from a finite history of \(z\) and \(u\), and forbids \(\bar A_k\) from depending on the current \(u\). That conditional independence keeps a one-shot quadratic program convex. It also forces the mixed partial \(\partial^2 z_{k+1} / \partial z\, \partial u^{(i)}\) to zero.

They put the product back. The drift they analyze is

\[
A_{\mathrm{eff}}(u_k) = \mathrm{diag}(A) + \sum_i u_k^{(i)} G_i,
\]

and the implemented step is a Lie–Trotter split of \(\exp((D + P(u))T)\) so that \(G_i = 0\) recovers MamKO’s per-mode discretization exactly, not merely up to a dense matrix exponential. \(G_i\) is initialized at zero. Added parameters are under 1%. Reported runs use full rank, latent size 8 on CartPole and 15 on the reactor–separator. The low-rank factorization is unused.

The loss is multi-step mean squared error in the original sensors, plus a hinge that pushes eigenvalues of the discrete operator inside a margin of the unit disk. The penalty is training-only. They say a nonzero \(G\) can move those eigenvalues outside the disk, and they leave runtime gating as future work.

The controller is sequential convex programming on the exact Jacobian of the implemented map (reverse-mode, not finite differences), with a trust region on the input step, solved by OSQP. One linearization is not enough on the hard cell. Five iterations is the reported controller.

### What the experiments demonstrate

Four cells, each with its own data: overlapping 60-step windows, i.i.d. uniform input excitation, full state, regular time, about 40,000 train/validation windows per variant. Architecture differs by system (Table 6). Nothing in the manuscript is a transfer run. Forecasting is 30-step open-loop MSE. Closed loop is setpoint tracking, 10 episodes.

The result they can defend:

- **RSCP, time-varying, closed loop.** Cumulative cost \(4.91 \times 10^{-3}\) linear versus \(3.44 \times 10^{-3}\) with five SCP steps, about 30%. One SCP step does not beat linear. The ODE has no \(u \cdot x\) term. The gain shows up when the convex program is iterated, and in stale plans, where the backbone is frozen and \(A_{\mathrm{eff}}(u)\) still moves with the committed input.
- **Training.** On that same cell the linear validation loss oscillates for 400 epochs. The bilinear model settles in about 50 and stays flat. The tail-mean forecast ties. A best-checkpoint comparison that favors the linear model is a spike on the oscillating curve.
- **CartPole forecast.** Strictly better open-loop MSE, which is what their population proposition says when the force really couples into the angle.
- **CartPole, time-invariant, closed loop.** Bilinear is worse, \(2.54 \times 10^{-2}\) against \(2.40 \times 10^{-2}\), about 6%, on the regime they call benign.
- **Cost.** About 0.1 s for the linear program, about 0.9 s for five bilinear steps. They call 0.9 s acceptable against an 18 s reactor sample, and the CartPole timings an offline stress test.
- **Uncertainty reporting.** Bands are \(\pm 0.3\sigma\) over 10 episodes, for display. They say that at \(1\sigma\) some panels overlap.

Proposition 2 is a statement about forecast risk, not about closed-loop cost. It says the bilinear class cannot be a worse forecaster in population, and is strictly better when the true latent step has a nonzero cross-derivative. On the reactor the physics has no such term, so a tie in forecast MSE is what the proposition predicts, unless the lift manufactures a product. The closed-loop win is a different claim: a stationary \(G\) absorbs drift that the history-only operator can only chase by regenerating \(\bar A\), and only an iterated linearization uses it. That claim is supported on one simulated reactor. It is the sentence to respect.

### Demonstrated limitations

These are in the paper. Say them as results, not as a review.

- The calm CartPole closed loop gets worse.
- The headline cell needs five iterations, roughly nine times the linear-program cost.
- At one standard deviation, some closed-loop panels overlap. Ten episodes.
- Their re-trained linear baseline misses the published MamKO number on CartPole time-varying (\(7.8 \times 10^{-3}\) against \(4.3 \times 10^{-4}\)). Absolute MSE is not comparable to Li et al. They say so. There is no deep-Koopman number in this manuscript.
- The spectral penalty does not run at inference.
- Scope, in their words: the encoder is assumed to find a chart where the step is approximately bilinear; the controller guarantee is local; this is a patch inside MamKO, not a new operator class; the plants are simulated.

### Not shown

These are absences. They are not failed experiments. Do not describe them as weaknesses he has already hit.

- A second plant, or one set of weights across the time-invariant and time-varying reactor.
- Irregular samples, missing tags, or the resampler.
- Training on a behavior policy (a PID, a human, a narrow operating band) and then optimizing off it. The inputs in the paper are random excitation, which is a favorable support for an optimizer, not a historian.
- A forecast that is allowed to split. The decision path in the product materials is deterministic. This paper never represents doubt.
- A procedure, a limit from a drawing, or a signed twin. The objective is setpoint cost.
- Runtime stability of \(A_{\mathrm{eff}}(u)\) along a committed plan.

### Three questions for Matan

Ask these during the paper block. Then stop talking.

1. **Where has this formulation actually broken in your hands?** SCP cost, a regime where \(G\) hurts, an encoder that never found the chart, stale plans past five steps. His answer picks the section. If nothing has broken, the test is still two simulators.
2. **Is the time-series model this bilinear step, and where does the resampler sit relative to the lift?** If the paper is the model, transfer and the loss are the work. If the paper is a probe under a larger foundation model, ask what that model cannot certify that the bilinear step can. If the resampler is upstream of \(\psi\), irregular data is an input to the lift, not a separate company.
3. **You train on random excitation and you test model-predictive control. What do you measure when the training actions are a historian instead, and the optimizer leaves that band?** If they have the measurement, read it. If the replan is so fast that the shift never matters, the product is advice inside the data support. If they have no measurement, that measurement is the eval.

---

## 3. Forecasting versus optimization

An observational forecast learns \(p(x_{t+1} \mid x_{\le t})\) on the actions that were already taken. An intervention-aware step learns the response to an action the optimizer is free to choose, including actions the historian never tried. The paper is already on the second side of that line: \(u\) is an argument of the step, the data are excited in \(u\), and the test is closed-loop tracking. Do not tell them they have only built a forecaster.

The gap that remains is the support of \(u\). Random excitation covers the box. A plant historian concentrates on whatever the existing controller does. Model-predictive control, and any later optimizer, will propose inputs off that concentration. Their stale-plan experiment freezes the backbone and still rolls the committed \(u\) through \(G\). It does not train on a narrow behavior policy. Distribution shift under a new policy is untested, not disproved.

Physical constraints in the paper are box constraints on \(u\) inside the quadratic program. Operational constraints — an interlock, an alarm limit, a procedure that forbids a move the quadratic program likes — live in the twin, and the paper never reads them. Predictive uncertainty is the \(0.3\sigma\) display band. It does not enter the cost and it does not refuse an action.

That gap is a real research problem. It is not the first one to own at two or three days a week. A risk-aware optimizer on top of a model that has never been shown on a second unit will not change the one-to-many claim. The piece that belongs in the first paper is an evaluation: fit on behavior-policy data, optimize, report closed-loop cost against the random-excitation model, and define the refusal when simulated futures disagree on the constraint. The generative machinery (a Koopman prior that is a distribution, a mixture over next latents) is how you produce those futures. The actuator still sees a page or a refusal, which is the audit constraint they are selling.

---

## 4. Where you contribute

Ranked for a part-time seat whose output is one paper and one pre-registered experiment, not a platform.

### A. Transferable Koopman representations — own this

Shared lift, local operator. Train \(\psi\) on one or more regimes. Freeze it. Refit a bias, a scale, and \(G\) from a short window on a held-out regime. The two ends of the same figure are a fully frozen model and a full refit.

- **Novelty.** Moderate, and real. Shared Koopman charts exist in the literature. The missing object is this bilinear \(G\) as the local piece, scored closed-loop, on a regime the encoder did not see. Their conclusion already asks for a structured prior on \(G\). A mask from a known flowsheet is the ablation that touches the twin without taking over Rosetta.
- **Business.** This is the model-transfer reading of one-to-many. The paper does not contain it.
- **Fit.** Consistent Koopman autoencoders (the chart, forward and backward consistency, the spectrum). KoVAE (a linear step as the prior, irregular samples, scarce trajectories).
- **Feasibility.** Their latents are 8 and 15. The cost is the closed-loop eval, about a second a step, not a training cluster. Two or three days a week is enough if the code and one simulator are available in month one. A customer historian behind an air gap will not be.
- **Six months.** Month 1: reproduce their RSCP time-varying cell, forecast and closed loop, on their stack. Months 2–3: shared encoder, local \(G\), held-out regime, three conditions (frozen, local, full refit), closed-loop cost as the primary number. Month 4: the loss ablation, sensor reconstruction against next-embedding prediction, same split. Months 5–6: the note. If their resampler exists as code, irregular sampling is a condition in this split. If it does not, drop samples from the same simulator and use a continuous-time encoder. That is one paper.

### C. Irregular observations, and the drawings — attach, do not lead

The resampler is the piece Matan already assigned to himself. Joining the formalization is high leverage and low novelty if the method is already working: you help write a paper they have started. Learning dynamics from asynchronous sensors is the part that matches KoVAE, and it should be the observation model inside A.

The multimodal half, reading plans into the dynamics, splits. The topology prior on \(G\) is a one-week ablation on the reactor whose flowsheet is known, and it is inside A. Owning Rosetta — scanned drawings, provenance, engineer sign-off — is a second team and a vision problem. At this fraction it crowds out the lift.

### B. Probabilistic dynamics for risk-aware optimization — third

Scientifically the largest. As a six-month program it collides with the deterministic decision path, and it assumes a model worth being uncertain about. Keep the refusal rule and the behavior-policy shift as sections of A’s eval. Build a full chance-constrained controller only if they say the actuator is allowed to consume a distribution. They have not said that.

**Recommendation.** Own A. The resampler, if he will share the draft, is how observations enter A. The flowsheet mask on \(G\) is the ablation that connects to the twin. Uncertainty enters as the refusal, not as a new optimizer.

---

## 5. Questions

Ask the first five if the time holds. Each one is a fork.

**1. Which one-to-many is the job for the next six months: one operator covering many sites, one model stepping many plants, or the optimizer writing actions?**

The research problem changes with the answer. Operator coverage means the twin and the procedure gate dominate, and a new operator class is secondary. Model transfer means A is the seat. Autonomy means the policy-shift eval comes first, and you need to hear whether a write is in scope or the product stops at a recommendation.

**2. On a new facility, what stays frozen, and what is fit locally?**

This is zero-shot, made into an interface. Nothing is fit: they need a representation result the paper does not contain, and A is exactly that experiment. A few matrices from a short window: the deliverable is those matrices and the protocol that clears them. A full refit: one-to-many is an integration project, and the research job shrinks to making the refit small enough to audit on an air-gapped site.

**3. Where has the bilinear formulation broken?**

You want his failures, not yours. SCP too slow for the asset they care about, \(G\) hurting a calm regime, the encoder failing to linearize, stale plans past the horizon they published. Any of those becomes the technical core of the meeting. “It hasn’t broken” means the evidence is still CartPole and one reactor.

**4. Is the foundation model this step, and where is the resampler relative to the encoder?**

Otherwise the proposal lands on the wrong artifact. The paper is the model: work on transfer and the loss. The paper is a certified core under a larger model: the question is what the large model is not allowed to do, because the Jacobian and the quadratic program are the reason to keep the bilinear step. The resampler sits in front of the lift: irregular series are an input condition of A. The resampler is the product, and the draft is the second paper: join that draft, and keep the shared lift as the experiment inside it.

**5. Training actions are random. Optimized actions will not be, once the data are a historian. What do you measure?**

This separates a controlled simulator from an intervention problem. They already compare random-excitation training to MPC on the simulator: the missing arm is a behavior policy. They replan inside the sample and the shift never accumulates: autonomy is advice inside the observed band, and a risk-aware controller is premature. They have no number: designing that number is the eval you can own without their customer data.

**6. When a rollout splits across a limit, what is computed, and what may reach the actuator?**

Uncertainty is either a product constraint or a research hole. One trajectory and no refusal: the contribution is the rule, and it is small. Quantiles or an ensemble already gate the action: they need the gate tied to a procedure, not a new generative model. A probability inside the write path: that conflicts with the audit story on the site, and the next sentence is whether a customer has accepted it.

**7. What can I actually train on in month one, and how many hours of a new site exist before a rollout may drive an optimization?**

This decides whether the six-month plan is real. A simulator you can check out: A is publishable on two regimes and should be labeled that way. A historian that cannot leave the site: the method and the public benchmark travel, and their asset is a confirmation you may not see in the half year. Weeks of integration before any series: the research does not start unless the simulator is the lab.

**8. Which single problem, if solved in six months, changes Psistar?**

Their ranking overrides yours when a pilot has a date. Formalize the resampler: join that paper. Show transfer across two units of one class: A, as scoped. Put a certified optimization on the Siemens asset: that is a deployment, and the seat’s piece is the eval gate, not the integration. Fix wrong edges in the drawings: that is the vision model, and your piece is the topology prior on \(G\), offered as an ablation.

---

## 6. Agenda

A guide. If Matan is in the middle of a real failure of the model, stay there.

| Min | Topic | What you are doing |
|-----|--------|--------------------|
| 0–5 | Which one-to-many | Question 1. One sentence on the 40–60% frame only if they open on the role. |
| 5–20 | The bilinear step | Questions 3 and 4. Listen. State the RSCP time-varying result back to him before any gap. |
| 20–30 | Forecast, then optimize | Questions 5 and 6. Pin down behavior-policy shift and the refusal. |
| 30–40 | One direction | A, with the resampler as the observation model and the flowsheet mask as the ablation. Do not pitch B and C as competing programs. |
| 40–45 | The next artifact | Question 7, then one concrete ask: their training loop and the resampler draft, or a written “not yet.” Agree the primary number (closed-loop cost on a held-out regime) before you leave. |

### The seat, if they ask what the months contain

Own the transfer experiment and the eval that says a forecast may drive an optimization. Reproduce their cell yourself. Write the paper. Review the Koopman line with Matan and Zohar as a collaborator, hands on the runs.

Leave outside the seat: drawing ingestion, customer tag mapping, air-gap packaging, and the pilot’s operational backlog. Those are how a part-time research role becomes the on-call engineer.

### Say, then stop

> The result I take from the paper is the time-varying reactor: with the backbone frozen, the bilinear term still moves with the committed input, and five convex steps are what make that show up in closed loop. The calm cart gets a little worse, and the forecast tie on the reactor matches the proposition, because that ODE has no product term. The piece I want to own is the chart around that step. A shared encoder, a local \(G\), a held-out regime, closed-loop cost as the number. The resampler is how irregular observations enter that experiment, if the draft is far enough along to use. The first ablation on the loss is redrawing the sensors against predicting the next embedding, because that decides what is even available to transfer.

---

## Mock

Start only when you want it. One question at a time, as Matan. First question:

> You want the lift to transfer. The paper treats the encoder as an assumption. Suppose I train on the time-invariant reactor, freeze the backbone, and refit only \(G\) on the decaying-catalyst regime. What do you expect the closed-loop cost to do relative to training bilinear from scratch on the time-varying data, and which term in the model is doing the work?

# Contribution and call card — Psistar follow-up

Read [`2026-10-27_one-to-many.md`](2026-10-27_one-to-many.md) first if the stack is still fuzzy. For the 45 minutes, use [`2026-10-27_technical-deep-dive.md`](2026-10-27_technical-deep-dive.md). This page is the frame and the offers.

| | |
|---|---|
| **When** | **Tue 27 Oct 2026, 00:15 Thailand** = **Mon 26 Oct 2026, 20:15 Israel**, unless the invite differs. |
| **Who** | **Yochai Pagi** (CEO), **Matan Pagi** (CTO). **Zohar Sorek** coauthored the paper and is not listed; if he is on the call, he is the other person who has lived in the bilinear model. |
| **What this meeting is** | The technical deep dive. The role frame is already agreed by email. Call log: [`2026-10-20_founders-call.md`](2026-10-20_founders-call.md). |
| **Agreed frame** | Part-time Principal Researcher at 40%–60% (your letter: Principal Research Scientist, 2–3 days/week). Research agenda plus hands-on. They asked for technical leadership and a hands-on approach as they scale. |
| **His action item** | Matan was going to formalize the zero-shot resampler for irregular series, and to publish a second paper within about a month of 20 Oct. Ask about both. |

Say “I.” If they open on the role, restate the frame in one sentence and move to the stack. Seattle and remote are in your letter; their reply did not repeat them, so leave location alone unless they raise it. Leave Amazon and the Siemens Data & AI loop out unless they ask. Siemens Energy Israel is their pilot, and it is a different organization. Raz’s process was open on 20 Oct. You already recommended him. Leave it there unless they ask.

---

## The frame they already accepted

Your letter named three areas: time-series modeling, generative AI, and representation learning, plus shaping the agenda and doing the technical work. Their reply accepted that combination at 40%–60%. On this call those three areas are already their stack:

| What you wrote | Where it sits for them |
|----------------|------------------------|
| Time-series modeling | The foundation model, the bilinear step, the resampler on irregular clocks. |
| Representation learning | The lift that is supposed to transfer, and whether the loss redraws sensors or predicts the next embedding. |
| Generative AI | Rolling a trajectory when the historian is short, and keeping several futures in the latent while the action that ships is one signed procedure. |
| Shaping the agenda | Which of those is the second paper, and what “good enough to optimize” means. They asked for this. One decision, then the experiment. A tour of the lab spends the deep dive. |

---

## Where you can actually help

Matan has a controller for one simulated plant, and a mechanism that keeps adapting after the backbone is frozen. Yochai has described the system around it: a signed Plant Model from the documents, a forecast conditioned on that model, an agent that recommends a procedure and does not invent one. The open scientific problem is the lift that is supposed to be shared, and the test that says the forecast is good enough to meet the playbook.

Six pieces. The first three are the ones to offer. The last three are answers you can give if they pull on cost, data, or doubt.

### 1. A shared lift, and a local operator you can measure

Their scope paragraph assumes an encoder that finds coordinates where the step is approximately linear, and they mark that assumption as inherited. The latent in the paper is 8 or 15 dimensions, on a fully observed simulator. A combined-cycle block has tens of thousands of tags. The September post says the Plant Model is what tells the forecaster which tags are states and which are controls. That sentence is the alignment between units. It is not yet an experiment.

The work this sits on:

- **Consistent Koopman autoencoders** (ICML 2020). An encoder, a linear step, a decoder. Forward and backward maps are trained together and required to be consistent, which is what keeps a long rollout from drifting. The spectrum is part of the model, and the forecasts hold up under noise. Their spectral penalty (equation 9) is the same instinct, applied at training time to the bilinear discrete operator, with runtime gating left to future work.
- **KoVAE** (ICLR 2024, with Ilan Naiman). The prior itself says the next latent is a linear image of the current one. The same model trains on irregular samples, through a neural controlled differential equation, and it generates trajectories when the real series are scarce. Eigenvalue penalties are how physics constraints enter. Stability is something you read off the spectrum.

The experiment, said as an experiment: train one encoder on several units, or on several regimes of a process you can actually resimulate. Freeze it. Refit a small local piece — a bias, a scale, \(G\), the linear step in those coordinates — from a short recent window. The two ends of the same plot are a fully frozen model and a full per-site refit. The quantity on the vertical axis is forecast error and closed-loop cost on a unit that was held out. The Plant Model’s sensory layer is the proposal for which coordinates correspond across units. If they do not have a second plant, two operating regimes with a shared encoder is the honest pilot, and it should be labeled as that.

A full refit per site recreates the project they are trying to leave behind: tag mapping, a training cut of the historian, a model operations has to be convinced to trust, and a new audit object. On an air-gapped site the weights often cannot be trained in place and cannot leave, so a refit is a controlled shipment. A thin local operator is a shipment of a few matrices, or a fit that can run on the historian they already have on site.

### 2. Put the signed topology into \(G\)

The last paragraph of their conclusion asks for structured priors on \(G_i\) that encode a known physical coupling topology. That topology is the physical layer of the Plant Model: what is connected to what, which an engineer has signed. A dense \(G\), which is what they train today because the latent is tiny, will invent couplings the drawing forbids. A mask taken from the signed graph makes the bilinear term a claim about the plant, with a page number behind it.

This is the joint between Rosetta and PsiFM made into a matrix. It is also the cleanest thing you can offer Matan without pretending to have their historian. The first version is on RSCP, whose flowsheet is known: zero out entries of \(G\) that the flowsheet says cannot interact, and see whether RSCP TV closed-loop cost and the training stability survive. If they do, the prior is free performance. If they do not, the lift was using couplings the physics does not have, which is a finding about the encoder.

### 3. Reconstruction against predicting the next embedding

Equation (10) trains the model to redraw the sensors over many steps. That is the right loss when the deliverable is a tag an operator can read. It is a suspicious loss when the deliverable is a latent that has to transfer. Sensor noise, scaling, and a mode one plant rarely visits all help reconstruction and all fail to show up on the next unit.

The JEPA video is this ablation with the brand removed. Predict the next embedding from the current one and the input. Keep a small decode loss so a tag can still be checked, and keep their spectral penalty so the step cannot collapse to a point. The comparison is the same held-out unit as in piece 1. The hypothesis is narrow: the embedding loss drops unit-specific detail and the forecast on the held-out unit improves, or it does not. Either result is a decision.

Say it as that ablation. A proposal to swap their controller for a JEPA planner throws away the Jacobian and the quadratic program, which is the part of the paper that makes the decision path something they can talk about in a control room.

### 4. Several futures, one signed action

KoVAE’s prior is a distribution whose conditional mean steps linearly. Ha’s memory model is a mixture over the next latent. A valve can stick or not, and both futures are in the data. Their product constraint is that the action written down is deterministic and points at a page.

The interface that respects the constraint: the model may return a small set of futures; Maverick asks whether they name the same procedure in the operational layer; if they do, the action is that procedure and the log stores the page and the spread; if they straddle a limit, the system returns the split to the operator and writes nothing. Doubt stays in the latent. The actuator sees a page number or a refusal. You can say this because you have already built generative models whose job is to roll a trajectory when one future is the wrong summary, and because their own plots admit that at one standard deviation some of the closed-loop panels overlap. Overlap is the case the refusal is for.

### 5. The resampler he already named

The paper’s data are overlapping 60-step windows from random excitation, full state, regular time. A site gives the opposite: closed-loop actions, missing tags, uneven sample times, and a short history on a new unit. On 20 Oct Matan took as his own task a zero-shot resampler for irregular series, to be formalized for a paper or for use. That is the object to ask him to teach you. Let him describe what is held fixed, what is resampled, and what “zero-shot” means on a second unit. Then the overlap is concrete: KoVAE trains a linear latent step on irregular samples, and the later completion work is about missing observations. Offer to help formalize it if his draft is the second paper. Arrive with the questions, and with the KoVAE prior in your head. A training recipe for data you have not seen can wait until he has drawn the resampler.

### 6. A cell that gets worse is a result

Table 1 loses on CartPole time-invariant, by about 6%, on the regime they call benign. The RSCP TV forecast gap that favors the linear model is a checkpoint artifact; the tail mean ties. You have killed training mixes because one slice regressed. The same rule here: a change that wins the drifting reactor and loses the calm cart is not ready to be the shared model, until the loss has a reason.

The success criterion for the shared model is not 30-step MSE. It is whether the rolled state and the signed Plant Model name the procedure an engineer would have named, on a unit the encoder was not fit to, and whether a calm regime stays calm. Offer to help define that gate. They already say, in the September post, that public benchmarks cover a single diagram and do not cover a facility, and that their current measurement is held-out drawings plus the rate at which engineers accept or correct the Plant Model. The forecast needs an analogue of that acceptance rate. MSE will not be it.

### Cost, only if they raise it

Five SCP steps cost about 0.9 s against 0.1 s for the linear program. Against an 18 s chemical-plant sample, that is fine. Against a faster asset, or against Maverick scoring many procedures inside one sample, it is the budget. The one-step distillation work (KDM) is the experience of replacing an iterative map by a single learned step and measuring the gap to the slow model. Use it if they say the inner model is getting heavier than the bilinear step. The bilinear step is already the fast object in the paper. The question to ask is how many candidate procedures have to be scored before the next sample arrives.

---

## Forty-five seconds

Say this, then stop. The role is already in the email. This paragraph is the work.

> I read one-to-many as the two models you described. The vision model has to read plans it has never seen and produce a twin an engineer will sign. The time-series model has to forecast a unit it has not been fit to, on that unit’s clocks. The published paper is a precise cut of the second model on one plant: with the backbone frozen, a bilinear term still lets the step change with the input, which is what the optimization needs if you cannot refit on site. The piece I want to work on is the one you were going to formalize, the zero-shot resampler for irregular series, together with the lift it feeds. I have spent a long time on coordinates where the step is linear, including a generative model that trains on irregular samples. The experiment I want is a shared encoder, a small local operator, and a held-out unit, with success defined as the forecast and the signed twin naming the same procedure.

If they say Horizon or PsiFM, use their word. Rosetta is the site’s name for the vision half. Use it once they do.

---

## Questions

Ask the first four. The rest only if the conversation is already there.

1. Walk me through the resampler. What is irregular in the input, what does zero-shot mean on a unit it has not seen, and is this the second paper?
2. Is the time-series foundation model the bilinear model, a larger model that contains it, or a separate stack that the paper is a probe for?
3. Which failure have you actually watched: the vision model misreading a new set of plans, or the forecast missing on a new unit?
4. On a new site, what is allowed to change after the twin is signed: nothing, a few local matrices, or a refit? Who decides the forecast is allowed to drive the optimization?
5. The stale-plan experiment freezes the backbone for a handful of steps. On the asset you care about, what is the replan interval relative to the sample time?
6. A forecast can split across a limit. Where does that refusal happen, and who sees it?

---

## Leave out

- A Koopman tutorial. They wrote one.
- “The paper beats deep Koopman,” and any absolute MSE compared with Li et al. Their CartPole time-varying re-run does not match the published number, and they say so.
- Replacing SCP with a world-model policy trained in imagination, or with a JEPA search. The deterministic page-numbered action is the product. The videos are a loss and a picture of planning, and the ablation in piece 3 is the part that survives contact with the paper.
- The CET directory’s customer list, presented as something they told you. Siemens Energy is public. The rest waits for them.
- A round size, a valuation, or the Founder Index revenue band, unless they bring up the business. You read it so you know the stage. You do not need to prove you read it.
- Conflating their Siemens Energy pilot with the Siemens Corporation Data & AI process.

---

## After the call

Write `2026-10-27_founders-call.md` in this folder: what the resampler actually is, whether it is the second paper, which half of the stack they pushed on, and any change to the 40%–60% frame. Add a row to the session log in [`../INDEX.md`](../INDEX.md).

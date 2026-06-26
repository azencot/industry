# Learn and Be Curious: Learned diffusion from the SDE up — turned a gap into a research line

**Leadership Principle:** Learn and Be Curious  
**Project:** Diffusion models (foundation work → ImagenTime / ImagenFew)  
**Status:** Draft v1 — DOC L6 (pre AI review)  
**Target length:** ~800 words (body) · **~8 min spoken** (descriptive primary) · backup variety story (non-VLM)

---

## Title

I admitted my group didn't understand diffusion, then learned it from the stochastic-process foundations up until I could build original work on top

## Outline

Diffusion models were becoming foundational, but I couldn't make real modeling decisions with them. I built a disciplined learning loop — math from the SDE view, hands-on reimplementation of fragile codebases, paused to fill a differential-equations gap — and turned that into **seven** diffusion papers at ICML/ICLR/NeurIPS plus reusable infrastructure behind **ImagenTime** and **ImagenFew**.

## Ecosystem

A few years into my faculty role at Ben-Gurion University, my group had a solid track record in sequential disentanglement, but diffusion models were appearing everywhere — in the papers I reviewed, in the literature, and in the work my strongest students kept flagging as the most exciting direction. I was not assigned this; I chose to make diffusion a core competency before it became table stakes. I drove the learning personally — I set the curriculum, worked the math myself, and wrote code alongside two students (Ilan and Nimrod) rather than delegating the understanding to them.

## Issue

The honest baseline was that none of us — including me — actually understood diffusion beyond surface level. The methods were mathematically heavy, tied to stochastic processes, and moving fast. The real risk was shipping shallow work: reusing a library, getting a plausible result, and never knowing *why* it worked or where it would break. The competing pressure was real — investing months in a fast-moving area could produce nothing publishable if the field moved on first. But staying superficial had a worse failure mode: irrelevance, missed top-tier publications, and weaker standing for funding and students.

## Objectives

**Goal:** Reach genuine mastery of diffusion — theory *and* implementation — to the point where I could make original modeling decisions, not just run existing code.

**Self-imposed bar:**

- Understand the **SDE / score formulation**, not just the discrete DDPM recipe.
- Own a **clean, correct, extensible codebase** instead of fighting fragile public ones.
- Convert the learning into **novel research**, for time series and beyond.

## Actions

I ran weekly three-to-four-hour deep-dive sessions, but treated them as hands-on technical work, not a reading group: focused paper/blog reading, rigorous walkthroughs of the math, joint coding, and idea generation in the same session.

The process quickly exposed a real gap. Once we framed diffusion through stochastic differential equations, I realized my students had little exposure to differential equations and almost none to stochastic ones — and I needed that footing to reason about samplers and noise schedules. Rather than paper over it, I paused the original plan and rebuilt the curriculum to detour through ODEs and SDEs first. It slowed us down and felt like falling further behind the field, but it changed how I could reason about *why* methods worked instead of copying them.

The second obstacle was tooling. The diffusion codebases at the time were poorly structured and fragile — small changes broke things unpredictably. Instead of working around the friction, I decided to own it: I cleaned up and rewrote key components to isolate the core ideas — the sampler, the noise schedule, the training objective, the evaluation — into a framework that stayed correct while making experimentation fast. That cost effort with no immediate paper, but it became the foundation everything else built on.

## Results

- We could read diffusion papers critically — understand the design choices and spot where new ideas fit — instead of being intimidated by them.
- The effort produced **seven diffusion papers**, all at top-tier venues (**ICML, ICLR, NeurIPS**).
- The cleaned-up codebase and intuition became reusable infrastructure — directly behind **ImagenTime** and **ImagenFew**, and every diffusion project since.
- New MSc students now ramp up far faster because I can teach the fundamentals clearly and the framework already exists; the expertise also led to talk and collaboration invitations inside and outside BGU.

## Learnings and Improvements

Curiosity only compounds when it's paired with a disciplined learning system: read the theory, implement the core pieces, debug the failure modes, then build. In fast-moving fields the easy path is to chase trends and accumulate surface knowledge. I learned to slow down, ask *why* a method is built the way it is, and invest in the foundational assumptions before building on them. I apply the same loop now to any new area — including the VLM work — where I'd rather own a clean reimplementation than inherit a fragile one.

---

## Interview notes

### Role & ownership (say early if probed)

I chose this direction (not assigned), set the curriculum, did the math and coding myself, and rewrote the framework. Students learned *with* me; I owned the understanding and the infrastructure.

### IC proof (artifacts I personally built/decided)

- Redesigned curriculum with the SDE/ODE detour.
- Rewrote diffusion framework (sampler / noise schedule / objective / eval isolated).
- Foundation reused in ImagenTime, ImagenFew, and later diffusion projects.
- **Single-step distillation (NeurIPS'25):** used an operator / dynamical-systems view of the reverse SDE to approximate the multi-step reverse process in one step — trained a student from a pretrained diffusion teacher. **Best concrete proof the SDE depth paid off** (would not have framed sampling as an operator-learning problem from libraries alone). *Validated quality-vs-speed tradeoff on image data.*

### Single-step distillation — drill the strong follow-up

Best answer to "a modeling decision your SDE understanding unlocked?" Plain-English framing: diffusion sampling is numerical integration of a reverse-time differential equation over many steps; the operator view lets you learn the trajectory map more directly and collapse it toward one step.
- **Lock before PS1:** teacher model · metric (FID / downstream) · speedup factor · closeness to teacher · vs consistency-models / existing distillation.
- **Delivery:** say "approximate the reverse process in one step via distillation" — *not* "change the main equation" (avoids a theory fight).

### Spoken script (~8 min)

A few years into my faculty role at Ben-Gurion University, diffusion models were showing up everywhere — in papers I was reviewing, in the literature, and in the work my strongest students kept pointing to as the most exciting direction. My group already had a solid track record in sequential disentanglement, but I had to be honest with myself: I did not understand diffusion deeply enough to make real modeling decisions. I could have treated it as a trend to monitor from a distance, or delegated the learning to students and stayed at the level of high-level supervision. I chose the harder path instead. I decided to make diffusion a core competency before it became table stakes, and I drove that learning personally — I set the curriculum, worked through the math myself, and wrote code alongside two students, Ilan and Nimrod, rather than outsourcing the understanding.

The baseline problem was not lack of exposure. Diffusion was already in my teaching — students were presenting DALL·E and related work — and I was seeing it constantly in reviews. The problem was depth. The methods are mathematically heavy, tied to stochastic processes, and they were evolving extremely fast. There were already many papers, each building on subtle theoretical assumptions. If I approached the topic superficially, I would get shallow work: reuse a library, obtain a plausible-looking result, and never know why it worked or where it would break. That was the operational risk I cared about.

There was also a real strategic risk on the other side. Investing months in a fast-moving area could easily fail to produce publishable results if the field moved on before we caught up. I was aware of that. Still, I felt the long-term upside justified the bet. If I could truly understand diffusion models, it would open entirely new research directions. If I failed to master them, I would be building on sand in a field that was clearly becoming foundational.

My objective was explicit and ambitious. I was not aiming for familiarity. I wanted to close my own knowledge gap — theory and practice — to the point where I could confidently produce novel research in that domain, for time series tasks or otherwise. I set three bars for myself. First, understand the SDE and score formulation, not just the discrete DDPM recipe everyone was copying. Second, own a clean, correct, extensible codebase instead of fighting fragile public implementations. Third, convert the learning into real research output, not a private reading group that never shipped.

To do that, I organized weekly meetings with Ilan and Nimrod, but I designed them as intensive technical sessions, not casual seminars. Each meeting ran three to four hours. I combined focused reading of blogs and papers, rigorous walkthroughs of the mathematical foundations, joint coding, and brainstorming of applications and research ideas in the same sitting. The point was to keep theory and implementation tied together. If I could not implement a concept, I did not yet understand it well enough to build on it.

Very quickly, that process surfaced a gap I could not ignore. One of our early realizations was that diffusion models can be framed using stochastic differential equations. That insight was powerful — and immediately problematic. My students had limited exposure to differential equations, and almost none to stochastic ones. I needed that footing myself to reason about samplers and noise schedules rather than treating them as magic hyperparameters. Ignoring the gap would have limited our understanding to recipe-following. So I deliberately paused the original plan and redesigned the curriculum to include a detour through the basics of ordinary differential equations and SDEs. That slowed us down in the short term. At times it felt like we were falling further behind the field rather than catching up. But it fundamentally changed how I could read papers and make design choices — I could ask why a method was built the way it was, not just whether the numbers moved.

The second major obstacle was tooling. At the time, most diffusion codebases were difficult to work with — poorly structured, fragile, and clearly not written with extensibility in mind. Progress was slow and error-prone. Even small changes could break things unexpectedly. Rather than working around that friction, I decided to own it. I established a parallel process where I cleaned up the code, rewrote key components to isolate core ideas, and built a framework that preserved correctness while making experimentation feasible. I separated the sampler, the noise schedule, the training objective, and the evaluation logic so we could change one piece without breaking the whole stack. That required extra effort and did not immediately translate into a paper. But it created a foundation I could build on safely — and that foundation later supported projects like ImagenTime and ImagenFew.

Over time, the structured learning process paid off in ways that went beyond confidence. I was no longer intimidated by diffusion papers. I could read them critically, understand why things were done the way they were, and identify where new ideas could fit. That effort has led, to date, to seven papers on diffusion models, all accepted to top-tier venues such as ICML, ICLR, and NeurIPS. The theoretical understanding and the cleaned-up codebase continue to serve me in every diffusion-related project since. New MSc students can ramp up much faster because I am comfortable teaching the fundamentals clearly and because the infrastructure is already in place. The expertise also led to invitations for talks and collaborations both within Ben-Gurion and externally.

The lesson I took from that experience is direct, and I still apply it. Curiosity becomes impactful only when it is paired with a disciplined learning strategy. In fast-moving fields, it is easy to chase trends or accumulate surface-level knowledge. I learned instead to slow down, ask why things are done the way they are, and invest in understanding the foundational assumptions before trying to build on them. Read the theory, implement the core pieces, debug the failure modes, then build. That is the same loop I use now when I enter a new technical area — including the vision-language work on time-series reasoning — where I would rather own a clean reimplementation than inherit a fragile one I cannot reason about under pressure.

### Short version (~90 sec)

Diffusion was becoming foundational but I couldn't make real modeling decisions with it. I set an explicit goal — master it from the SDE view and own a clean codebase. I ran weekly deep dives, paused to fill a differential-equations gap even though it slowed us down, and rewrote the fragile public code into an extensible framework. That turned into seven diffusion papers at ICML/ICLR/NeurIPS and reusable infrastructure behind ImagenTime and ImagenFew. The lesson: curiosity only compounds when paired with a disciplined learn-implement-debug loop.

### Likely follow-ups

- What specifically did *you* implement vs the students?
- Concrete example of a modeling decision the SDE understanding unlocked?
- How did you decide it was worth months of risk?
- Which of the seven papers was most yours technically?

### Weak spots / facts to verify

- [ ] Exact count "seven papers" — confirm and list venues.
- [x] Sharpen one concrete technical decision the SDE detour enabled → **single-step distillation (NeurIPS'25)**; still lock teacher/metric/speedup/quality-gap numbers.
- [ ] Managerial-voice risk: keep "I implemented/debugged," trim "my group / students" framing — recurred in 26 Jun drill.
- [ ] Delivery: drop filler openers ("great question", "Feynman 101") in interview mode.

### FinTech bridge (only if asked)

Same loop for a new finance modeling area: learn the theory, own a clean reference implementation, validate failure modes before building production work on top.

### Related stories

- **Invent and Simplify:** ImagenTime — [`invent-simplify_imagentime.md`](invent-simplify_imagentime.md) (don't overlap the repo cleanup beat).

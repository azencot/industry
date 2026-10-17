# Psistar founders call — 20 Oct 2026

**Tue 20 Oct 2026, 00:00 Thailand (ICT, UTC+7).** That is **Mon 19 Oct 2026, 20:00 Israel (IDT, UTC+3).** Israel is still on summer time; the clocks differ by four hours.

If the calendar invite says 12:00 and not 00:00, noon Thai time is 08:00 the same calendar day in Israel. The note below assumes midnight Thai time, as written.

| | |
|---|---|
| **Who** | **Yochai Pagi** (CEO) and **Matan Pagi** (CTO), co-founders |
| **How it started** | They contacted **Raz Marshanski** |
| **Site** | [psistar.ai](https://psistar.ai/) |
| **Ask** | Unknown. Learn the work; let them say whether this is advice, a collaboration, students, or a role. |

No public white paper, no code release, and no mainstream press piece turned up. The record is the site, two company-directory cards, LinkedIn, and one arXiv paper.

---

## One-hour plan

Read in this order. Stop at the hour even if the optional list is untouched.

| Min | Read | Why |
|-----|------|-----|
| 0–10 | [Homepage](https://psistar.ai/) · [PLANETech card](https://planetech.themarketsquare.org/startup/psistar/) · [IVC card](https://www.ivc-online.com/Google-Card?id=28fe5c18-a2ca-f011-b81a-00505695cd29) | What they sell. Two model families, air gap, markets. |
| 10–35 | Their paper, [arXiv:2605.04793](https://arxiv.org/abs/2605.04793) ([HTML](https://arxiv.org/html/2605.04793), [PDF](https://arxiv.org/pdf/2605.04793), [mirror on the site](https://psistar.ai/bilinear-mamba-koopman-neural-mpc-for-varying-dynamics/)). **Abstract, §1, eq. (1), §2, Table 1, Table 2, §5.2–5.4.** Skip the SCP proof. | This is the only technical artifact. Matan is first author. |
| 35–50 | [MamKO, ICLR 2025 Spotlight](https://openreview.net/forum?id=hNjCVVm0EQ) ([PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/e99847f8d8006806fd35d6f536136c0d-Paper-Conference.pdf)). **Abstract and the first two pages.** | The model they extend. “Linear” in their paper means MamKO with the bilinear terms set to zero. |
| 50–60 | LinkedIn posts in the press list below: rebrand, paper, Siemens Energy, F/AI. | What they are willing to say in public, and what they are explicitly holding back. |

### If the hour runs long

Only if §2 of their paper feels thin:

| Paper | Link | One line |
|-------|------|----------|
| Korda & Mezić, Koopman MPC | [arXiv:1611.03537](https://arxiv.org/abs/1611.03537) | The convex-MPC-from-a-linear-lift result their whole stack sits on. |
| Lusch, Kutz, Brunton, deep Koopman | [Nat. Commun. 2018](https://www.nature.com/articles/s41467-018-07210-0) | Learned encoder instead of a fixed observable dictionary. MamKO’s static baseline. |
| Mamba | [arXiv:2312.00752](https://arxiv.org/abs/2312.00752) | Selective state space. MamKO borrows the idea of emitting a step-varying operator from recent history; it is a conv + FCNN, not a language model. |
| Mao et al., successive convexification | [arXiv:1804.06539](https://arxiv.org/abs/1804.06539) | The SCP convergence result they invoke for the non-convex bilinear MPC. |

Skip on a first pass: Williams EDMD (2015), SINDy / SINDy-MPC (Brunton, Kaiser), Neural ODE, Mohler’s bilinear control book. They cite all of these. None of them is the conversation.

---

## What they are building

Public product description, mainly the [IVC card](https://www.ivc-online.com/Google-Card?id=28fe5c18-a2ca-f011-b81a-00505695cd29) and the [homepage](https://psistar.ai/):

1. **A documentation engine.** Manuals, SOPs, schematics, P&IDs, control-logic diagrams become a queryable operational graph with a pointer back to the source page.
2. **A perception model they call Horizon.** Forecast the next physical state from the sensor stream. The stated ambition is zero-shot on assets the model has not seen.
3. **An interface constraint.** LLMs sit at the chat layer. The decision path is supposed to stay deterministic, on-prem, and auditable.

Inputs they ask a customer for: an existing sensor stream and an existing playbook. No new hardware. Domains on the site: power plants, aerospace, defense, data centers, oil and gas. Buyers they name: heads of operations, reliability, and engineering. Beachhead on the IVC card: defense primes, critical energy, hyperscale data centers with an air-gap requirement.

Tagline, including on the rebrand post: predict the physics, understand the logic, control the chaos. Yochai’s comment on the rebrand says the name comes from operator theory. Psi is the usual symbol for the Koopman observable.

The arXiv paper is narrower than the product page. It is a bilinear latent dynamics term plus sequential convex programming, evaluated on CartPole and a reactor–separator process. Horizon, the playbook graph, and zero-shot transfer are not in that paper.

---

## The paper in one sitting

**Bilinear Mamba-Koopman Neural MPC for Varying Dynamics.** Matan Pagi, Zohar Sorek. Psistar. [arXiv:2605.04793](https://arxiv.org/abs/2605.04793). Matan posted it on LinkedIn on **7 May 2026** as the first paper out of the company. No venue listed. No code found.

### The constraint they relax

MamKO emits a local linear model from recent state and control history, then runs a convex QP. The drift matrix is not allowed to depend on the current input, because \(A(u)\,z\) is bilinear and the one-shot QP stops being convex.

They put that term back:

\[
z_{k+1} = \Big(\mathrm{diag}(A) + \sum_i u_k^{(i)} G_i\Big) z_k + B_k u_k
\]

\(G_i = 0\) recovers MamKO. \(G_i\) is factored low-rank and initialized at zero, so training starts as the linear model. They report the added parameters as under 1% of the backbone. Latent size in the runs is small: 8 on CartPole, 15 on RSCP, and they use full rank there. The low-rank option is for later, larger latents.

Because the map is bilinear, the state Jacobian is analytic. They solve the MPC by sequential convex programming (linearize, QP, repeat), and cite Mao et al. for monotone descent and KKT convergence under standard trust-region assumptions. One SCP step is a single linearization. Five steps is where the time-varying result shows up. Wall-clock in their Table 3 is about 0.1 s per step for the linear QP and about 0.9 s for five bilinear SCP steps.

### What the experiments actually say

Two systems, each time-invariant and time-varying.

- **CartPole.** Force couples into the angle. This is the control–state coupling case.
- **RSCP.** Liu et al. reactor–separator: two CSTRs, a flash tank, recycle. 9 states, 3 heat duties. The duties enter the energy balance additively, so the ODE has no \(u \cdot x\) term. The time-varying version modulates feed composition. This is the “parameters drift” case.

Closed-loop cumulative cost, their Table 1, bilinear with 5 SCP steps vs their re-trained MamKO:

| Cell | Linear | Bilinear-SCP-5 |
|------|--------|----------------|
| CartPole TI (20 s) | **2.40e-2** | 2.54e-2 |
| CartPole TV (20 s) | 1.79e-2 | **1.73e-2** |
| RSCP TI (2 h) | 7.90e-4 | **6.43e-4** |
| RSCP TV (2 h) | 4.91e-3 | **3.44e-3** |

The number they emphasize is RSCP TV, about a 30% lower cumulative cost, and only once SCP is iterated. One SCP step does not beat linear there. CartPole TI is a small loss for the bilinear controller. Forecasting (Table 2, 30-step open-loop MSE) improves on CartPole and is essentially tied on RSCP once they average the last 50 epochs. On RSCP TV the linear model’s validation loss oscillates for the whole training run; bilinear settles in about 50 epochs. They treat that stability as part of the result.

The other experiment is stale plans: commit to a control sequence for \(d \in \{0,1,3,5\}\) steps with the backbone frozen. On RSCP TV the bilinear model degrades more slowly, because \(A_{\mathrm{eff}}(u)\) still changes along the committed input while MamKO’s drift is fixed until the next replan. That is the industrial sentence in the paper: replan intervals are longer than the simulator step.

### Caveats worth having in your head

- They compare to their own re-run of MamKO, and that re-run does not match the published MamKO numbers. CartPole TV forecast MSE is \(7.8 \times 10^{-3}\) in their linear baseline versus \(4.3 \times 10^{-4}\) in Li et al. They say so. Absolute numbers are not comparable to the ICLR table.
- “We beat deep Koopman by transitivity” means MamKO beat DKO in the original paper, and they beat their own MamKO re-run. There is no DKO, MLP, or SAC number in this manuscript.
- Closed-loop plots use \(\pm 0.3\sigma\) bands over 10 episodes. They note that at \(1\sigma\) some panels overlap.
- §5.2 says the CartPole TI loss is a regime with no \(u \cdot x\) coupling. §5.1 says CartPole is exactly the system whose generator is bilinear in \(u\). The table is clear; that sentence is not. Easy thing to ask about, not to open with.
- Scope paragraph in the paper: local KKT guarantees, encoder has to find a lifting where the step is approximately linear, and they are explicit that this is a structural patch inside the MamKO family, not a new operator class.
- Benchmarks are simulated. Nothing in the paper is a plant, a turbine, or a data hall.

---

## People

| Person | Role | Public background |
|--------|------|-------------------|
| **Yochai Pagi** | CEO, co-founder. On the call. | [LinkedIn](https://www.linkedin.com/in/yochaipagi). Israeli Air Force, captain, 2016–2022. Elbit: UAS specialist, then software engineer, through Mar 2025. B.Sc. CS, Open University of Israel. M.Sc. CS, Reichman, listed as in progress. The old Maverick page also called him a UAV specialist and a former product lead. Operator and product side of the company. |
| **Matan Pagi** | CTO, co-founder. On the call. First author. | [LinkedIn](https://www.linkedin.com/in/matan-pagi-319224187). Left Google on 3 Apr 2026 after 6+ years; the old Maverick page described him as a tech lead in ML, reliability, and ML infrastructure. Columbia Applied Mathematics M.S., October 2025 ([APAM news PDF](https://www.apam.columbia.edu/sites/default/files/2026-07/apam_news_columbia_engineering_spring_2026.pdf), commencement list). This is the person to talk Koopman with. |
| **Zohar Sorek** | Research scientist. Coauthor. Not listed for the call. | [LinkedIn](https://www.linkedin.com/in/zohar-sorek-electrical-and-computers-engineer). M.Sc. EE, BGU. Physics-informed modeling. |
| **Yuval Dayan** | Business development lead (IVC). Not listed for the call. | Pushed the F/AI application. Posted in Hebrew on 29 Sep 2026 that they are hiring, including roles not on the site. The paper mirror on psistar.ai is filed under an author page named Yuval. |

---

## Company facts, as public as they get

| Fact | Source |
|------|--------|
| Founded 2025. Formerly **Maverick AI** ([maverickai1p.com](https://maverickai1p.com/)). Rebrand announced **14 Apr 2026**. | [Rebrand post](https://www.linkedin.com/posts/psistar_we-are-excited-to-announce-our-rebranding-activity-7449840794364047360-E8RP) |
| ~10 employees (IVC). LinkedIn range 10–20. Tel Aviv and the US. IVC address: 16 Sheinkin St, Tel Aviv. | [IVC](https://www.ivc-online.com/Google-Card?id=28fe5c18-a2ca-f011-b81a-00505695cd29) |
| [PLANETech](https://planetech.themarketsquare.org/startup/psistar/) lists pre-seed/angel and “MVP to pilot.” IVC lists a seed (25 Nov 2025), a seed extension (7 Jan 2026), a government R&D grant (1 Jan 2026), and “currently seeking capital ($10m as of May 2026).” Amounts and investor names on the IVC card are redacted. A board seat is attributed to a principal at ICI Fund; the person’s name is redacted. | Both cards. Treat stage as early and raising. Do not quote a round size. |
| **F/AI F26**, STATION F, Paris. Yochai posted this on **28 Sep 2026**. Referral-only program, Sep–Dec 2026 batch, aimed at teams that can reach about €1M revenue in six months. He names the partner list (Microsoft, Google, AWS, Mistral, Anthropic, and others) and thanks Roxanne Varza. No Station F page found that lists Psistar by name. | [His post](https://www.linkedin.com/posts/yochaipagi_two-months-ago-yuval-dayan-sent-a-message-activity-7510393660119801858-p4UL) · [program news](https://stationf.co/news/fai-newpartners) · [how admission works](https://stationf.co/news/get-into-f-ai) |
| **Siemens Energy** pilot. First public mention **10 Sep 2026**, with **Ori Shpigel** (Head of Innovation, Siemens Energy Israel). Hosted via Innovation Hunters (Ruth Arazi Sheffer) and Startup Nation Central. They describe preparation, pace, and trust. Yochai explicitly leaves “what happens after the pilot” off LinkedIn. A follow-up company post on 14 Sep repeats that the details can wait. | [Yochai](https://www.linkedin.com/posts/yochaipagi_a-special-moment-for-us-at-psistar-today-activity-7503811354261282816-8S48) · [Psistar](https://www.linkedin.com/posts/psistar_the-what-gets-attention-the-how-gets-it-activity-7505252165347672065-C3Gc) |

Siemens Energy Israel is a different organization from the Siemens Corporation Data & AI loop. Ori Shpigel’s public Siemens Energy page is about venture clienting at a gas power plant; the Percepto drone writeup is his, and it is not a Psistar project. [That page](https://www.siemens-energy.com/global/en/home/innovations/ventures/percepto.html) is only useful as context for who he is.

---

## Press and posts

| Date | What | Link |
|------|------|------|
| 2026-04-03 | Matan leaves Google | [LinkedIn](https://www.linkedin.com/posts/matan-pagi-319224187_after-an-incredible-6-years-at-google-its-activity-7445824409757634560-f1Oo) |
| 2026-04-14 | Maverick AI becomes Psistar | [LinkedIn](https://www.linkedin.com/posts/psistar_we-are-excited-to-announce-our-rebranding-activity-7449840794364047360-E8RP) |
| 2026-05-07 | First paper | [Matan](https://www.linkedin.com/posts/matan-pagi-319224187_bilinear-mamba-koopman-neural-mpc-for-varying-activity-7458175801524551680-pNZF) · [arXiv](https://arxiv.org/abs/2605.04793) |
| 2026-09-10 | Siemens Energy pilot, public for the first time | [Yochai](https://www.linkedin.com/posts/yochaipagi_a-special-moment-for-us-at-psistar-today-activity-7503811354261282816-8S48) |
| 2026-09-14 | Same pilot, “details can wait” | [Psistar](https://www.linkedin.com/posts/psistar_the-what-gets-attention-the-how-gets-it-activity-7505252165347672065-C3Gc) |
| 2026-09-28 | Accepted to F/AI F26 | [Yochai](https://www.linkedin.com/posts/yochaipagi_two-months-ago-yuval-dayan-sent-a-message-activity-7510393660119801858-p4UL) |
| 2026-09-29 | Hiring, including unlisted roles (Hebrew, Yuval Dayan) | [LinkedIn](https://www.linkedin.com/posts/yuval-dayan_psistarr-%D7%A6%D7%95%D7%9E%D7%97%D7%AA-%D7%95%D7%96%D7%94-%D7%91%D7%93%D7%99%D7%95%D7%A7-%D7%94%D7%96%D7%9E%D7%9F-%D7%9C%D7%94%D7%A6%D7%98%D7%A8%D7%A3-%D7%90%D7%9C%D7%99%D7%A0%D7%95-activity-7510617640344637440-WYov) |

---

## If they ask what you work on

One stretch of the overlap, then stop. They already know the Koopman literature; a tutorial will waste the call.

> I spent a long time on Koopman models of sequential data, including learned coordinates where nonlinear dynamics become easier to forecast. More recently the work has been generative: models that can roll a trajectory forward when real series are scarce, including one-step sampling so the rollout is cheap. The shared piece with what you published is the lifting. The piece I would want to understand in your setting is where the model sits — inside the control loop, or next to the operator — and how you represent doubt when the decision itself has to stay deterministic.

Leave Amazon collaboration, paper venues, and lab structure out unless they ask. Say “I.”

---

## Questions worth the time

1. What do you want from this conversation — a technical read, a research collaboration, students, or something else?
2. Is Horizon the bilinear model, a larger model that contains it, or a separate perception stack? Where do the playbooks attach to the forecast?
3. On a real asset, does the model advise the operator, or does it write setpoints?
4. The zero-shot claim: across units of one class, or across different physics? What was the eval?
5. Siemens Energy: which asset, what was measured, what is still open? They have already said the post-pilot story is not public; ask only if the conversation gets there.
6. Uncertainty. Sensor dropout, model error, a stale plan. The site says the decision path has no probabilistic component. How does a wrong forecast get refused?
7. Training data on a new site: simulation, historian, or both, and how many hours before they trust a rollout?

---

## After the call

Drop `2026-10-20_founders-call.md` in this folder with what they actually asked, and add a row to the session log in [`../INDEX.md`](../INDEX.md).

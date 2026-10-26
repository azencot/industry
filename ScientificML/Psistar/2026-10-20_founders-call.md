# Psistar founders call — 20 Oct 2026

**Tue 20 Oct 2026.** Yochai Pagi (CEO), Matan Pagi (CTO), Omri Azencot.

Logged 25 Oct 2026 from the meeting summary Omri kept (TL;DR, topic splits, action items, decisions). The recording is not in this folder. Wording below follows that summary. It is a brief, not a transcript. The summary spells the company “PsyStar.”

Prep going in: [`2026-10-20_founders-call-prep.md`](2026-10-20_founders-call-prep.md). The technical follow-up this call produced is [`2026-10-27_one-to-many.md`](2026-10-27_one-to-many.md) and [`2026-10-27_contribution-and-call.md`](2026-10-27_contribution-and-call.md).

---

## What the meeting was

An introduction and a collaboration conversation. They described the company, Omri described the sabbatical, and both sides agreed the next meeting should be technical. About a fifth of the summary is the collaboration and the next step. The longest stretch is the two-model stack.

| Topic in the summary | Share |
|----------------------|-------|
| Raz Marshanski | 5% |
| Omri’s background | 10% |
| Founder introductions | 5% |
| Business vision and the market need | 15% |
| The two-model architecture | 25% |
| Competitors and timing | 20% |
| Collaboration and next steps | 20% |

---

## What was said

**Raz Marshanski.** Omri recommended him. Raz is a former student and was in Psistar’s interview process. They had not decided.

**Omri.** On sabbatical from the academic post, looking for large-scale industrial problems to work on directly. Still leads the research group at Ben-Gurion.

**Founders.** Yochai: computer science, military service, Elbit. Matan: mathematics, research at Google. The company is the two brothers’ shared project.

**The problem, in their words.** Heavy infrastructure and energy capacity are the bottleneck, and the people who know how to run them are aging out. The mission they stated is to make that infrastructure autonomous, in a **one-to-many** operational model.

**The stack, in their words.** Two models.

1. A **time-series foundation model** for physics-informed forecasting.
2. A **vision model** that builds an operational digital twin from engineering plans.

Together they are supposed to support predictive operations and optimization in real time. Public names that match this split, from the site rather than from this summary: Rosetta is the document side, Horizon / PsiFM is the forecast, Maverick is the agent. Use their words on the call if they have not switched to the product names.

**Competitors.** They said fully autonomous power plants are not in the market. The systems they compare themselves with are digital twins that are slow, offline relative to operations, and hard to scale. The advantage they claimed is zero-shot transfer into real-time operations.

**Collaboration.** They want a professor on the team. They are building the company as an industrial AI research lab, and that choice is driving hiring, publications, and the wish to bring academic work in-house. The agreed next step was a technical meeting on the stack and the open problems, and on whether a collaboration fits.

---

## Decisions in the summary

1. **Predictive operations.** The architecture forecasts a future state and then optimizes. Reacting to the current state is the smaller problem. This is the decision that makes the Koopman MPC paper a piece of the product: the forecast is the model, and the optimization runs on that forecast.
2. **Research lab, on purpose.** Brand, hiring, and papers are aimed at a leading industrial AI lab, which is why they want academic people inside.
3. **A technical follow-up.** Yochai, Matan, and Omri agreed to go deeper on the stack before judging the collaboration.

---

## Action items from the summary

| Who | What | Status on 25 Oct |
|-----|------|------------------|
| **Omri** | Decide the constellation: advisory, hands-on, or another form. | Sent after the call. They agreed the frame. See below. |
| **Yochai, Matan, Omri** | Schedule the technical follow-up. | This is the Tue 27 Oct 00:15 Thailand meeting, unless the invite differs. |
| **Matan** | Publish a second paper within about a month of this call. | No second Psistar paper was public as of 25 Oct. The bilinear MPC paper (7 May 2026) is still the only one. Ask what the second paper is. |
| **Matan** | Formalize the zero-shot **resampler** for irregular time series, toward a paper or wider use. | Unpublished. This is the technical object he put on his own list. It is the overlap with KoVAE and the later irregular-series work. Ask him to walk through it. |

---

## Email after the call

Omri wrote the next day (“yesterday”). Yochai replied for both founders. Dates beyond that are not in the paste. This is an agreement on the frame. It is not an offer letter: no compensation, no start date, no written scope.

Omri proposed a part-time **Principal Research Scientist** role. The work he named is shaping the research agenda and hands-on technical work, on time-series modeling, generative AI, and representation learning. The arrangement he asked for is about 2–3 days a week, remote from Seattle.

Their reply, in their words: framing the **Principal Researcher** role at **40%–60%** makes sense. They want the combination of technical leadership and a hands-on approach as the team scales. 40%–60% is the same band as 2–3 days of a five-day week. They used “Researcher,” where the letter said “Research Scientist.” Their reply restates the fraction and the kind of contribution. It does not restate Seattle or remote.

---

## What this changes for Tuesday

The role frame is settled. Tuesday is the technical deep dive he already asked to continue: where, inside their stack, those three areas actually land. The unpublished object Matan named is the irregular-series resampler, zero-shot. The bilinear paper is the published control cut. Both sit inside the time-series foundation model. The vision twin is the other half. Re-opening advisory versus hands-on, or re-pitching the fraction, spends the meeting they already moved past.

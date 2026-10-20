# Ozan mock log

One file for every mock aimed at Ozan Sener. Append a section. Add a row to the index. Do not open a new file per mock.

## Index

| Date | Kind | Focus | Break |
|------|------|-------|-------|
| 2026-10-19 | Technical, ~7 min | KDM, one result he still defends | CIFAR numbers only on the second ask. No one-step teacher control. ImageNet described with no FID. |
| 2026-10-19 | General, ~8 min | Why leave the university | Dodged the job-shape question once. “Technical lead,” then “all of the code.” |
| 2026-10-19 | General, ~15 min | A method he thinks is wrong | No second-benchmark number. Reasoning guessed as 28 vs 25. Trace pilot has no delta. |
| 2026-10-19 | Telling, ~5 min | KDM, no notes | CIFAR numbers in the first pass. Missed CTM 1.98. “SOTA” overclaims GET. No 64×64 FID. |
| 2026-10-19 | Telling, ~5 min | Twice Upon a Time, no notes | 45.2 said. Dual said as 53.1. Missed same-view controls, event prediction, and flat TSExam. |
| 2026-10-19 | Profile C, ~10 min | What he would start | Token cost, then a representation. KVP is the baseline. No y-axis. Mixed graph becomes a selector. |
| 2026-10-20 | Hiring, ~12 min | Intro, then the job | Week stayed the lab week. “May or may not” did not pick. Students leading is still his lab. |

---

## 2026-10-19 — KDM, one result

**Kind:** Technical mock, about seven minutes, four answers. Interviewer was Ozan with Raja’s note only. Answers were not supplied in advance. Stopped when the scaling claim had no number.

**Opening:** Of the work from the last two years, which piece did you build yourself, and which result would you still defend?

### What he said

Offline one-step distillation of a visual diffusion model. The account started from an SDE and a Kolmogorov forward equation: under a time-invariant vector field the equation integrates in one step by a matrix exponential. He called himself the technical lead. The setting he defended was offline: precomputed noise and data endpoints, no trajectory, no further teacher access. He named CIFAR-10 and FFHQ, said ImageNet had not scaled, and said the theory still holds.

Pressed for numbers: KDM FID 4.65 at 1 step, GET 6.91, EDM teacher 2.04 at 35 steps. He then said he had started ImageNet-1k, results were mixed, and compute made him stop.

Asked for the teacher at one step: he did not remember that run, and agreed it would be informative.

Asked for the ImageNet FID and resolution: maybe 128×128, the 1000-class set, overall FID high, some portions better, no pattern he could name, exact numbers gone.

### What landed

The three CIFAR numbers, once asked. Offline was stated as a constraint: endpoints only, teacher weights unused after the pairs exist. He did not invent a one-step teacher FID.

### What broke

- The first answer had no FID and no step count. “Technical lead” is the wrong noun. Say which decision was his.
- 4.65 versus 6.91 compares two students. 4.65 versus 2.04 is the teacher at 35 steps. Neither number is the teacher at one step. Agreeing that the control would be easy does not close it. Say the run was not done.
- ImageNet was described as a run. He could not find those numbers afterward. On a call, say scaling stopped at FFHQ and AFHQv2. The paper also omits ImageNet; an interviewer who has not opened it will not catch that. The failure on the call is quoting a result with no FID.

### Spoken lock

The result I can defend is unconditional CIFAR-10. The EDM teacher is FID 2.04 at 35 steps. My student is 4.65 at one step. GET, the offline method I ran against, is 6.91 at one step. I did not evaluate the teacher at one step, so I do not claim the student beats a truncated teacher. The best online one-step number in that table is CTM at 1.98, and it is better than mine. Scaling in the paper stops at FFHQ and AFHQv2, 64×64, where my FID is about two and a half times the teacher’s.

### Next

CTM at 1.98, and what the offline constraint costs against that online number. Not run in this mock.

---

## 2026-10-19 — why leave the university

**Kind:** General mock, about eight minutes, five answers. No paper. Interviewer was Ozan with Raja’s note: professor, considering industry. Answers were not supplied in advance.

**Opening:** If you left the university, what part of that job are you trying to leave, and what part are you trying to keep?

### What he said

He would leave a compute ceiling. BGU was a good home for six years. He enjoyed scaling the group and widening it across multimodal modeling, generative modeling, and forecasting. Industry would let him compete with better-resourced groups.

Asked whether he would take a job where he writes the code and does not grow a group, he answered with a different pair of reasons: seeing algorithms affect millions of users, and personal reasons to move from Israel to the US.

Asked again, yes or no, he said yes. He described himself as hands-on, then a technical lead, and said he never left that. Being a group director let him run more directions in parallel. The core, he said, stayed a small set of technical problems.

Asked if he would stay on one problem for a year, he said yes, and that the past year was already that: a multimodal time-series reasoning project, new to him, ending in an arXiv preprint submitted to ICLR. He said the group’s other projects continued.

Asked who wrote the training code and how many days a week he ran experiments: Hedi and he wrote all of the code. He was the technical lead, responsible for the architecture and a two-stage training curriculum. Hedi ran ablations. He coded about three days a week on that project.

### What landed

The second yes was direct. Three days a week, the architecture, and the two-stage curriculum are concrete. The move to the US was stated as personal, without a story wrapped around it.

### What broke

- The first answer was about the group. Compute was the only thing he named as the reason to leave. He did not say what he would keep.
- The job-shape question went unanswered the first time. Millions of users and a move to the US were a new subject. “Potentially” and “witness” do not say the job he wants.
- “Technical lead” and “group director” came immediately after he agreed not to build a group. “Director so I could explore more directions” fights the one-problem yes.
- “Hedi and I wrote all of the code” is too closed. The preprint’s equal-contribution authors are Hedi Zisling and Liran Nochumsohn. He will not have the author list in front of him on the call. The sentence is still wrong to practice. Name Liran, or do not say “all.”
- The other two days of the week were never said.

### Spoken lock

I would leave the compute ceiling. I would keep working on one technical problem, and I would take a job where I write the code and train the model without growing a group. This past year was already close to that. About three days a week I worked on one multimodal time-series project that was new to me. I wrote the architecture and the two-stage training curriculum. Hedi wrote code with me and ran the ablations. Liran is an equal-contribution author on that preprint, so I will not say the two of us wrote all of it. The other two days I can account for if you ask.

### Next

The millions-of-users sentence, against a group whose public work is papers and prototypes. Not run in this mock.

---

## 2026-10-19 — a method he thinks is wrong

**Kind:** General mock, about fifteen minutes. No assigned project. Interviewer asked for one method he thinks is wrong, and the result that would change his mind. Answers were not supplied in advance.

**Opening:** Name one method you think is wrong, and the result that would convince you that you are the one who is wrong.

### What he said

He named the time-series language-model line. Incorporation by text, patches, or plots improved results, and each paper uses its own benchmark. He would reconsider if a method generalized past the benchmark it was built for. He named Twice Upon a Time as the attempt.

Asked whether that paper cleared the bar: partly. He called perception the stride, trend and seasonality from plots and from a second view. He put the reasoning slice at about 28% against a 25% random baseline, and said he thought that was the number.

After checking: closer to 40%. He could not verify the random baseline or the slice size. Those were looked up during the mock and added to the paper card. The slice is 1,710 questions. There is no published chance row. A uniform guess over the real choice counts is about 23.9%. Plot-only is 35.8. Dual is 40.1.

Asked for a second benchmark and a number, he said TSRBench is fine and that he would extend it with gold reasoning traces. Asked whether a correct letter with a bad trace is a failure, he said yes, at least a soft one, and that traces trump accuracy.

He then described a Stage C GRPO attempt: a synthetic set with gold traces, reward on trace plus answer. Preliminary results did not move the benchmark whether traces were correct or not. He did not pursue it, and it is not in the paper. No delta.

### What landed

The falsifier was stated before the paper: generalization past a home benchmark. He corrected 28% to about 40% once he looked, and he did not invent a chance level after being told the paper has none. The GRPO pilot is a real negative, if it stays qualitative.

### What broke

- The first answer did not name a method that is wrong. It named a missing evaluation property, then his own paper.
- Perception was called the stride. On his table, perception stays flat. The reasoning gap on the 1,710-question slice is 35.8 to 40.1. Twenty-five percent is not the chance level.
- Asked for a second benchmark and a number, he proposed a new annotation instead.
- “Soft failure” and “traces trump accuracy” cannot both be the rule.
- The trace pilot has no benchmark name and no delta. On a call, that is the failure. He will not know it was left out of the paper unless it is described as a result.

### Spoken lock

I would drop my objection if a method beat a strong baseline on a benchmark it was not built for, by a gap I can name. On TSRBench reasoning, 1,710 questions, the plot-only model is 35.8 and the dual model is 40.1. There is no published chance baseline. A uniform guess over the actual choices is about 24%, not 25%. Perception is not where the gain is. I tried rewarding gold reasoning traces on synthetic data. That run is not in the paper, and I will not quote a delta I do not have.

### Next

The second benchmark he already evaluated, with one number, before any proposal to extend TSRBench. Not run in this mock.

---

## 2026-10-19 — KDM, five minutes, no notes

**Kind:** Spoken telling. Not an interview. The bar was teacher FID, his FID, GET, the online number that beats him, and why offline is the setting.

### What he said

Diffusion as an SDE and as a Kolmogorov forward equation. Under certain conditions the equation integrates in one step by a matrix exponential. He called himself the technical lead. The use he defended was offline distillation: the teacher precomputes noise and data, the trajectory is not stored, and the teacher is not available afterward. Unconditional CIFAR-10: KDM FID 4.65 at 1 step, GET 6.91, EDM teacher 2.04 at 35 steps. He said this shrinks the gap to SOTA without beating the teacher. He said the one-step teacher was never run. Scaling: ImageNet was not run, for compute. FFHQ and AFHQv2 were named, with no FID.

### What landed

The three CIFAR numbers were in the first pass. Offline was a constraint, not a slogan. The missing one-step teacher was stated as missing. ImageNet was not narrated as a result.

### What broke

- CTM at 1.98, one step, online, was not said. It beats KDM and the teacher. “SOTA” makes GET the frontier.
- FFHQ and AFHQv2 had no number. At 64×64 the student FID is about 2.5× the teacher’s.
- “Technical lead” still does not name the decision: offline, a linear map on the endpoints, and the comparison to GET. The measured sampler is one student forward pass.

### Spoken lock

On unconditional CIFAR-10 the EDM teacher is FID 2.04 at 35 steps. My student is 4.65 at one step. GET, the offline method I compared against, is 6.91 at one step. CTM, the online one-step number in that table, is 1.98, and it is better than mine. I did not evaluate the teacher at one step. Reported scaling stops at FFHQ and AFHQv2, 64×64, where my FID is about two and a half times the teacher’s.

---

## 2026-10-19 — Twice Upon a Time, five minutes, no notes

**Kind:** Spoken telling. Not an interview. The bar was 45.2 to 53.2, the same-view controls, event prediction, and the flat TSExam result, without being asked.

### What he said

He called himself the technical lead, working with his PhD student. He set the problem as multimodal time-series reasoning and the approach as complementary visual representations. TSRBench was the main benchmark, with TSExam and ChatTS also run. He wrote the architecture, the training curriculum, and much of the data pipeline. Plots keep scale. A delay view was motivated by earlier image-based generative work, along with STFT. The two streams are fused in the prompt, under 300 visual tokens, with extra features into the first language-model layers. Qwen3-VL-8B. Plot only 45.2%. Dual views he said as 53.1%, with perception left high on TSExam.

### What landed

Qwen3-VL-8B, plots plus a second view, prompt fusion under 300 tokens, and 45.2 for plots alone. The work he named — architecture and curriculum — is specific.

### What broke

- The table is 53.2, not 53.1.
- Same-view controls, 44.8 and 42.6, were not said.
- Event prediction, 21.7 to 84.2, was not said. Forecasting only moves from 46.2 to 50.4.
- TSExam was used as a perception win. It is 89.9 either way. TSRBench perception stays flat, 87.4 to 86.4.
- “My PhD student” is one person. Hedi Zisling and Liran Nochumsohn are the equal-contribution authors.

### Spoken lock

On TSRBench, plot only is 45.2 and the dual view is 53.2. Plot+Plot and Delay+Delay, same picture to both towers, are 44.8 and 42.6. The overall jump is mostly event prediction, 21.7 to 84.2. Forecasting is 46.2 to 50.4. TSExam is 89.9 either way, so it is not evidence for the second view. Perception on TSRBench stays flat.

---

## 2026-10-19 — what he would start

**Kind:** Profile C mock, about ten minutes, five answers. The question was one project for the first six months, and why not an extension of a paper he already has.

**Opening:** Suppose the first six months were yours to define. What one project would you start, and why that one rather than extending a paper you already have?

### What he said

A project on making multimodal models more efficient. Several channels make the token count explode. Related to his multimodal work, and more general than it. He would start it rather than continue a paper because of impact and generality. The target is broad multimodal models, not time series in particular.

Asked which tokens he would remove, and which existing method already removes tokens: he might not do eviction. The cache policy had crossed his mind as a baseline. He wants a representation that stores what is important and drops what is not. The policy’s advantage is that it is dynamic. He believes a strong representation can keep that.

Asked what number against the policy is a win, and what number makes him stop: he wants a graph over token budgets where the representation is consistently better. He stops if it is always worse.

Asked about winning only at tight budgets and losing when the cache is large: he would combine the two with a small selector, or start with rough thresholds.

Asked whether he still ships the selector or drops the representation: the selector switches regimes. The representation is for tight budgets. The cache policy is for large ones. He will not drop the representation if some regime clearly improves on the policy.

### What landed

The cost is tokens. The baseline is the learned cache policy, at the same budget, across more than one budget. Losing at every budget is a stop. The mixed case got a rule: keep the representation where it wins, and keep the policy where it wins.

### What broke

- The first answer was a program. Impact and generality were the reason to start. No input, no tokens removed, no task.
- “Stores what is important” restates the policy. Nothing was said about when the representation is computed, or what it throws away.
- “Consistently better” has no y-axis. “Clearly improves” has no gap.
- The selector arrived before a mixed graph existed. A threshold can be the rule. A learned selector is a third method.
- The representation is never dropped if any regime wins. That is a keep rule. The only kill is losing everywhere.

### Spoken lock

I would start one comparison. The cost is tokens when several views enter the model. The baseline is the learned cache policy at the same token budget. The plot is task accuracy against that policy across budgets, on a task I name before I train. I stop if the representation is worse at every budget. If it wins only below a budget I also name in advance, I use it in that regime and the cache policy above it. I do not train a selector until that split is already on the graph.

### Next

Name the task and the token budget that counts as tight, before any selector. Not run in this mock.

---

## 2026-10-20 — hiring manager, the job

**Kind:** Hiring-manager mock, about twelve minutes, five answers. No paper. Interviewer was Ozan with Raja’s note only. Omri introduced himself. Answers were not supplied in advance. The 20:00 meeting was still unconfirmed.

**Opening:** Raja’s note was short. Tell me what you do, and what you’re hoping this conversation is.

### What he said

Associate professor at BGU, computer and information science. He directs the sequential learning group, about twenty people, five of them PhD students. Six years on sequential learning: representation learning, disentanglement, forecasting, generative modeling, multimodal. Day to day he is a hands-on technical lead. He likes one project, coding, and turning observations into algorithms. He is looking for industry opportunities and thinks this group is a top west-coast candidate.

Asked what job he is picturing, given that hired roles do not come with a group: a scientist role that may or may not be a technical lead, collaborating toward a shared goal. A normal week would look like his current week. Once a project is set, he meets the team, from one person to many, decides directions, sets experiment gates, implements code, runs experiments, and reports back.

Asked about the west coast: he is in Seattle. He understood from Raja that most of the work is remote, and that works. He will travel for onsite meetings. If most of the group is in the Bay Area, short-notice trips and several visits a year are easier.

Asked whether he would still want the job as one scientist on a project someone else owns: yes. He is fine as a member of the scientific team. He said this is close to his group already. In principle he is the technical lead, and in many projects his students lead for a time and tell him what to do.

Asked whether a fixed quarterly goal and one experiment, owned by someone else, is a week he wants: yes. He does not see much difference from today. The team sets quarterly goals and more detailed plans per project, runs experiments, and updates the plans as observations come in. He believes a similar loop happens at Apple Research.

### What landed

Seattle, and a yes to travel. The second and third asks got a yes. Implementing the code and running the experiment were in the week. Quarterly goals that move when the experiment moves are a real loop.

### What broke

- The introduction was the group. “Technical lead” and “directs” arrived before the job he wants. “Industry opportunities” and “a top west-coast candidate” do not say what he thinks the group works on.
- “May or may not” did not pick. “Very similar to my current week,” a meeting of one to many, deciding directions, and reporting back to the team are the lab. The constraint was that the role does not come with a group. The week did not change.
- “Raja said most of the work is remote” was stated as the arrangement. The Bay Area was the city that would be convenient. A group that is not remote, or not in the Bay Area, was left open.
- Students telling him what to do are still his students. “In principle I am the technical lead” puts the title back in the sentence that was supposed to drop it.
- “Not much difference” refuses the last constraint. “We set the goals” keeps him among the people who set the quarter. The question was a goal already fixed, and one experiment. “I believe a similar loop happens at Apple Research” describes their process for them.

### Spoken lock

I would take a scientist role on a project someone else owns. I would not be hiring a group or directing one. A normal week is the experiment: I implement it, I run it, and I bring the result back. The quarter’s goal is already set, and I do not reset it in the meeting. I am in Seattle. Remote work is what I understood from Raja, and I can travel. If the group is not in the Bay Area, I still want the job.

### Next

What he thinks the group actually works on, in one sentence, before any paper. Not run in this mock.

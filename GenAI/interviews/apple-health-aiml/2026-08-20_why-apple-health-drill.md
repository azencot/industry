# Debrief — 2026-08-20 — Apple Health AIML: group briefing + why-Apple-Health drill

**Type:** Prep (group briefing) + 5-question fit drill  
**Track:** GenAI / Apple Health AIML HM screen  
**Duration:** ~afternoon (briefing + glossary) then 5 spoken Qs on **why Apple Health**  
**Call:** Fri 2026-08-21, 11:05–11:50 AM PDT · Shirley Ren · fit, no coding  
**Prior:** [`2026-08-12_hm-screen-prep.md`](2026-08-12_hm-screen-prep.md) · [`2026-08-12_recruiter-debrief.md`](2026-08-12_recruiter-debrief.md)  
**Artifacts:** [`2026-08-20_shirley-group-briefing.md`](2026-08-20_shirley-group-briefing.md) (group facts); this file (drill)

---

## Session

Covered: what Shirley’s group publishes (RelCon, speech-FM transfer, TS-reasoning LLM); sensor glossary (accel / HR / PPG, Hz, gait regression); Workout Buddy attribution correction; then five fit questions on why Apple Health (not the training-run).

---

## Conclusions

**Group (do not name-drop unless she goes there)**

- Stack: wearable series → sensor/motion FMs → language/reasoning layer → product under privacy / Apple Intelligence.
- Scientific overlap with you: perception bottleneck, two-stage align-then-reason, LoRA. Difference: they bet a **native TS encoder** into Mistral-7B; you bet **dual visual encodings**. Defend without dying on matplotlib.
- **Workout Buddy** is a **LinkedIn shipped claim**, not a paper or newsroom byline under her name. Do not say “you shipped Workout Buddy.”

**Drill — what landed**

- Did not fake clinician / health papers. Best answer was Q4: **not married to TS-as-image**; learn constraints, then design; year one might be encoder or eval harness.
- Honest on Apple vs Google scientifically (“question is similar”) — keep that. Never keep the follow-on “the company doesn’t matter.”

**Drill — what broke (repeat tomorrow and she will filter you)**

| Said | Why it fails | Do instead |
|------|----------------|------------|
| Impact at scale / millions of users / real-world data | Works at Google Health, Meta, any startup | **Setting:** device-resident, longitudinal, user-specific series |
| Privacy / safe AI as a virtue | Ethics paragraph; she hears it all week | Privacy / on-device **constrain the representation** (freeze, probe, distill) |
| “Academic; company doesn’t matter” | Tourist / will leave for the next paper | Question **same**; setting **different**; this seat in Seattle |
| Expertise + passion + “work you are doing” | Answered what you like, not why you vs a PPG person | This seat is representation + multimodal + LLM training, not clinician+classifier; you’ll learn wearable failure modes |
| “I don’t know yet” / “not necessarily the first question” | Sounds like you might ignore the job | Pair uncertainty with year-one: *their* series, *their* eval, ablate encoder families |
| “This chapter / narrative / exactly” | Resume-speak; skipped the **cost** (slower pub, privacy) | Name the cost as the reason you want it |

**Locked combined “why Apple Health” (~50s) — say twice before the call:**

> The question I work on is how to represent time series so a model can use them — perception first, then language. That question isn’t unique to Apple. The setting is: the series already live on the device, they’re longitudinal and user-specific, and privacy / on-device change how you build the representation, not just the compliance appendix. I’m not a clinician and I won’t reprint TS-as-image on PPG. Year one I’d learn your signals and your eval, then ablate encoder families under your constraints. I want that problem here, not a cleaner public benchmark.

**If Google vs Apple:** same question; choosing this setting and this seat in Seattle — not the logo.

---

## Decisions / artifacts updated

- [x] [`2026-08-20_shirley-group-briefing.md`](2026-08-20_shirley-group-briefing.md) — locked script + drill anti-patterns
- [x] [`2026-08-12_hm-screen-prep.md`](2026-08-12_hm-screen-prep.md) — Google probe + drill anti-patterns in pillars
- [ ] `omri_azencot_experience.md` — no; Apple-loop specific
- [ ] `AGENTS.md` — no; not a global convention

---

## Open questions

- None for the HM **fit** topics. Training-run 2–3 min still needs a spoken pass if not done today (detail: [`2026-08-12_hm-3c-training-run.md`](2026-08-12_hm-3c-training-run.md)).
- Do **not** prep the 5-interview on-site before this call.

---

## Next session (Fri morning, 15 min — then stop)

Skim three HM topics + locked 50s above + kill-decision sentence (TR synth 26.9 → 21.9). Join Webex **after 10:55 AM PDT**. After the call: write `2026-08-21_hm-screen-debrief.md`.

**Handoff prompt**

```
@GenAI/interviews/apple-health-aiml/2026-08-20_why-apple-health-drill.md
@GenAI/interviews/apple-health-aiml/2026-08-20_shirley-group-briefing.md
@GenAI/interviews/apple-health-aiml/2026-08-12_hm-screen-prep.md
HM screen was Fri 2026-08-21 with Shirley Ren. Write 2026-08-21_hm-screen-debrief.md from the call notes; do not invent.
```

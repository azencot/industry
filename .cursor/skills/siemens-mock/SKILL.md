---
name: siemens-mock
description: >-
  Run a Siemens Principal Applied Scientist phone-screen mock and append it to
  ScientificML/Siemens/mocks.md. Use when the user asks for a Siemens mock,
  a story-bank drill, a 15-minute behavioral on stories A–F, or to log a
  Siemens mock. Interviewer asks and follows up. Do not supply the answer first.
---

# Siemens mock

Phone-screen practice for the Siemens Principal Applied Scientist loop. Behavioral source: [`ScientificML/Siemens/2026-10-15_behavioral-story-bank.md`](../../../ScientificML/Siemens/2026-10-15_behavioral-story-bank.md). Coding source: [`ScientificML/Siemens/coding/README.md`](../../../ScientificML/Siemens/coding/README.md). All mocks append to [`ScientificML/Siemens/mocks.md`](../../../ScientificML/Siemens/mocks.md). Do not create a new file per mock.

## Run the mock

1. Read the story or problem file. Read the index at the top of `mocks.md` so you do not repeat a break he already logged.
2. Ask one question. Wait. Follow up on what he actually said.
3. Do not lead with the model answer, the headline, or the numbers.
4. About 15 minutes, or until a factual miss that would hurt on the screen. Then stop and debrief in chat: what landed, what broke, one next pass.
5. IC language. If he says "my students," "the lab," or "I did not use my seniority," follow up on who owned the other side and what evidence moved the decision. Do not coach that mid-answer.
6. Do not invent metrics, collaborators, or a product ship. Numbers already in the story bank are fair to demand; if he skips them, ask for one.

## Log it

Append to `mocks.md` in the same session, before you finish.

1. Add an index row: date, kind, focus, the break in one line.
2. Append a section:

```markdown
## YYYY-MM-DD — [focus]

**Kind:**
**Prompt:**

### What he said

### What landed

### What broke

### Next pass
```

3. Add a session-log row in [`ScientificML/INDEX.md`](../../../ScientificML/INDEX.md) and a thread row in [`ScientificML/Siemens/README.md`](../../../ScientificML/Siemens/README.md).
4. If the same correction appears twice, promote it into the story bank or `AGENTS.md`. One miss stays in `mocks.md`.

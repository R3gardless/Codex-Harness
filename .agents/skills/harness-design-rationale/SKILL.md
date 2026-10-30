---
name: harness-design-rationale
description: Extract only decided design choices and their stated reasons from AI-user conversations into a concise rationale log. Use to preserve agreed architecture, API, UX, or dependency decisions without copying the discussion.
---

# Record decided design and its rationale

Review the conversation actually available to you. Extract only design choices
that were settled: explicitly agreed choices, firm user requirements, or choices
the agent actually made within authorized implementation scope. Identify who
decided; an agent's implementation choice is not automatically user approval.

Exclude brainstorming, unanswered questions, suggestions not selected, routine
progress reports, full chat transcripts, and private personal details. Do not
reconstruct missing conversations from memory or infer intent from code alone.

Use the existing ADR log, or `docs/DESIGN_RATIONALE.md` when no convention exists.
For each material decision record only:

| Field | Content |
| --- | --- |
| Decision | The settled design choice, in concrete terms |
| Reason | The reason actually stated in the conversation |
| Constraint / tradeoff | Only a material constraint or consequence that was discussed |
| Basis | A short paraphrase of the confirming exchange and decision owner |
| Implementation | Relevant file/function if checked; otherwise omit |

If the decision is clear but no reason was stated, write `Reason not recorded`.
Do not invent a plausible justification after the fact. Ask for clarification
only when that missing rationale matters to the current task. Do not turn a
tentative suggestion into a decision to make the log look complete.

Merge repeated statements about the same decision into one entry. For a changed
decision, link the prior entry as superseded and record the stated reason for
the change. Do not silently rewrite history or manufacture dates.

Keep the log short and in the user's preferred language. The skill itself is
English; generated explanatory notes may be Korean. Preserve truthful AI
involvement and do not attribute an agent's rationale to the user.

Before saving, check every entry against the conversation. Include no generic
architecture advice and no release changelog. A design explanation requested
later can use this log with the actual code through `harness-explain`.

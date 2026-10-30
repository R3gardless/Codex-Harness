---
name: harness-explain
description: Explain the actual implementation, design tradeoffs, evidence, and limitations for learning or a technical handoff. Use source code and observed results, not generic architecture claims.
---

# Explain what exists

Trace one real request or data item through the implementation. Link the relevant
files/functions and distinguish intended behavior from verified behavior.

Explain the few decisions that matter: requirement, chosen approach, why it fits,
one credible alternative if useful, and the cost or failure mode accepted.
Point out unfinished pieces and conditions under which the design would need to
change. Do not invent an architectural rationale after the fact; label inferred
reasons and confirm them with the user when necessary.

For learning, invite the user to explain the main flow in their own words and
correct misunderstandings using code. Do not claim the user understands because
a document exists. For a handoff, give concise verified facts the reader can
check: run command, tests, data assumptions, error handling, and known limits.

Use this during permitted development or preparation. If the user is currently
in an independent-answer phase that prohibits AI, do not generate, polish, or
coach answers for that phase. Stop and defer to the stated phase rules.

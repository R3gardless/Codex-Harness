---
name: harness-discover
description: Turn an ambiguous business request into a small implementation contract by inspecting the project and eliciting missing requirements. Use before building when scope or success is unclear.
---

# Discover the work

Read the task brief and existing implementation before proposing features. Extract
the user, workflow, painful step, input/output, non-negotiable constraints, and
observable success condition. Cite the file or supplied statement behind each
important requirement. Keep guesses separate.

If a stakeholder or domain channel exists, prepare a few questions that change a
decision. Ask through an authorized channel; otherwise give the user concise
questions to relay. Do not automate a chat UI or invent an integration. Choose
follow-ups from the answers instead of sending a fixed questionnaire.

Useful questions, selected for the actual uncertainty:
- Walk through one recent real example, including the inconvenient part.
- Who consumes the result and what decision should become easier?
- What must be correct even when inputs are missing, duplicated, or late?
- What is the minimum useful result? What can be left out?
- Which existing rule, example, or measurement defines a good result?

Ask for examples or constraints, not for a hidden solution, scoring rubric, or
an exhaustive feature list. Summarize your interpretation back when an ambiguity
would cause costly rework. Do not block a reversible implementation choice on an
unnecessary preference question.

Produce a compact contract in the project's required document, or in chat if no
document is needed:

| Requirement / source | User-visible behavior | Acceptance check | State |
| --- | --- | --- | --- |

Use `confirmed`, `assumed`, or `open` for state. Add explicit non-goals and the
smallest working slice. Reconcile contradictory requirements before dependent
work. Stop discovery when the critical path and its acceptance checks are clear;
leave low-impact unknowns as stated assumptions.

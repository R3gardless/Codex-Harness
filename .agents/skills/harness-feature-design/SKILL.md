---
name: harness-feature-design
description: Turn understood requirements into a functional specification covering normal and exception flows, business rules, state changes, acceptance checks, and maintainable documentation. Use before implementing new or materially changed behavior; keep small fixes to a brief contract delta.
---

# Design the behavior before implementation

Read the requested outcome, relevant code/tests, and existing feature documents.
Identify the actor, goal, trigger, scope, and current behavior. Separate confirmed
requirements, assumptions, and open decisions. If the business problem is still
unclear, use [harness-discover](../harness-discover/SKILL.md) first. Do not turn a
design request into authorization to implement or deploy.

Use the existing specification format. Otherwise adapt the optional
[feature specification template](assets/feature-spec.md). A small change needs
only the affected behavior and checks in the response or existing work note;
do not require a new document, a full checklist, or a separate approval ceremony.

## Define the functional contract

- Actor and access: who can initiate the action, on which resources, and under
  which preconditions. Identify the source of material business rules.
- Inputs and outputs: required/optional values, defaults, bounds, relevant units
  or time zones, and the observable result. Distinguish missing, empty, and zero
  where the domain does; use concrete examples to resolve ambiguous semantics.
- Normal and alternative flows: trigger, ordered steps, decisions, success, and
  cancellation where supported. Include UI/API behavior only where it exists.
- State and effects: allowed transitions, invariants, persistent changes, and
  external effects. Specify the point at which work is committed and what the
  caller can safely retry. Use a small state/sequence diagram only when useful.
- Compatibility and limits: behavior preserved for existing callers/data, plus
  workload or performance limits actually required. Label unmeasured targets.

## Design exceptions as observable behavior

Select cases relevant to the feature: missing/invalid/boundary input, empty data,
missing/deleted resources, unauthenticated/forbidden access, stale updates,
duplicate requests, concurrency, timeout, unavailable dependencies, partial
failure, or interrupted work. These are prompts, not mandatory features.

For each material case record the trigger, user-visible result or API error,
state/side effects, recovery action, and acceptance check. Define whether work
was rejected before a write, rolled back, partially committed, or has an unknown
outcome. A timeout does not establish that a write failed. Specify safe retry,
status lookup, reconciliation, or compensation only where the actual flow needs
it. Avoid blind retries, success-shaped errors, and messages that expose secrets.

Clarify high-impact unknowns before dependent implementation: permissions,
irreversible effects, state invariants, or incompatible output changes. Continue
independent design work and keep low-impact assumptions explicit. Never invent a
stakeholder answer or silently promote a proposal to a requirement.

## Make the specification testable and maintainable

Link each material rule and exception to an observable acceptance scenario:
precondition/input → action → expected response and final state. Use stable case
IDs when several documents or tests need to refer to the same behavior. Cover
the main flow and high-impact failures; prioritize by impact and likelihood.

Write for the next implementer or maintainer: define domain terms, show meaningful
input/output examples, identify unresolved decisions, and link relevant code or
contracts instead of copying them. Mark examples as illustrative unless they are
actual requirements. Keep proposed, implemented, and verified behavior distinct.

Maintain one authoritative location per fact: the feature spec for behavior,
the existing decision log for settled choices and stated reasons, README/API
docs for usage, and an operations guide only when recovery steps are needed.
Update affected docs with the implementation and check examples, commands, and
links against the delivered behavior. Do not create empty documents or duplicate
the full spec across these locations. Hand off the smallest working slice, its
acceptance cases, and remaining unknowns; record test results only after execution.

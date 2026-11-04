# Feature specification

Use the host project's format first. Keep only relevant sections and replace the
prompts with evidence. This is a template, not a record of approved requirements.

## Outcome and scope

- Actor and user goal:
- Requirement sources:
- Current behavior and intended change:
- In scope / non-goals:
- Confirmed requirements / assumptions / open questions:

## Functional contract

- Trigger, access rules, and preconditions:
- Inputs, defaults, validation, and relevant limits:
- Outputs and a meaningful input/output example:
- Normal flow and supported alternatives:
- States, allowed transitions, and invariants:
- Persistence/external effects and commit boundary:
- Compatibility with existing callers/data:

## Exceptions and recovery

Include only material cases. State what happens to data as well as what the
caller sees; a timeout can leave the outcome unknown.

| Case ID | Trigger / condition | User or API result | State / side effects | Safe recovery | Acceptance check |
| --- | --- | --- | --- | --- | --- |

## Acceptance and evidence

Keep planned expectations separate from observed results. Use case IDs to link
tests or manual checks without copying their implementation into the document.

| Case ID / rule | Given / when / then | Test or manual check | Result / unverified |
| --- | --- | --- | --- |

## Implementation and documentation links

- Relevant entrypoints, contracts, and test paths:
- Settled decisions and their recorded reasons:
- Usage/API documentation affected:
- Rollout/recovery instructions, if needed:
- Remaining questions and delivery limits:

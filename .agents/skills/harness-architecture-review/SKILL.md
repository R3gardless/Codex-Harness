---
name: harness-architecture-review
description: Review actual code flow against available AI-user design decisions, evaluate optimizations, and identify evidence-backed infrastructure risks. Use for architecture walkthroughs or design and operational reviews; not for a single bug or decision-log extraction alone.
---

# Review the implemented design with the user

Start from the requested workflow, relevant source/tests, deployment configuration,
and available conversation or decision records. Identify the real entrypoint and
review scope. Read only enough to trace that flow and its dependencies. A review
request alone does not authorize refactoring, deployment, or cloud changes.

## Trace the logic from code

Follow one concrete input through UI/API entry, validation/DTO, authentication,
service rules and authorization, DB/external calls, response mapping, and UI state
where those stages exist. Link actual files/functions. Include important branches,
transaction boundaries, side effects, asynchronous work, retries, and failure
propagation. Use a compact Mermaid sequence/flow diagram or a table when it makes
the flow easier to inspect. Do not invent layers or callers absent from the code.

Distinguish code-observed behavior, test/runtime-verified behavior, and assumptions.
Inspect tests for the main flow and material failure cases. A test file's existence
is not evidence that it passed; record executed commands and results separately.

## Compare implementation with the design conversation

Use available decisions and their attributed sources. For each material choice,
link its implementation and mark it matched, different, or unresolved. Without
conversation/decision evidence, historical intent remains unknown. A mismatch is
a finding, not permission to alter code or rewrite history.

Use [harness-design-rationale](../harness-design-rationale/SKILL.md) to extract or
record settled choices and stated reasons; keep proposals, inferred explanations,
and open issues in the review. Ask only about differences affecting behavior or
architecture and continue independent analysis while waiting. Do not invent the
user's answer or require an interview to complete an explanatory review.

## Evaluate optimization with evidence

Separate optimizations already implemented from proposed improvements. For each
relevant one, identify the path/query/component, intended benefit, evidence, cost,
and possible correctness regression. Inspect actual query counts/plans, latency,
allocations, bundle size, or network waterfalls only where the flow warrants it.
Do not prescribe caches, indexes, batching, or service splits from generic advice.

Without a baseline, report a hypothesis and a concrete measurement plan. When
optimization is authorized, compare before/after with the same workload, data,
environment, and correctness checks; report tradeoffs such as memory, freshness,
write cost, or complexity. Never invent a speedup or infer capacity from structure.

## Assess infrastructure and failure risks

Follow the dependencies actually found. Consider applicable risks such as DB pool
exhaustion across replicas, slow/N+1 queries, lock contention, migration rollout,
retry storms, duplicate jobs, stale caches, external outages, missing timeouts,
secret exposure, and untested restore paths. Treat these as review prompts, not
automatic findings or reasons to add infrastructure.

For each finding record: code/config evidence, trigger, user/data impact,
priority with a reason, detection signal, mitigation, and a verification step.
Separate observed defects from conditional risks and unknowns. State the missing
workload/configuration evidence rather than assuming a production topology or
SLO. Use read-only evidence; fault injection or load tests need an isolated,
authorized environment. Never modify live resources to confirm a suspected risk.

## Deliver a review that supports the next decision

Use the existing review document or the response for a small review. Include the
traced flow, design/code comparison, implemented and proposed optimizations,
prioritized risks, and checks run/unverified. Lead with consequential findings;
omit empty sections and generic checklists. Link evidence and give the next useful
validation or implementation step. If implementation is also requested, apply
only the authorized changes and verify the affected behavior before handoff.

---
name: harness-context
description: Manage context and time budgets, account for agent execution/response latency, and create factual continuation checkpoints. Use when context grows, work resumes, or a bounded time/token budget needs management.
---

# Spend context on decisions

Start with a focused file search, then inspect only the matching sections. Reuse
known commands and facts instead of rediscovering the repository. Request bounded
tool output and keep the relevant failure excerpt, not repeated full logs.

Load one relevant skill and its needed references at a time. Do not fetch entire
manuals or repeatedly enumerate unchanged tools. Use a documentation MCP when a
specific unknown justifies it, with public library/version queries. Stop research
when the implementation decision has enough evidence.

For an explicit time budget, reserve integration, result verification,
documentation, and submission time before allocating the remaining time to
implementation or delegation. Include a recovery buffer proportional to the
actual uncertainty. Use observed execution/response durations when available;
label estimates and revise them after the first result or a meaningful delay.
Without a deadline, keep the same ordering without inventing a countdown.

Use one agent unless bounded delegation is authorized and reduces the actual
critical path. Include startup/context transfer, queue/response latency, tool
execution, likely clarification, review, and integration in the estimate. Give
each worker a latest useful return time that still leaves room to verify and
deliver. Do not start a late worker whose result cannot be checked before handoff.
At a checkpoint, compare remaining time with required checks and delivery work;
reduce optional scope or reclaim an overdue task rather than silently waiting
through the reserved verification window. Coordinate ownership before takeover
so two agents do not edit the same files. Report pending/unverified work honestly.

Do not trade correctness checks for cosmetic token savings. Report measured
usage only when a tool supplies it; no invented percentage savings or exact token
counts. Assess AI use by verified, timely delivery and sound delegation decisions,
not the number of workers or the amount of generated code.

Parallel latency is not total token cost. A worker repeats some input context and
adds coordination and integration work. Prefer delegation for a bounded research
question, independent implementation with an agreed contract, or a valuable
read-only review. Keep small fixes and evolving shared designs in one session.
Send only the relevant goal, files, constraints, acceptance check, and desired
output. Avoid full-history cloning where a focused brief is enough. Reconcile
worker findings before integration and never assume separate workers are free.

Before compaction, context handoff, or a session restart, record a brief checkpoint
in an existing work note or `WORKLOG.md`:
- Current goal, hard constraints, and confirmed acceptance criteria.
- Decisions, their reasons, and unresolved questions.
- Changed files and current implementation status.
- Actual verification commands/results and known failures.
- Next concrete action and any running process/session needed to continue.
- If time-bounded: deadline, remaining phase budgets, pending workers, latest
  useful return times, and the fallback that protects verification and delivery.

Do not repeat the transcript or include hidden reasoning. A checkpoint is a
factual work summary. In Codex CLI, use `/compact` only when available and useful;
it is not a substitute for durable project state. After resuming, inspect the
current diff and relevant work note before acting on potentially stale context.

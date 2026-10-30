---
name: harness-context
description: Reduce context waste and create a factual continuation checkpoint for long coding sessions. Use when context grows, work resumes, or a bounded time/token budget needs management.
---

# Spend context on decisions

Start with a focused file search, then inspect only the matching sections. Reuse
known commands and facts instead of rediscovering the repository. Request bounded
tool output and keep the relevant failure excerpt, not repeated full logs.

Load one relevant skill and its needed references at a time. Do not fetch entire
manuals or repeatedly enumerate unchanged tools. Use a documentation MCP when a
specific unknown justifies it, with public library/version queries. Stop research
when the implementation decision has enough evidence.

For an explicit budget, prioritize required behavior, risky integration, then
verification and handoff. Use one agent unless bounded delegation is authorized
and reduces the actual critical path. Do not trade correctness checks for cosmetic
token savings. Report measured usage only when a tool supplies it; no invented
percentage savings or exact token counts.

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

Do not repeat the transcript or include hidden reasoning. A checkpoint is a
factual work summary. In Codex CLI, use `/compact` only when available and useful;
it is not a substitute for durable project state. After resuming, inspect the
current diff and relevant work note before acting on potentially stale context.

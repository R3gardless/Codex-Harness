---
name: harness-test
description: Build a focused test harness and regression suite for important software behavior, API boundaries, and integration failures. Use when implementing or changing testable behavior.
---

# Tests that protect the contract

Use the existing test runner, fixtures, and CI conventions. Identify observable
requirements and failure risks before choosing cases. A small harness should
provide one documented command, deterministic setup, isolated inputs/resources,
clear exit status, and cleanup even after failure.

Choose the cheapest layer that proves each claim:
- Unit: domain rules, boundary conditions, transformations, and error mapping.
- API/contract: schema, status, authorization, object ownership, pagination, and
  backwards compatibility for changed endpoints.
- Integration: database constraints/transactions, filesystem, and adapter
  boundaries. Use temporary databases/directories and controlled fixtures.
- UI components: accessible roles, user input, validation, loading/failure states.
  DOM-level tests do not prove visual layout or real browser behavior.
- End-to-end: the critical flow, using an allowed runtime. If GUI automation is
  prohibited, use service-level integration plus explicit manual UI checks.

For a real bug, preserve the failing example as a regression when practical.
Prefer a demonstrated failure before the fix and success after it. Do not mock
the function being tested, assert only implementation details, or use snapshots
as the sole evidence of correctness. Coverage percentages are secondary to risk.

Keep clocks, randomness, and external responses controlled when necessary.
Tests should not need personal credentials or mutate shared services. Distinguish
mocked integration tests from live ones. Set bounded timeouts; fix nondeterminism
instead of adding arbitrary waits.

Run changed tests and relevant regressions, then the existing required checks.
If a check cannot run, record the command, blocker, and unverified behavior.
Do not reduce assertions, skip a failure silently, or change acceptance criteria
to fit the implementation. Re-run only when a new change or uncertainty warrants it.

Report what the suite protects, actual results, and remaining coverage gaps.

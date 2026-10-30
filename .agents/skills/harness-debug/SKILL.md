---
name: harness-debug
description: Reproduce and resolve a concrete failure, regression, or incorrect output using observable evidence. Use for debugging, not speculative refactoring.
---

# Debug from evidence

Capture the failing command or input, expected result, actual result, and relevant
environment details. Keep sensitive values out of output. Reproduce with the
smallest available example; if reproduction is impossible, state that limitation.

Trace the failing path and form a falsifiable hypothesis. Choose a focused probe
that distinguishes it from plausible alternatives. Change one cause at a time.
After repeated identical failures, inspect new evidence or revise the hypothesis.

Prefer the smallest root-cause fix that preserves the public contract. Avoid
blanket exception handling, fake success responses, broad dependency upgrades,
arbitrary sleeps, or deleting checks to silence a failure.

Rerun the original reproduction after the fix and check nearby behavior that
could regress. Add a regression test when it captures a real, repeatable failure.
Do not write a test that merely duplicates implementation details.

When the failure is environmental, distinguish missing configuration, exhausted
resources, unavailable dependencies, and application defects. Use documented
recovery actions within permission boundaries. Do not alter platform management
processes or repeatedly retry an unchanged blocked operation.

Conclude with cause, change, before/after evidence, and any remaining uncertainty.

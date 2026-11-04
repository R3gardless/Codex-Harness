---
name: harness-build
description: Implement a scoped feature as a working end-to-end slice in an existing project. Use once requirements are concrete; preserve the stack, interfaces, and required artifacts.
---

# Build a useful slice

Find the established build/run/test commands and dependency lockfile. Inspect the
closest existing feature. Do not replace the project's stack to fit a template.
If the project is empty, choose the smallest stack that satisfies the actual
deliverable and available runtime; explain that choice briefly.

Use the existing feature contract to connect one primary flow from input through
domain logic to persistence/output and any required UI. Implement its success
and material failure cases first. If behavior is still undefined, use
[harness-feature-design](../harness-feature-design/SKILL.md) only for the missing
rules; preserve already settled decisions and acceptance cases.

- Apply [harness-frontend](../harness-frontend/SKILL.md) for UI design and behavior,
  [harness-backend](../harness-backend/SKILL.md) for API/service boundaries, and
  [harness-infra](../harness-infra/SKILL.md) when persistence/runtime setup changes.
  Load only the relevant workflow; keep its detailed rules in that skill.
- Keep domain rules explicit and testable. Validate at input boundaries.
- Add persistence, authentication, concurrency, caching, or external services only
  when the requirements justify them. Do not build hypothetical future workloads.
- Use real provided data for the real flow; label fixtures and simulated behavior.
  Do not substitute a mock for a required integration and claim it is complete.
- For a managed preview, check its documented bind address and actual port.
  Use `0.0.0.0` only when that environment requires it. Do not create a public
  tunnel. Give the user the port/path and manual interaction steps.

After each meaningful slice, run the relevant check and report the observable
result. If required behavior cannot be completed, preserve the last working
slice and identify the specific gap. New evidence can change the plan; record
the reason rather than silently adding features.

For longer tasks, update the existing work note with progress, next action, and
verification evidence; use `harness-context` when a continuation checkpoint is needed.

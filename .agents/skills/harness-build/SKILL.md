---
name: harness-build
description: Implement a scoped feature as a working end-to-end slice in an existing project. Use once requirements are concrete; preserve the stack, interfaces, and required artifacts.
---

# Build a useful slice

Find the established build/run/test commands and dependency lockfile. Inspect the
closest existing feature. Do not replace the project's stack to fit a template.
If the project is empty, choose the smallest stack that satisfies the actual
deliverable and available runtime; explain that choice briefly.

Map one primary flow from input to domain logic to persistence/output and, if
required, UI. Define success and a meaningful failure case before implementing.
Build this path first so integration failures appear early.

- Keep domain rules explicit and testable. Validate at input boundaries.
- Add persistence, authentication, concurrency, caching, or external services only
  when the requirements justify them. Do not build hypothetical future workloads.
- Use real provided data for the real flow; label fixtures and simulated behavior.
  Do not substitute a mock for a required integration and claim it is complete.
- For UI work, include meaningful empty, loading, error, and success states where
  applicable, readable labels, keyboard operation, and a layout that fits the
  intended screen. Avoid decorative work that delays the core flow.
- For a managed preview, check its documented bind address and actual port.
  Use `0.0.0.0` only when that environment requires it. Do not create a public
  tunnel. Give the user the port/path and manual interaction steps.

After each meaningful slice, run the relevant check and report the observable
result. If required behavior cannot be completed, preserve the last working
slice and identify the specific gap. New evidence can change the plan; record
the reason rather than silently adding features.

For longer tasks, keep a short checkpoint with completed behavior, next step,
changed files, known issue, and useful commands. Existing project documentation
takes precedence over creating a parallel set of files.

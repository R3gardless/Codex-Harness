---
name: harness-verify
description: Verify an integrated software change against its requirements and prepare a reproducible delivery. Use near handoff or after substantive integration, not after every minor edit.
---

# Verify the delivered behavior

Use the confirmed acceptance criteria and required output contract. For each
material criterion, find an implementation location and an observable check.
Mark it passed, failed, or unverified based on evidence.

Run the project's relevant checks with the current dependencies and documented
commands. Distinguish a clean build from correct behavior. Cover the main flow,
important invalid input, and persistence/restart behavior if promised. Test only
risks relevant to the change; do not invent a broad audit project.

For UI work, verify server readiness and available automated non-GUI checks.
Provide exact manual preview actions and expected results when GUI automation is
not available or not permitted. Do not report visual or interactive checks as
passed unless they were actually observed or the user confirmed them.

Inspect the final diff, filenames, required documents, dependency lockfile, and
startup instructions. Check that credentials and private inputs are not included
in deliverables. Preserve third-party attribution and licenses. A submission
preview may not list every file, so rely on the actual delivery contract.

Do not mutate remote systems, push, publish, or press final submission controls
unless separately authorized. End with what works, exact run/test commands,
their results, and remaining limitations. If time is short, stop optional
features and prioritize a runnable artifact plus accurate status.

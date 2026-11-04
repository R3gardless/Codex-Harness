---
name: harness-verify
description: Verify an integrated software change against its requirements and prepare a reproducible delivery. Use near handoff or after substantive integration, not after every minor edit.
---

# Verify the delivered behavior

Reconcile the existing feature contract with the final implementation: for each
material normal, alternative, or exception case, link its code and observable
check and mark it passed, failed, or unverified. Check affected documentation,
examples, and recovery steps against the same contract; keep open decisions visible.

Run the project's relevant checks with the current dependencies and documented
commands. Distinguish a clean build from correct behavior. Cover the main flow,
important invalid input, and persistence/restart behavior if promised. Test only
risks relevant to the change; do not invent a broad audit project.

For UI, verify readiness and the applicable automated checks, then use the agreed
theme/viewport/state matrix from [harness-frontend](../harness-frontend/SKILL.md).
When GUI automation is unavailable or prohibited, provide manual actions and
expected results. Report visual/interactive checks as passed only when observed
or confirmed by the user; identify the remaining unverified combinations.

For backend/infra, trace the changed request across the agreed layer boundaries.
Reconcile API/authorization and isolated DB/migration evidence from the relevant
implementation checks. Configuration alone does not prove deployment, recovery,
or capacity; match operational claims to observed results.

Inspect the final diff, filenames, required documents, dependency lockfile, and
startup instructions. Check that credentials and private inputs are not included
in deliverables. Preserve third-party attribution and licenses. A submission
preview may not list every file, so rely on the actual delivery contract.

Do not mutate remote systems, push, publish, or press final submission controls
unless separately authorized. End with what works, exact run/test commands,
their results, and remaining limitations. If time is short, stop optional
features and protect the reserved result-review, documentation, and submission
time. Include agent response delays and tool execution in the remaining estimate;
pending worker output is not a verified deliverable. Prioritize a runnable
artifact plus accurate status and distinguish ready-to-submit from submitted.

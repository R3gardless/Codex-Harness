---
name: harness-ideate
description: Develop a feasible product idea for a supplied theme by researching public capabilities, APIs, enterprise features, and open-source options. Use for concept selection or build-versus-reuse decisions.
---

# Research toward a buildable idea

Start with the theme, target user, painful workflow, desired outcome, available
data, allowed integrations, and time budget. If some are unknown, distinguish
assumptions and ask only questions that change the concept. A supplied theme is
not evidence that a particular vendor or model is required.

Inspect available public primary sources: official product docs, API docs,
official repositories, license files, releases, and examples. Use available
authorized search/documentation tools; do not fabricate findings when access is
unavailable. Keep private briefs, datasets, code, and identifiable customer details
out of external queries. Search by generic capability and public technical terms.

Compare a few materially different options, not a long undifferentiated list:

| Option | User value | Verified reusable capability / source | Access and license | Cost / limit / dependency | Smallest proof | Main risk |
| --- | --- | --- | --- | --- | --- | --- |

Separate these categories explicitly: open-source code, public documentation,
public API, free hosted tier, source-available code, and paid enterprise feature.
Public docs do not mean a feature is free, generally available, or usable without
an enterprise contract. Verify licensing and attribution for the exact component;
do not infer rights from a public GitHub repository alone.

For APIs check authentication, quotas, plan restrictions, network/data handling,
and a fallback. For OSS check maintained releases, runtime/dependency fit, license,
setup cost, and the smallest portion worth reusing. Record source and access date.
Do not create accounts, buy plans, install arbitrary code, or connect services
merely because research discovered them.

Recommend a concept by value, feasibility, data availability, measurable outcome,
and integration risk. Describe the core journey, simple architecture, one decisive
validation experiment, non-goals, and a working fallback if the external piece
is unavailable. If the fallback cannot meet a required outcome, say so.

Prefer an end-to-end useful prototype to a collection of novel components.
Hand confirmed scope to `harness-discover`/`harness-build`; record consequential
settled choices and their stated reasons with `harness-design-rationale`. Keep
unselected concepts out of that log. Treat new evidence as a reason
to revise the concept, not to accumulate unvalidated features.

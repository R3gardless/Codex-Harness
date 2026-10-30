---
name: harness-data-check
description: Validate data pipelines, analytics, ranking, retrieval, or model-backed features against a baseline and explicit data contracts. Use only when correctness depends on data or statistical evaluation.
---

# Check the data and the claim

Inspect a small representative sample, schema, types, units, identifiers, missing
values, duplicates, and time boundaries. Use only authorized data and compute.
Identify the decision the output supports before choosing a metric or model.

Create a cheap, interpretable baseline appropriate to the task: a direct rule,
simple aggregation, exact lookup, or existing implementation. Compare changes on
the same examples and conditions. Add complexity only for a demonstrated gap.

For learned or tuned systems, separate development from held-out evaluation. Split
by time, entity, or group when row-wise splitting would leak information. Fit
preprocessing on the permitted training partition. Do not use future information,
target leakage, or hidden evaluation data.

For retrieval or generative features, use a small meaningful case set: answerable,
unanswerable, ambiguous, and malformed inputs. Check source support, unsupported
claims, failure handling, latency, and cost when relevant. Use the provided model
or interface; do not introduce a personal key or external provider. If the task
does not require a model, do not add one.

Record the input version, metric definition and direction, baseline, candidate
result, sample size, and known limitations. Never generalize from a few examples
to a reliable production performance claim. Separate measured results from
estimates and tests that could not be run.

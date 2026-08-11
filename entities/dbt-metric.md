---
title: "dbt:metric"
type: entity
subtype: metamodel-construct
aliases: ["dbt metric"]
tags: [semantic-layer]
concepts: ["[[metric-definition]]"]
sources: ["[[dbt-semantic-layer]]"]
updated: 2026-08-10
---

# dbt:metric

## What it is
A dbt metric is a YAML-defined, centrally maintained business metric in MetricFlow — a
function that combines simple metrics, constraints, or other mathematical functions to
produce a quantitative indicator that downstream tools query through the Semantic Layer.

## Key facts
- Metrics are functions that combine simple metrics, constraints, or other mathematical functions to define new quantitative indicators ⟨dbt: about-metricflow/metrics⟩.
- MetricFlow supports five metric types — simple, ratio, derived, cumulative, and conversion ⟨dbt: metrics-overview/type⟩.
- Simple metrics are defined within a semantic model, while advanced metrics (cumulative, ratio, derived, conversion) that reference metrics from different semantic models are defined at the top level under a separate `metrics` key ⟨dbt: metrics-overview/parameters⟩.
- Required metric parameters are `name` (a unique name of lowercase letters, numbers, and underscores) and `type`; `description`, `label`, `config`, and `filter` are optional ⟨dbt: metrics-overview/parameters⟩.
- A derived metric is an `expr` over other metrics listed in `input_metrics`; a ratio metric is defined by a `numerator` and `denominator`; a cumulative metric aggregates a simple metric over a `window` or `grain_to_date`; a conversion metric tracks a base event followed by a conversion event for an entity within a time window ⟨dbt: metrics-overview/type⟩.
- A `filter` string using Jinja templating can be applied to any metric type, acting as a WHERE clause during metric computation ⟨dbt: metrics-overview/filters⟩.
- Dimensions add context to metrics; without them a metric is simply a number for all time ⟨dbt: about-metricflow/metrics⟩.

## Relations
- Realizes: [[metric-definition]]
- Defined in: [[dbt-semantic-layer]]
- Maintained by: [[org-dbt-labs]]
- Related: [[dbt-measure]] · [[dbt-semantic-model]] · [[dbt-dimension]]

## See also
[[metric-definition]] · [[dbt-measure]] · [[dbt-metricflow]]

---
title: "dbt:simple_metric"
type: entity
subtype: metamodel-construct
aliases: ["dbt simple metric", "dbt measure"]
tags: [semantic-layer]
concepts: ["[[metric-definition]]"]
sources: ["[[dbt-semantic-layer]]"]
updated: 2026-08-10
---

# dbt:simple_metric

## What it is
A simple metric in MetricFlow is a direct aggregation over a single column expression
within a semantic model. It is the foundational building block for more complex metric
types, and replaces the older MetricFlow "measure" construct.

## Key facts
- Simple metrics are metrics that directly reference a single column expression within a semantic model, without any additional columns involved ⟨dbt: about-metricflow/semantic-models⟩.
- Simple metrics are direct aggregations over columns in the data warehouse using different aggregation types, and serve as building blocks for more complex metrics ⟨dbt: semantic-models/simple-metrics⟩.
- The `agg` parameter is required and accepts sum, max, min, average, median, count_distinct, percentile, count, or sum_boolean; `expr` is optional and defaults to the metric name ⟨dbt: metrics-overview/simple-metrics⟩.
- Simple metrics replace measures and are declared within a semantic model with `type: simple` ⟨dbt: semantic-models/components⟩.
- A percentile aggregation requires `percentile` and `percentile_type` (discrete or continuous); a `non_additive_dimension` can restrict aggregation across a dimension via `window_agg` (min or max) ⟨dbt: metrics-overview/simple-metrics⟩.
- Optional properties include `join_to_timespine`, `fill_nulls_with`, `agg_time_dimension`, and `filter` ⟨dbt: metrics-overview/type-specific-parameters⟩.

## Relations
- Realizes: [[metric-definition]]
- Defined in: [[dbt-semantic-layer]]
- Maintained by: [[org-dbt-labs]]
- Related: [[dbt-metric]] · [[dbt-semantic-model]]

## See also
[[metric-definition]] · [[dbt-metric]] · [[dbt-semantic-model]]

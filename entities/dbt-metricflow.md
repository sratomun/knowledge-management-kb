---
title: "MetricFlow"
type: entity
subtype: system
aliases: ["MetricFlow"]
tags: [semantic-layer]
concepts: ["[[semantic-layer]]"]
sources: ["[[dbt-semantic-layer]]"]
updated: 2026-08-10
---

# MetricFlow

## What it is
MetricFlow is the SQL query-generation engine that powers the dbt Semantic Layer. It
is an opinionated set of abstractions that defines the specification for dbt semantic
models and metrics and constructs SQL to retrieve metric datasets from a data platform.

## Key facts
- MetricFlow powers the dbt Semantic Layer and is an opinionated set of abstractions that helps data consumers retrieve metric datasets from a data platform quickly and efficiently ⟨dbt: about-metricflow/MetricFlow⟩.
- MetricFlow handles SQL query construction and defines the specification for dbt semantic models and metrics ⟨dbt: about-metricflow/MetricFlow⟩.
- MetricFlow operates through YAML files where a semantic graph links language to data; the graph comprises semantic models (data entry points) and metrics (functions creating quantitative indicators) ⟨dbt: about-metricflow/semantic-graph⟩.
- MetricFlow is developed and maintained by dbt Labs, is distributed under the Apache 2.0 license, and works with the Apache Ossie format ⟨dbt: about-metricflow/MetricFlow⟩.
- MetricFlow is compatible with dbt version 1.6 and higher and can be used with Snowflake, BigQuery, Databricks, Postgres (dbt Core only), or Redshift ⟨dbt: about-metricflow/prerequisites⟩.
- When generating a metric, MetricFlow uses its SQL engine to find the best path between tables using the framework defined in the semantic-model and metric YAML files ⟨dbt: about-metricflow/semantic-graph⟩.
- MetricFlow constructs any joins needed to reach requested dimensions at query time rather than pre-materializing every possible grouping ⟨dbt: semantic-models/dimensions⟩.
- MetricFlow does not support dbt builtin functions or packages at this time, though support is planned ⟨dbt: about-metricflow/note⟩.

## Relations
- Realizes: [[semantic-layer]]
- Defined in: [[dbt-semantic-layer]]
- Maintained by: [[org-dbt-labs]]
- Related: [[dbt-semantic-model]] · [[dbt-metric]]

## See also
[[semantic-layer]] · [[dbt-semantic-model]] · [[dbt-metric]]

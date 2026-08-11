---
title: "dbt:semantic_model"
type: entity
subtype: metamodel-construct
aliases: ["dbt semantic model"]
tags: [semantic-layer]
concepts: ["[[semantic-model]]"]
sources: ["[[dbt-semantic-layer]]"]
updated: 2026-08-10
---

# dbt:semantic_model

## What it is
A dbt semantic model is the foundational data-definition construct in MetricFlow: a
`semantic_model` block annotating a dbt model with the metadata (entities, dimensions,
and simple metrics) needed for MetricFlow to navigate the semantic graph and generate
metric queries.

## Key facts
- Semantic models are the foundation for data definition in MetricFlow, which powers the dbt Semantic Layer ⟨dbt: semantic-models/overview⟩.
- Each semantic model corresponds to a dbt model in the DAG and requires a unique YAML configuration; each dbt model can define one semantic model via a `semantic_model` block ⟨dbt: semantic-models/overview⟩.
- A semantic model carries three main pieces of metadata — entities (join keys), dimensions (ways to group or slice metrics), and simple metrics (aggregations over a single column) ⟨dbt: about-metricflow/semantic-models⟩.
- Semantic models are the nodes of the semantic graph, connected by entities, and are a subset of the dbt DAG ⟨dbt: about-metricflow/semantic-graph⟩.
- A semantic model requires an `agg_time_dimension` (the default time dimension for its simple metrics) and supports `meta`, `group`, and `enabled` config properties ⟨dbt: semantic-models/components⟩.
- Semantic models can alternatively be defined using Apache Ossie documents instead of dbt's native YAML configuration ⟨dbt: semantic-models/overview⟩.

## Relations
- Realizes: [[semantic-model]]
- Defined in: [[dbt-semantic-layer]]
- Maintained by: [[org-dbt-labs]]
- Related: [[dbt-metricflow]] · [[dbt-entity]] · [[dbt-dimension]] · [[dbt-measure]]

## See also
[[semantic-model]] · [[dbt-metricflow]] · [[dbt-metric]]

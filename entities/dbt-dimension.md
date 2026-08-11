---
title: "dbt:dimension"
type: entity
subtype: metamodel-construct
aliases: ["dbt dimension"]
tags: [semantic-layer]
concepts: ["[[semantic-model]]"]
sources: ["[[dbt-semantic-layer]]"]
updated: 2026-08-10
---

# dbt:dimension

## What it is
A dimension in MetricFlow is a way to group or slice a metric — effectively the
`group by` parameter for metrics. Dimensions are defined at the column level within a
semantic model and are either categorical or time.

## Key facts
- Dimensions are the ways you want to group or slice/dice your metrics ⟨dbt: about-metricflow/semantic-models⟩.
- Dimensions are effectively the group-by parameters for metrics, for example grouping data by region, country, or job title ⟨dbt: semantic-models/dimensions⟩.
- There are two types of dimensions — categorical (non-numeric) and time (dates and timestamps); time dimensions require a column-level granularity ⟨dbt: semantic-models/dimensions⟩.
- Dimensions are bound to the primary entity of the semantic model in which they are defined and are referenced by the fully qualified name `entity__dimension` (for example `user__full_name`) ⟨dbt: semantic-models/dimensions⟩.
- Dimension names must be unique within each semantic model sharing the same primary entity, but may repeat across models with a different primary entity ⟨dbt: semantic-models/dimensions⟩.
- MetricFlow makes dimensions available dynamically, constructing any joins necessary to reach a requested dimension at query time rather than pre-materializing groupings ⟨dbt: semantic-models/dimensions⟩.
- Dimensions that do not match a single physical column can be created with the `derived_semantics` key, which requires the `expr` field ⟨dbt: semantic-models/derived-semantics⟩.

## Relations
- Realizes: [[semantic-model]]
- Defined in: [[dbt-semantic-layer]]
- Maintained by: [[org-dbt-labs]]
- Related: [[dbt-semantic-model]] · [[dbt-entity]] · [[dbt-metric]]

## See also
[[semantic-model]] · [[dbt-entity]] · [[dbt-semantic-model]]

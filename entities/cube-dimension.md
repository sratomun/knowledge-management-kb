---
title: "Cube: dimension"
type: entity
subtype: metamodel-construct
aliases: []
tags: [semantic-layer]
concepts: ["[[semantic-model]]"]
sources: ["[[cube]]"]
updated: 2026-08-10
---

# Cube: dimension

## What it is
A dimension is Cube's construct for an attribute that describes individual rows of data —
the fields consumers group by and filter on, such as status, city, or created_at. Each
dimension maps to a column or SQL expression in the underlying data source.

## Key facts
- Dimensions represent attributes of individual rows — the fields you group by and filter on, such as status, city, product_name, or created_at — and are referred to as categorical data ⟨cube: dimensions⟩.
- Each dimension maps to a column or SQL expression and declares a `type`: `time`, `string`, `number`, or `boolean`, mapping from the SQL data type ⟨cube: dimensions/dimension types⟩.
- Every cube that participates in joins should define a `primary_key` dimension, which Cube uses to avoid fanouts where rows get duplicated during joins and aggregates are over-counted ⟨cube: dimensions/primary keys⟩.
- Time dimensions (type `time`) enable grouping by granularity (year, quarter, month, week, day, hour, minute, second) and support custom granularities such as Sunday-starting weeks or fiscal years ⟨cube: dimensions/time dimensions⟩.
- Proxy dimensions reference dimensions from the same cube or, across joined cubes, from other cubes, reusing definitions and reducing duplication ⟨cube: dimensions/proxy dimensions⟩.
- Subquery dimensions (`sub_query: true`) reference a measure from another cube to turn an aggregate into a per-row value, enabling nested aggregations; dimensions can also be organized into `hierarchies` for drill-down paths ⟨cube: dimensions/subquery dimensions⟩.

## Relations
- Realizes: [[semantic-model]]
- Defined in: [[cube]]
- Published by: [[org-cube-dev]]
- Related: [[cube-cube]], [[cube-measure]]

## See also
[[semantic-model]] · [[semantic-layer]]

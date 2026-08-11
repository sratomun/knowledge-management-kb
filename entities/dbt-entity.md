---
title: "dbt:entity"
type: entity
subtype: metamodel-construct
aliases: ["dbt entity"]
tags: [semantic-layer]
concepts: ["[[semantic-model]]"]
sources: ["[[dbt-semantic-layer]]"]
updated: 2026-08-10
---

# dbt:entity

## What it is
An entity in MetricFlow is a join key of a semantic model — the traversal path (edge)
that connects semantic models in the semantic graph so MetricFlow can join tables to
answer a metric query.

## Key facts
- Entities are the join keys of a semantic model — the traversal paths, or edges, between semantic models ⟨dbt: about-metricflow/semantic-models⟩.
- Entities are declared at the column level with `type` set to primary, foreign, unique, or natural, optionally with `name` and `expr` when the join key's name differs from the column ⟨dbt: semantic-models/entities⟩.
- A primary key has only one record per row and includes every record; a unique key has one record per row but may cover a subset with possible nulls; a foreign key can have zero, one, or many instances with possible nulls; a natural key uniquely identifies a record based on real-world data ⟨dbt: semantic-models/entity-types⟩.
- MetricFlow requires that all dimensions be tied to an entity to guarantee unique dimension names ⟨dbt: semantic-models/primary-entity⟩.
- If no column is marked primary, a top-level `primary_entity` names the model's primary entity; the primary entity need not map to a column and naming it does not affect query generation ⟨dbt: semantic-models/primary-entity⟩.
- Entities that do not match a single physical column can be created with the `derived_semantics` key, which requires the `expr` field ⟨dbt: semantic-models/derived-semantics⟩.

## Relations
- Realizes: [[semantic-model]]
- Defined in: [[dbt-semantic-layer]]
- Maintained by: [[org-dbt-labs]]
- Related: [[dbt-semantic-model]] · [[dbt-dimension]]

## See also
[[semantic-model]] · [[dbt-dimension]] · [[dbt-semantic-model]]

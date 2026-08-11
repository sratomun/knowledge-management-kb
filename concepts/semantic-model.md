---
title: "Semantic Model"
type: concept
tags: [semantic-layer]
related: ["[[semantic-layer]]", "[[metric-definition]]", "[[headless-bi]]"]
updated: 2026-08-10
---

# Semantic Model

## What it is

A semantic model is the structured description of a business domain that a semantic layer reasons over — the entities, their attributes (dimensions), the metrics computed from them, and the relationships (joins) between them. It maps physical tables and columns to business meaning, giving the query engine, BI tools, and AI agents a shared, machine-readable picture of the business to plan queries against.

## How sources treat it

- **[[dbt-semantic-layer]]** _(provider-doc · vendor)_ — Semantic models are the foundation for data definition in MetricFlow; each corresponds to a dbt model in the DAG and is configured via a `semantic_model` block, with a model defining at most one semantic model ⟨dbt: semantic-models/overview⟩
- **[[dbt-semantic-layer]]** _(provider-doc · vendor)_ — A semantic model carries three main pieces of metadata: entities (the join keys / edges), dimensions (ways to group or slice metrics), and simple metrics (aggregations over a single column) ⟨dbt: about-metricflow/semantic-models⟩
- **[[dbt-semantic-layer]]** _(provider-doc · vendor)_ — Entities are declared at the column level with type primary, foreign, unique, or natural, and MetricFlow requires all dimensions be tied to an entity to guarantee unique dimension names; the semantic graph links language to data and is a subset of the DAG ⟨dbt: about-metricflow/semantic-graph⟩
- **[[cube]]** _(provider-doc · vendor)_ — Cube's data model is described as the knowledge graph the platform and any AI agent uses to understand the business; it is dataset-centric, expands on dimensional modeling, and defines metrics, entities, joins, and how they relate ⟨cube: introduction/data modeling⟩
- **[[cube]]** _(provider-doc · vendor)_ — Cubes represent business entities (customers, orders, line items) and define measures, dimensions, and joins; usually one cube per database table, with a base table set via `sql_table`, and every cube that participates in joins should define a `primary_key` dimension to avoid fanouts ⟨cube: getting started/creating a cube⟩
- **[[cube]]** _(provider-doc · vendor)_ — Joins define relationships between cubes using one_to_one, one_to_many, and many_to_one types, and are all directed, placing the source cube on the left of the generated LEFT JOIN ⟨cube: joins/relationship types⟩

## Where sources differ

Both vendors model a business domain as entities, dimensions, metrics, and joins, but structure and terminology diverge. [[dbt-semantic-layer]] binds each semantic model one-to-one to a dbt model in the DAG, configured in a `semantic_model` block, and organizes it as a semantic graph that is a subset of the transformation DAG — tightly coupling the model to dbt's modeling layer. [[cube]] uses "cubes" (typically one per table) composed into "views," calls the whole a knowledge graph "expanding on dimensional modeling," and makes join directionality explicit (directed joins, LEFT JOIN semantics, primary keys to prevent fanouts). dbt's join keys are typed entities (primary/foreign/unique/natural); Cube's joins are typed by cardinality (one_to_one/one_to_many/many_to_one).

## See also
[[semantic-layer]] · [[metric-definition]] · [[headless-bi]]

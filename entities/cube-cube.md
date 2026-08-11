---
title: "Cube: cube"
type: entity
subtype: metamodel-construct
aliases: []
tags: [semantic-layer]
concepts: ["[[semantic-model]]"]
sources: ["[[cube]]"]
updated: 2026-08-10
---

# Cube: cube

## What it is
A cube is the core data-modeling construct in Cube's semantic layer: it represents a
business entity (such as customers, orders, or line items) and groups the measures,
dimensions, and joins defined over a single base table. Usually one cube is created per
database table.

## Key facts
- Cubes are used to organize tables and connections between tables, with usually one cube created for each table in the database, such as users, orders, or products ⟨cube: getting started/creating a cube⟩.
- A cube's base table is defined in the `sql_table` parameter; cubes are authored in YAML or JavaScript and managed in version control ⟨cube: getting started/creating a cube⟩.
- Cubes represent business entities and define measures, dimensions, and joins between entities, upstream of any consumer ⟨cube: introduction/data modeling⟩.
- The data model of cubes is dataset-centric, expanding on dimensional modeling, and is described as the knowledge graph the platform and any AI agent uses to understand the business ⟨cube: introduction/data modeling⟩.
- Every cube that participates in joins should define a `primary_key` dimension, which Cube uses to avoid fanouts where rows get duplicated during joins and aggregates are over-counted ⟨cube: joins/primary key is required when join is defined⟩.
- All business logic — SQL definitions, measure calculations, and join relationships — should live in cubes, with views acting only as a curation layer on top ⟨cube: views/keep shared logic in cubes⟩.

## Relations
- Realizes: [[semantic-model]]
- Defined in: [[cube]]
- Published by: [[org-cube-dev]]
- Related: [[cube-view]], [[cube-measure]], [[cube-dimension]], [[cube-join]]

## See also
[[semantic-model]] · [[semantic-layer]]

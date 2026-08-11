---
title: "Cube — Semantic Layer / Headless BI"
type: source
kind: provider-doc
authority: vendor
subtype: system-documentation
aliases: ["Cube semantic layer"]
publisher: Cube Dev
url: https://cube.dev/docs
version: "current"
published: 2024-01
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [semantic-layer]
updated: 2026-08-10
---

# Cube — Semantic Layer / Headless BI

## Scope & purpose
The Cube documentation describes Cube, an agentic analytics platform for business
intelligence and embedded analytics built on an open-source semantic layer (Cube Core).
Cube centralizes metric definitions, joins, access rules, and caching upstream of every
BI tool, application, and AI agent, exposing a governed data model through standard query
APIs. This is vendor documentation covering the platform's data-modeling constructs
(cubes, views, measures, dimensions, joins), access control, caching, and API surface.

## Structure
The docs are a multi-page manual. Core conceptual pages captured here: the Introduction
(how Cube differs, Semantic SQL, the four architectural pillars — data modeling, access
control, caching, APIs), the Data Modeling "Getting started" tutorial (building a cube
with measures, dimensions, filters, calculated measures, and a view), and the reference-
style concept pages for Views, Joins, Measures, and Dimensions. Models are authored in
YAML or JavaScript and managed in version control (code-first).

## Key points
- Cube is an agentic analytics platform built on a semantic layer serving two primary use cases: internal business intelligence and embedded analytics ⟨cube: introduction⟩.
- At the foundation is Cube Core, an open-source semantic layer that provides the shared context every consumer works from, centralizing metric definitions, joins, access rules, and caching upstream of every BI tool, application, and AI agent ⟨cube: introduction/how is cube different⟩.
- The data model is described as the knowledge graph the platform and any AI agent uses to understand the business; it is dataset-centric, expanding on dimensional modeling, and defines metrics, entities, joins, and how they relate ⟨cube: introduction/data modeling⟩.
- Cubes represent business entities (customers, orders, line items) and define measures, dimensions, and joins between entities; usually one cube is created per database table, with a base table set via the sql_table parameter ⟨cube: getting started/creating a cube⟩.
- Measures are quantitative aggregations across rows (count, sum, avg) and support filtered measures, calculated measures that reference other measures, and multi-stage measures for rolling windows, period-to-date, time shift, percent/share of total, nested aggregates, and ranking ⟨cube: measures⟩.
- Dimensions are attributes of individual rows (the fields you group by and filter on) mapped to a column or SQL expression, typed as time, string, number, or boolean ⟨cube: dimensions/dimension types⟩.
- Every cube that participates in joins should define a primary_key dimension; Cube uses primary keys to avoid fanouts, where rows get duplicated during joins and aggregates are over-counted ⟨cube: dimensions/primary keys⟩.
- Joins define relationships between cubes using three relationship types — one_to_one, one_to_many, and many_to_one — and all joins are directed, placing the source cube on the left side of the generated LEFT JOIN so its rows are preserved ⟨cube: joins/relationship types⟩.
- Cube automatically generates multi-table SQL JOIN clauses when a view combines members from multiple cubes, and views resolve ambiguous "diamond subgraph" paths by specifying an exact join_path ⟨cube: joins/diamond subgraphs⟩.
- Views sit on top of cubes and create a facade of the whole data model; they do not define their own members but reference cubes by join paths and selectively include measures, dimensions, hierarchies, and segments, forming the primary interface for consumers and AI agents ⟨cube: views/how views work⟩.
- Cube AI agents query the semantic layer using Semantic SQL, a Postgres-compatible interface that extends SQL with the MEASURE function; every query is validated against the data model and has access policies applied deterministically before reaching the warehouse ⟨cube: introduction/semantic SQL⟩.
- The semantic layer exposes standard APIs: a Postgres-compatible SQL API (with MEASURE), REST (JSON) and GraphQL for programmatic access, and a Meta API for model introspection so AI agents can discover what is queryable and BI tools can auto-map to the model ⟨cube: introduction/APIs⟩.
- Caching is built on pre-aggregations — rollup tables declared in the data model, refreshed in the background and stored in Cube Store — and an aggregate awareness engine routes incoming queries to a matching pre-aggregation when one exists ⟨cube: introduction/caching⟩.
- Access control runs at the semantic layer so the same code-defined policies (Python or JavaScript, from row-level rules to tenant-aware models) apply to every consumer — AI agents, BI tools, and embedded applications ⟨cube: introduction/access control⟩.
- As vendor documentation, this source presents Cube's own product framing (agentic analytics, "the semantic layer is what makes AI useful") and describes proprietary Cube Cloud features (Workbooks, dashboards, Analytics Chat, Semantic Model IDE) alongside the open-source Cube Core ⟨cube: introduction⟩.

## Concepts & entities covered
Concepts: [[semantic-layer]] · [[semantic-model]] · [[metric-definition]] · [[headless-bi]]
Entities: [[cube-cube]] · [[cube-view]] · [[cube-measure]] · [[cube-dimension]] · [[cube-join]]

---
title: "dbt Semantic Layer"
type: source
kind: provider-doc
authority: vendor
subtype: system-documentation
aliases: ["dbt SL", "dbt Semantic Layer"]
publisher: dbt Labs
url: https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
version: "current"
published: 2024-01
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [semantic-layer]
updated: 2026-08-10
---

# dbt Semantic Layer

## Scope & purpose
The dbt Semantic Layer is dbt Labs' vendor documentation for defining business
metrics centrally in the modeling layer (the dbt project) rather than in the BI
layer, so that different tools and business units query one consistent metric
definition. Powered by MetricFlow, it lets data teams define metrics on top of
existing dbt models, handles data joins automatically, and exposes the metrics to
downstream tools through APIs and first-class integrations. This is vendor system
documentation (dbt Developer Hub), not a normative standard.

## Structure
The material spans a hub page plus the "Build your metrics" conceptual pages. The hub
(`use-dbt-semantic-layer/dbt-sl`) points to get-started, configure (administer,
architecture), deploy (jobs, exports, caching), and consume/integrate (APIs,
integrations) resources. The captured concept pages are: About MetricFlow (the query
engine, semantic graph, principles), Semantic models (components: entities,
dimensions, simple metrics, primary entity, config), and Creating metrics (the five
metric types and their parameters). Reference syntax is YAML, with an alternative
Apache Ossie document format.

## Key points
- The dbt Semantic Layer eliminates duplicate coding by letting data teams define metrics on top of existing models and automatically handling data joins ⟨dbt: dbt-sl/overview⟩.
- The Semantic Layer is powered by MetricFlow and centralizes metric definitions in the modeling layer (the dbt project) so downstream tools get consistent self-service access ⟨dbt: dbt-sl/overview⟩.
- Moving metric definitions out of the BI layer into the modeling layer means a metric definition changed in dbt is refreshed everywhere it is invoked, creating consistency across applications; the Semantic Layer implements access-permission mechanisms for secure access control ⟨dbt: dbt-sl/overview⟩.
- Metrics are defined and queried on a dbt Starter or Enterprise-tier account (multi-tenant or single-tenant); the Semantic Layer APIs let downstream tools query metrics for consistent, reliable data metrics ⟨dbt: dbt-sl/get-started⟩.
- MetricFlow, which powers the Semantic Layer, is an opinionated set of abstractions that handles SQL query construction and defines the specification for dbt semantic models and metrics ⟨dbt: about-metricflow/MetricFlow⟩.
- MetricFlow operates through YAML files where a semantic graph links language to data; the graph comprises semantic models (data entry points) and metrics (functions creating quantitative indicators), and is a subset of the DAG ⟨dbt: about-metricflow/semantic-graph⟩.
- MetricFlow is developed and maintained by dbt Labs, is distributed under the Apache 2.0 license, is compatible with dbt version 1.6 and higher, and works with the Apache Ossie format ⟨dbt: about-metricflow/MetricFlow⟩.
- Semantic models are the foundation for data definition in MetricFlow; each corresponds to a dbt model in the DAG and is configured via a `semantic_model` block, with a model defining at most one semantic model ⟨dbt: semantic-models/overview⟩.
- A semantic model carries three main pieces of metadata: entities (the join keys / edges), dimensions (ways to group or slice metrics), and simple metrics (aggregations over a single column) ⟨dbt: about-metricflow/semantic-models⟩.
- Entities are declared at the column level with type primary, foreign, unique, or natural; MetricFlow requires that all dimensions be tied to an entity to guarantee unique dimension names, and a top-level `primary_entity` names the model's primary entity when no column is primary ⟨dbt: semantic-models/entities⟩.
- Dimensions are the group-by parameters for metrics and are of two types, categorical and time (time dimensions require a column-level granularity); MetricFlow constructs any joins needed to reach requested dimensions at query time rather than pre-materializing groupings ⟨dbt: semantic-models/dimensions⟩.
- Dimensions are bound to the primary entity of their semantic model and referenced by the fully qualified name `entity__dimension` (for example `user__full_name`) ⟨dbt: semantic-models/dimensions⟩.
- MetricFlow supports five metric types — simple, ratio, derived, cumulative, and conversion; simple metrics reference a single column expression, derived metrics are expressions of other metrics, ratio metrics are the ratio of two metrics, cumulative metrics aggregate a simple metric over a window, and conversion metrics track a base event followed by a conversion event for an entity within a time period ⟨dbt: metrics-overview/type⟩.
- Simple metrics are defined within a semantic model, while advanced metrics (cumulative, ratio, derived, conversion) that reference metrics from different semantic models are defined at the top level under a separate `metrics` key ⟨dbt: metrics-overview/parameters⟩.
- Filters use Jinja templating to reference entities, dimensions, time dimensions, or metrics — `{{ Entity(...) }}`, `{{ Dimension(...) }}`, `{{ TimeDimension('time_dimension','granularity') }}`, `{{ Metric(...) }}` — acting as a WHERE clause on any metric type ⟨dbt: metrics-overview/filters⟩.

## Concepts & entities covered
Concepts: [[semantic-layer]] · [[metric-definition]] · [[semantic-model]]
Entities: [[dbt-metricflow]] · [[dbt-semantic-model]] · [[dbt-metric]] · [[dbt-measure]] · [[dbt-dimension]] · [[dbt-entity]]

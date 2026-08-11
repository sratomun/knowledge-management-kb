---
title: "Metric Definition"
type: concept
tags: [semantic-layer]
related: ["[[semantic-layer]]", "[[semantic-model]]", "[[headless-bi]]"]
updated: 2026-08-10
---

# Metric Definition

## What it is

A metric definition is the declarative specification of a business measure — how a number like revenue, active users, or conversion rate is computed from underlying data, including its aggregation, the columns or expressions it draws on, and how it can be sliced. Held centrally in a semantic layer, a single definition is meant to serve every consumer identically, so the same metric returns the same value regardless of which tool asks for it.

## How sources treat it

- **[[dbt-semantic-layer]]** _(provider-doc · vendor)_ — MetricFlow supports five metric types — simple, ratio, derived, cumulative, and conversion; simple metrics reference a single column expression, derived metrics are expressions of other metrics, ratio metrics are the ratio of two metrics, cumulative metrics aggregate a simple metric over a window, and conversion metrics track a base event followed by a conversion event for an entity within a time period ⟨dbt: metrics-overview/type⟩
- **[[dbt-semantic-layer]]** _(provider-doc · vendor)_ — Simple metrics are defined within a semantic model, while advanced metrics (cumulative, ratio, derived, conversion) that reference metrics from different semantic models are defined at the top level under a separate `metrics` key ⟨dbt: metrics-overview/parameters⟩
- **[[dbt-semantic-layer]]** _(provider-doc · vendor)_ — Filters use Jinja templating to reference entities, dimensions, time dimensions, or metrics, acting as a WHERE clause on any metric type ⟨dbt: metrics-overview/filters⟩
- **[[cube]]** _(provider-doc · vendor)_ — Measures are quantitative aggregations across rows (count, sum, avg) and support filtered measures, calculated measures that reference other measures, and multi-stage measures for rolling windows, period-to-date, time shift, percent/share of total, nested aggregates, and ranking ⟨cube: measures⟩
- **[[cube]]** _(provider-doc · vendor)_ — AI agents query metrics through Semantic SQL, a Postgres-compatible interface that extends SQL with the MEASURE function ⟨cube: introduction/semantic SQL⟩
- **[[osi]]** _(whitepaper · informational)_ — Treats metrics as first-class semantic-layer constructs — its spec defines a vendor-neutral, extensible model for data sets, metrics, dimensions, relationships, and contexts interpretable across tools — and points to metrics like churn rate and net margin as the business logic that must not stay locked in proprietary silos ⟨osi: specs §The OSI specification is live⟩

## Where sources differ

The vendor sources describe metrics in their own construct vocabularies: [[dbt-semantic-layer]] names a fixed taxonomy of five metric types (simple, ratio, derived, cumulative, conversion) and distinguishes simple metrics defined inside a semantic model from advanced metrics defined at the top level, whereas [[cube]] calls them "measures," typed as aggregations with filtered, calculated, and multi-stage variants, and exposes them through a MEASURE function in Semantic SQL. [[osi]] does not prescribe a metric implementation at all; it treats "metrics" as one of several semantic-layer constructs its interchange format must carry portably across tools. So the two vendors differ on naming and typing while OSI differs in kind — standardizing exchange rather than computation.

## See also
[[semantic-layer]] · [[semantic-model]] · [[headless-bi]]

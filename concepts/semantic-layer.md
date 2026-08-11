---
title: "Semantic Layer"
type: concept
tags: [semantic-layer]
related: ["[[metric-definition]]", "[[semantic-model]]", "[[headless-bi]]", "[[semantic-interoperability]]"]
updated: 2026-08-10
---

# Semantic Layer

## What it is

A semantic layer is a governed layer that sits between raw data (warehouses, models) and the tools that consume it — BI platforms, applications, and AI agents — holding the business definitions of metrics, dimensions, and relationships in one place. By centralizing that logic upstream of every consumer, it aims to give an organization a single, consistent source of truth for what "revenue" or "churn" means, instead of each tool re-implementing definitions independently.

## How sources treat it

- **[[dbt-semantic-layer]]** _(provider-doc · vendor)_ — Defines business metrics centrally in the modeling layer (the dbt project) rather than in the BI layer, so different tools and business units query one consistent metric definition; a metric changed in dbt is refreshed everywhere it is invoked ⟨dbt: dbt-sl/overview⟩
- **[[dbt-semantic-layer]]** _(provider-doc · vendor)_ — Is powered by MetricFlow, which handles SQL query construction and automatic joins and exposes metrics to downstream tools through APIs and first-class integrations, with access-permission mechanisms for secure control ⟨dbt: about-metricflow/MetricFlow⟩
- **[[cube]]** _(provider-doc · vendor)_ — Cube Core is an open-source semantic layer that provides the shared context every consumer works from, centralizing metric definitions, joins, access rules, and caching upstream of every BI tool, application, and AI agent ⟨cube: introduction/how is cube different⟩
- **[[cube]]** _(provider-doc · vendor)_ — Structures the layer around four pillars — data modeling, access control, caching (pre-aggregations), and APIs (Postgres-compatible SQL with MEASURE, REST, GraphQL, and a Meta API) — with access policies applied deterministically before queries reach the warehouse ⟨cube: introduction/APIs⟩
- **[[osi]]** _(whitepaper · informational)_ — Frames the semantic layer as the "business definitions of metrics, dimensions, and relationships" and seeks a vendor-neutral open standard for exchanging semantic-layer models consistently across data analytics, AI, and BI tools ⟨osi: announce §A Common Semantic Standard⟩
- **[[osi]]** _(whitepaper · informational)_ — Casts the problem as business logic (churn rate, net margin) being locked inside proprietary silos, forcing teams to rebuild the same semantic context repeatedly ⟨osi: specs §intro⟩

## Where sources differ

The three sources agree the semantic layer centralizes business definitions upstream of consumers, but they occupy different positions. [[dbt-semantic-layer]] and [[cube]] are vendor products describing concrete implementations: dbt anchors the layer in the modeling layer (the dbt project) and MetricFlow, while Cube supplies a standalone open-source semantic layer organized around modeling, access control, caching, and APIs and framed as "agentic analytics." [[osi]] is not a product at all but an initiative (both Cube and dbt Labs are founding partners) proposing a vendor-neutral standard for exchanging semantic-layer models between tools — so where the vendors describe how to build a layer, OSI describes how to make competing layers interchange. All three are informational or vendor sources presenting their own framing, not an independently ratified standard.

## See also
[[metric-definition]] · [[semantic-model]] · [[headless-bi]] · [[semantic-interoperability]]

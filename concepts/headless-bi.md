---
title: "Headless BI"
type: concept
tags: [semantic-layer]
related: ["[[semantic-layer]]", "[[semantic-model]]", "[[metric-definition]]"]
updated: 2026-08-10
---

# Headless BI

## What it is

Headless BI decouples the analytics logic — metric definitions, data modeling, joins, access rules, and caching — from any particular visualization front end, exposing it instead through standard query APIs that any BI tool, application, or AI agent can consume. The "headless" idea is that the governed data model lives once, upstream, and many heads (dashboards, notebooks, agents) attach to it, rather than each BI tool owning its own copy of the logic.

## How sources treat it

- **[[cube]]** _(provider-doc · vendor)_ — Cube is an agentic analytics platform for business intelligence and embedded analytics built on an open-source semantic layer (Cube Core) that centralizes metric definitions, joins, access rules, and caching upstream of every BI tool, application, and AI agent, exposing a governed data model through standard query APIs ⟨cube: introduction⟩
- **[[cube]]** _(provider-doc · vendor)_ — Serves two primary use cases from that layer — internal business intelligence and embedded analytics — with Cube Core providing the shared context every consumer works from ⟨cube: introduction/how is cube different⟩
- **[[cube]]** _(provider-doc · vendor)_ — Exposes the layer through standard APIs: a Postgres-compatible SQL API (with MEASURE), REST (JSON) and GraphQL, plus a Meta API for model introspection so AI agents can discover what is queryable and BI tools can auto-map to the model ⟨cube: introduction/APIs⟩
- **[[cube]]** _(provider-doc · vendor)_ — Views sit on top of cubes as a facade of the whole data model, referencing cubes by join paths and selectively including measures, dimensions, hierarchies, and segments, forming the primary interface for consumers and AI agents ⟨cube: views/how views work⟩
- **[[cube]]** _(provider-doc · vendor)_ — Applies access control and caching (pre-aggregation rollups routed by an aggregate-awareness engine) at the semantic layer, so the same code-defined policies apply to every consumer before queries reach the warehouse ⟨cube: introduction/caching⟩

## Where sources differ

Only [[cube]] is cited here, so there is no cross-source disagreement to surface. As vendor documentation, Cube presents its own product framing — "agentic analytics" and "the semantic layer is what makes AI useful" — and describes proprietary Cube Cloud features alongside the open-source Cube Core. Within the corpus, headless BI is the consumption-side face of the [[semantic-layer]]: the [[semantic-model]] and its [[metric-definition]]s are authored once and served through APIs to many front ends rather than embedded in a single BI tool.

## See also
[[semantic-layer]] · [[semantic-model]] · [[metric-definition]]

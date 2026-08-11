---
title: "Cube: view"
type: entity
subtype: metamodel-construct
aliases: []
tags: [semantic-layer]
concepts: ["[[semantic-model]]"]
sources: ["[[cube]]"]
updated: 2026-08-10
---

# Cube: view

## What it is
A view is Cube's curation construct that sits on top of one or more cubes and creates a
business-friendly facade of the data model. Views are the primary interface through which
downstream consumers, BI tools, and AI agents query the semantic layer.

## Key facts
- Views sit on top of the data graph of cubes and create a facade of the whole data model with which data consumers can interact ⟨cube: views⟩.
- Views do not define their own members; instead they reference cubes by specific join paths and selectively include measures, dimensions, hierarchies, and segments from those cubes ⟨cube: views/how views work⟩.
- Views are the primary interface between the data model and users, reshaping the raw cube model into business-friendly datasets, and end-users query data through views ⟨cube: views/why views matter⟩.
- Smaller, focused views are recommended because they are easier for business users to understand, AI agents perform better with focused context, and they translate to simpler SQL queries with fewer joins ⟨cube: views/favor focused views⟩.
- Views can carry curation metadata — `description`, `title`, `meta.ai_context` to guide AI agents, and `folders` to organize fields — and can be hidden via `public: false` or made conditionally visible with `COMPILE_CONTEXT` ⟨cube: views/curate with metadata⟩.
- Views resolve diamond-subgraph join ambiguity by specifying the exact `join_path` for each included cube ⟨cube: joins/diamond subgraphs⟩.

## Relations
- Realizes: [[semantic-model]]
- Defined in: [[cube]]
- Published by: [[org-cube-dev]]
- Related: [[cube-cube]], [[cube-join]]

## See also
[[semantic-model]] · [[headless-bi]]

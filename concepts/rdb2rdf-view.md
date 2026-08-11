---
title: "RDB2RDF View"
type: concept
aliases: []
tags: [obda]
related: ["[[rdb-to-rdf-mapping]]", "[[virtual-knowledge-graph]]", "[[incremental-view-maintenance]]", "[[enterprise-knowledge-graph]]", "[[ontology-based-data-access]]"]
updated: 2026-08-10
---

# RDB2RDF View

## What it is
An RDB2RDF view is an RDF view over relational data: a set of mappings that translate source tuples into RDF triples expressed in a target ontology's vocabulary, exposing legacy relational data as a knowledge graph. The view can be virtual (queried by rewriting) or materialized (its triples computed and stored). It is the mechanism by which relational databases are made accessible through an enterprise knowledge graph.

## How sources treat it
- **[[relational-data-ekg]]** _(article · informational)_ — To make legacy relational data accessible through the organization's knowledge graph it is necessary to create an RDF view over the relational data — an RDB2RDF view — specified by a set of mappings that translate source data into the organization's ontology vocabulary ⟨arXiv 2603.04184 §1⟩
- **[[relational-data-ekg]]** _(article · informational)_ — An RDB2RDF view can be materialized to improve query performance and data availability: a set of mappings M translates a source state into a data graph T, and a query Q over the view is answered by executing Q over T ⟨arXiv 2603.04184 §1⟩
- **[[relational-data-ekg]]** _(article · informational)_ — Defines an RDB2RDF view formally as a triple W = (V, S, M): V the target ontology vocabulary, S the source relational schema, and M a set of mappings defined by transformation rules ⟨arXiv 2603.04184 §3.2⟩
- **[[relational-data-ekg]]** _(article · informational)_ — Uses three transformation-rule types — Class Transformation Rules (CTR), Datatype Property Transformation Rules (DTR), and Object Property Transformation Rules (OTR) — expressed in a DATALOG-based notation simpler than SQL or R2RML yet expressive enough for object-preserving views ⟨arXiv 2603.04184 §3.2⟩
- **[[relational-data-ekg]]** _(article · informational)_ — Introduces the object-preserving property: RDB2RDF views typically preserve the base entities of the source rather than creating new ones, so each view instance corresponds to a database tuple ⟨arXiv 2603.04184 §1⟩

## Where sources differ
Only [[relational-data-ekg]] treats the RDB2RDF view directly, so there is no cross-source disagreement to record. Within it, the notation is positioned relative to existing standards descriptively — the authors' DATALOG-based transformation rules are characterized as simpler than SQL or R2RML while remaining expressive enough for the object-preserving views they target — without claiming superiority over the W3C mapping languages in general.

## See also
[[rdb-to-rdf-mapping]] · [[virtual-knowledge-graph]] · [[incremental-view-maintenance]] · [[enterprise-knowledge-graph]] · [[ontology-based-data-access]]

---
title: "Incremental View Maintenance"
type: concept
aliases: []
tags: [obda]
related: ["[[rdb2rdf-view]]", "[[enterprise-knowledge-graph]]", "[[rdb-to-rdf-mapping]]"]
updated: 2026-08-10
---

# Incremental View Maintenance

## What it is
Incremental view maintenance is keeping a materialized view synchronized with its source under updates by computing and applying only the small set of changes an update induces, rather than recomputing (rematerializing) the whole view. For a materialized RDB2RDF view, this means computing a correct changeset of triples to remove and add for each source-database update, ideally without reading the materialized view itself.

## How sources treat it
- **[[relational-data-ekg]]** _(article · informational)_ — Contrasts rematerialization (recomputing view data at set times) with incremental maintenance (periodically modifying part of the view to reflect updates), noting incremental maintenance generally outperforms full rematerialization and enables live synchronization with only a small delay ⟨arXiv 2603.04184 §1⟩
- **[[relational-data-ekg]]** _(article · informational)_ — Frames maintenance as computing a correct changeset ⟨∆⁻(u), ∆⁺(u)⟩ for an update u, where ∆⁻(u) is the set of triples removed and ∆⁺(u) the set added, required to satisfy M(σ₁) = (M(σ₀) − ∆⁻(u)) ∪ ∆⁺(u) ⟨arXiv 2603.04184 §1⟩
- **[[relational-data-ekg]]** _(article · informational)_ — The algorithm computes a changeset in three steps — identify relations relevant to the update, identify the relevant tuples, and compute ⟨∆⁻(u), ∆⁺(u)⟩ by rematerializing only the RDF state of the relevant tuples ⟨arXiv 2603.04184 §6.1⟩
- **[[relational-data-ekg]]** _(article · informational)_ — Because changesets are computed solely from the update and the source state (no access to the materialized view), the view is self-maintainable, which matters when the view is maintained externally where accessing a remote copy would be too slow ⟨arXiv 2603.04184 §1⟩⟨arXiv 2603.04184 §7⟩
- **[[relational-data-ekg]]** _(article · informational)_ — Implementation uses a single statement-level AFTER trigger per relevant relation to compute and publish the changeset, reconstructing the pre-update state σ₀(R) = (R(σ₁) \ I) ∪ D to correctly evaluate ∆⁻(u) ⟨arXiv 2603.04184 §6.5⟩⟨arXiv 2603.04184 §7⟩

## Where sources differ
Only [[relational-data-ekg]] treats incremental view maintenance, so there is no cross-source disagreement. The source itself contrasts incremental maintenance with the rematerialization alternative and states incremental maintenance generally outperforms full rematerialization; this is reported as the paper's stated position, tied to its self-maintenance and object-preservation assumptions, not adjudicated here.

## See also
[[rdb2rdf-view]] · [[enterprise-knowledge-graph]] · [[rdb-to-rdf-mapping]]

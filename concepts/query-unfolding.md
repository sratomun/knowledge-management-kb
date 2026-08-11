---
title: "Query Unfolding"
type: concept
tags: [obda]
related: ["[[ontology-based-data-access]]", "[[query-rewriting]]", "[[virtual-knowledge-graph]]", "[[rdb-to-rdf-mapping]]"]
updated: 2026-08-10
---

# Query Unfolding

## What it is
The translation of an ontology-level query into a query over the actual data sources by expanding the mapping definitions. Unfolding takes the reformulated query and, using the mappings that connect ontology vocabulary to source structures, produces an executable query (typically SQL) that the source's own engine can run.

## How sources treat it
- **[[xiao-obda-survey]]** _(article · informational)_ — the rewritten query is then unfolded through the mappings into an SQL query executed directly by the relational database engine ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — mappings associate SQL queries over the source with assertions over the ontology vocabulary, and the W3C R2RML standard is a common mapping language ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — optimizations exploit source integrity constraints, mapping saturation, and query containment to reduce rewriting size and improve SQL performance ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — the DL-Lite implementation QuOnto queries data held in any standard RDBMS by relying on ontology-to-relational mappings, the mechanism that connects ontology-level queries to the actual database ⟨§9⟩
- **[[ontop-swj]]** _(article · informational)_ — Ontop's online SPARQL-to-SQL translation (Algorithm 1) replaces each triple-pattern leaf of the SPARQL algebra tree by the union of the T-mapping SQL definitions of its predicate, then maps SPARQL operators (JOIN, OPTIONAL, UNION, FILTER, PROJECT) to their SQL counterparts ⟨§4.2.1⟩
- **[[ontop-swj]]** _(article · informational)_ — because the ontology hierarchy is already compiled into the T-mappings off-line, unfolding a triple pattern via the T-mappings avoids the union that a naive mapping would otherwise introduce, keeping the generated SQL smaller ⟨§4.2.1⟩

## Where sources differ
The OBDA survey names unfolding as a distinct, data-facing phase: after rewriting against the ontology, the mappings are expanded to produce SQL executed directly by the database engine ⟨xiao-obda-survey — IJCAI 2018, pp. 5511-5519⟩. The DL-Lite family paper does not isolate an unfolding step — it models the stored data directly as an ABox and rewrites to first-order queries over it — but it does note that implementations such as QuOnto rely on ontology-to-relational mappings to reach data in a real RDBMS ⟨dl-lite-short-course §9⟩. The Ontop system paper realizes unfolding concretely as the T-mapping-driven leaf replacement inside its bottom-up SPARQL-to-SQL translation, folding the ontology hierarchy into the mappings off-line so that unfolding produces compact SQL ⟨ontop-swj §4.2.1⟩.

## See also
[[query-rewriting]] · [[ontology-based-data-access]] · [[rdb-to-rdf-mapping]]

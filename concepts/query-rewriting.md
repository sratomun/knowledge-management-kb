---
title: "Query Rewriting"
type: concept
tags: [obda]
related: ["[[ontology-based-data-access]]", "[[query-unfolding]]", "[[first-order-rewritability]]", "[[virtual-knowledge-graph]]"]
updated: 2026-08-10
---

# Query Rewriting

## What it is
The reformulation of a user query posed over an ontology into a new query that accounts for the ontology's axioms, so that all answers entailed by the ontology are captured. Rewriting is the step in ontology-based query answering that compiles the meaning of the TBox into the query itself, before the query is evaluated against the data.

## How sources treat it
- **[[xiao-obda-survey]]** _(article · informational)_ — query answering proceeds by rewriting: a user query over the ontology is reformulated to account for the TBox axioms, so ontology-entailed answers are captured ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — perfect rewriting algorithms (e.g. PerfectRef) compute a sound and complete union of conjunctive queries for DL-Lite ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — naive rewritings can blow up combinatorially, motivating optimization techniques such as the tree-witness rewriting and semantic/structural optimizations that use database constraints ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — optimizations exploit source integrity constraints, mapping saturation, and query containment to reduce rewriting size and improve SQL performance ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — AC0 data complexity is characterized concretely: a conjunctive query together with the TBox can be rewritten, independently of the ABox, into a union of conjunctive queries evaluated over the ABox alone ⟨§1⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — the rewritten first-order query can be substantially larger than the original; two sources of blow-up are the sub-formulas testing concept membership (linear in |T| for DL-Lite^{HN}_core, exponential for DL-Lite^{HN}_horn) and a disjunction over paths that is exponential in the number of non-distinguished query variables ⟨§9⟩
- **[[ontop-swj]]** _(article · informational)_ — Ontop answers SPARQL by rewriting it into SQL and delegating execution to the data source, so there is no need to apply rules to the datasource to generate all the facts entailed by the ontology ⟨§4⟩
- **[[ontop-swj]]** _(article · informational)_ — query rewriting is the common strategy for OBDA systems, which makes OWL 2 QL the most suitable OWL profile; to guarantee rewritability, recursion and property chains are disallowed in OWL 2 QL ⟨§6⟩
- **[[ontop-swj]]** _(article · informational)_ — the PerfectRef rewriting used in the early QuOnto system could produce hundreds of thousands of conjunctive queries even for simple ontologies, motivating the later adoption of the tree-witness algorithm and semantic query optimization to shrink rewritings ⟨§7⟩

## Where sources differ
All three cited sources treat rewriting as reformulating a query against the TBox into a union of conjunctive queries. The OBDA survey emphasizes named algorithms and optimizations (PerfectRef, tree-witness, constraint-based) and pairs rewriting with an unfolding step through the mappings ⟨xiao-obda-survey — IJCAI 2018, pp. 5511-5519⟩. The DL-Lite family paper instead treats rewriting as the mechanism realizing AC0 data complexity and analyzes when it is possible and how large the result can grow across the DL-Lite variants, without naming a specific algorithm ⟨dl-lite-short-course §1, §9⟩. The Ontop system paper reports rewriting as an engineering choice whose naive form (PerfectRef) blows up in practice, and describes concrete mitigations — the tree-witness algorithm, T-mappings, and semantic query optimization — used to make rewriting-based query answering executable as efficient SQL ⟨ontop-swj §7⟩.

## See also
[[ontology-based-data-access]] · [[query-unfolding]] · [[first-order-rewritability]]

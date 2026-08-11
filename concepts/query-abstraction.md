---
title: "Query Abstraction"
type: concept
tags: [obda]
related: ["[[certain-answer-semantics]]", "[[query-rewriting]]", "[[query-unfolding]]", "[[ontology-based-data-access]]"]
updated: 2026-08-10
---

# Query Abstraction

## What it is
The reverse of ontological query answering: taking a query written at the data (source) level and translating it up into a query over the ontology that returns the same answers. Where query rewriting and unfolding push an ontological query down to the data, abstraction lifts a data query up to the conceptual layer. A translation that returns exactly the source query's answers is a "perfect" abstraction; when none exists, one settles for best over- or under-approximations.

## How sources treat it
- **[[obda-query-abstractions]]** _(article · informational)_ — query abstraction is the translation of a data query into an ontological query — the opposite direction of query answering, where an ontological query is rewritten and unfolded down to the data level ⟨§1⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — the OBDA setting uses existential rules (TGDs) for both the mapping — yielding GLAV mappings — and the ontology, letting the same tools (the chase and query rewriting) handle both ⟨§1⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — motivating scenarios include checking during OBDA design whether the mapping covers important data queries, reverse-engineering the semantics of source-level data services, and improving open-data semantics and the FAIRness of data services ⟨§1⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — a perfect abstraction of a data (U)CQ need not exist at all, even with an empty ontology, because mappings may fail to transfer all answers or may make distinct source relations indistinguishable ⟨§1⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — when no perfect abstraction exists one seeks best approximations within a target class: a minimally complete abstraction (a minimal superset of the source answers) and a maximally sound abstraction (a maximal subset) ⟨§2⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — it distinguishes M-abstraction (data integration, ignoring the ontology) from Σ-abstraction (full OBDA specification Σ = (S, O, M, R) including the ontology) ⟨§2⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — it introduces the query class UCQ≠,C (UCQs with a limited inequality and a special unary predicate C marking database-originating values); a perfect Σ-abstraction, when it exists, is always expressible in UCQ≠,C, which is a minimal language with this property ⟨§3, §4⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — a minimally complete abstraction is obtained by chasing Q_S with the mapping M (a modified chase); existence of a complete abstraction is characterized by each answer variable being reachable through some mapping rule's frontier ⟨§4⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — maximally sound abstractions are characterized via a link to maximum recovery from data exchange; expressing such a maximum recovery requires disjunction in rule heads, beyond GLAV, and the ontology plays no role in minimal completeness but does in maximal soundness ⟨§5⟩

## Where sources differ
Only one source in this KB, the Leclère–Mugnier–Pérution-Kihli paper, treats query abstraction directly, so no cross-source disagreement is recorded. Internally the paper positions abstraction as the inverse of the rewriting-and-unfolding direction that the other OBDA sources describe, and separates the ontology-free M-abstraction from the ontology-aware Σ-abstraction, noting the ontology matters for maximal soundness but not for minimal completeness ⟨obda-query-abstractions §1, §2, §5⟩.

## See also
[[certain-answer-semantics]] · [[query-rewriting]] · [[query-unfolding]] · [[ontology-based-data-access]]

---
title: "Certain-Answer Semantics"
type: concept
tags: [obda]
related: ["[[query-rewriting]]", "[[first-order-rewritability]]", "[[query-abstraction]]", "[[ontology-based-data-access]]"]
updated: 2026-08-10
---

# Certain-Answer Semantics

## What it is
The correct notion of an answer when data is incomplete and interpreted under the open-world assumption, as in ontology-based data access. A tuple is a certain answer to a query if it holds in every model of the ontology together with its data — that is, no matter how the missing information could consistently be filled in. Because the ontology entails facts beyond those explicitly stored, certain answering is what query rewriting and query abstraction are designed to compute.

## How sources treat it
- **[[poggi-linking-data]]** _(article · informational)_ — a conjunctive query is answered by computing certain answers — tuples that hold in every model of the ontology (with mappings) — which is the correct semantics under incomplete information ⟨§2⟩⟨§3⟩
- **[[poggi-linking-data]]** _(article · informational)_ — the reformulation step PerfectRef rewrites a UCQ against the TBox into a new UCQ whose evaluation over the data alone yields the certain answers, compiling all relevant TBox knowledge into the query ⟨§2⟩⟨§4⟩
- **[[poggi-linking-data]]** _(article · informational)_ — mapping assertions capture the closed-world semantics of the database by evaluating Φ as a standard relational query, while the open-world semantics of the ontology allows additional facts beyond those the mapping supplies ⟨§3⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — the family's query-answering results concern positive existential query answering, whose data complexity (AC0 for the tractable logics) is exactly what makes certain answers computable by rewriting the query and TBox, independently of the ABox, into a union of conjunctive queries over the ABox ⟨§1, §7⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — dropping the unique name assumption and allowing equality between object names raises the AC0 memberships to LogSpace-completeness and destroys first-order rewritability of query answering ⟨§1, §8⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — the OBDA setting is based on existential rules with GLAV mappings and certain-answer semantics, under which sound / complete / perfect abstractions are all defined ⟨§1, §2⟩
- **[[obda-query-abstractions]]** _(article · informational)_ — formally an ontological query Q_O is a complete Σ-abstraction of Q_S if Q_S(D) ⊆ Q_O^cert(D,Σ) for all databases D, a sound Σ-abstraction if Q_O^cert(D,Σ) ⊆ Q_S(D), and a perfect Σ-abstraction if it is both — all under the certain-answer semantics ⟨§2⟩

## Where sources differ
The three sources share the same semantics — answers that hold in every model — but use it toward different ends. Poggi et al. define certain answers as the target that the reformulation-unfolding-evaluation method must soundly and completely compute ⟨poggi-linking-data §2, §4⟩. The DL-Lite short course treats certain answering as a complexity object, locating which logics keep positive existential query answering in AC0 and hence first-order rewritable, and when the unique name assumption breaks that ⟨dl-lite-short-course §1, §7, §8⟩. The query-abstraction paper takes certain-answer semantics as the fixed yardstick against which soundness, completeness, and perfectness of an abstraction are defined, applying it to the reverse (data-to-ontology) direction ⟨obda-query-abstractions §2⟩.

## See also
[[query-rewriting]] · [[first-order-rewritability]] · [[query-abstraction]] · [[ontology-based-data-access]]

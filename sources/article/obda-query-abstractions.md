---
title: "Abstractions of Queries in Ontology-Based Data Access"
type: source
kind: article
authority: informational
subtype: academic-paper
aliases: ["arXiv:2606.24618"]
publisher: arXiv
url: https://arxiv.org/abs/2606.24618
version: "arXiv:2606.24618"
published: 2026-06
effective_from: 2026-06
effective_to: ongoing
status: current
tags: [obda, semantic-web]
updated: 2026-08-10
---

# Abstractions of Queries in Ontology-Based Data Access

## Scope & purpose
A theoretical study, by Michel Leclère, Marie-Laure Mugnier and Guillaume Pérution-Kihli (LIRMM, Inria, University of Montpellier, CNRS), of *query abstraction* in ontology-based data access — the task of translating a data-level query up to the ontology layer, i.e. the reverse of the usual ontological query answering / rewriting direction. It works in an OBDA setting based on existential rules (TGDs) with GLAV mappings and certain-answer semantics, and asks when a source query can be re-expressed as an ontological query that returns the same answers (a *perfect* abstraction), and how to approximate one when it cannot. The arXiv item is an extended version of the KR 2025 paper, adding detailed proofs and further examples in an appendix.

## Structure
The paper runs: an introduction motivating query abstraction and stating three contributions (§1); preliminaries fixing database/existential-rule theory, the chase, query rewriting, OBDA specifications, and formal definitions of sound/complete/perfect and minimally-complete/maximally-sound abstractions (§2); a study of the extended query class UCQ≠,C and its complexity (§3); computation of minimally complete and perfect abstractions via a (modified) chase (§4); a characterization of maximally sound abstractions through a connection to *maximum recovery* from data exchange (§5); and a conclusion with open questions (§6). An appendix supplies full proofs.

## Key points
- The OBDA setting uses existential rules (aka TGDs) for both the mapping — yielding Global-Local-As-View (GLAV) mappings — and the ontology, generalizing classical Horn-description-logic frameworks and letting the same tools (the chase and query rewriting) handle both ⟨§1⟩
- Query abstraction is the translation of a data query into an ontological query — the opposite direction of query answering, where an ontological query is rewritten and unfolded down to the data level ⟨§1⟩
- Motivating scenarios: checking during (incremental) OBDA design whether the mapping adequately covers important data queries; reverse-engineering / characterizing the semantics of data services implemented at the source level; and improving open-data semantics and the FAIRness of data services ⟨§1⟩
- A perfect abstraction of a data (U)CQ need not exist at all, even with an empty ontology, because mappings may fail to transfer all answers or may make distinct source relations indistinguishable (Example 1: s1(u) has no perfect abstraction when both s1 and s2 map to r) ⟨§1⟩
- When no perfect abstraction exists, one seeks best approximations within a target query class: a minimally complete abstraction (a minimal superset of the source query's answers) and a maximally sound abstraction (a maximal subset) ⟨§2⟩
- Formally, an ontological query Q_O is a complete Σ-abstraction of Q_S if Q_S(D) ⊆ Q_O^cert(D,Σ) for all databases D, a sound Σ-abstraction if Q_O^cert(D,Σ) ⊆ Q_S(D), and a perfect Σ-abstraction if it is both — all under the certain-answer semantics ⟨§2⟩
- The paper distinguishes M-abstraction (data integration, ignoring the ontology R) from Σ-abstraction (full OBDA specification Σ = (S, O, M, R) including the ontology) ⟨§2⟩
- It introduces the query class UCQ≠,C: UCQs extended with a limited inequality (variables in a ≠-atom must map to constants) and a special unary predicate C marking values that come from the database (C originates in Fagin et al.'s inverse-mapping work) ⟨§3⟩
- Extending UCQ to UCQ≠,C does not raise complexity: verifying whether a candidate M-abstraction is perfect stays Π^P_2-complete ⟨§3⟩
- An FO-rewritable existential-rule fragment is exhibited for which perfectness verification of a Σ-abstraction remains in Π^P_2, subsuming earlier DL-Lite results ⟨§3⟩
- A non-Boolean query Q_S may have no complete abstraction; existence is characterized purely by interactions between Q_S and the mapping — each answer variable must be reachable through some mapping rule's frontier (Proposition 11) ⟨§4⟩
- For a query that has one, a minimally complete abstraction is obtained by chasing Q_S with M (a modified chase); UCQ≠,C can in fact express a minimally complete M- and Σ-abstraction of any source UCQ≠,C, minimal with respect to all ontological queries answered under certain-answer semantics ⟨§4⟩
- Consequently a perfect Σ-abstraction, when it exists, is always expressible in UCQ≠,C, and UCQ≠,C is a minimal language with this property even when the source query is a plain UCQ ⟨§4⟩
- Deciding whether a perfect M-abstraction of a UCQ≠,C exists is Π^P_2-complete when mapping rules have bounded-size frontier, and in Co-NExpTime otherwise ⟨§4⟩
- Maximally sound abstractions are characterized via a new link to *maximum recovery* from data exchange: a maximally sound M-abstraction of a source UCQ≠,C Q_S is precisely the rewriting of Q_S with a maximum recovery of the mapping M ⟨§5⟩
- Expressing such a maximum recovery requires disjunction in rule heads (beyond GLAV); the paper corrects a mistaken literature claim that a maximum recovery for CQs is always expressible by a conjunctive (disjunction-free) mapping, and extends maximum recovery to OBDA specifications, showing it is still expressible by the same disjunctive mapping when the ontology is FO-rewritable (fus) — the ontology plays no role in minimal completeness but does in maximal soundness ⟨§5⟩

## Concepts & entities covered
Concepts: [[query-abstraction]] · [[ontology-based-data-access]] · [[query-rewriting]] · [[query-unfolding]] · [[first-order-rewritability]]
Entities: [[ucq-ineq-c]]

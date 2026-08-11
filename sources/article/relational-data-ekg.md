---
title: "Publication and Maintenance of Relational Data in Enterprise Knowledge Graphs"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["RDB2RDF view publication and maintenance"]
publisher: "arXiv"
url: https://arxiv.org/abs/2603.04184
version: "v1 (revised version), arXiv:2603.04184 [cs.DB]"
published: 2026-03
effective_from: 2026-03
effective_to: ongoing
status: current
tags: [obda]
concepts: ["[[rdb2rdf-view]]", "[[incremental-view-maintenance]]", "[[enterprise-knowledge-graph]]", "[[rdb-to-rdf-mapping]]"]
entities: ["[[rdb2rdf-view-maintenance]]"]
updated: 2026-08-10
---

# Publication and Maintenance of Relational Data in Enterprise Knowledge Graphs

## Scope & purpose

A revised-version article by Vânia Maria Ponte Vidal, Valéria Magalhães Pequeno, Marco Antonio Casanova, Narciso Arruda, and Carlos Brito (Universidade Federal do Ceará, Universidade Autónoma de Lisboa, PUC-Rio), posted to arXiv as 2603.04184 [cs.DB] in March 2026. It addresses how to make legacy relational data accessible through an enterprise knowledge graph (EKG) by creating an RDF view over the relational data (an RDB2RDF view), materializing that view to improve query performance and data availability, and then keeping the materialized view continuously synchronized with source-database updates. Its central contribution is a formal framework — a first-order/DATALOG-based rule formalism plus algorithms — for constructing the materialized data graph and for INCREMENTALLY maintaining it by computing correct changesets, illustrated with a MusicBrainz case study ⟨arXiv 2603.04184 §Abstract⟩⟨arXiv 2603.04184 §1⟩.

## Structure

- §1 Introduction — EKGs as a semantic data layer; RDB2RDF views; materialization; incremental maintenance vs. rematerialization; the changeset problem (Fig. 1); the three challenges (simplicity, efficiency, self-maintenance) and three key ideas (object-preservation, the mapping formalism, named graphs).
- §2 Related Work — incremental view maintenance for relational, object-oriented, semi-structured and XML views; duplicate handling; prior RDF/RDB2RDF maintenance approaches; positioning against reference [33].
- §3 Object-Preserving RDB2RDF Views — §3.1 basic concepts and notation (relation schemes, foreign keys, relational paths, related tuples); §3.2 the formalism for specifying object-preserving views (CTR/DTR/OTR transformation rules, TR patterns).
- §4 Case Study: MusicBrainz RDF — fragment of the MusicBrainz PostgreSQL schema and target ontology (FOAF, Music Ontology, Dublin Core); a set of example transformation rules.
- §5 Materialization of an RDB2RDF view — duplicate-triple handling; named graphs; the RDF-state definitions (per rule, per pivot tuple, per view).
- §6 Formal Framework for Computing Correct Changesets — §6.1 overview (three steps); §6.2 formal definitions; §6.3 computation of ∆⁻(u) and ∆⁺(u); §6.4 MusicBrainz changeset example; §6.5 generating triggers.
- §7 Conclusions and Final Remarks.

## Key points

- An enterprise knowledge graph (EKG) is presented as a paradigm for consolidating and semantically integrating many heterogeneous data sources into a comprehensive dataspace, whose goal is a unified data layer semantically connected to enterprise data so applications get integrated access through the semantic layer, supporting ad hoc queries without complex preprocessing ⟨arXiv 2603.04184 §1⟩
- A key element of an EKG is the ontology, which describes all information in the knowledge graph and serves as the semantic layer that combines and enriches source data into a unified view that users and applications can query transparently ⟨arXiv 2603.04184 §1⟩
- To make legacy relational data accessible through the organization's knowledge graph it is necessary to create an RDF view over the relational data — an RDB2RDF view — specified by a set of mappings that translate source data into the organization's ontology vocabulary ⟨arXiv 2603.04184 §1⟩
- An RDB2RDF view can be materialized to improve query performance and data availability: a set of mappings M translates a source state into a data graph T, and a query Q over the view is answered by executing Q over T ⟨arXiv 2603.04184 §1⟩
- A materialized view must be continuously maintained; the authors contrast rematerialization (recomputing view data at set times) with incremental maintenance (periodically modifying part of the view to reflect updates), noting incremental maintenance generally outperforms full rematerialization and enables live synchronization with only a small delay ⟨arXiv 2603.04184 §1⟩
- Maintenance is framed as computing a correct changeset ⟨∆⁻(u), ∆⁺(u)⟩ for an update u, where ∆⁻(u) is the set of triples removed and ∆⁺(u) the set added, required to satisfy M(σ₁) = (M(σ₀) − ∆⁻(u)) ∪ ∆⁺(u) so the incrementally updated view equals the rematerialized view ⟨arXiv 2603.04184 §1⟩
- The solution targets three challenges — simplicity (minimize infrastructure complexity), efficiency (identify the minimal data needed to correctly maintain the view), and self-maintenance (compute the changeset solely from the update and the source database state, without accessing the materialized view) ⟨arXiv 2603.04184 §1⟩
- The first key idea is the object-preserving property: RDB2RDF views typically preserve the base entities (objects) of the source rather than creating new ones, so each view instance corresponds to a database tuple, letting the framework precisely identify the tuples relevant to an update and rematerialize only their RDF image ⟨arXiv 2603.04184 §1⟩
- The second key idea is a formalism, based on first-order logic and widely adopted in OBDA, data exchange and data integration, for specifying object-preserving view mappings; queries on the right-hand side of transformation rules are expressed in a DATALOG-based notation simpler than SQL or R2RML yet expressive enough for object-preserving views ⟨arXiv 2603.04184 §1⟩⟨arXiv 2603.04184 §3.2⟩
- An RDB2RDF view is defined as a triple W = (V, S, M): V the target ontology vocabulary, S the source relational schema, and M a set of mappings defined by transformation rules ⟨arXiv 2603.04184 §3.2⟩
- Three transformation-rule types are used: Class Transformation Rules (CTR, mapping pivot-relation tuples to class instances via a hasURI predicate over primary keys), Datatype Property Transformation Rules (DTR, extracting attribute values from the pivot tuple or path-reachable tuples), and Object Property Transformation Rules (OTR, relating instances across a relational path); the predicate B[r,x] must define a partial one-to-one function so tuples and instances are semantically equivalent (r ≡ x) ⟨arXiv 2603.04184 §3.2⟩
- The third key idea is that view content is stored in an RDF dataset of named graphs (quads) that record the context in which triples were produced, so duplicate triples produced from different pivot relations land in different named graphs — a property used to prove correct changeset computation ⟨arXiv 2603.04184 §1⟩⟨arXiv 2603.04184 §5⟩
- Materialization is defined via RDF-state functions: RDF State[Ψ](p,σ) gives the quads a rule Ψ produces for pivot tuple p, RDF State[R\*](p,σ) unions over all rules with pivot R\*, and RDF State(W,σ) unions RDF states of all pivot tuples of all pivot relations of the view ⟨arXiv 2603.04184 §5⟩
- The incremental-maintenance algorithm computes a changeset in three steps — identify relations relevant to the update, identify the relevant tuples in those relations, and compute ⟨∆⁻(u), ∆⁺(u)⟩ by rematerializing only the RDF state of the relevant tuples; relevant tuples before the update (RTB) are evaluated over σ₀ and relevant tuples after (RTA) over σ₁, using relational-path prefixes to reach affected pivot tuples ⟨arXiv 2603.04184 §6.1⟩⟨arXiv 2603.04184 §6.2⟩⟨arXiv 2603.04184 §6.3⟩
- Because changesets are computed solely from the update and the source state (no access to the materialized view), the view is self-maintainable, which matters when the view is maintained externally where accessing a remote copy would be too slow ⟨arXiv 2603.04184 §1⟩⟨arXiv 2603.04184 §7⟩
- Implementation uses a single statement-level AFTER trigger per relevant relation to compute and publish the changeset; since the trigger fires when the database is already in state σ₁, the pre-update state of R is reconstructed as σ₀(R) = (R(σ₁) \ I) ∪ D to correctly evaluate ∆⁻(u), and a tool to auto-generate such triggers from the view mappings is under development ⟨arXiv 2603.04184 §6.5⟩⟨arXiv 2603.04184 §7⟩

## Concepts & entities covered
Concepts: [[rdb2rdf-view]] · [[incremental-view-maintenance]] · [[enterprise-knowledge-graph]] · [[rdb-to-rdf-mapping]]
Entities: [[rdb2rdf-view-maintenance]]

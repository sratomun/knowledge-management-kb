---
title: "Incremental RDB2RDF view maintenance (Vidal et al.)"
type: entity
subtype: technique
aliases: ["object-preserving changeset maintenance"]
tags: [obda]
status: current
concepts: ["[[incremental-view-maintenance]]", "[[rdb2rdf-view]]", "[[rdb-to-rdf-mapping]]", "[[enterprise-knowledge-graph]]"]
sources: ["[[relational-data-ekg]]"]
updated: 2026-08-10
---

# Incremental RDB2RDF view maintenance (Vidal et al.)

## What it is
A formal framework and algorithm, proposed by Vidal, Pequeno, Casanova, Arruda and Brito (arXiv 2603.04184), for incrementally maintaining a materialized RDB2RDF view over a relational source: when the database is updated, it computes a correct changeset ⟨∆⁻(u), ∆⁺(u)⟩ of RDF triples to remove and add, rematerializing only the portion of the view affected by the update. It exploits the object-preserving property of typical RDB2RDF views and stores view content as named graphs so it can be maintained without accessing the materialized view.

## Key facts
- A correct changeset for update u is a pair ⟨∆⁻(u), ∆⁺(u)⟩ of removed and added triples satisfying M(σ₁) = (M(σ₀) − ∆⁻(u)) ∪ ∆⁺(u), i.e. the incrementally updated view must equal the view obtained by rematerialization ⟨arXiv 2603.04184 §1⟩
- The approach pursues three goals: simplicity of the maintenance infrastructure, efficiency (identifying the minimal data needed for correct maintenance), and self-maintenance — computing the changeset solely from the update and the source state, with no access to the materialized view ⟨arXiv 2603.04184 §1⟩
- It applies only to object-preserving views, which preserve the base entities (objects) of the source rather than creating new ones, so each RDF instance corresponds to a database tuple and the tuples relevant to an update can be precisely identified ⟨arXiv 2603.04184 §1⟩
- View mappings are specified by transformation rules (CTR, DTR, OTR) in a DATALOG-based first-order formalism, where a pivot relation's tuples anchor the subject URIs (built by a hasURI predicate over primary keys) and B[r,x] defines a partial one-to-one correspondence r ≡ x between tuples and instances ⟨arXiv 2603.04184 §3.2⟩
- The changeset algorithm has three steps: identification of relevant relations, identification of relevant tuples, and computation of the changeset by rematerializing only the RDF state of the relevant tuples ⟨arXiv 2603.04184 §6.1⟩
- Relevant tuples before the update (RTB) are computed over the pre-update state σ₀ and relevant tuples after (RTA) over the post-update state σ₁; a pivot tuple is relevant either because it is directly in the deleted/inserted set (pivot-relation case) or because it is reachable from an affected tuple along a prefix of the rule's relational path ⟨arXiv 2603.04184 §6.2⟩⟨arXiv 2603.04184 §6.3⟩
- ∆⁻(u) is the union of RDF states of RTB tuples evaluated over σ₀, and ∆⁺(u) is the union of RDF states of RTA tuples evaluated over σ₁ ⟨arXiv 2603.04184 §6.3⟩
- View content is stored as an RDF dataset of named graphs (quads); duplicate triples produced from different pivot relations are placed in different named graphs, which the framework relies on to correctly handle deletes and prove changeset correctness ⟨arXiv 2603.04184 §5⟩
- Implementation uses a single statement-level AFTER trigger per relevant relation; because the trigger fires in state σ₁, the pre-update state is reconstructed as σ₀(R) = (R(σ₁) \ I) ∪ D to evaluate ∆⁻(u) correctly ⟨arXiv 2603.04184 §6.5⟩
- The method extends prior trigger-based synchronization work (reference [33]) to more complex mapping rules and is characterized as "tracking the relevant tuples in the pivot relations for a given update" rather than tracking updated triples in the view; a tool to auto-generate the triggers from the view mappings is under development ⟨arXiv 2603.04184 §2⟩⟨arXiv 2603.04184 §7⟩

## Relations
- Realizes: [[incremental-view-maintenance]]
- Applies to: [[rdb2rdf-view]]
- Defined in: [[relational-data-ekg]]
- Related: [[rdb-to-rdf-mapping]] · [[enterprise-knowledge-graph]]

## See also
[[rdb2rdf-view]] · [[incremental-view-maintenance]] · [[enterprise-knowledge-graph]]

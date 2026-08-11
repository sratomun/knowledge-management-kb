---
title: "T-mappings"
type: entity
subtype: technique
aliases: ["saturated mappings", "mapping saturation"]
tags: [obda]
concepts: ["[[rdb-to-rdf-mapping]]", "[[query-rewriting]]"]
sources: ["[[ontop-swj]]"]
updated: 2026-08-10
---

# T-mappings

## What it is
T-mappings are Ontop's saturated mappings: mappings obtained by composing the classified
ontology class/property hierarchy with the user-supplied mappings, so that the RDF triples
entailed by the ontology are captured directly in the mapping layer and can be used to
translate SPARQL triple patterns into SQL without further ontology reasoning at query time.

## Key facts
- The most critical task during Ontop's off-line stage is compiling the ontology into the mappings and generating the so-called T-mappings ⟨ontop-swj §4⟩⟨ontop-swj §4.1⟩.
- T-mappings are constructed by composing the complete class and property hierarchies with the mappings, so that a concept with no user-defined mapping (e.g. :Neoplasm, inferred from its subclasses) still receives mapping rules ⟨ontop-swj §4.1⟩.
- T-mappings are optimized using SQL disjunction (OR) and interval expressions and semantic query optimization (SQO); this is relatively expensive (SQO uses an NP-complete conjunctive-query-containment check) but is performed only once off-line, giving negligible online cost ⟨ontop-swj §4.1⟩.
- The resulting T-mappings define all the RDF triples inferable from the database and the ontology, and during the online stage they are the basis for translating individual SPARQL triple patterns into SQL ⟨ontop-swj §4.1⟩.
- The tree-witness query rewriting algorithm was implemented specifically to take advantage of the T-mappings (and the Semantic Index) and to reduce the size of rewritings ⟨ontop-swj §7⟩.
- Ultrawrap uses an analogue of Ontop's T-mappings, called saturated mappings, which are used for creating regular and materialized views in the relational database ⟨ontop-swj §6⟩.

## Relations
- Realizes: [[rdb-to-rdf-mapping]]
- Realizes: [[query-rewriting]]
- Defined in: [[ontop-swj]]
- Related: [[ontop]] · [[tree-witness-rewriting]] · [[r2rml]]

## See also
[[ontop]] · [[tree-witness-rewriting]] · [[rdb-to-rdf-mapping]]

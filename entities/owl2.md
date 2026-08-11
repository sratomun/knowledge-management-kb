---
title: "OWL 2"
type: entity
subtype: formalism
aliases: []
tags: [semantic-web]
concepts: ["[[description-logic]]"]
sources: ["[[owl2-overview]]", "[[owl2-profiles]]"]
updated: 2026-08-10
---

# OWL 2

## What it is
The OWL 2 Web Ontology Language (informally OWL 2) is an ontology language for the
Semantic Web with formally defined meaning; OWL 2 ontologies provide classes, properties,
individuals, and data values, are stored as Semantic Web documents, and are an extension
and revision of the OWL 1 language published in 2004.

## Key facts
- OWL 2 ontologies can be used along with information written in RDF, and OWL 2 ontologies themselves are primarily exchanged as RDF documents ⟨owl2-overview Abstract⟩.
- An OWL 2 ontology can be understood either as an abstract structure or, equivalently, as an RDF graph, with the Mapping to RDF Graphs document defining the mapping between the two views ⟨owl2-overview §2.1⟩.
- The primary exchange syntax for OWL 2 is RDF/XML; this is indeed the only syntax that must be supported by all OWL 2 tools ⟨owl2-overview §2.2⟩.
- Two semantic specifications assign meaning to OWL 2 ontologies — the Direct Semantics (compatible with the SROIQ description logic, giving "OWL 2 DL") and the RDF-Based Semantics (giving "OWL 2 Full") — linked by a correspondence theorem ⟨owl2-overview §2.3⟩.
- Backwards compatibility with OWL 1 is, to all intents and purposes, complete: all OWL 1 ontologies remain valid OWL 2 ontologies with identical inferences in all practical cases ⟨owl2-overview §3⟩.
- OWL 2 adds new expressivity over OWL 1, including keys, property chains, richer datatypes and data ranges, qualified cardinality restrictions, and asymmetric/reflexive/disjoint properties ⟨owl2-overview §3⟩.

## Relations
- Realizes: [[description-logic]]
- Defined in: [[owl2-overview]]
- Defined in: [[owl2-profiles]]
- Published by: [[org-w3c]]
- Related: [[owl2-el]] · [[owl2-ql]] · [[owl2-rl]]

## See also
[[description-logic]] · [[owl2-ql]]

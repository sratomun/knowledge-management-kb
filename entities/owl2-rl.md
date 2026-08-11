---
title: "OWL 2 RL"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: []
sources: ["[[owl2-overview]]", "[[owl2-profiles]]"]
updated: 2026-08-10
---

# OWL 2 RL

## What it is
OWL 2 RL is one of the three OWL 2 profiles: a syntactic subset of OWL 2, more restrictive
than OWL DL, aimed at applications requiring scalable reasoning without sacrificing too
much expressive power, and implementable using rule-based reasoning engines operating
directly on RDF triples.

## Key facts
- OWL 2 RL enables the implementation of polynomial time reasoning algorithms using rule-extended database technologies operating directly on RDF triples; it is particularly suitable for applications with relatively lightweight ontologies organizing large numbers of individuals ⟨owl2-overview §2.4⟩.
- When using OWL 2 RL a rule-based implementation can operate directly on an arbitrary RDF graph; in this case reasoning will always be sound (only correct answers computed) but may not be complete (not all correct answers guaranteed) ⟨owl2-overview §2.4⟩.
- Theorem PR1 of the Profiles document states that (in general) when the ontology is consistent with the structural definition of OWL 2 RL, a suitable rule-based implementation performing ground atomic queries will be both sound and complete ⟨owl2-overview §2.4⟩.
- OWL 2 RL supports all OWL 2 axioms apart from DisjointUnion and ReflexiveObjectProperty, and the owl:real and owl:rational datatypes must not be used in OWL 2 RL ⟨owl2-profiles §4.1, §4.2.1, §4.2.5⟩.
- §4.3 presents a partial axiomatization of the OWL 2 RDF-Based Semantics as universally quantified first-order implications over a ternary predicate T (the OWL 2 RL/RDF rules), a starting point for rule-based implementations ⟨owl2-profiles §4.3⟩.

## Relations
- Defined in: [[owl2-profiles]]
- Defined in: [[owl2-overview]]
- Related: [[owl2]] · [[owl2-el]] · [[owl2-ql]]

## See also
[[owl2]] · [[owl2-profiles]]

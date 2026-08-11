---
title: "OWL 2 EL"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[description-logic]]"]
sources: ["[[owl2-overview]]", "[[owl2-profiles]]"]
updated: 2026-08-10
---

# OWL 2 EL

## What it is
OWL 2 EL is one of the three OWL 2 profiles: a syntactic subset of OWL 2, more restrictive
than OWL DL, designed for applications with ontologies defining very large numbers of
classes and/or properties, where expressive power can be traded for performance guarantees.

## Key facts
- OWL 2 EL enables polynomial time algorithms for all the standard reasoning tasks; it is particularly suitable for applications where very large ontologies are needed ⟨owl2-overview §2.4⟩.
- OWL 2 EL is based on the EL family of description logics, which provide only Existential quantification, and it suffices to express the biomedical ontology SNOMED CT ⟨owl2-profiles §2, §2.1⟩.
- OWL 2 EL supports existential quantification, self-restriction, single-individual/single-literal enumerations, intersections, property chains, and keys, but does not support universal quantification, cardinality restrictions, disjunction, class negation, inverse object properties, or (inverse-)functional/symmetric/asymmetric object properties ⟨owl2-profiles §2.1, §2.2.1⟩.
- In OWL 2 EL certain datatypes (e.g. xsd:double, xsd:float, xsd:boolean) must not be used, and anonymous individuals are not supported ⟨owl2-profiles §2.1, §2.2.1⟩.
- OWL 2 EL adds a global restriction: if the axiom closure contains a property-chain SubObjectPropertyOf axiom and imposes a range restriction to some class expression CE on the super-property, then it must impose a range restriction to CE on the chain's last property ⟨owl2-profiles §2.2.6⟩.

## Relations
- Realizes: [[description-logic]]
- Defined in: [[owl2-profiles]]
- Defined in: [[owl2-overview]]
- Related: [[owl2]] · [[owl2-ql]] · [[owl2-rl]]

## See also
[[owl2]] · [[description-logic]]

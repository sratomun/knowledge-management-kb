---
title: "Impedance Mismatch"
type: concept
tags: [obda]
related: ["[[object-generating-terms]]", "[[ontology-based-data-access]]", "[[rdb-to-rdf-mapping]]", "[[term-map]]"]
updated: 2026-08-10
---

# Impedance Mismatch

## What it is
In ontology-based data access, the gap between what a relational source stores and what a conceptual ontology talks about: databases hold data values (strings, numbers) in table cells, whereas the ontology's concepts have as instances objects that are denoted by object identifiers, not values. Bridging that gap is a job the mapping language must do, since a raw value in a source column is not the same thing as the object it stands for at the conceptual level.

## How sources treat it
- **[[poggi-linking-data]]** _(article · informational)_ — the impedance mismatch problem is that sources store data values whereas instances of concepts are objects denoted by object identifiers not to be confused with data values, and the mapping language must address it ⟨§1⟩⟨§3⟩
- **[[poggi-linking-data]]** _(article · informational)_ — it is listed as one of the five core issues OBDA must face, alongside ontology-language expressivity versus complexity, large data volumes on relational technology, the mapping, and query answering ⟨§1⟩
- **[[poggi-linking-data]]** _(article · informational)_ — the paper's second contribution is a novel mapping language whose purpose is to solve the impedance mismatch between data values at the sources and objects at the conceptual level ⟨Scope, §1⟩
- **[[poggi-linking-data]]** _(article · informational)_ — to solve it, DL-LiteA builds object identifiers as logic terms of the form f(d1,...,dn), applying object-generating function symbols to data values drawn from the sources ⟨§3⟩
- **[[poggi-linking-data]]** _(article · informational)_ — mappings are split into typing assertions (Φ ~> Ti, assigning source values to DL-LiteA/RDF data types) and data-to-object assertions (Φ ~> Ψ) that construct objects from those values ⟨§3⟩
- **[[poggi-linking-data]]** _(article · informational)_ — the mapping and impedance-mismatch ideas are argued to be of general value beyond DL-LiteA, and the solution is implemented on top of the QuOnto reasoner ⟨§7⟩

## Where sources differ
Only one source in this KB, the foundational Poggi et al. OBDA paper, treats the impedance mismatch directly, so no cross-source disagreement is recorded. The paper frames it both as one of five design issues for OBDA and as the specific problem its mapping language was built to solve, and argues the solution generalizes beyond the DL-LiteA logic in which it is presented ⟨poggi-linking-data §1, §7⟩.

## See also
[[object-generating-terms]] · [[ontology-based-data-access]] · [[rdb-to-rdf-mapping]] · [[term-map]]

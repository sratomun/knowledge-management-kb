---
title: "sh:targetClass"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:targetClass

## What it is

A SHACL target-declaration property that binds a shape to a class so that all SHACL instances of that class become focus nodes for the shape during validation.

## Key facts

- A class target is specified with the sh:targetClass predicate ⟨§2.1.3.2⟩
- Each value of sh:targetClass in a shape is an IRI ⟨§2.1.3.2⟩
- If s is a shape in a shapes graph SG and s has value c for sh:targetClass in SG then the set of SHACL instances of c in a data graph DG is a target from DG for s in SG ⟨§2.1.3.2⟩
- A potential SPARQL definition selects focus nodes via ?this rdf:type/rdfs:subClassOf* $targetClass ⟨§2.1.3.2⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-nodeshape]]

## See also
[[sh-nodeshape]] · [[constraint-validation]]

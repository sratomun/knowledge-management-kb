---
title: "sh:PropertyShape"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:PropertyShape

## What it is

A SHACL vocabulary class for property shapes: shapes that specify constraints on the values reachable from the focus node via a given SHACL property path. sh:PropertyShape is a subclass of sh:Shape.

## Key facts

- A property shape is a shape in the shapes graph that is the subject of a triple that has sh:path as its predicate ⟨§2.3⟩
- A shape has at most one value for sh:path, and each value of sh:path must be a well-formed SHACL property path ⟨§2.3⟩
- It is recommended, but not required, for a property shape to be declared as a SHACL instance of sh:PropertyShape ⟨§2.3⟩
- SHACL instances of sh:PropertyShape have one value for the property sh:path ⟨§2.3⟩
- For property shapes with a value for sh:path p, the value nodes are the set of nodes in the data graph that can be reached from the focus node with the path mapping of p ⟨§3.7⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-nodeshape]] · [[sh-path]]

## See also
[[sh-nodeshape]] · [[sh-path]] · [[constraint-validation]]

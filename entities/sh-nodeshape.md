---
title: "sh:NodeShape"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:NodeShape

## What it is

A SHACL vocabulary class for node shapes: shapes that specify constraints on the focus node itself rather than on the values of one of its properties. sh:NodeShape is a subclass of sh:Shape.

## Key facts

- A node shape is a shape in the shapes graph that is not the subject of a triple with sh:path as its predicate ⟨§2.2⟩
- It is recommended, but not required, for a node shape to be declared as a SHACL instance of sh:NodeShape ⟨§2.2⟩
- SHACL instances of sh:NodeShape cannot have a value for the property sh:path ⟨§2.2⟩
- sh:Shape is the SHACL superclass of node shapes and property shapes ⟨§2.1⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-propertyshape]]

## See also
[[sh-propertyshape]] · [[constraint-validation]]

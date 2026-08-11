---
title: "sh:path"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[property-paths]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:path

## What it is

The SHACL property that gives a property shape its path: the SHACL property path whose value nodes (reached from the focus node) the property shape constrains.

## Key facts

- A property shape is a shape in the shapes graph that is the subject of a triple that has sh:path as its predicate ⟨§2.3⟩
- A shape has at most one value for sh:path ⟨§2.3⟩
- Each value of sh:path in a shape must be a well-formed SHACL property path ⟨§2.3⟩
- SHACL includes RDF terms to represent a subset of SPARQL property paths: PredicatePath, InversePath, SequencePath, AlternativePath, ZeroOrMorePath, OneOrMorePath and ZeroOrOnePath ⟨§2.3.1⟩
- A node p is not a well-formed SHACL property path if p is a blank node and any path mappings of p directly or transitively reference p ⟨§2.3.1⟩

## Relations

- Realizes: [[property-paths]]
- Defined in: [[shacl]]
- Related: [[sh-propertyshape]]

## See also
[[sh-propertyshape]] · [[property-paths]]

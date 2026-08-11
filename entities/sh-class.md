---
title: "sh:class"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:class

## What it is

The parameter of the SHACL Core value-type constraint component sh:ClassConstraintComponent, requiring each value node to be a SHACL instance of a given type.

## Key facts

- For each value node that is either a literal, or a non-literal that is not a SHACL instance of $class in the data graph, there is a validation result with the value node as sh:value ⟨§4.1.1⟩
- Multiple values for sh:class are interpreted as a conjunction, i.e. the values need to be SHACL instances of all of them ⟨§4.1.1⟩
- The values of sh:class in a shape are IRIs ⟨§4.1.1⟩
- A potential SPARQL definition tests each value with ASK { $value rdf:type/rdfs:subClassOf* $class . } ⟨§4.1.1⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-datatype]] · [[sh-nodekind]]

## See also
[[sh-datatype]] · [[sh-nodekind]] · [[constraint-validation]]

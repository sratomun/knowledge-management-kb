---
title: "sh:datatype"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]", "[[literal-datatyping]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:datatype

## What it is

The parameter of the SHACL Core value-type constraint component sh:DatatypeConstraintComponent, requiring each value node to be a literal of a specified datatype.

## Key facts

- For each value node that is not a literal, or is a literal with a datatype that does not match $datatype, there is a validation result with the value node as sh:value ⟨§4.1.2⟩
- The datatype of a literal is determined following the datatype function of SPARQL 1.1 ⟨§4.1.2⟩
- A literal matches a datatype if the literal's datatype has the same IRI and, for the datatypes supported by SPARQL 1.1, is not an ill-typed literal ⟨§4.1.2⟩
- The values of sh:datatype in a shape are IRIs, and a shape has at most one value for sh:datatype ⟨§4.1.2⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-nodekind]] · [[sh-class]]

## See also
[[sh-nodekind]] · [[literal-datatyping]] · [[constraint-validation]]

---
title: "sh:nodeKind"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:nodeKind

## What it is

The parameter of the SHACL Core value-type constraint component sh:NodeKindConstraintComponent, restricting the RDF node kind (IRI, blank node, literal, or combinations) of each value node.

## Key facts

- For each value node that does not match $nodeKind, there is a validation result with the value node as sh:value ⟨§4.1.3⟩
- The values of sh:nodeKind are one of six instances of sh:NodeKind: sh:BlankNode, sh:IRI, sh:Literal, sh:BlankNodeOrIRI, sh:BlankNodeOrLiteral and sh:IRIOrLiteral ⟨§4.1.3⟩
- Any IRI matches only sh:IRI, sh:BlankNodeOrIRI and sh:IRIOrLiteral; any blank node matches only sh:BlankNode, sh:BlankNodeOrIRI and sh:BlankNodeOrLiteral; any literal matches only sh:Literal, sh:BlankNodeOrLiteral and sh:IRIOrLiteral ⟨§4.1.3⟩
- A shape has at most one value for sh:nodeKind ⟨§4.1.3⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-datatype]] · [[sh-class]]

## See also
[[sh-datatype]] · [[constraint-validation]]

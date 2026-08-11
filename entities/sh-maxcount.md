---
title: "sh:maxCount"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:maxCount

## What it is

The parameter of the SHACL Core cardinality constraint component sh:MaxCountConstraintComponent, restricting the maximum number of value nodes a property shape permits.

## Key facts

- If the number of value nodes is greater than $maxCount, there is a validation result ⟨§4.2.2⟩
- Node shapes cannot have any value for sh:maxCount ⟨§4.2.2⟩
- A property shape has at most one value for sh:maxCount, and the values are literals with datatype xsd:integer ⟨§4.2.2⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-mincount]] · [[sh-propertyshape]]

## See also
[[sh-mincount]] · [[constraint-validation]]

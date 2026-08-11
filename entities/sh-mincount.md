---
title: "sh:minCount"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:minCount

## What it is

The parameter of the SHACL Core cardinality constraint component sh:MinCountConstraintComponent, restricting the minimum number of value nodes a property shape permits.

## Key facts

- If the number of value nodes is less than $minCount, there is a validation result ⟨§4.2.1⟩
- If the minimum cardinality value is 0 then this constraint is always satisfied and so may be omitted ⟨§4.2.1⟩
- Node shapes cannot have any value for sh:minCount ⟨§4.2.1⟩
- A property shape has at most one value for sh:minCount, and the values are literals with datatype xsd:integer ⟨§4.2.1⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-maxcount]] · [[sh-propertyshape]]

## See also
[[sh-maxcount]] · [[constraint-validation]]

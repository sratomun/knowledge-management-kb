---
title: "sh:ValidationReport"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:ValidationReport

## What it is

The SHACL Validation Report Vocabulary class describing the RDF graph that a validation process produces: the overall conformance result plus the set of individual validation results.

## Key facts

- The result of a validation process is an RDF graph with exactly one SHACL instance of sh:ValidationReport ⟨§3.6.1⟩
- Each SHACL instance of sh:ValidationReport has exactly one value for sh:conforms, of datatype xsd:boolean; it is true if and only if the validation did not produce any validation results ⟨§3.6.1.1⟩
- For every validation result produced, the sh:ValidationReport has a value for sh:result, and each value is a SHACL instance of sh:ValidationResult ⟨§3.6.1.2⟩
- Each sh:ValidationResult has mandatory sh:focusNode, sh:resultSeverity and sh:sourceConstraintComponent ⟨§3.6.2⟩
- Only SHACL implementations that can produce all of the mandatory properties of the Validation Report Vocabulary are standards-compliant ⟨§3⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-severity]]

## See also
[[sh-severity]] · [[constraint-validation]]

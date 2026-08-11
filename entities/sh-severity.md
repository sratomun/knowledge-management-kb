---
title: "sh:severity"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[constraint-validation]]"]
sources: ["[[shacl]]"]
updated: 2026-08-10
---

# sh:severity

## What it is

The SHACL property by which a shape declares the severity level attached to the validation results it produces, chosen from the SHACL severity IRIs.

## Key facts

- Shapes can specify one value for the property sh:severity in the shapes graph, and each value of sh:severity in a shape is an IRI ⟨§2.1.4⟩
- SHACL includes three IRIs as SHACL instances of sh:Severity: sh:Info (a non-critical constraint violation indicating an informative message), sh:Warning (a non-critical constraint violation indicating a warning) and sh:Violation (a constraint violation) ⟨§2.1.4⟩
- For every shape, sh:Violation is the default if sh:severity is unspecified ⟨§2.1.4⟩
- The specific values of sh:severity have no impact on the validation, but may be used by user interface tools to categorize validation results ⟨§2.1.4⟩
- Each validation result has exactly one value for sh:resultSeverity, equal to the value of sh:severity of the shape, defaulting to sh:Violation if no sh:severity has been specified ⟨§3.6.2.8⟩

## Relations

- Realizes: [[constraint-validation]]
- Defined in: [[shacl]]
- Related: [[sh-validationreport]]

## See also
[[sh-validationreport]] · [[constraint-validation]]

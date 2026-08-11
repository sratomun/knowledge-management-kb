---
title: "Shapes Constraint Language (SHACL)"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["SHACL"]
publisher: W3C
url: https://www.w3.org/TR/shacl/
version: "1.0 (2017-07-20)"
published: 2017-07
effective_from: 2017-07-20
effective_to: ongoing
status: current
tags: [semantic-web]
updated: 2026-08-10
---

# Shapes Constraint Language (SHACL)

## Scope & purpose

SHACL is a W3C Recommendation defining a language for validating RDF graphs against a set of conditions expressed themselves as an RDF graph. The conditions are provided as shapes and other constructs in a "shapes graph"; the graphs validated against them are "data graphs". Because a shapes graph describes the data graphs that satisfy its conditions, it can also serve purposes beyond validation, including user-interface building, code generation, and data integration. The specification is divided into SHACL Core (frequently needed shape/constraint/target features that all implementations must support) and SHACL-SPARQL (Core plus SPARQL-based constraints and an extension mechanism for new constraint components).

## Structure

- §1 Introduction — terminology, document conventions, conformance, worked example, relationships to RDFS inferencing and to SPARQL.
- §2 Shapes and Constraints — shapes; constraints/parameters/constraint components; focus nodes; targets (§2.1.3); severity, messages, deactivation; node shapes (§2.2); property shapes and SHACL property paths (§2.3).
- §3 Validation and Graphs — shapes graph, data graph, sh:shapesGraph, validation, failures, recursion, conformance checking, validation report (§3.6), value nodes (§3.7).
- §4 Core Constraint Components — value type, cardinality, value range, string-based, property pair, logical, shape-based, and other components.
- §5 SPARQL-based Constraints — sh:sparql / sh:select, prefix declarations, validation, pre-bound variables, solution-to-result mapping.
- §6 SPARQL-based Constraint Components — parameter declarations, label templates, validators (SELECT-/ASK-based), validation.
- Appendices A–H — pre-binding, syntax-rule summary, SHACL-for-SHACL shapes, Core validator summary, security, acknowledgements, references.

## Key points

- SHACL validates a **data graph** against a **shapes graph**; a shapes graph is an RDF graph containing zero or more shapes, and any RDF graph can be a data graph ⟨§3.1, §3.2⟩.
- A **shape** is an IRI or blank node that is a SHACL instance of sh:NodeShape/sh:PropertyShape, is subject of a target or parameter triple, or is a value of a shape-expecting parameter ⟨§2.1⟩.
- A **node shape** applies to the focus node itself and is not the subject of a triple with sh:path; a **property shape** is the subject of a triple with sh:path and applies to nodes reached from the focus node via that path; sh:Shape is the SHACL superclass of both ⟨§2.1, §2.2, §2.3⟩.
- **Constraint components** are IRIs with mandatory and optional **parameters** (each a property); a shape declares a constraint when it has values for the mandatory parameters, and components are associated with **validators** ⟨§2.1.1⟩.
- **Focus nodes** are the RDF terms validated against a shape; they are produced by **target declarations**, by shape-expecting parameters (e.g. sh:node), or supplied directly to the processor ⟨§2.1.2⟩.
- SHACL Core **targets**: node targets (sh:targetNode), class-based targets (sh:targetClass, plus implicit class targets when a shape is also an rdfs:Class), subjects-of targets (sh:targetSubjectsOf) and objects-of targets (sh:targetObjectsOf) ⟨§2.1.3⟩.
- SHACL property paths cover a subset of SPARQL property paths: predicate, inverse (sh:inversePath), sequence (SHACL list), alternative (sh:alternativePath), and sh:zeroOrMorePath / sh:oneOrMorePath / sh:zeroOrOnePath ⟨§2.3.1⟩.
- A shape can declare a **severity** (sh:Info, sh:Warning, sh:Violation); sh:Violation is the default if sh:severity is unspecified, and the value populates sh:resultSeverity in results ⟨§2.1.4, §3.6.2.8⟩.
- Core constraint components include value-type (sh:class, sh:datatype, sh:nodeKind), cardinality (sh:minCount, sh:maxCount), value-range, string-based (sh:minLength, sh:maxLength, sh:pattern, sh:languageIn, sh:uniqueLang), property-pair (sh:equals, sh:disjoint, sh:lessThan, sh:lessThanOrEquals), logical (sh:not, sh:and, sh:or, sh:xone), shape-based (sh:node, sh:property, sh:qualifiedValueShape) and others (sh:closed/sh:ignoredProperties, sh:hasValue, sh:in) ⟨§4⟩.
- All SHACL implementations **must** at least implement SHACL Core; SHACL Core processors that do not support SHACL-SPARQL ignore SHACL-SPARQL constructs such as sh:sparql triples ⟨§1.1, §1.3⟩.
- During validation the data graph and shapes graph **must** remain immutable and SHACL processing is idempotent; if the shapes graph is ill-formed the result is undefined and a processor **should** produce a failure ⟨§3.4, §3.4.2⟩.
- Validation with **recursive shapes** is not defined in SHACL and is left to implementations (which may support recursion or produce a failure) ⟨§3.4.3⟩.
- A **validation report** is an RDF graph with exactly one sh:ValidationReport, carrying sh:conforms (xsd:boolean) and sh:result values; each sh:ValidationResult has mandatory sh:focusNode, sh:resultSeverity and sh:sourceConstraintComponent, and optional sh:resultPath, sh:value, sh:sourceShape, sh:detail, sh:resultMessage ⟨§3.6⟩.
- **Conformance checking** produces true iff the focus node's validation results are empty and no failure occurred; components such as sh:not, sh:or and sh:node rely on it ⟨§3.5⟩.
- **SHACL-SPARQL** adds sh:SPARQLConstraintComponent (via sh:sparql / sh:select) and a mechanism to declare new constraint components (sh:ConstraintComponent with sh:parameter and SELECT-/ASK-based validators), pre-binding variables such as $this, $shapesGraph and $currentShape ⟨§5, §6⟩.

## Concepts & entities covered
Concepts: [[constraint-validation]] · [[property-paths]] · [[literal-datatyping]]
Entities: [[sh-nodeshape]] · [[sh-propertyshape]] · [[sh-targetclass]] · [[sh-path]] · [[sh-mincount]] · [[sh-maxcount]] · [[sh-datatype]] · [[sh-nodekind]] · [[sh-class]] · [[sh-validationreport]] · [[sh-severity]] · [[org-w3c]]

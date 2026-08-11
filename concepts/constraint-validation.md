---
title: "Constraint Validation"
type: concept
tags: [semantic-web]
related: ["[[rdf-vocabulary-schema]]", "[[property-paths]]", "[[graph-pattern-matching]]"]
updated: 2026-08-10
---

# Constraint Validation

## What it is
Checking that RDF data satisfies a set of conditions expressed as shapes, where the conditions are themselves recorded as an RDF graph. A "shapes graph" states which nodes must be checked (targets) and what must hold of them (constraints); a "data graph" is validated against it, producing a machine-readable report of whether the data conforms and, if not, which nodes violated which constraints. Because the same shapes describe the data that would satisfy them, they can also drive uses beyond validation, such as form building, code generation, and data integration.

## How sources treat it
- **[[shacl]]** _(standard · normative)_ — SHACL validates a data graph against a shapes graph; a shapes graph is an RDF graph containing zero or more shapes, and any RDF graph can be a data graph ⟨§3.1, §3.2⟩
- **[[shacl]]** _(standard · normative)_ — a node shape applies to the focus node itself and is not the subject of a triple with sh:path, while a property shape is the subject of a triple with sh:path and applies to nodes reached from the focus node via that path; sh:Shape is the superclass of both ⟨§2.1, §2.2, §2.3⟩
- **[[shacl]]** _(standard · normative)_ — focus nodes are the RDF terms validated against a shape, produced by target declarations (sh:targetNode, sh:targetClass and implicit class targets, sh:targetSubjectsOf, sh:targetObjectsOf), by shape-expecting parameters, or supplied directly to the processor ⟨§2.1.2, §2.1.3⟩
- **[[shacl]]** _(standard · normative)_ — constraint components are IRIs with mandatory and optional parameters; a shape declares a constraint when it has values for the mandatory parameters, and components are associated with validators ⟨§2.1.1⟩
- **[[shacl]]** _(standard · normative)_ — Core constraint components cover value-type (sh:class, sh:datatype, sh:nodeKind), cardinality (sh:minCount, sh:maxCount), value-range, string-based (sh:pattern, sh:minLength, sh:languageIn, …), property-pair, logical (sh:not, sh:and, sh:or, sh:xone) and shape-based (sh:node, sh:property, sh:qualifiedValueShape) checks ⟨§4⟩
- **[[shacl]]** _(standard · normative)_ — a shape can declare a severity (sh:Info, sh:Warning, sh:Violation), with sh:Violation the default if sh:severity is unspecified ⟨§2.1.4, §3.6.2.8⟩
- **[[shacl]]** _(standard · normative)_ — all SHACL implementations **must** at least implement SHACL Core, and SHACL Core processors that do not support SHACL-SPARQL ignore SHACL-SPARQL constructs such as sh:sparql triples ⟨§1.1, §1.3⟩
- **[[shacl]]** _(standard · normative)_ — during validation the data graph and shapes graph **must** remain immutable and SHACL processing is idempotent; if the shapes graph is ill-formed the result is undefined and a processor **should** produce a failure ⟨§3.4, §3.4.2⟩
- **[[shacl]]** _(standard · normative)_ — validation with recursive shapes is not defined in SHACL and is left to implementations, which may support recursion or produce a failure ⟨§3.4.3⟩
- **[[shacl]]** _(standard · normative)_ — a validation report is an RDF graph with exactly one sh:ValidationReport carrying sh:conforms and sh:result values, each result carrying mandatory sh:focusNode, sh:resultSeverity and sh:sourceConstraintComponent plus optional details ⟨§3.6⟩
- **[[shacl]]** _(standard · normative)_ — SHACL-SPARQL adds SPARQL-based constraints (sh:sparql / sh:select) and a mechanism to declare new constraint components with SELECT-/ASK-based validators, pre-binding variables such as $this, $shapesGraph and $currentShape ⟨§5, §6⟩

## Where sources differ
Only one source in this KB, the normative SHACL Recommendation, treats constraint validation directly, so no cross-source disagreement is recorded. Internally the specification draws a firm line between the mandatory SHACL Core feature set that every processor **must** implement and the optional SHACL-SPARQL extension that Core-only processors ignore, and it leaves recursive-shape validation undefined for implementations to decide ⟨shacl §1.1, §1.3, §3.4.3⟩.

## See also
[[rdf-vocabulary-schema]] · [[property-paths]] · [[graph-pattern-matching]]

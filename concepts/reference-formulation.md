---
title: "Reference Formulation"
type: concept
tags: [semantic-web]
related: ["[[logical-source-abstraction]]", "[[term-map]]", "[[rdb-to-rdf-mapping]]"]
updated: 2026-08-09
---

# Reference Formulation

## What it is
The declaration of which expression language a mapping uses to address elements of a source — for example SQL column names for a database, XPath for XML, or JSONPath for JSON. Naming the reference formulation lets format-agnostic mapping constructs (references and iterators) be interpreted correctly against whatever source they run over.

## How sources treat it
- **[[rml]]** _(standard · normative)_ — the reference formulation (rml:referenceFormulation) defines how references address elements of the source and should always be specified via rml:referenceFormulation; for relational databases rr:sqlVersion may be used instead to stay backwards-compliant with R2RML ⟨§4.1⟩
- **[[rml]]** _(standard · normative)_ — example reference formulations are rr:SQL2008, ql:XPath (XML), and ql:JSONPath (JSON) ⟨§4.1⟩
- **[[rml]]** _(standard · normative)_ — a reference (rml:reference) refers to a column (databases), a record (CSV/TSV), an element (XML), or an object (JSON), and must be a valid expression per the specified reference formulation (e.g. a valid XPath or JSONPath expression) ⟨§6.2⟩
- **[[rml]]** _(standard · normative)_ — the logical iterator (rml:iterator) defines the iteration loop; the default iterator is the row for databases/CSV/TSV, an element for XML, and an object for JSON — a generalization not present in R2RML, which iterates rows only ⟨§4.1⟩

## Where sources differ
Reference formulation is an RML construct; the cited coverage is from RML alone. RML positions it as the mechanism that makes its logical-source abstraction format-independent, while keeping a fallback to R2RML's rr:sqlVersion for relational databases so relational mappings stay backward-compatible ⟨rml §4.1⟩. R2RML has no separate reference-formulation notion because it addresses relational data exclusively through SQL.

## See also
[[logical-source-abstraction]] · [[term-map]] · [[rdb-to-rdf-mapping]]

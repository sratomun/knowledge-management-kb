---
title: "Literal datatyping"
type: concept
tags: [semantic-web]
related: ["[[rdf-data-model]]", "[[iri-identity]]", "[[entailment-equivalence]]"]
updated: 2026-08-09
---

# Literal datatyping

## What it is

Literals are the data values that appear as objects in RDF — strings, numbers, dates, and the like. Each literal carries a lexical form (how it is written), a datatype IRI that says how that lexical form maps to a value, and, only for language-tagged strings, a language tag. Datatyping is what separates a literal's written form from its meaning, so that "1" and "01" can share a value while remaining distinct terms, and it lets processors handle values whose datatypes they do not recognize without rejecting the data.

## How sources treat it

- **[[rdf-11-concepts]]** _(standard · normative)_ — A literal consists of a lexical form (a Unicode string, which SHOULD be in Normal Form C), a datatype IRI, and — if and only if the datatype IRI is `rdf:langString` — a non-empty, well-formed language tag per BCP47 ⟨§3.3⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Simple literals (lexical form only) are syntactic sugar for literals with datatype IRI `xsd:string`, while language-tagged strings always carry datatype IRI `rdf:langString` ⟨§3.3⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Implementations MUST accept ill-typed literals and produce RDF graphs from them, and MAY produce warnings; an ill-typed literal is a semantic inconsistency but is not syntactically ill-formed ⟨§3.3⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Two literals are term-equal if and only if their lexical forms, datatype IRIs, and language tags (if any) compare equal character by character; two literals can share a value without being term-equal (e.g. `"1"^^xsd:integer` vs `"01"^^xsd:integer`) ⟨§3.3⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — A datatype consists of a lexical space, a value space, and a lexical-to-value mapping, denoted by one or more IRIs; RDF processors are not required to recognize datatype IRIs and SHOULD NOT reject RDF using unrecognized ones ⟨§5, §5.4⟩.

## Where sources differ

This concept is covered by a single source, rdf-11-concepts, so there is no divergence to report here.

## See also

[[rdf-data-model]] · [[iri-identity]] · [[entailment-equivalence]]

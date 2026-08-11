---
title: "Datatype IRI"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[literal-datatyping]]"]
sources: ["[[rdf-11-concepts]]"]
updated: 2026-08-09
---

# Datatype IRI

## What it is
A datatype IRI is the IRI that identifies the datatype of a literal, determining how its lexical form maps to a value. IRIs used to refer to datatypes are called recognized datatype IRIs.

## Key facts
- Datatypes are identified by IRIs; if D is the set of IRIs used to refer to datatypes, its elements are called recognized datatype IRIs, and recognized IRIs have fixed referents ⟨§5.4⟩.
- If any IRI of the form http://www.w3.org/2001/XMLSchema#xxx is recognized, it must refer to the RDF-compatible XSD type named xsd:xxx for every XSD type listed in section 5.1 ⟨§5.4⟩.
- RDF processors are not required to recognize datatype IRIs; any literal typed with an unrecognized IRI is treated just like an unknown IRI, and processors should not reject such RDF as either a syntactic or semantic error ⟨§5.4⟩.

## Relations
- Realizes: [[literal-datatyping]]
- Defined in: [[rdf-11-concepts]]
- Related: [[rdf-literal]], [[rdf-html]], [[rdf-xmlliteral]]

## See also
[[rdf-langstring]]

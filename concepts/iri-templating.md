---
title: "IRI Templating"
type: concept
tags: [semantic-web]
related: ["[[term-map]]", "[[rdb-to-rdf-mapping]]", "[[iri-identity]]"]
updated: 2026-08-09
---

# IRI Templating

## What it is
The construction of stable IRIs (and other RDF terms) by substituting source values into a string template — a pattern with placeholders that name source references. Because generated IRIs must be syntactically valid, templating includes percent-encoding of the substituted data values so that arbitrary source content yields IRI-safe output.

## How sources treat it
- **[[r2rml]]** _(standard · normative)_ — a string template references column names in unescaped curly braces; when the term type is rr:IRI, R2RML always percent-encodes each data value into an IRI-safe version per the iunreserved production of RFC 3987 ⟨§7.3⟩
- **[[r2rml]]** _(standard · normative)_ — a template-valued term map (rr:template) is one of the three permitted kinds of term map generating an RDF term from a logical table row ⟨§7⟩
- **[[r2rml]]** _(standard · normative)_ — a term map with term type rr:IRI that generates an invalid IRI is a data error; a processor MUST abort any operation that would inspect or return such a term and report an error, though the presence of data errors does not make a mapping non-conforming ⟨§4.3⟩

## Where sources differ
Only R2RML is cited here for IRI templating. It fixes the template mechanism to column names enclosed in unescaped curly braces and mandates percent-encoding to the iunreserved production of RFC 3987 when the term type is rr:IRI ⟨r2rml §7.3⟩, with invalid IRIs treated as data errors that a processor MUST abort on ⟨r2rml §4.3⟩.

## See also
[[term-map]] · [[rdb-to-rdf-mapping]]

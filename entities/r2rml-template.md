---
title: "rr:template"
type: entity
subtype: vocabulary-term
aliases: ["R2RML string template"]
tags: [obda]
concepts: ["[[iri-templating]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:template

## What it is
The R2RML property defining a template-valued term map: a format string that builds an RDF term (usually an IRI) from one or more column values referenced by name in curly braces.

## Key facts
- A template-valued term map is represented by a resource that has exactly one rr:template property whose value MUST be a valid string template; column names are referenced by enclosing them in curly braces ⟨§7.3⟩
- When the term type is rr:IRI, each column value is replaced by an IRI-safe (percent-encoded) version per the iunreserved production in RFC 3987; R2RML always performs percent-encoding when IRIs are generated from string templates ⟨§7.3⟩
- The referenced columns of a template-valued term map are the set of column names enclosed in unescaped curly braces in the template string ⟨§7.3⟩

## Relations
- Realizes: [[iri-templating]]
- Defined in: [[r2rml]]
- Related: [[r2rml-column]], [[r2rml-constant]], [[r2rml-termtype]]

## See also
[[r2rml-termmap]] · [[org-w3c]]

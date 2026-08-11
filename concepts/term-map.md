---
title: "Term Map"
type: concept
tags: [semantic-web]
related: ["[[iri-templating]]", "[[reference-formulation]]", "[[rdb-to-rdf-mapping]]", "[[logical-source-abstraction]]"]
updated: 2026-08-09
---

# Term Map

## What it is
A function inside a mapping that produces a single RDF term (an IRI, blank node, or literal) from one row or record of the source. Term maps are the building blocks that populate the subject, predicate, object, and graph positions of the generated triples, and they come in a small fixed set of kinds: a constant value, a direct reference to a source value, or a string template.

## How sources treat it
- **[[r2rml]]** _(standard · normative)_ — a term map is a function generating an RDF term from a logical table row and MUST be exactly one of: a constant-valued term map (rr:constant), a column-valued term map (rr:column), or a template-valued term map (rr:template) ⟨§7⟩
- **[[r2rml]]** _(standard · normative)_ — rr:termType selects the generated kind (rr:IRI, rr:BlankNode, or rr:Literal); absent an explicit value the term type defaults to rr:Literal for an object map that is column-based or has rr:language or rr:datatype, and to rr:IRI otherwise ⟨§7.4⟩
- **[[r2rml]]** _(standard · normative)_ — a datatypeable term map MAY have one rr:datatype to override the natural datatype; a term map MUST NOT have more than one rr:datatype value, and a term map that is not datatypeable MUST NOT have an rr:datatype property ⟨§7.6⟩
- **[[rml]]** _(standard · normative)_ — a term map MUST be exactly one of a constant-valued (rr:constant), reference-valued (rml:reference), or template-valued (rr:template) term map; RML replaces R2RML's column-only rr:column with the format-agnostic rml:reference ⟨§6, §6.2⟩
- **[[rml]]** _(standard · normative)_ — adds a language map (rml:languageMap), whose value must be a term map generating a language tag, with precedence: a valid language-map value, else rr:language, else no language ⟨§6.5⟩

## Where sources differ
Both specifications define the same three-way choice of term map (constant, reference/column, template) with the same syntax. R2RML's value-reference kind is the column-valued term map, tied to a SQL column name ⟨r2rml §7⟩. RML generalizes that kind to rml:reference, which addresses a column, record, element, or object depending on the reference formulation ⟨rml §6.2⟩. RML additionally introduces the language map to compute language tags dynamically, extending R2RML's fixed rr:language tag ⟨rml §6.5⟩.

## See also
[[iri-templating]] · [[reference-formulation]] · [[rdb-to-rdf-mapping]]

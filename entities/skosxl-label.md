---
title: "skosxl:Label"
type: entity
subtype: specification-construct
aliases: []
tags: [knowledge-organization]
concepts: ["[[lexical-labeling]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skosxl:Label

## What it is
A special class of lexical entities defined by the optional SKOS eXtension for Labels (SKOS-XL). An instance is a resource (which may be named with a URI) that reifies a label, so labels can themselves be identified, described and linked. Each instance has a single RDF plain literal form.

## Key facts
- skosxl:Label is an instance of owl:Class ⟨S47⟩.
- skosxl:Label is disjoint with each of skos:Concept, skos:ConceptScheme and skos:Collection ⟨S48⟩.
- skosxl:Label is a sub-class of a restriction on skosxl:literalForm cardinality exactly 1 ⟨S52⟩; two instances with the same literal form are not necessarily the same individual ⟨B.2.1⟩.

## Relations
- Realizes: [[lexical-labeling]]
- Defined in: [[skos]]
- Related: [[skosxl-literalform]] · [[skosxl-preflabel]] · [[skosxl-labelrelation]]

## See also
[[skos-preflabel]] · [[skosxl-literalform]]

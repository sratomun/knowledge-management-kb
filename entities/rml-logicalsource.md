---
title: "rml:LogicalSource"
type: entity
subtype: vocabulary-term
aliases: []
tags: [obda]
concepts: ["[[logical-source-abstraction]]"]
sources: ["[[rml]]"]
updated: 2026-08-09
---

# rml:LogicalSource

## What it is
The RML vocabulary class of logical sources — the abstract handle through which a triples map retrieves data from an input source, generalizing R2RML's logical table to any structured format.

## Key facts
- "rml:LogicalSource is the class of logical sources" ⟨§2⟩.
- A logical source "extends R2RML's logical Table" and "is a Base Source, rml:BaseSource" ⟨§3, §4⟩.
- A triples map "must have exactly one logical source (rml:logicalSource) property" whose value specifies the source to be mapped ⟨§5⟩.
- A base source is represented by a resource that has exactly one `rml:source`, exactly one logical iterator (`rml:iterator`), and zero or one `rml:referenceFormulation` ⟨§4.1⟩.

## Relations
- Realizes: [[logical-source-abstraction]]
- Defined in: [[rml]]
- Related: [[rml-source]], [[rml-iterator]], [[rml-referenceformulation]]
- Reuses (R2RML): [[r2rml-triplesmap]]

## See also
[[logical-source-abstraction]] · [[org-kgc-cg]] · [[org-idlab-ghent]]

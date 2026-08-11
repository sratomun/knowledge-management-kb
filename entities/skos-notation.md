---
title: "skos:notation"
type: entity
subtype: vocabulary-term
aliases: []
tags: [knowledge-organization]
concepts: ["[[notation]]"]
sources: ["[[skos]]"]
updated: 2026-08-09
---

# skos:notation

## What it is
A datatype property used to assign a notation — a string of characters (e.g. "T58.5" or "303.4833") that uniquely identifies a concept within the scope of a given concept scheme — as a typed literal.

## Key facts
- skos:notation is an instance of owl:DatatypeProperty ⟨S15⟩.
- A notation differs from a lexical label in that it "is not normally recognizable as a word or sequence of words in any natural language" ⟨§6.1⟩.
- By convention skos:notation is used only with a typed literal in the object position, where the datatype URI denotes a user-defined datatype for a particular notation/classification system; no domain is stated, so its effective domain is all resources ⟨§6.5.1⟩ ⟨§6.5.5⟩.

## Relations
- Realizes: [[notation]]
- Defined in: [[skos]]
- Related: [[skos-preflabel]]

## See also
[[notation]]

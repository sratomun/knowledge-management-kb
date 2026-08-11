---
title: "Object-Generating Terms"
type: concept
tags: [obda]
related: ["[[impedance-mismatch]]", "[[iri-templating]]", "[[term-map]]", "[[skolemization]]"]
updated: 2026-08-10
---

# Object-Generating Terms

## What it is
The construct that mints an object identifier at the conceptual level from data values pulled out of a relational source. Instead of treating a source value as the object itself, a mapping applies a function symbol to one or more values — written f(d1,...,dn) — so that the resulting term denotes an object. This is how ontology-based data access populates concepts (whose instances are objects) from databases (which only hold values), and it echoes object invention in deductive object-oriented databases.

## How sources treat it
- **[[poggi-linking-data]]** _(article · informational)_ — to solve the impedance mismatch, DL-LiteA builds object identifiers as logic terms of the form f(d1,...,dn) — object-generating function symbols applied to data values drawn from the sources — an idea borrowed from object invention in deductive object-oriented databases ⟨§3⟩
- **[[poggi-linking-data]]** _(article · informational)_ — the paper takes seriously the distinction between objects and values, adding attributes (binary relations between objects and values) alongside concepts, roles, and value-domains ⟨§2⟩
- **[[poggi-linking-data]]** _(article · informational)_ — data-to-object mapping assertions have the form Φ ~> Ψ, where Φ is an arbitrary SQL query over the database and Ψ is a conjunctive query over the ontology possibly involving variable terms (the object-constructing terms) ⟨§3⟩
- **[[poggi-linking-data]]** _(article · informational)_ — mapping assertions are read as material implications: the closed-world evaluation of Φ over the database supplies the values, while the ontology's open-world semantics allows additional facts beyond those the mapping generates ⟨§3⟩
- **[[poggi-linking-data]]** _(article · informational)_ — at evaluation time the unfolding step (UnfoldDB) translates the object-term-bearing query into SQL over the source relations, completely getting rid of the mappings ⟨§5⟩

## Where sources differ
Only one source in this KB, the Poggi et al. OBDA paper, treats object-generating terms directly, so no cross-source disagreement is recorded. The paper presents the f(d1,...,dn) construct as its mechanism for the impedance mismatch and explicitly credits object invention in deductive object-oriented databases as the origin of the idea ⟨poggi-linking-data §3⟩.

## See also
[[impedance-mismatch]] · [[iri-templating]] · [[term-map]] · [[skolemization]]

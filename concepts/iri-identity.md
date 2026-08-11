---
title: "IRI identity"
type: concept
tags: [semantic-web]
related: ["[[rdf-data-model]]", "[[rdf-vocabulary-namespace]]", "[[blank-node]]", "[[linked-data]]"]
updated: 2026-08-09
---

# IRI identity

## What it is

In RDF, an IRI (Internationalized Resource Identifier) is a globally-scoped name that identifies a resource. Because IRIs are global, any two occurrences of the same IRI — in the same graph, in another graph, or in another system — are taken to denote the same resource, which is what lets independently authored data join up. Deciding when two IRIs are "the same" is therefore a precise, syntactic question rather than a matter of interpretation.

## How sources treat it

- **[[rdf-11-concepts]]** _(standard · normative)_ — An IRI within an RDF graph is a Unicode string conforming to RFC 3987 syntax; IRIs in the abstract syntax MUST be absolute and MAY contain a fragment identifier ⟨§3.2⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — Two IRIs are equal if and only if they are equivalent under Simple String Comparison per RFC 3987 §5.1, and further normalization MUST NOT be performed when comparing IRIs for equality ⟨§3.2⟩.
- **[[rdf-11-concepts]]** _(standard · normative)_ — By design IRIs have global scope, so two different appearances of an IRI denote the same resource, and an IRI once minted SHOULD never change its intended referent ⟨§1.3, §1.5⟩.
- **[[json-ld-11]]** _(standard · normative)_ — Adds a universal identifier mechanism (IRIs) to JSON; a context maps terms to IRIs, introduced with the `@context` key ⟨§3.1⟩.
- **[[json-ld-11]]** _(standard · normative)_ — When serializing a dataset, whenever practical the graph name SHOULD be an IRI, and a directed-arc (predicate) SHOULD be labeled with an IRI ⟨§8⟩.

## Where sources differ

The two sources treat IRI identity at different layers rather than in conflict. rdf-11-concepts fixes the abstract rules — absoluteness, character-by-character equality under Simple String Comparison, and the stability of a minted IRI's referent. json-ld-11 supplies the serialization-level machinery for producing IRIs from a JSON document (contexts, term-to-IRI mapping, compact IRIs) and expresses several of its identifier choices as SHOULD-strength recommendations. Neither source resolves the other; the abstract equality rules and the concrete authoring mechanisms simply address different concerns.

## See also

[[rdf-data-model]] · [[rdf-vocabulary-namespace]] · [[blank-node]] · [[linked-data]]

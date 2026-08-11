---
title: "@context"
type: entity
subtype: vocabulary-term
aliases: []
tags: [semantic-web]
concepts: ["[[linked-data-serialization]]"]
sources: ["[[json-ld-11]]"]
updated: 2026-08-09
---

# @context

## What it is
The keyword that introduces a JSON-LD context — the set of rules that map terms to IRIs so a JSON-LD document can be interpreted as Linked Data.

## Key facts
- The @context keyword MUST NOT be aliased, and MAY be used as a key in node objects, value objects, graph objects, list objects, set objects, nested properties, and expanded term definitions ⟨§9.16⟩.
- The value of @context MUST be null, an IRI reference, a context definition, or an array composed of any of these ⟨§9.16⟩.
- A context maps terms to IRIs and may be directly embedded in the document (an embedded context) or referenced using a URL ⟨§3.1⟩.

## Relations
- Realizes: [[linked-data-serialization]]
- Defined in: [[json-ld-11]]
- Related: [[jsonld-import]]
- Related: [[jsonld-vocab]]
- Related: [[jsonld-base]]

## See also
[[linked-data-serialization]] [[jsonld-vocab]]

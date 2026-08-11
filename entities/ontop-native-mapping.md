---
title: "Ontop native mapping (.obda)"
type: entity
subtype: convention
aliases: ["OBDA mapping file"]
tags: [obda]
concepts: ["[[rdb-to-rdf-mapping]]"]
sources: ["[[ontop-guide]]"]
updated: 2026-08-10
---

# Ontop native mapping (.obda)

## What it is
The Ontop native mapping language is a text-based (`.obda`) syntax for declaring how
relational data is exposed as RDF, provided by Ontop as an alternative to the W3C
R2RML standard and fully interoperable with it.

## Key facts
- An OBDA mapping file has two sections: a `PrefixDeclaration` of prefix-to-IRI pairs and a `MappingDeclaration` of mapping assertions ⟨guide: mapping-language⟩.
- Each mapping assertion has three fields — a `mappingId` string, a `source` (an arbitrary SQL query over the database), and a `target` triple template referencing the source query's columns ⟨guide: mapping-language⟩.
- The `target` uses an adaptation of Turtle subject-predicate-object syntax, where terms can be IRI/blank-node/literal constants, templates with `{column}` placeholders, or bare columns, and the predicate `a` is a shortcut for `rdf:type` ⟨guide: mapping-language/Target Triple Structure⟩.
- IRI and blank-node templates apply IRI-safe percent-encoding to their column values following the R2RML standard, whereas IRI columns are passed through untransformed and must already be valid IRIs ⟨guide: mapping-language/IRI or Blank Node Template⟩.
- The syntax supports Turtle-style compact predicate lists (`;`) and object lists (`,`), named graphs via the `GRAPH` keyword, explicit literal typing with `^^`, and constant language tags with `@` (language tags cannot be taken dynamically from the database) ⟨guide: mapping-language/Compact Form⟩.
- Meta-mapping assertions allow variables anywhere in the target, so class and property names can be constructed dynamically from database values ⟨guide: mapping-language/Meta-Mapping⟩.
- Ontop's SQL parser only parses simple source queries (no unions, aggregations, or order by); non-parsed queries are treated as black-box views sent directly to the database, limiting the optimizations Ontop can apply ⟨guide: mapping-language/Source Query⟩.

## Relations
- Realizes: [[rdb-to-rdf-mapping]]
- Defined in: [[ontop-guide]]
- Related: [[r2rml]] · [[ontop]]

## See also
[[ontop]] · [[r2rml]] · [[rdb-to-rdf-mapping]]

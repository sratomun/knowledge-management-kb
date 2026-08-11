---
title: "PerfectRef"
type: entity
subtype: technique
aliases: []
tags: [obda]
concepts: ["[[query-rewriting]]"]
sources: ["[[xiao-obda-survey]]"]
updated: 2026-08-09
---

# PerfectRef

## What it is
PerfectRef is a perfect-rewriting technique that reformulates a conjunctive query against
a DL-Lite ontology into a union of conjunctive queries capturing all certain answers.

## Key facts
- PerfectRef is a perfect-rewriting technique producing a sound and complete union of conjunctive queries for DL-Lite ⟨IJCAI 2018, pp. 5511-5519⟩.
- PerfectRef incorporates the ontology's axioms into the query so that ontology-entailed answers are captured under certain-answer semantics ⟨IJCAI 2018, pp. 5511-5519⟩.

## Relations
- Realizes: [[query-rewriting]]
- Defined in: [[xiao-obda-survey]]
- Related: [[tree-witness-rewriting]] · [[dl-lite]]

## See also
[[tree-witness-rewriting]] · [[query-rewriting]]

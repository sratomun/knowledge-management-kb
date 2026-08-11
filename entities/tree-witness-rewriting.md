---
title: "Tree-witness rewriting"
type: entity
subtype: technique
aliases: []
tags: [obda]
concepts: ["[[query-rewriting]]", "[[first-order-rewritability]]"]
sources: ["[[xiao-obda-survey]]", "[[ontop-swj]]"]
updated: 2026-08-10
---

# Tree-witness rewriting

## What it is
Tree-witness rewriting is an optimized query-rewriting technique that compactly encodes
existential reasoning to mitigate the combinatorial blow-up of naive rewritings in OBDA.

## Key facts
- Tree-witness rewriting is an optimization technique that reduces the size of query rewritings compared with naive approaches ⟨IJCAI 2018, pp. 5511-5519⟩.
- Tree-witness rewriting helps keep query answering first-order rewritable and practically executable as SQL ⟨IJCAI 2018, pp. 5511-5519⟩.
- The tree-witness query rewriting algorithm was implemented in Ontop to drastically reduce the size of rewritings and to take advantage of the T-mappings and the Semantic Index ⟨ontop-swj §7⟩.
- Adopting tree-witness rewriting addressed the earlier problem in QuOnto, whose PerfectRef algorithm could produce hundreds of thousands of conjunctive queries even for simple ontologies and mappings ⟨ontop-swj §7⟩.

## Relations
- Realizes: [[query-rewriting]]
- Realizes: [[first-order-rewritability]]
- Defined in: [[xiao-obda-survey]]
- Defined in: [[ontop-swj]]
- Related: [[perfectref]] · [[t-mappings]] · [[ontop]]

## See also
[[perfectref]] · [[query-rewriting]] · [[t-mappings]]

---
title: "SPARQL UNION"
type: entity
subtype: specification-construct
aliases: []
tags: [semantic-web]
concepts: ["[[graph-pattern-matching]]"]
sources: ["[[sparql-11-query]]"]
updated: 2026-08-10
---

# SPARQL UNION

## What it is
UNION is the SPARQL construct for matching alternatives: it combines graph patterns so that one of several alternative patterns may match, collecting the solutions of each.

## Key facts
- "SPARQL provides a means of combining graph patterns so that one of several alternative graph patterns may match. If more than one of the alternatives matches, all the possible pattern solutions are found." ⟨§7⟩
- "Pattern alternatives are syntactically specified with the UNION keyword." ⟨§7⟩
- Each alternative of a UNION can contain more than one triple pattern, and using different variables in the two branches reveals which branch produced a solution ⟨§7⟩
- "If neither part of the UNION pattern matched, then the graph pattern would not match." ⟨§7⟩

## Relations
- Realizes: [[graph-pattern-matching]]
- Defined in: [[sparql-11-query]]
- Related: [[sparql-bgp]] · [[sparql-optional]] · [[sparql-filter]]

## See also
[[graph-pattern-matching]] · [[org-w3c]]

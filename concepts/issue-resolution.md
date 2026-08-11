---
title: "Issue resolution"
type: concept
subtype: use-case-profile
aliases: []
tags: [knowledge-processing]
related: ["[[demand-driven-knowledge]]", "[[information-typing]]"]
updated: 2026-08-10
---

# Issue resolution

## What it is
Issue resolution is the knowledge-processing use case in which a user's reported problem drives the retrieval — or creation — of the knowledge that answers it. The defining query is roughly "how do I resolve this specific issue the user is experiencing?", and the artifact is a reusable support/help-desk answer produced or found in the flow of solving. Which processing pattern fits depends on the nature of the underlying documents: support content is typically low-normativity, moderately structured (typed articles), high-volatility, demand-created (its provenance is the interaction itself), and its lifecycle is tied to reuse rather than authoritative issuance. Those document-nature attributes — structure, normativity, volatility, sensitivity, provenance, lifecycle — condition how the pattern is realized.

## How sources treat it
- **[[kcs]]** _(provider-doc · vendor)_ — frames knowledge as a by-product of solving user issues in real time via the Solve Loop (Capture, Structure, Reuse, Improve), so resolution and knowledge creation are the same act rather than separate steps ⟨KCS v6 Practices Guide⟩ [gen]
- **[[kcs]]** _(provider-doc · vendor)_ — enumerates issue-resolution benefits including improved self-service for known issues, faster resolution and first-contact resolution, and fewer escalations/handoffs ⟨serviceinnovation.org/kcs⟩
- **[[dita]]** _(standard · normative)_ — supports resolution through information typing, providing a task type (procedural "how to") and a troubleshooting type (added in DITA 1.3) so resolution content is structured by its nature ⟨OASIS DITA 1.3 spec⟩ [gen]

## Where sources differ
The two sources approach issue resolution from different angles rather than in conflict. [[kcs]] is a process/operating-model view — it treats resolution as a real-time workflow in which articles are captured on demand and improved in the moment of use, emphasizing behaviour and content health over document form. [[dita]] is a document-architecture view — it says nothing about the resolution workflow but classifies the content itself into typed structures (task, troubleshooting) that a resolution process can consume. Both are authored [gen] in part (KCS's double-loop detail; all of DITA), a caveat each source page records.

## See also
[[demand-driven-knowledge]] · [[information-typing]]

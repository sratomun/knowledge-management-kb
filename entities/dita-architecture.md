---
title: "DITA architecture"
type: entity
subtype: framework
aliases: []
tags: [knowledge-processing]
concepts: ["[[information-typing]]"]
sources: ["[[dita]]"]
updated: 2026-08-10
---

# DITA architecture

## What it is
The DITA (Darwin Information Typing Architecture) architecture is an OASIS XML approach to topic-based, typed authoring in which content is written as discrete typed topics and assembled, reused, and filtered for delivery. Details below are `[gen]` from general knowledge, as the OASIS spec page was unreachable this session.

## Key facts
- Content is authored as discrete, self-contained **topics** — the unit of authoring, reuse, and management — rather than as monolithic documents ⟨OASIS DITA 1.3 spec⟩ [gen]
- Base **information types** classify content by nature: concept ("what it is"), task ("how to"), and reference (fact/lookup), with a generic topic parent and troubleshooting added in DITA 1.3 ⟨OASIS DITA 1.3 spec⟩ [gen]
- **Maps** (`.ditamap`) assemble topics into ordered, hierarchical deliverables — defining the table of contents, relationship tables, and links — without embedding topic content ⟨OASIS DITA 1.3 spec⟩ [gen]
- **Specialization** derives new, more specific topic and element types from base types while remaining compatible with base processing, enabling domain-specific types without breaking interoperability ⟨OASIS DITA 1.3 spec⟩ [gen]
- **Conditional processing / profiling** uses select attributes (audience, product, platform, otherprops, props, rev) and a DITAVAL (`.ditaval`) file to include, exclude, or flag content at build time, producing multiple audience-specific renditions from one source ⟨OASIS DITA 1.3 spec⟩ [gen]

## Relations
- Realizes: [[information-typing]]
- Defined in: [[dita]]
- Published by: [[org-oasis]]
- Related: [[document-element-classification]]

## See also
[[information-typing]] · [[document-element-classification]] · [[org-oasis]]

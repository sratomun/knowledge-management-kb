---
title: "DITA (Darwin Information Typing Architecture)"
type: source
kind: standard
authority: normative
subtype: standard
aliases: ["DITA", "Darwin Information Typing Architecture"]
publisher: "OASIS"
url: https://www.oasis-open.org/committees/dita/
version: "DITA 1.3"
published:
effective_from:
effective_to: ongoing
status: current
tags: [knowledge-processing]
updated: 2026-08-10
---

# DITA (Darwin Information Typing Architecture)

> _Authored from general knowledge, not the primary spec — verify._

DITA is an OASIS standard XML architecture for authoring, producing, and delivering topic-oriented, typed technical information. The canonical OASIS spec pages moved during an infrastructure migration and were not retrievable this session, so all points below are `[gen]` from general knowledge and should be verified against the OASIS DITA 1.3 specification before relying on element names or specifics.

## Scope & purpose
DITA (Darwin Information Typing Architecture) is an OASIS XML architecture for topic-based, typed authoring and multi-channel delivery of technical content, maintained by the OASIS DITA Technical Committee. It formalizes classifying content by its nature (information typing) and audience-adaptive delivery (conditional processing/profiling), letting a single authored source produce multiple filtered renditions.

## Structure
The architecture centers on discrete **topics** as the unit of authoring, reuse, and management; **maps** (`.ditamap`) that assemble topics into ordered, hierarchical deliverables with relationship tables and links; a small set of base **information types** (topic, concept, task, reference, plus troubleshooting in 1.3); **specialization** for deriving new types; and **conditional processing** driven by select attributes and DITAVAL filter files.

## Key points
- DITA is an OASIS standard XML architecture for authoring, producing, and delivering topic-oriented, typed technical information, maintained by the OASIS DITA Technical Committee (current base version DITA 1.3) ⟨OASIS DITA 1.3 spec⟩ [gen]
- **Topic-based authoring**: content is written as discrete, self-contained topics (each covering one subject) rather than monolithic documents; topics are the unit of authoring, reuse, and management ⟨OASIS DITA 1.3 spec⟩ [gen]
- **Information typing**: DITA defines base topic types that classify content by its nature — concept (explanatory "what it is"), task (procedural "how to"), and reference (fact/lookup: tables, syntax) — with a generic "topic" parent and troubleshooting added in DITA 1.3; typing by nature drives consistent structure and downstream processing ⟨OASIS DITA 1.3 spec⟩ [gen]
- **DITA maps**: a map (`.ditamap`) assembles topics into an ordered, hierarchical deliverable, defining the table of contents, relationships (reltables), and links between topics without embedding the topic content itself ⟨OASIS DITA 1.3 spec⟩ [gen]
- **Content reuse**: topics and elements are reused across deliverables via references (conref/keyref); keys indirect references so the same source resolves differently by context ⟨OASIS DITA 1.3 spec⟩ [gen]
- **Specialization**: new, more specific topic and element/attribute types can be derived from base types while remaining compatible with base processing — the "Darwin" (inheritance) aspect — enabling domain- or organization-specific types without breaking interoperability ⟨OASIS DITA 1.3 spec⟩ [gen]
- **Conditional processing / profiling**: elements carry select attributes (audience, product, platform, otherprops, props, rev) that mark content for filtering or flagging; a DITAVAL (`.ditaval`) file specifies which attribute values to include, exclude, or flag at build time, so a single source can produce multiple audience-specific renditions ⟨OASIS DITA 1.3 spec⟩ [gen]
- **Metadata**: topics carry prolog metadata (audience, author, keywords, etc.) supporting search, retrieval, and processing ⟨OASIS DITA 1.3 spec⟩ [gen]

## Concepts & entities covered
Concepts: [[information-typing]] · [[document-element-classification]]
Entities: [[dita-architecture]] · [[org-oasis]]

---
title: "OKF type frontmatter field"
type: entity
subtype: specification-construct
aliases: []
tags: [knowledge-management]
concepts: ["[[knowledge-interchange-format]]"]
sources: ["[[okf]]"]
updated: 2026-08-09
---

# OKF type frontmatter field

## What it is

The `type` field is the single mandatory YAML frontmatter field OKF requires of every concept document; it is the minimal interoperability surface the specification enforces, leaving all other structure to the producer.

## Key facts

- "OKF requires exactly one thing of every concept: a type field" ⟨Three principles behind the design⟩
- Everything else — "what types exist, what other fields to include, what sections the body has — is left to the producer" ⟨Three principles behind the design⟩
- "The spec defines the interoperability surface, not the content model" ⟨Three principles behind the design⟩
- `type` is one of the frontmatter fields "that need to be queryable," alongside title, description, resource, tags, and timestamp ⟨Introducing the Open Knowledge Format⟩

## Relations

- Realizes: [[knowledge-interchange-format]]
- Defined in: [[okf]]
- Related: [[okf-concept-file]]

## See also
[[okf-concept-file]] · [[okf-spec]]

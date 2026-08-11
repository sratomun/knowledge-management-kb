---
title: "OKF enrichment agent"
type: entity
subtype: vendor-product
aliases: []
tags: [knowledge-management]
concepts: ["[[agent-ready-knowledge]]"]
sources: ["[[okf]]"]
updated: 2026-08-09
---

# OKF enrichment agent

## What it is

The enrichment agent is a reference producer implementation shipped with OKF that generates conformant concept documents from a BigQuery dataset and then enriches them via a second LLM pass.

## Key facts

- It "walks a BigQuery dataset, drafts an OKF concept document for every table and view" ⟨What we're shipping with the spec⟩
- It "runs a second LLM pass that crawls authoritative documentation and enriches each concept with citations, schemas, and join paths" ⟨What we're shipping with the spec⟩
- It is a proof of concept: "The agent demonstrates one way to produce OKF; nothing about the format requires a specific agent framework or LLM" ⟨What we're shipping with the spec⟩

## Relations

- Realizes: [[agent-ready-knowledge]]
- Defined in: [[okf]]
- Published by: [[org-google-cloud]]
- Related: [[okf-visualizer]] · [[okf-bundle]]

## See also
[[okf-visualizer]] · [[agent-ready-knowledge]]

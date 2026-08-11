---
title: "Agent-Ready Knowledge"
type: concept
aliases: []
tags: [semantic-layer]
related: ["[[knowledge-interchange-format]]", "[[concept-per-file-bundle]]"]
updated: 2026-08-09
---

# Agent-Ready Knowledge

## What it is
Agent-ready knowledge is internal knowledge — schemas, metric definitions, runbooks, join paths, deprecation notices, and the like — captured in a form that AI and agentic systems can consume directly for context, without each builder re-solving context assembly from scratch. It is knowledge that is both human-friendly and parseable by agents with no translation layer, so it survives moving between systems.

## How sources treat it
- **[[okf]]** _(provider-doc · vendor)_ — motivates the format by the problem that internal knowledge (table schemas, metric definitions, runbooks, join paths, deprecation notices) is scattered across fragmented, mutually incompatible systems, forcing every agent builder to solve context assembly from scratch ⟨Scope & purpose⟩
- **[[okf]]** _(provider-doc · vendor)_ — positions OKF as a portable, interoperable format for the metadata, context, and curated knowledge that modern AI and agentic systems need, described as agent- and human-friendly ⟨Introducing the Open Knowledge Format⟩
- **[[okf]]** _(provider-doc · vendor)_ — argues the needed answer is knowledge readable by humans and parseable by agents with no translation layer, that survives moving between systems and lives in version control ⟨What's missing is a format, not another service⟩
- **[[okf]]** _(provider-doc · vendor)_ — cites Andrej Karpathy's LLM Wiki gist that LLMs "don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass," making the bookkeeping humans abandon exactly what LLMs are good at ⟨Knowledge as a living wiki⟩
- **[[okf]]** _(provider-doc · vendor)_ — ships reference tooling that makes knowledge agent-consumable: an enrichment agent drafting a concept doc per BigQuery table/view, and Google Cloud's Knowledge Catalog updated to ingest OKF and serve it to agents ⟨What we're shipping with the spec⟩

## Where sources differ
Only [[okf]] addresses agent-ready knowledge in this KB, as a vendor provider-doc from Google Cloud. With a single source, no divergence can be reported.

## See also
[[knowledge-interchange-format]] · [[concept-per-file-bundle]]

<!-- REVIEW: possible J1 near-duplicate between [[agent-ready-knowledge]] and [[knowledge-interchange-format]] (both sourced only from OKF). Judge confidence low-med: property-vs-mechanism split is defensible. Human to decide merge vs keep. -->

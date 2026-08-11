---
title: "Knowledge Interchange Format"
type: concept
aliases: []
tags: [semantic-layer]
related: ["[[agent-ready-knowledge]]", "[[concept-per-file-bundle]]"]
updated: 2026-08-09
---

# Knowledge Interchange Format

## What it is
A knowledge interchange format is a shared, vendor-neutral convention for representing curated knowledge so that it can pass between different producers and consumers without a translation layer. The emphasis is on the format as a contract — anyone can produce it without a special SDK and anyone can consume it without an integration — rather than on a service, runtime, or platform that owns the knowledge.

## How sources treat it
- **[[okf]]** _(provider-doc · vendor)_ — frames its answer as "a format, not another service" — knowledge anyone can produce without an SDK and consume without an integration, that survives moving between systems and lives in version control ⟨What's missing is a format, not another service⟩
- **[[okf]]** _(provider-doc · vendor)_ — represents knowledge as a directory of markdown files with YAML frontmatter plus a small set of agreed-upon conventions, so wikis from different producers can be consumed by different agents without translation ⟨Introducing the Open Knowledge Format⟩
- **[[okf]]** _(provider-doc · vendor)_ — a bundle is "just markdown, just files, just YAML frontmatter" with no compression scheme, no new runtime, and no required SDK ⟨Introducing the Open Knowledge Format⟩
- **[[okf]]** _(provider-doc · vendor)_ — Principle 2, Producer/consumer independence: the format is the contract and the tooling at each end is independently swappable ⟨Three principles behind the design⟩
- **[[okf]]** _(provider-doc · vendor)_ — Principle 3, Format not platform: OKF is not tied to any cloud, database, model provider, or agent framework and will never require a proprietary account or SDK to read, write, or serve ⟨Three principles behind the design⟩
- **[[okf]]** _(provider-doc · vendor)_ — Principle 1, Minimally opinionated: OKF requires exactly one thing of every concept — a `type` field — defining the interoperability surface, not the content model ⟨Three principles behind the design⟩

## Where sources differ
Only [[okf]] addresses the knowledge interchange format idea in this KB, as a vendor provider-doc from Google Cloud. With a single source, no divergence can be reported.

## See also
[[agent-ready-knowledge]] · [[concept-per-file-bundle]]

<!-- REVIEW: possible J1 near-duplicate between [[agent-ready-knowledge]] and [[knowledge-interchange-format]] (both sourced only from OKF). Judge confidence low-med: property-vs-mechanism split is defensible. Human to decide merge vs keep. -->

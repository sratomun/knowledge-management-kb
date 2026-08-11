---
title: "Domain-oriented decentralized data ownership"
type: entity
subtype: principle
aliases: ["Data mesh domain ownership principle"]
tags: [data-architecture]
concepts: ["[[domain-oriented-ownership]]", "[[data-mesh]]"]
sources: ["[[data-mesh-dehghani]]"]
updated: 2026-08-09
---

# Domain-oriented decentralized data ownership

## What it is
The first data mesh principle: distribute ownership of analytical data, its metadata, and the computation that serves it to the teams closest to the data, decomposed along business-domain seams.

## Key facts
- Data mesh is founded in decentralization and distribution of responsibility to people closest to the data, to support continuous change and scalability ⟨martinfowler.com/articles/data-mesh-principles.html, §Domain Ownership⟩
- The components decentralized are analytical data, its metadata, and the computation necessary to serve it ⟨martinfowler.com/articles/data-mesh-principles.html, §Domain Ownership⟩
- Decomposition follows the seams of organizational units — business domains and their bounded contexts — localizing the impact of continuous change ⟨martinfowler.com/articles/data-mesh-principles.html, §Domain Ownership⟩
- Each domain exposes both operational APIs and analytical data endpoints, and must serve/deploy its analytical data independently of other domains ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: domain-oriented data and compute⟩
- Enables scale-out: as the number of sources, use cases, and access models grows, one simply adds autonomous nodes to the mesh ⟨martinfowler.com/articles/data-mesh-principles.html, §Principles Summary and the high level logical architecture⟩

## Relations
- Realizes: [[domain-oriented-ownership]]
- Defined in: [[data-mesh-dehghani]]
- Related: [[dm-principle-data-as-product]]

## See also
[[data-mesh]] · [[person-dehghani]] · [[org-thoughtworks]]

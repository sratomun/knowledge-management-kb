---
title: "Data mesh supervision plane"
type: entity
subtype: specification-construct
aliases: ["Data mesh mesh-supervision plane"]
tags: [data-architecture]
concepts: ["[[self-serve-data-platform]]"]
sources: ["[[data-mesh-dehghani]]"]
updated: 2026-08-09
---

# Data mesh supervision plane

## What it is
The highest self-serve platform plane, providing capabilities best offered globally at the level of the mesh — the graph of connected data products.

## Key facts
- Provides a set of capabilities best delivered at the mesh level — a graph of connected data products — globally ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩
- Supports the ability to discover data products for a particular use case, best provided by searching or browsing the mesh of data products ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩
- Supports correlating multiple data products to create higher-order insight, best provided through execution of a data semantic query operating across multiple data products on the mesh ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩

## Relations
- Realizes: [[self-serve-data-platform]]
- Defined in: [[data-mesh-dehghani]]
- Related: [[dm-plane-infrastructure]] · [[dm-plane-devex]]

## See also
[[self-serve-data-platform]] · [[dm-principle-self-serve]]

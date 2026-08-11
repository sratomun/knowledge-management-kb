---
title: "Data infrastructure provisioning plane"
type: entity
subtype: specification-construct
aliases: ["Data mesh infrastructure provisioning plane"]
tags: [data-architecture]
concepts: ["[[self-serve-data-platform]]"]
sources: ["[[data-mesh-dehghani]]"]
updated: 2026-08-09
---

# Data infrastructure provisioning plane

## What it is
The lowest of the three self-serve data platform planes, responsible for provisioning the underlying infrastructure needed to run the components of a data product and the mesh of products.

## Key facts
- Supports provisioning of the underlying infrastructure required to run the components of a data product and the mesh of products ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩
- Includes provisioning of distributed file storage, storage accounts, an access control management system, orchestration to run data products' internal code, and a distributed query engine over a graph of data products ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩
- Expected to be used directly only by other platform planes or by advanced data product developers; it is a fairly low-level data infrastructure lifecycle management plane ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩
- A plane represents a level of existence — integrated yet separate — and is neither a layer nor implies a strong hierarchical access model ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩

## Relations
- Realizes: [[self-serve-data-platform]]
- Defined in: [[data-mesh-dehghani]]
- Related: [[dm-plane-devex]] · [[dm-plane-supervision]]

## See also
[[self-serve-data-platform]] · [[dm-principle-self-serve]]

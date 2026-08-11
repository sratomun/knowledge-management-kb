---
title: "Data product developer experience plane"
type: entity
subtype: specification-construct
aliases: ["Data mesh developer experience plane"]
tags: [data-architecture]
concepts: ["[[self-serve-data-platform]]"]
sources: ["[[data-mesh-dehghani]]"]
updated: 2026-08-09
---

# Data product developer experience plane

## What it is
The middle self-serve platform plane and the main interface a typical data product developer uses, abstracting the complexities of the data product developer's workflow.

## Key facts
- This is the main interface that a typical data product developer uses, abstracting many of the complexities of supporting the developer's workflow ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩
- Provides a higher level of abstraction than the provisioning plane and uses simple declarative interfaces to manage the lifecycle of a data product ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩
- Automatically implements the cross-cutting concerns defined as a set of standards and global conventions applied to all data products and their interfaces ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩

## Relations
- Realizes: [[self-serve-data-platform]]
- Defined in: [[data-mesh-dehghani]]
- Related: [[dm-plane-infrastructure]] · [[dm-plane-supervision]]

## See also
[[self-serve-data-platform]] · [[dm-principle-self-serve]]

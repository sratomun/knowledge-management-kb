---
title: "Self-serve data infrastructure as a platform"
type: entity
subtype: principle
aliases: ["Data mesh self-serve platform principle"]
tags: [data-architecture]
concepts: ["[[self-serve-data-platform]]", "[[data-mesh]]"]
sources: ["[[data-mesh-dehghani]]"]
updated: 2026-08-09
---

# Self-serve data infrastructure as a platform

## What it is
The third data mesh principle: provide a high-level infrastructure-as-a-platform abstraction that removes the complexity and friction of provisioning and managing data products, enabling domain autonomy.

## Key facts
- The only way teams can autonomously own their data products is access to a high-level abstraction of infrastructure that removes provisioning and lifecycle complexity ⟨martinfowler.com/articles/data-mesh-principles.html, §Self-serve data platform⟩
- The self-serve platform must provide a new category of tools and interfaces so generalist developers can build data products with less specialized knowledge than existing technologies assume ⟨martinfowler.com/articles/data-mesh-principles.html, §Self-serve data platform⟩
- The platform can be considered an extension of the existing delivery platform, though the big-data technology stack today differs from the operational delivery platform ⟨martinfowler.com/articles/data-mesh-principles.html, §Self-serve data platform⟩
- Its capabilities fall into multiple planes, each serving a different profile of platform users ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩
- So that domain teams can create and consume data products autonomously using platform abstractions that hide the complexity of building, executing, and maintaining secure, interoperable data products ⟨martinfowler.com/articles/data-mesh-principles.html, §Principles Summary and the high level logical architecture⟩

## Relations
- Realizes: [[self-serve-data-platform]]
- Defined in: [[data-mesh-dehghani]]
- Related: [[dm-plane-infrastructure]] · [[dm-plane-devex]] · [[dm-plane-supervision]]

## See also
[[data-mesh]]

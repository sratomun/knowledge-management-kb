---
title: "Data product owner"
type: entity
subtype: role
aliases: ["Domain data product owner"]
tags: [data-architecture]
concepts: ["[[data-product]]"]
sources: ["[[data-mesh-dehghani]]"]
updated: 2026-08-09
---

# Data product owner

## What it is
A domain role introduced by data mesh, accountable for the objective measures that ensure a domain's analytical data is delivered as a product.

## Key facts
- Organizations must introduce the domain data product owner role, responsible for the objective measures that ensure data is delivered as a product ⟨martinfowler.com/articles/data-mesh-principles.html, §Data as a product⟩
- Accountable measures include data quality, decreased lead time of data consumption, and general data user satisfaction through net promoter score ⟨martinfowler.com/articles/data-mesh-principles.html, §Data as a product⟩
- Must have a deep understanding of who the data users are, how they use the data, and the native methods they are comfortable consuming it with ⟨martinfowler.com/articles/data-mesh-principles.html, §Data as a product⟩
- Together with data platform product owners, forms the federation that leads the governance decision-making model ⟨martinfowler.com/articles/data-mesh-principles.html, §Federated computational governance⟩
- Best placed to decide how to measure their domain's data quality, while complying with global quality/SLO standards automated by the platform ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: computational policies embedded in the mesh⟩

## Relations
- Realizes: [[data-product]]
- Defined in: [[data-mesh-dehghani]]
- Related: [[dm-principle-data-as-product]] · [[dm-principle-federated-governance]]

## See also
[[data-product]] · [[dm-data-product-characteristics]]

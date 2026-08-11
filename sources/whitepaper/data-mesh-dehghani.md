---
title: "Data Mesh (Dehghani)"
type: source
kind: whitepaper
authority: practitioner
subtype: book
aliases: ["Data Mesh (book)", "Dehghani"]
publisher: "O'Reilly Media"
url: https://www.oreilly.com/library/view/data-mesh/9781492092384/
version: "1st edition"
published: 2022-03
effective_from: 2022-03
effective_to: ongoing
status: current
tags: [data-architecture]
updated: 2026-08-09
---
# Data Mesh (Dehghani)

## Scope & purpose

> Note: the book itself is a paid title and was not consulted. Key points below come from (1) a secondary source — Zhamak Dehghani's canonical article 'Data Mesh Principles and Logical Architecture' (martinfowler.com, 2020), which mirrors the book's four principles — and (2) general knowledge; they are not quoted from the book's text.

## Structure

Data mesh is organized around four principles plus a supporting platform:

1. Domain-oriented decentralized data ownership and architecture
2. Data as a product
3. Self-serve data infrastructure as a platform
4. Federated computational governance

The self-serve platform is realized as a multi-plane architecture (data infrastructure provisioning plane, data product developer experience plane, and data mesh supervision plane), each serving a different profile of platform users.

## Key points

- Data mesh is a paradigm shift for managing analytical data at scale, addressing dimensions that prior technology failed to address: change in the data landscape, proliferation of sources, diversity of use cases and users, and speed of response to change ⟨martinfowler.com/articles/data-mesh-principles.html, §intro⟩
- Today's data landscape is split across two planes — operational data (transactional, current state, behind microservices) and analytical data (temporal, aggregated, feeds ML and reports) — connected by fragile, continuously failing ETL pipelines ⟨martinfowler.com/articles/data-mesh-principles.html, §The great divide of data⟩
- The four principles are intended to be collectively necessary and sufficient to enable scale with resiliency while avoiding siloing of incompatible data and increased operational cost ⟨martinfowler.com/articles/data-mesh-principles.html, §Core principles and logical architecture of data mesh⟩
- Domain ownership decentralizes responsibility for analytical data, its metadata, and its serving computation to the teams closest to the data, following the seams of business domains and their bounded contexts ⟨martinfowler.com/articles/data-mesh-principles.html, §Domain Ownership⟩
- Each domain exposes both operational APIs and analytical data endpoints, and must be able to serve and deploy its analytical data independently of other domains ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: domain-oriented data and compute⟩
- Data as a product treats analytical data as a product and its consumers as delighted customers, addressing the friction and cost of discovering, understanding, trusting, and using data — the "dark data" problem ⟨martinfowler.com/articles/data-mesh-principles.html, §Data as a product⟩
- The data product owner role is accountable for objective product measures — data quality, decreased lead time of consumption, and user satisfaction (net promoter score); the accountability for data quality shifts upstream, as close to the source as possible ⟨martinfowler.com/articles/data-mesh-principles.html, §Data as a product⟩
- The data product is the architectural quantum — the smallest unit of architecture independently deployable with high functional cohesion — encapsulating three structural components: code, data-and-metadata, and infrastructure ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture:data product the architectural quantum⟩
- Unlike prior paradigms where pipelines and shared warehouse/lake infrastructure are managed independently of the data, a data product composes code, data, and infrastructure together at the granularity of a domain's bounded context ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture:data product the architectural quantum⟩
- The self-serve data platform provides high-level infrastructure abstractions so generalist domain developers can autonomously build, deploy, monitor, and access data products without specialized big-data skills ⟨martinfowler.com/articles/data-mesh-principles.html, §Self-serve data platform⟩
- The platform is organized into three planes — infrastructure provisioning plane, data product developer experience plane, and data mesh supervision plane — where a plane is a level of existence, not a strict hierarchical layer ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: a multi-plane data platform⟩
- Federated computational governance is a decision-making model led by domain data product owners and platform product owners, balancing domain autonomy with global interoperability rules that are automatically executed by the platform ⟨martinfowler.com/articles/data-mesh-principles.html, §Federated computational governance⟩
- Global decisions exist to create interoperability and a compounding network effect through discovery and composition of data products; domains model polysemes — data elements crossing multiple domain boundaries — such as a unified 'user' identity ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: computational policies embedded in the mesh⟩
- Data mesh governance inverts traditional centralized governance: instead of certifying golden datasets and centrally cleansing data, domains apply quality assurance locally while complying with global standards and SLOs automated by the platform ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: computational policies embedded in the mesh⟩
- Success is measured by the network effect (connections representing consumption of data on the mesh) rather than by the number or volume of governed tables, and governance shifts from preventing errors to detecting and recovering from them automatically ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: computational policies embedded in the mesh⟩

## Concepts & entities covered

Concepts: [[data-mesh]] · [[data-product]] · [[domain-oriented-ownership]] · [[self-serve-data-platform]] · [[federated-computational-governance]] · [[architectural-quantum]] · [[analytical-vs-operational-plane]]
Entities: [[dm-principle-domain-ownership]] · [[dm-principle-data-as-product]] · [[dm-principle-self-serve]] · [[dm-principle-federated-governance]] · [[dm-data-product-characteristics]] · [[dm-plane-infrastructure]] · [[dm-plane-devex]] · [[dm-plane-supervision]] · [[dm-role-data-product-owner]]

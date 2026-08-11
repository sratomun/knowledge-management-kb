---
title: "Data Product"
type: concept
tags: [data-architecture]
related: ["[[data-mesh]]", "[[dataset-description]]", "[[data-catalog]]", "[[domain-oriented-ownership]]", "[[architectural-quantum]]"]
updated: 2026-08-10
---

# Data Product

## What it is

"Data product" names the idea that data should be packaged, delivered, and maintained the way a product is — with an owner, defined consumers, quality expectations, and a stable interface — rather than dumped into a shared store as a by-product of some other system. Different communities stress different parts of this idea: ownership and accountability, catalogued publication, or portable self-describing packaging.

## How sources treat it

- **[[data-mesh-dehghani]]** _(whitepaper · practitioner)_ — Data as a product treats analytical data as a product and its consumers as delighted customers, addressing the friction and cost of discovering, understanding, trusting, and using data — the "dark data" problem ⟨martinfowler.com/articles/data-mesh-principles.html, §Data as a product⟩
- **[[data-mesh-dehghani]]** _(whitepaper · practitioner)_ — A data product owner is accountable for objective product measures — data quality, decreased lead time of consumption, and user satisfaction (net promoter score) — and the accountability for data quality shifts upstream, as close to the source as possible ⟨martinfowler.com/articles/data-mesh-principles.html, §Data as a product⟩
- **[[data-mesh-dehghani]]** _(whitepaper · practitioner)_ — The data product is the architectural quantum — the smallest unit of architecture independently deployable with high functional cohesion — encapsulating three structural components: code, data-and-metadata, and infrastructure ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture:data product the architectural quantum⟩
- **[[data-monolith-to-mesh]]** _(blog · practitioner)_ — Origin (2019): domain teams must "apply product thinking with similar rigor to the datasets that they provide; considering their data assets as their products and the rest of the organization's data scientists, ML and data engineers as their customers" ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Domain data as a product⟩
- **[[data-monolith-to-mesh]]** _(blog · practitioner)_ — Enumerates the required qualities of a domain data product: Discoverable (register in a central data catalogue), Addressable (unique global-convention address for polyglot storage), Trustworthy & truthful (SLOs on data integrity, plus provenance and lineage as metadata), Self-describing semantics & syntax (schemas and sample datasets), Inter-operable & governed by global standards (harmonization rules, polyseme identity via federated entity identifiers), and Secure & governed by global access control (SSO/RBAC applied per data product) ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Domain data as a product⟩
- **[[data-monolith-to-mesh]]** _(blog · practitioner)_ — Introduces the **data product owner** role, who owns the vision/roadmap, consumer satisfaction, and lifecycle of the domain datasets, and defines business-aligned KPIs such as the "lead time for consumers of a data product to discover and use the data product successfully" ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Domain data cross-functional teams⟩
- **[[data-monolith-to-mesh]]** _(blog · practitioner)_ — Illustrates that one domain may expose multiple data products with different SLOs — e.g. a 'play events' domain serving near-real-time events (lower accuracy, possible missing/duplicate events) and higher-accuracy delayed aggregates ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Trustworthy and truthful⟩
- **[[dcat-3]]** _(standard · normative)_ — Does not use the term "data product"; its nearest framing is a dataset as a "collection of data, published or curated by a single agent, and available for access or download in one or more serializations or formats" — a conceptual entity distinct from its distributions ⟨§5.1⟩
- **[[dcat-3]]** _(standard · normative)_ — A dataset can be delivered as an operational interface via `dcat:DataService`, giving access to one or more datasets or data processing functions ⟨§5.1, §6.9⟩
- **[[okf]]** _(provider-doc · vendor)_ — Does not use the term "data product"; it represents each unit of data or knowledge as a "concept" — one markdown file whose file path is the concept's identity, cross-linked into a graph ⟨How OKF works: The design in one screen⟩
- **[[okf]]** _(provider-doc · vendor)_ — Frames such units around producer/consumer independence: the format is the contract and the tooling at each end is independently swappable, so a producer's knowledge is portable to any consumer without an integration ⟨Three principles behind the design⟩

## Where sources differ

The three sources frame the unit of data very differently. Data Mesh (Dehghani) alone uses "data as a product" explicitly and loads it with organizational meaning: an accountable product owner, consumer-satisfaction metrics, upstream quality accountability, and a self-contained architectural quantum bundling code, data-and-metadata, and infrastructure. DCAT-3 never speaks of a "product"; it frames the unit as a *dataset* — a cataloged, published-or-curated resource described by metadata and delivered through distributions or data services — an interoperability-and-discovery framing with no notion of ownership-as-product. OKF also avoids "data product," framing the unit as a portable, self-describing *concept* file whose value proposition is producer/consumer independence and format portability rather than product ownership or catalog conformance. In short: an accountability/ownership framing (Data Mesh), a publication/catalog framing (DCAT), and a packaging/portability framing (OKF). Within the Data Mesh framing itself, [[data-monolith-to-mesh]] (2019) is the origin that first enumerated the product qualities (discoverable, addressable, trustworthy, self-describing, interoperable, secure), while the later [[data-mesh-dehghani]] (2021) recast the data product as the self-contained architectural quantum bundling code, data-and-metadata, and infrastructure.

## See also
[[data-mesh]] · [[architectural-quantum]] · [[domain-oriented-ownership]] · [[dataset-description]] · [[data-catalog]]

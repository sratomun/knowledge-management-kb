---
title: "How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh"
type: source
kind: blog
authority: practitioner
subtype: article
aliases: ["Data Monolith to Mesh", "Dehghani 2019"]
publisher: "martinfowler.com"
url: https://martinfowler.com/articles/data-monolith-to-mesh.html
version: "2019-05-20"
published: 2019-05
effective_from: 2019-05
effective_to: ongoing
status: current
tags: [data-architecture]
updated: 2026-08-10
---

# How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh

## Scope & purpose
Zhamak Dehghani's original 2019 article introducing **data mesh**. It argues that data-lake and data-warehouse platforms share common failure modes at enterprise scale, and proposes a paradigm shift built on the convergence of distributed domain-driven architecture, product thinking with data, and self-serve platform design. Written for software leadership and enterprise architects, using an internet media-streaming business (Spotify, SoundCloud, iTunes) as its running example. This is the ORIGINATING articulation of data mesh; it predates Dehghani's later "Data Mesh Principles and Logical Architecture" article that crystallized the four principles (domain ownership, data as a product, self-serve platform, federated computational governance).

## Structure
- §The current enterprise data platform architecture — three generations of centralized, monolithic, domain-agnostic data platforms (EDW/BI, data lake, streaming/cloud) and why they underdeliver
- §Architectural failure modes — three recurring failure modes: centralized & monolithic; coupled pipeline decomposition; siloed & hyper-specialized ownership
- §The next enterprise data platform architecture — the proposed convergence of three disciplines
- §Domain oriented data decomposition and ownership — inverting locality/ownership so domains host and serve their own datasets; the domain (not the pipeline stage) becomes the architectural quantum
- §Source oriented domain data — reality/fact datasets aligned to systems of origin
- §Consumer oriented and shared domain data — datasets fitted to consumption, plus newly reified shared datasets
- §Distributed pipelines as domain internal implementation — pipelines become an internal implementation detail of each domain
- §Domain data as a product — product thinking applied to datasets, with a set of required qualities
- §(qualities) Discoverable, Addressable, Trustworthy and truthful, Self-describing semantics and syntax, Inter-operable and governed by global standards, Secure and governed by a global access control
- §Domain data cross-functional teams — new roles: data product owner and embedded data engineers
- §Data and self-serve platform design convergence — domain-agnostic self-serve data infrastructure as a platform
- §The paradigm shift towards a data mesh — synthesis; data lake/warehouse become mere nodes on the mesh; new governing principles/language

## Key points
- The article opens by asserting that data platforms based on the data-lake architecture "have common failure modes that lead to unfulfilled promises at scale," motivating a shift away from centralized lake/warehouse paradigms ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §The current enterprise data platform architecture⟩
- It frames three generations of data platforms — (1) proprietary EDW/BI with large price tags and unmaintainable ETL tech debt, (2) big-data ecosystem with the data lake as a "silver bullet" run by hyper-specialized engineers, (3) streaming (Kappa), unified batch/stream (Apache Beam) and cloud managed services — all sharing the failings of their predecessors ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §The current enterprise data platform architecture⟩
- First failure mode, **centralized & monolithic**: one platform ingests, cleanses/transforms, and serves data owned across many disparate domains; it can work for simple domains but "fails for enterprises with rich domains, a large number of sources and a diverse set of consumers" under the pressures of ubiquitous data/source proliferation and consumer/innovation proliferation ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Centralized and monolithic⟩
- Second failure mode, **coupled pipeline decomposition**: decomposing the platform into ingestion/cleansing/aggregation/serving stages is "decomposed orthogonally to the axis of change" — a new feature (e.g. 'podcasts play rate') requires changes across every stage, so the whole monolithic pipeline is the smallest unit that must change ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Coupled pipeline decomposition⟩
- Third failure mode, **siloed & hyper-specialized ownership**: data platform engineers are siloed by big-data tooling expertise, "often absent of business and domain knowledge," disconnected from both source teams (no incentive to provide good data) and frustrated consumers fighting for backlog priority ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Siloed and hyper-specialized ownership⟩
- The proposed answer is a **convergence of Distributed Domain Driven Architecture, Self-serve Platform Design, and Product Thinking with Data**, applying lessons from a decade of distributed operational systems to the domain of data ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §The next enterprise data platform architecture⟩
- **Domain-oriented decomposition**: reverse how we think about data locality and ownership so that "domains need to host and serve their domain datasets in an easily consumable way," shifting from a push-and-ingest (ETL/event) model to a serving-and-pull model; this may duplicate data across domains as each shapes it for its needs ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Domain oriented data decomposition and ownership⟩
- The **architectural quantum** in a domain-oriented data platform is "a domain and not the pipeline stage" (borrowing the quantum concept from Building Evolutionary Architectures) ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Domain oriented data decomposition and ownership⟩
- **Source-oriented domain data** are fact/reality datasets aligned to systems of origin, best served as immutable time-stamped business Domain Events plus periodic historical snapshots; they change less often, must be separated from operational systems' internal data, and are permanently captured ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Source oriented domain data⟩
- **Consumer-oriented and shared domain data** are transformed/aggregated to fit particular access models (e.g. a social-network graph), change more structurally, and can be regenerated from source; frequently useful datasets may be "reified" into shared domain datasets ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Consumer oriented and shared domain data⟩
- **Distributed pipelines as internal implementation**: cleansing/prep/aggregation still happen but become an internal implementation detail of each domain rather than shared stages; each domain dataset establishes Service Level Objectives (timeliness, error rates) ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Distributed pipelines as domain internal implementation⟩
- **Data as a product**: domain teams treat datasets as products and other data scientists/engineers as customers; the article enumerates required product qualities — Discoverable (registry/data catalogue), Addressable (unique global-convention address for polyglot storage), Trustworthy & truthful (SLOs, provenance, lineage, integrity testing at creation), Self-describing semantics & syntax (schemas, sample data), Inter-operable & governed by global standards (harmonization, polysemes, federated entity identifiers), and Secure & governed by global access control (SSO, RBAC applied per-product) ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Domain data as a product⟩
- **Cross-functional domain data teams** need two new roles: a **data product owner** (owns vision/roadmap, consumer satisfaction, dataset lifecycle, business-aligned KPIs such as consumer lead time) and embedded **data engineers**, ending the local optimization of centralized data-engineering teams ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Domain data cross-functional teams⟩
- **Self-serve data infrastructure as a platform** harvests domain-agnostic capabilities (polyglot big-data storage, encryption, versioning, schema, de-identification, unified access control, orchestration, catalog registration, lineage, monitoring, quality metrics, federated identity, compute/data locality) so domains don't duplicate effort; success is measured by lowering the "lead time to create a new data product" ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §Data and self-serve platform design convergence⟩
- In the resulting **data mesh** the data lake and data warehouse are "simply nodes on the mesh"; the mesh is "an intentionally designed distributed data architecture, under centralized governance and standardization for interoperability, enabled by a shared and harmonized self-serve data infrastructure" — not fragmented silos ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §The paradigm shift towards a data mesh⟩
- The article closes with new governing language: "serving over ingesting; discovering and using over extracting and loading; publishing events as streams over flowing data around via centralized pipelines; ecosystem of data products over centralized data platform" ⟨martinfowler.com/articles/data-monolith-to-mesh.html, §The paradigm shift towards a data mesh⟩

## Concepts & entities covered
Concepts: —
Entities: [[person-dehghani]] · [[org-thoughtworks]]

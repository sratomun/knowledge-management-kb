---
title: "Federated Computational Governance"
type: concept
tags: [data-architecture]
related: ["[[data-mesh]]", "[[data-governance]]", "[[domain-oriented-ownership]]", "[[self-serve-data-platform]]"]
updated: 2026-08-09
---

# Federated Computational Governance

## What it is

Federated computational governance is a governance model for decentralized data in which the domains that own the data participate in setting global rules, and those rules are then encoded and enforced automatically by the platform rather than by a central authority making case-by-case decisions. It balances local domain autonomy against organization-wide interoperability.

## How sources treat it

- **[[data-mesh-dehghani]]** _(whitepaper · practitioner)_ — Federated computational governance is a decision-making model led by domain data product owners and platform product owners, balancing domain autonomy with global interoperability rules that are automatically executed by the platform ⟨martinfowler.com/articles/data-mesh-principles.html, §Federated computational governance⟩
- **[[data-mesh-dehghani]]** _(whitepaper · practitioner)_ — Global decisions exist to create interoperability and a compounding network effect through discovery and composition of data products; domains model polysemes — data elements crossing multiple domain boundaries — such as a unified 'user' identity ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: computational policies embedded in the mesh⟩
- **[[data-mesh-dehghani]]** _(whitepaper · practitioner)_ — Inverts traditional centralized governance: instead of certifying golden datasets and centrally cleansing data, domains apply quality assurance locally while complying with global standards and SLOs automated by the platform, and governance shifts from preventing errors to detecting and recovering from them automatically ⟨martinfowler.com/articles/data-mesh-principles.html, §Logical architecture: computational policies embedded in the mesh⟩

## Where sources differ

Data Mesh (Dehghani) explicitly frames this model as an inversion of "traditional centralized governance." That contrast is with the arrangement DAMA-DMBOK2 depicts elsewhere in the corpus, where Data Governance sits at the hub of the DAMA Wheel providing authority, oversight, and policy centrally across all knowledge areas ⟨DAMA Wheel⟩. The two describe opposite loci of control — automated federation across domains versus a central coordinating function — and the corpus records both without reconciling them.

## See also
[[data-mesh]] · [[data-governance]] · [[domain-oriented-ownership]] · [[self-serve-data-platform]]

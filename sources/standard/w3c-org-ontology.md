---
title: "The Organization Ontology (W3C ORG)"
type: source
kind: standard
authority: normative
subtype: standard
aliases: ["W3C ORG", "ORG ontology"]
publisher: "W3C"
url: https://www.w3.org/TR/vocab-org/
version: "W3C Recommendation 2014-01-16"
published: 2014-01
effective_from: 2014-01
effective_to: ongoing
status: current
tags: [semantic-web]
updated: 2026-08-10
---

# The Organization Ontology (W3C ORG)

> _Authored from general knowledge, not from the primary text. Verify against the primary W3C Recommendation before relying on specifics or term IRIs._

## Scope & purpose
The W3C Organization Ontology is a vocabulary for publishing information about organizations and organizational structure as linked data, designed for interoperability and extension into domain-specific models (government, business). Captured here **lightweight** as a semantic-web vocabulary relevant to modeling an enterprise in a knowledge graph.

## Key points
- Provides core classes including `org:Organization`, `org:FormalOrganization`, `org:OrganizationalUnit`, `org:Site`, `org:Post`, `org:Role`, and `org:Membership` ⟨W3C ORG, §Classes⟩ [gen]
- Models **membership** as an n-ary relation (`org:Membership`) linking an agent, an organization, and a role, so that role and time context can be attached ⟨W3C ORG, §Membership⟩ [gen]
- Reuses and aligns with existing vocabularies such as FOAF, SKOS, Dublin Core, and W3C Time, rather than redefining them ⟨W3C ORG, §Overview⟩ [gen]
- Is explicitly designed as a **generic core to be extended** for specific domains (e.g., reporting structures, organizational change over time) ⟨W3C ORG, §Introduction⟩ [gen]
- Supports representing organizational **change over time** (e.g., merging, splitting) through dedicated terms ⟨W3C ORG, §Organizational change⟩ [gen]

## Concepts & entities covered
Concepts: [[organization-ontology]]
Entities: [[org-w3c]]

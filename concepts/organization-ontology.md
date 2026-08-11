---
title: "Organization ontology"
type: concept
subtype: null
aliases: []
tags: [semantic-web]
related: ["[[rdf-vocabulary-schema]]", "[[linked-data]]"]
updated: 2026-08-10
---

# Organization ontology

## What it is
A reusable RDF vocabulary for describing organizations, their internal structure (units, sites, posts, roles), and memberships, designed as a generic core to be extended for specific domains and to model organizational change over time.

## How sources treat it
- **[[w3c-org-ontology]]** _(standard · normative)_ — provides core classes `org:Organization`, `org:FormalOrganization`, `org:OrganizationalUnit`, `org:Site`, `org:Post`, `org:Role`, and `org:Membership` ⟨W3C ORG, §Classes⟩ [gen]
- **[[w3c-org-ontology]]** _(standard · normative)_ — models membership as an n-ary relation linking an agent, an organization, and a role, and reuses FOAF, SKOS, Dublin Core, and W3C Time rather than redefining them ⟨W3C ORG, §Membership⟩ [gen]

## Where sources differ
Single normative source; it is deliberately a generic core intended to be extended rather than a complete domain model.

## See also
[[rdf-vocabulary-schema]] · [[temporal-ontology]] · [[linked-data]]

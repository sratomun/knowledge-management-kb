---
title: "European Case Law Identifier (ECLI)"
type: source
kind: standard
authority: normative
subtype: standard
aliases: ["ECLI", "European Case Law Identifier"]
publisher: "Council of the European Union"
url: https://en.wikipedia.org/wiki/European_Case_Law_Identifier
version: ""
published: 2011
effective_from: 2011-04-29
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# European Case Law Identifier (ECLI)

## Scope & purpose

The European Case Law Identifier (ECLI) is an identifier for court decisions in European Union member states, together with a minimum set of uniform metadata for case law ⟨Wikipedia, intro⟩. **Note on sourcing:** the raw for this page is a Wikipedia article, a **secondary** summary of the EU Council Conclusions inviting the introduction of the ECLI; the **primary** source is the Council Conclusions 2011/C 127/01 (decided 22 Dec 2010; published in the Official Journal 29 April 2011), which should be verified before relying on specifics ⟨Wikipedia, secondary-source note⟩. The ECLI framework contains a uniform metadata set to improve search facilities for case law, and decisions with an ECLI can be indexed by the ECLI Search Engine of the European e-Justice portal ⟨Wikipedia, intro⟩. The ECLI metadata set is based on the Dublin Core (`dcterms`) metadata standard ⟨Wikipedia, Metadata⟩.

## Structure

- Identifier: five colon-separated parts — `ECLI` self-identifier, country code, court code, year, unique code ⟨Wikipedia, Identifier construction⟩
- Metadata: nine mandatory and eight optional elements, all based on Dublin Core ⟨Wikipedia, Metadata⟩
- Governance: Council of Ministers responsible for changes; Commission maintains the website and Search Engine; national ECLI co-ordinators per Member State ⟨Wikipedia, Governance⟩

## Key points

- The standard is laid down in the Council Conclusions inviting the introduction of the ECLI and a minimum set of uniform metadata (decided 22 Dec 2010; published 29 April 2011, 2011/C 127/01) ⟨Wikipedia, intro⟩.
- ECLI does not primarily identify a paper or electronic document but identifies the court decision at a more abstract level — in FRBR terminology it is a work-level identifier ⟨Wikipedia, Identifier construction⟩.
- ECLI is intended to be meaningful, open, technologically neutral, recognisable for humans and computers, error-proof, and interoperable ⟨Wikipedia, Identifier construction⟩.
- An ECLI consists of five parts separated by colons: `ECLI`; a country code; a court code; the year of the judgment; and a unique code ⟨Wikipedia, Identifier construction⟩.
- The country code is mostly ISO 3166-1 alpha-2 (with UK, and EL for Greece; special codes for non-states assigned by the European Commission) ⟨Wikipedia, Identifier construction⟩.
- The court code is assigned by the national ECLI co-ordinator (max 7 positions), and the unique code is max 25 chars of letters, digits, and dots ⟨Wikipedia, Identifier construction⟩.
- ECLI uses only the Latin alphabet and is case-insensitive (preferably capitals); e.g. `ECLI:NL:HR:1841:1` is a Dutch 1841 Supreme Court decision, serial 1, with a resolver at e-justice.europa.eu ⟨Wikipedia, Identifier construction⟩.
- The Council Conclusions list nine mandatory and eight optional metadata elements, all based on the Dublin Core metadata standard ⟨Wikipedia, Metadata⟩.
- Mandatory metadata include `dcterms:identifier`, `dcterms:isVersionOf`, `dcterms:creator`, `dcterms:coverage`, `dcterms:date`, `dcterms:language`, `dcterms:publisher`, `dcterms:accessRights`, and `dcterms:type` (defaulting to "judicial decision") ⟨Wikipedia, Metadata⟩.
- Metadata can relate to the ECLI itself (bibliographic work level, e.g. date of decision) or to a specific editorial version (expression level, e.g. a summary) ⟨Wikipedia, Metadata⟩.
- Governance is shared: the Council of Ministers is responsible for future changes and the European Commission maintains the ECLI website and Search Engine ⟨Wikipedia, Governance⟩.
- Each participating Member State (or entity, including the EU itself) has a national ECLI co-ordinator who decides court codes, the fifth-part construction, national info pages, and metadata language varieties ⟨Wikipedia, Governance⟩.
- Member States choose their own implementation route (big-bang or step-by-step); Slovenia was the first to implement (2011) ⟨Wikipedia, Governance⟩.

## Concepts & entities covered

Concepts: [[legal-resource-identifier]] · [[descriptive-metadata]]

Entities: [[org-eu-commission]]

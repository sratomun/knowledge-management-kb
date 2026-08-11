---
title: "DCMI Metadata Terms (Dublin Core)"
type: source
kind: standard
authority: normative
subtype: metadata-vocabulary
aliases: ["Dublin Core", "DCMI Metadata Terms", "DCMI Terms"]
publisher: Dublin Core Metadata Initiative
url: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
version: "2020-01-20"
published: 2020-01
effective_from: 2020-01-20
effective_to: ongoing
status: current
tags: [metadata, semantic-web]
updated: 2026-08-09
---

# DCMI Metadata Terms (Dublin Core)

## Scope & purpose

An up-to-date, authoritative specification of all metadata terms maintained by the Dublin Core Metadata Initiative (DCMI): properties, vocabulary encoding schemes, syntax encoding schemes (datatypes), and classes. It bundles the fifteen terms of the Dublin Core Metadata Element Set ("the Dublin Core") plus several dozen extension properties, classes, datatypes, and vocabulary encoding schemes, collectively "DCMI metadata terms." The terms are intended for use in combination with terms from other compatible vocabularies within application profiles. They are expressed as RDF vocabularies for Linked Data, but non-RDF users (XML, JSON, UML, relational databases) may treat domain/range/subproperty/subclass relations as usage suggestions and rely on the natural-language definitions. The document is a descriptive, non-adjudicating registry of term definitions; it standardizes descriptive metadata for resource discovery across heterogeneous systems.

## Structure

The specification organizes terms across four DCMI namespaces (each backed by an RDF schema) and nine numbered sections:

- `http://purl.org/dc/elements/1.1/` — the legacy fifteen-element Dublin Core (created 2000); corresponds to the original scope of ISO 15836 (first published 2003, revised as ISO 15836-1:2017).
- `http://purl.org/dc/terms/` — the full term set (created 2001), including the fifteen elements mirrored with formal ranges; the most useful properties/classes are published as ISO 15836-2:2019. DCMI gently encourages use of this namespace over /elements/1.1/.
- `http://purl.org/dc/dcmitype/` — the DCMI Type Vocabulary (created 2001): classes for basic types of resource.
- `http://purl.org/dc/dcam/` — the DCMI Abstract Model terms (created 2008) used to describe the vocabulary itself (domainIncludes, rangeIncludes, memberOf, VocabularyEncodingScheme).

Sections: (1) Introduction and Definitions; (2) Properties in /terms/; (3) Properties in /elements/1.1/; (4) Vocabulary Encoding Schemes; (5) Syntax Encoding Schemes; (6) Classes; (7) DCMI Type Vocabulary; (8) Terms for vocabulary description; (9) Bibliography. Each term is specified with minimal attributes (Name, Label, URI, Definition, Type of Term) and optional additional attributes (Comment, See, Subproperty Of, Sub/Superclass Of, Domain, Domain Includes, Range, Range Includes, Member Of, Instance Of, Equivalent Property).

## Key points

- The specification bundles the fifteen-element Dublin Core plus "several dozen properties, classes, datatypes, and vocabulary encoding schemes," collectively "DCMI metadata terms." ⟨§1 Introduction⟩
- Terms are expressed in RDF vocabularies for use in Linked Data; non-RDF users may disregard RDF-specific implications and rely on natural-language definitions. ⟨§1 Introduction⟩
- Each term is identified with a URI serving as a global identifier that resolves to this document in a browser or to one of four RDF schemas programmatically. ⟨§1 Introduction⟩
- Four namespaces exist: /elements/1.1/, /terms/, /dcmitype/, and /dcam/. ⟨§1 Introduction⟩
- The /elements/1.1/ namespace (2000) holds the original fifteen elements and corresponds to the original scope of ISO 15836, revised in 2017 as ISO 15836-1:2017. ⟨§1 Introduction⟩
- The fifteen elements were mirrored into /terms/ in 2008 with formal semantic constraints; e.g. dcterms:date has a formal range of "literal" while dc:date has none. Most users can treat the parallel properties as equivalent. ⟨§1 Introduction⟩
- The most useful properties and classes are published as ISO 15836-2:2019; /elements/1.1/ "will be supported indefinitely" but DCMI "gently encourages use of the /terms/ namespace." ⟨§1 Introduction⟩
- The /terms/ namespace defines ~55 properties including 40+ beyond the core fifteen (e.g. abstract, accessRights, conformsTo, created, modified, issued, license, provenance, spatial, temporal). ⟨§2 Properties in /terms/⟩
- Vocabulary Encoding Schemes name external controlled vocabularies for values: DCMIType, DDC, IMT, LCC, LCSH, MESH, NLM, TGN, UDC. ⟨§4 Vocabulary Encoding Schemes⟩
- Syntax Encoding Schemes (datatypes) specify value syntaxes: Box, ISO3166, ISO639-2, ISO639-3, Period, Point, RFC1766, RFC3066, RFC4646, RFC5646, URI, W3CDTF. ⟨§5 Syntax Encoding Schemes⟩
- Successive language-tag RFCs are cross-linked by supersession: RFC 5646 obsoletes RFC 4646, which obsoletes RFC 3066, which obsoleted RFC 1766. ⟨§5 Syntax Encoding Schemes⟩
- Classes model value types and resource types: Agent, AgentClass, BibliographicResource, FileFormat, Frequency, Jurisdiction, LicenseDocument, LinguisticSystem, Location, MediaType, PeriodOfTime, PhysicalResource, Policy, RightsStatement, SizeOrDuration, Standard, and others. ⟨§6 Classes⟩
- The DCMI Type Vocabulary enumerates twelve resource-genre classes, each a member of DCMIType: Collection, Dataset, Event, Image, InteractiveResource, MovingImage, PhysicalObject, Service, Software, Sound, StillImage, Text. ⟨§7 DCMI Type Vocabulary⟩
- Recommended practice repeatedly points to external controlled vocabularies (e.g. Getty TGN for coverage, Internet Media Types for format, ISO 639 / BCP 47 for language, ISO 8601 / W3CDTF / EDTF for dates). ⟨§2 Properties in /terms/⟩
- The /dcam/ namespace supplies the meta-vocabulary used to describe the terms themselves: domainIncludes, rangeIncludes, memberOf, and the VocabularyEncodingScheme class. ⟨§8 Terms for vocabulary description⟩
- Document status is "DCMI Recommendation," issued 2020-01-20 by the DCMI Usage Board, licensed CC BY 4.0. ⟨§ header⟩

## Concepts & entities covered
Concepts: [[descriptive-metadata]] · [[application-profile]] · [[vocabulary-encoding-scheme]] · [[syntax-encoding-scheme]] · [[controlled-vocabulary]]
Entities: [[dcterms-title]] · [[dcterms-creator]] · [[dcterms-subject]] · [[dcterms-date]] · [[dcterms-type]] · [[dcterms-contributor]] · [[dcterms-coverage]] · [[dcterms-description]] · [[dcterms-format]] · [[dcterms-identifier]] · [[dcterms-language]] · [[dcterms-publisher]] · [[dcterms-relation]] · [[dcterms-rights]] · [[dcterms-source]] · [[dc-elements-namespace]] · [[dcterms-namespace]] · [[dcmitype-namespace]] · [[dcam-namespace]] · [[ves-ddc]] · [[ves-lcc]] · [[ves-lcsh]] · [[ves-mesh]] · [[ves-udc]] · [[ves-tgn]] · [[ses-w3cdtf]] · [[ses-iso8601]] · [[ses-rfc5646]] · [[ses-box]] · [[ses-point]] · [[ses-period]] · [[class-agent]] · [[class-bibliographicresource]] · [[class-location]] · [[class-rightsstatement]] · [[class-mediatype]] · [[class-standard]] · [[dcmitype-collection]] · [[dcmitype-dataset]] · [[dcmitype-image]] · [[dcmitype-text]] · [[dcmitype-event]] · [[dcmitype-service]] · [[dcmitype-software]] · [[dcmitype-sound]] · [[dcmitype-movingimage]] · [[dcmitype-stillimage]] · [[dcmitype-physicalobject]] · [[dcmitype-interactiveresource]] · [[iso-15836-1-2017]] · [[iso-15836-2-2019]]

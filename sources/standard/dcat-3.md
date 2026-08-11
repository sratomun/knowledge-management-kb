---
title: "DCAT 3: Data Catalog Vocabulary"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["DCAT", "DCAT 3", "Data Catalog Vocabulary"]
publisher: W3C
url: https://www.w3.org/TR/vocab-dcat-3/
version: "3"
published: 2024-08
effective_from: 2024-08-22
effective_to: ongoing
status: current
tags: [metadata, data-architecture]
updated: 2026-08-09
---
# DCAT 3: Data Catalog Vocabulary

## Scope & purpose

DCAT (Data Catalog Vocabulary) is an RDF vocabulary published as a W3C Recommendation (22 August 2024) and designed to facilitate interoperability between data catalogs published on the Web ⟨Abstract⟩. It enables a publisher to describe datasets and data services in a catalog using a standard model and vocabulary that facilitates consumption and aggregation of metadata from multiple catalogs, increasing discoverability and enabling federated search across catalogs ⟨Abstract, §1⟩. The DCAT namespace is `http://www.w3.org/ns/dcat#` with suggested prefix `dcat` ⟨Abstract⟩. DCAT 3 is a major revision of DCAT 2 that adds versioning, dataset series, and checksum support while preserving backward compatibility; it supersedes DCAT 2 but does not make it obsolete ⟨Status⟩. The document was produced by the W3C Dataset Exchange Working Group (DXWG) ⟨Status⟩. The specification is descriptive of a modeling vocabulary; it does not prescribe any particular method of deploying catalogs, syntax, access protocol, or access policy ⟨§1, §4⟩.

## Structure (§ numbers)

- §1 Introduction; §2 Motivation for change
- §3 Namespaces (§3.1 normative, §3.2 non-normative)
- §4 Conformance
- §5 Vocabulary overview (§5.1 DCAT scope, §5.2 RDF considerations, §5.3 Basic example, §5.4–5.9 classification/access examples)
- §6 Vocabulary specification — classes and properties: §6.3 Catalog, §6.4 Cataloged Resource (dcat:Resource), §6.5 Catalog Record, §6.6 Dataset, §6.7 Dataset Series, §6.8 Distribution, §6.9 Data Service, §6.10 Concept Scheme, §6.11 Concept, §6.12 Organization/Person, §6.13 Relationship, §6.14 Role, §6.15 Period of Time, §6.16 Location, §6.17 Checksum
- §7 Use of inverse properties; §8 Dereferenceable identifiers; §9 License and rights statements; §10 Time and space
- §11 Versioning; §12 Dataset series; §13 Data citation; §14 Quality information; §15 Qualified relations; §16 DCAT Profiles
- §17 Security and Privacy Considerations; §18 Accessibility Considerations
- Appendices: A Acknowledgments, B Alignment with Schema.org, C Examples, D–J Change history, K References

## Key points

- DCAT is based around seven main classes: `dcat:Catalog`, `dcat:Resource`, `dcat:Dataset`, `dcat:Distribution`, `dcat:DataService`, `dcat:DatasetSeries`, and `dcat:CatalogRecord` ⟨§5.1⟩.
- `dcat:Resource` is the parent class of `dcat:Dataset`, `dcat:DataService` and `dcat:Catalog`; it "is actually an extension point for defining a catalog of any kind of resources" and is not intended to be used directly ⟨§5.1⟩.
- A dataset is defined as a "collection of data, published or curated by a single agent, and available for access or download in one or more serializations or formats"; a dataset is a conceptual entity distinct from its distributions ⟨§5.1⟩.
- A conforming catalog MUST organize access to data into datasets, distributions, data services and dataset series, and an RDF description of the catalog, its cataloged resources and distributions MUST be available ⟨§4⟩.
- All classes and properties defined in DCAT MUST be used in a way consistent with the semantics declared in this specification; DCAT-compliant catalogs MAY include additional non-DCAT metadata fields ⟨§4⟩.
- The key words MAY, MUST, MUST NOT, and SHOULD are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals ⟨§4⟩.
- `dcat:Distribution` represents an accessible form of a dataset such as a downloadable file; `dcat:accessURL` gives a location that gives access, while `dcat:downloadURL` is used for a direct, downloadable distribution ⟨§5.1, §6.8.9, §6.8.11⟩.
- `dcat:DataService` represents a collection of operations accessible through an interface (API) providing access to one or more datasets or data processing functions; its root endpoint is given by `dcat:endpointURL` and `dcat:servesDataset` links it to datasets ⟨§5.1, §6.9⟩.
- DCAT 3 added a `dcat:DatasetSeries` class and properties (`dcat:inSeries`, `dcat:seriesMember`, and ordering properties `dcat:first`/`dcat:last`/`dcat:prev`/`dcat:next`) for representing collections of datasets published separately but sharing characteristics ⟨Status, §6.7, §12⟩.
- DCAT 3 added properties for versioning — e.g., `dcat:version`, `dcat:previousVersion`, `dcat:hasCurrentVersion`, `dcat:hasVersion`, `dcterms:replaces`, `adms:versionNotes`, `adms:status` — following the [PAV] approach for version chains and hierarchies ⟨Status, §6.4, §11⟩.
- DCAT 3 added the `spdx:checksum` property and `spdx:Checksum` class (with `spdx:algorithm` and `spdx:checksumValue`) to provide a digest for DCAT distributions ⟨Status, §6.8.20, §6.17⟩.
- DCAT incorporates terms from pre-existing vocabularies (e.g., `foaf:homepage`, `dcterms:title`); definitions of terms outside the DCAT namespace are provided for convenience and MUST NOT be considered normative ⟨External terms, §6.2.2⟩.
- Where possible, DCAT properties do not have specified domains, to leave the property open for reuse with any kind of resource ⟨§6.1⟩.
- It is recommended that instances of the DCAT main classes have a global identifier (IRI); use of blank nodes is generally discouraged when encoding DCAT in RDF ⟨§5.2⟩.
- `dcat:resource` (added in DCAT 3) is the most general predicate for membership of a catalog and is a sub-property of `dcterms:hasPart`; `dcat:dataset`, `dcat:service` and `dcat:catalog` are sub-properties of it ⟨§6.3.3⟩.
- A DCAT profile is a specification that adds additional constraints to DCAT (cardinality, sub-classes/sub-properties, controlled vocabularies, required access mechanisms); a catalog conforming to the profile also conforms to DCAT ⟨§4, §16⟩.
- Qualified relations (`dcat:qualifiedRelation` with `dcat:Relationship`/`dcat:hadRole`) and qualified attribution (`prov:qualifiedAttribution`) allow the role of a related resource or agent to be characterized where a simple property is insufficient ⟨§6.4.15, §6.4.18, §15⟩.

## Concepts & entities covered
Concepts: [[data-catalog]] · [[dataset-description]] · [[data-distribution]] · [[data-service]] · [[dataset-series]] · [[catalog-record]]
Entities: [[dcat-catalog]] · [[dcat-resource]] · [[dcat-dataset]] · [[dcat-distribution]] · [[dcat-dataservice]] · [[dcat-datasetseries]] · [[dcat-catalogrecord]] · [[dcat-checksum]] · [[dcat-accessurl]] · [[dcat-downloadurl]] · [[dcat-endpointurl]] · [[dcat-2]]

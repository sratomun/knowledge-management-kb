---
title: "Akoma Ntoso Version 1.0 (LegalDocML)"
type: source
kind: standard
authority: normative
subtype: standard
aliases: ["Akoma Ntoso", "LegalDocML"]
publisher: OASIS
url: https://docs.oasis-open.org/legaldocml/akn-core/v1.0/os/part1-vocabulary/akn-core-v1.0-os-part1-vocabulary.html
version: "1.0"
published: 2018
effective_from: 2018-08-29
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# Akoma Ntoso Version 1.0 (LegalDocML)

## Scope & purpose

Akoma Ntoso (LegalDocML) is an OASIS Standard providing a common data and metadata model for parliamentary, legislative, and judicial documents, aimed at their interchange between institutions anywhere in the world and at long-term storage and access with search, interpretation, and visualization ⟨§2.1⟩. This page covers **both** the Akoma Ntoso v1.0 standard as a whole and, specifically, its **Part 1: XML Vocabulary** work product, which sets out the motivations, scope, and design principles of the XML standard ⟨Abstract⟩. Part 1 is explicitly non-normative narrative material intended to present Akoma Ntoso's pillars to stakeholders deciding how to manage legal sources digitally in a Semantic Web society ⟨§1.4⟩; the accompanying Part 2 (Specifications) and the XML schemas carry the normative machine-readable content ⟨Additional artefacts⟩. Akoma Ntoso is an open standard whose stated goal is to make the structure and meaning of legal documents "machine readable" through XML markup ⟨§2.1⟩. Concrete element/attribute definitions cited here are drawn from Part 1's descriptive prose; where a plain-text machine-readable file and the prose disagree, the plain-text file prevails ⟨Notices⟩.

## Structure

- §1 Introduction (IPR, Terminology, Normative/Non-normative References, Status) ⟨§1⟩
- §2 Overview — Descriptiveness; rich data models (ontologies); separation of data and metadata ⟨§2⟩
- §3 Scope of the language — document format, interchange model, document-centric schema, metadata schema & ontology, citation/cross-referencing ⟨§3⟩
- §4 Design issues — simple data model (XML schema, URI/IRI, FRBR, ontology, design patterns), widest scope, author/editor distinction, content/structure/semantics/presentation ⟨§4⟩
- §5 Basic building blocks — document types, generic and borrowed HTML elements, references, metadata, analytical metadata ⟨§5⟩
- §6 Akoma Ntoso document types (collection, hierarchical, debate, amendment, judgment, open, portion structures) ⟨§6⟩
- §7 Levels of Compliance; §8 Conformance; Appendices A–B ⟨§7–§8⟩

## Key points

- The standard defines a common legal document format, a common model for document interchange, a common data schema, a common metadata schema and ontology, and a common model for citation and cross-referencing ⟨§3.1⟩.
- The declared XML namespace is `http://docs.oasis-open.org/legaldocml/ns/akn/3.0`, the official unambiguous identifier of the language ⟨§4.1.1⟩.
- The vocabulary currently defines 310 element names and 69 attribute names, using lowerCamelCase for both (e.g. `mainBody`, `amendmentList`, `showAs`, `refersTo`) ⟨§4.1.1⟩.
- Defining the XML language proceeds through four specifications — namespace, vocabulary, grammar (content models), and semantics — a four-part distinction made explicit to ensure long-lived, widely usable documents ⟨§4.1.1⟩.
- Descriptiveness is a core principle: every part with a relevant meaning and role must have a machine-readable "name" (tag) revealing its structural or semantic role, with generic elements used only when no specific term is available ⟨§2.2⟩.
- The Akoma Ntoso informal ontology is centred on the document and models legal resources at the four IFLA FRBR levels — WORK, EXPRESSION, MANIFESTATION, and ITEM ⟨§4.1.3⟩.
- The schema organizes all content models into six categories — markers, inlines, blocks, subFlow, containers, and hierarchy — so elements can be treated by category rather than individually ⟨§4.1.5.1⟩.
- All metadata elements are markers, so metadata values are held as attribute values and are not part of a document's text content ⟨§4.1.5.1⟩.
- Akoma Ntoso makes an explicit and complete separation between the role of authors (responsible for content) and editors (who mark up, name, and add metadata), with markup, naming, and metadata treated as editorial processes ⟨§2.4⟩.
- The specification supports major legal document types — bill/act (hierarchicalStructure), debate (debateStructure), judgment (judgmentStructure), amendment (amendmentStructure), documentCollection/officialGazette/amendmentList (collectionStructure), doc/statement (openStructure), and portion (portionStructure) ⟨§4.2.1⟩.
- The Akoma Ntoso naming convention provides a persistent, location-independent mechanism for resource identification and active referencing, enabling full automation of access across a distributed hypertext of legal documents ⟨§3.6⟩.
- Metadata values are collected according to a common ontology and offer direct translation of some values into corresponding Dublin Core metadata properties, while remaining extensible for parliaments and courts with more specific needs ⟨§3.5⟩.
- The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL are to be interpreted as described in RFC 2119 ⟨§1.1⟩.
- Objectives include being self-explanatory (understandable through examination of the schema and examples without specialized software) and extensible (allowing local customisation without sacrificing interoperability) ⟨§2.1⟩.

## Concepts & entities covered

Concepts: [[legislative-document-model]] · [[document-element-classification]]

Entities: [[org-oasis]]

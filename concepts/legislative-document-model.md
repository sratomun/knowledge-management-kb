---
title: "Legislative Document Model"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[legal-resource-identifier]]"]
updated: 2026-08-10
---

# Legislative Document Model

## What it is
A legislative document model is a structured, machine-readable representation of legal documents — legislation, parliamentary debates, judgments, amendments — that captures their hierarchy, content, semantics, and metadata rather than treating them as opaque text. It makes the structure and meaning of legal sources explicit so they can be interchanged, stored, searched, cited, and processed across institutions.

## How sources treat it
- **[[akoma-ntoso]]** _(standard · normative)_ — An OASIS Standard providing a common data and metadata model for parliamentary, legislative, and judicial documents, defining a common document format, interchange model, data schema, metadata schema and ontology, and citation/cross-referencing model ⟨§3.1⟩
- **[[akoma-ntoso]]** _(standard · normative)_ — Its informal ontology is centred on the document and models legal resources at the four IFLA FRBR levels — WORK, EXPRESSION, MANIFESTATION, and ITEM ⟨§4.1.3⟩
- **[[eli-akn-mapping]]** _(article · informational)_ — Motivates alignment between ELI (identifier + metadata ontology for legislation) and Akoma Ntoso (XML document model), which address complementary but distinct layers of the legal-document stack ⟨general knowledge⟩

## Where sources differ
The sources treat the document-model layer consistently and complementarily. [[akoma-ntoso]] specifies the model itself — a normative XML vocabulary with FRBR-based abstraction and a document-centric ontology; [[eli-akn-mapping]] positions that document model as one layer to be aligned with the identifier/metadata layer of ELI, noting both draw on FRBR-style abstraction as an anchor for mapping ⟨general knowledge⟩. The mapping source is authored lightweight-from-knowledge and flags that its specifics should be verified against the primary text.

## See also
[[legal-resource-identifier]] · [[machine-readable-legal-norms]] · [[document-element-classification]]

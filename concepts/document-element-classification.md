---
title: "Document Element Classification"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[document-layout-analysis]]", "[[document-parsing]]"]
updated: 2026-08-10
---

# Document Element Classification

## What it is
Document element classification is the assignment of semantic or structural types to the parts of a document — labelling a block as a title, paragraph, list item, table, or figure, or labelling a whole document by type. It spans several granularities: element-level typing within a page, page/document-level type classification, and the tagging of legal or domain structures with their role.

## How sources treat it
- **[[akoma-ntoso]]** _(standard · normative)_ — Descriptiveness is a core principle: every part with a relevant meaning and role must have a machine-readable "name" (tag) revealing its structural or semantic role, with generic elements used only when no specific term is available ⟨§2.2⟩
- **[[unstructured-io]]** _(provider-doc · vendor)_ — Precise document extraction: the library extracts elements and metadata from documents, including a variety of document element types and metadata ⟨Overview: Key functionality⟩
- **[[cuad]]** _(article · informational)_ — Frames contract review as classifying and extracting clause spans across 41 label categories, with models predicting the relevant span for each category ⟨arXiv:2103.06268, §3 Task Definition⟩
- **[[google-document-ai]]** _(provider-doc · vendor)_ — Classifies document types to drive downstream processes such as extraction and storage, and can split and classify documents by type (e.g., a PDF containing multiple real documents) ⟨Document AI overview: "Using Document AI"⟩

## Where sources differ
The sources classify at different granularities and are complementary rather than competing. [[akoma-ntoso]] mandates element-level semantic tagging as a normative design principle for legal XML; [[unstructured-io]] classifies content into a set of document element types during partitioning; [[cuad]] classifies text spans into 41 legal clause categories; [[google-document-ai]] classifies and splits at the whole-document level to route processing. Each operates on a different unit — legal structure, generic block, clause span, or document — so together they span the granularity range without contradiction.

## See also
[[document-layout-analysis]] · [[document-parsing]] · [[contract-clause-extraction]] · [[legislative-document-model]]

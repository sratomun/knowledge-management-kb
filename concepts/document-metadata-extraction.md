---
title: "Document Metadata Extraction"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[descriptive-metadata]]", "[[provenance]]"]
updated: 2026-08-10
---

# Document Metadata Extraction

## What it is
Document metadata extraction is the derivation of structured descriptive data about a document — such as title, authors, language, references, key-value fields, or text-derived attributes like entities and key phrases — from the document's content. It ranges from bibliographic metadata about the whole document to field- and entity-level data mined from the body text, and it feeds catalogues, search, and downstream retrieval.

## How sources treat it
- **[[docling]]** _(provider-doc · vendor)_ — Extracts metadata from the document, such as title, authors, references, and language, augmenting features via language detection, figure–caption matching, and metadata labelling during assembly ⟨tech report §1⟩
- **[[eli]]** _(standard · normative)_ — Pillar 2 (Description): metadata is added to the legal text describing aspects such as the type of legislation, when it was adopted, and the jurisdiction it is subject to ⟨Pillar 2⟩
- **[[aws-comprehend]]** _(provider-doc · vendor)_ — A natural language processing (NLP) service positioned to derive and understand valuable insights from text within documents, whose capabilities typically include entity recognition, key phrase extraction, and sentiment analysis as text-derived metadata ⟨Comprehend overview: capability list [gen]⟩

## Where sources differ
The sources extract metadata at different levels and are complementary. [[docling]] extracts bibliographic metadata (title, authors, references, language) as a byproduct of conversion; [[eli]] specifies a normative descriptive-metadata layer added to legislation (type, adoption date, jurisdiction) rather than extracted automatically; [[aws-comprehend]] mines text-derived attributes (entities, key phrases, sentiment) via NLP, with its capability list flagged as general knowledge because the product page did not fully load. These describe different targets — document-level bibliographic data, prescribed legal metadata, and mined text attributes — without conflicting.

## See also
[[descriptive-metadata]] · [[provenance]] · [[legal-resource-identifier]] · [[intelligent-document-processing]]

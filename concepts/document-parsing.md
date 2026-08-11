---
title: "Document Parsing"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[layout-aware-parsing]]", "[[semantic-chunking]]", "[[reading-order-reconstruction]]"]
updated: 2026-08-10
---

# Document Parsing

## What it is
Document parsing is the conversion of raw documents — PDFs, images, office files, HTML — into a structured, machine-processable representation that preserves more than plain text: element types, hierarchy, layout, and relationships. It is the front of a document-processing or retrieval pipeline, turning unstructured input into typed content that downstream stages (chunking, embedding, extraction) can consume.

## How sources treat it
- **[[docling]]** _(provider-doc · vendor)_ — Parses PDF and other formats into a machine-processable representation via a linear pipeline (PDF backend, layout analysis, table structure, optional OCR, assembly), exporting a unified DoclingDocument to Markdown, HTML, lossless JSON, DocTags, and more ⟨tech report §3⟩
- **[[unstructured-io]]** _(provider-doc · vendor)_ — Partitioning functions extract structured content from raw, unstructured documents, transforming unorganized data into usable formats, with both open-source and Pipelines/API offerings emitting a canonical JSON schema ⟨Overview: Key functionality⟩
- **[[gcp-parse-chunk]]** _(provider-doc · vendor)_ — Provides three parser techniques — a digital parser, an OCR parser for PDFs, and a layout parser — and also allows bringing your own parsed documents ⟨Parse & chunk: PARSERS⟩
- **[[document-parsing-rag-omdena]]** _(blog · practitioner)_ — Defines document parsing for RAG as converting raw documents into structured, semantically meaningful content that can be indexed, retrieved, and used by LLMs, going beyond simple text extraction by preserving structure, hierarchy, and relationships ⟨Omdena, What is document parsing for RAG⟩
- **[[chonkie-docling-unstructured]]** _(blog · practitioner)_ — Characterizes Docling as a high-fidelity conversion toolkit strongest at the "Extract" stage (PDFs with tables, multi-column layouts, formulas) and Unstructured as an end-to-end ETL platform whose defining trait is breadth of connectivity ⟨thinkdeeply.ai, §2.2 Docling⟩

## Where sources differ
The sources describe overlapping but differently scoped parsing surfaces and are largely complementary. [[docling]] frames parsing as a fixed model-driven linear pipeline emitting one rich document object; [[unstructured-io]] frames it as modular partitioning into a canonical element schema across many formats; [[gcp-parse-chunk]] exposes parsing as a choice among digital, OCR, and layout parsers tied to a retrieval product. The two practitioner blogs add framing rather than mechanism: [[document-parsing-rag-omdena]] positions parsing as the foundation whose errors propagate through the RAG chain, while [[chonkie-docling-unstructured]] (itself AI-generated) contrasts libraries versus platforms and reports third-party fidelity numbers. None is presented as authoritative over the others.

## See also
[[layout-aware-parsing]] · [[semantic-chunking]] · [[reading-order-reconstruction]] · [[optical-character-recognition]] · [[intelligent-document-processing]]

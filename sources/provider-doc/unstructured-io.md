---
title: "Unstructured — Open-Source Document Processing (Docs)"
type: source
kind: provider-doc
authority: vendor
subtype: system
aliases: ["Unstructured open source"]
publisher: Unstructured
url: https://docs.unstructured.io/
version: "current"
published: 2024-01
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# Unstructured — Open-Source Document Processing (Docs)

## Scope & purpose
The Unstructured open-source documentation describes an open-source Python toolkit for
ingesting and pre-processing diverse document formats — PDFs, images, HTML, Word, and more —
and transforming them into structured formats optimized for Large Language Model (LLM)
workflows. It is vendor documentation covering the library's core functionality
(partitioning, cleaning, extracting, staging, chunking), its intended prototyping role, and
its limits relative to the commercial Unstructured Pipelines/API.

## Key points
- The Unstructured open-source library is a toolkit designed to simplify the ingestion and pre-processing of diverse data formats — including images and text-based documents such as PDFs, HTML, and Word — providing modular functions and connectors that transform unstructured data into structured formats, with a focus on optimizing data workflows for LLMs ⟨Overview⟩
- The open-source library is designed as a starting point for quick prototyping and has limits; for production scenarios Unstructured recommends its Pipelines/API ⟨Overview⟩
- Precise document extraction: the library extracts elements and metadata from documents, including a variety of document element types and metadata ⟨Overview: Key functionality⟩
- Partitioning functions extract structured content from raw, unstructured documents, transforming unorganized data into usable formats ⟨Overview: Key functionality⟩
- Cleaning functions sanitize output, remove unwanted content, and improve NLP model performance ⟨Overview: Key functionality⟩
- Extracting isolates specific entities within documents to identify and isolate relevant pieces of information ⟨Overview: Key functionality⟩
- Chunking is distinct from conventional methods: instead of relying solely on text-based features, Unstructured uses a deep understanding of document formats to partition documents into semantic units (document elements) ⟨Overview: Key functionality⟩
- Staging prepares data for ingestion into downstream systems, and is being deprecated in favor of destination connectors in the Unstructured Ingest CLI / Python library ⟨Overview: Key functionality⟩
- Common use cases are pretraining models, fine-tuning models, retrieval-augmented generation (RAG), and traditional ETL; GPU usage is not supported for the open-source library ⟨Overview⟩
- Both the open source and Pipelines/API offerings transform source documents into Unstructured's canonical JSON schema, with 20+ source and destination connectors and 35+ types of metadata ⟨Overview: Comparison⟩
- Open-source limits include: not designed for production; significantly decreased performance on document and table extraction; no access to the latest VLM offerings or fine-tuned OCR models; no by-page and by-similarity chunking strategies; and less sophisticated document hierarchy detection ⟨Overview: Limits⟩
- The open-source offering has no SOC 2 / HIPAA / GDPR / ISO 27001 / FedRAMP / CMMC compliance and no authentication or identity management ⟨Overview: Limits⟩
- An Unstructured Transform MCP server lets MCP-compatible AI tools/agents send documents to Unstructured for parsing without pipeline setup ⟨Overview⟩
- Page/billing definition: for .pdf/.pptx/.tiff a page is a page/slide/image; for .docx with page metadata it is based on that metadata; for other file types it is file size divided by 100 KB ⟨Overview: Page/billing⟩

## Concepts & entities covered
Concepts: [[document-parsing]] · [[semantic-chunking]] · [[document-element-classification]] · [[document-metadata-extraction]]
Entities: [[org-unstructured]]

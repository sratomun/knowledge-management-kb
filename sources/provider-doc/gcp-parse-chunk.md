---
title: "Google Cloud — Parse and Chunk Documents (Agent Search)"
type: source
kind: provider-doc
authority: vendor
subtype: system
aliases: ["GCP parse and chunk documents"]
publisher: "Google Cloud"
url: https://cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents
version: "current"
published: 2024-01
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# Google Cloud — Parse and Chunk Documents (Agent Search)

## Scope & purpose
This page captures Google Cloud's "Parse and chunk documents" guide at the technique level:
it records the document-parsing options (digital, OCR, layout) and layout-aware chunking
for retrieval-augmented generation (RAG) that the feature embodies, rather than the
product's configuration surface in full. Consistent with the KB's technique-first framing,
no vendor product entity is created and the provider is referenced only in the trailer.
Provider-specific solution depth and cross-provider comparison are deferred to Wave 5.

## Key points
- The guide configures parsing/chunking settings both to specify how Agent Search parses content and to use Agent Search for retrieval-augmented generation (RAG) ⟨Parse & chunk: Purpose⟩.
- It provides three parser techniques — a digital parser, an OCR parser for PDFs, and a layout parser — and also allows bringing your own parsed documents ⟨Parse & chunk: PARSERS⟩.
- The digital parser extracts machine-readable text and detects text blocks but not tables, lists, or headings; it is the default for all file types and the fallback when a specified parser does not support a file type ⟨Parse & chunk: Digital parser⟩.
- The OCR parser handles scanned PDFs and PDFs where text is part of an image; useNativeText=true merges machine-readable text with OCR output, it applies only to PDFs, and it parses the first 500 pages ⟨Parse & chunk: OCR parser for PDFs⟩.
- The layout parser detects text blocks, tables, lists, and structural elements (titles, headings, headers, footnotes) to define a document's organization/hierarchy, can perform OCR on images/scanned documents, and is available only when document chunking for RAG is enabled — layout-aware parsing ⟨Parse & chunk: Layout parser⟩.
- The layout parser is recommended when documents have rich content and structural elements such as sections, paragraphs, tables, images, and lists ⟨Parse & chunk: Purpose⟩.
- For RAG, document chunking breaks documents into chunks so search can return relevant chunks instead of whole documents, increasing relevance for LLM answers and reducing computational load ⟨Parse & chunk: CHUNKING FOR RAG⟩.
- Layout-aware document chunking detects the document's layout and takes it into account during chunking, improving semantic coherence and reducing noise so that all text in a chunk comes from the same layout entity (heading, subheading, list); it requires layout parsing to be on ⟨Parse & chunk: Layout-aware document chunking⟩.
- On retrieval, callers can request adjacent chunks (numPreviousChunks / numNextChunks) for added context; responses include the relevant chunk, adjacent chunks, document metadata, and the span of document pages each chunk was derived from ⟨Parse & chunk: Retrieval⟩.
- The Gemini layout parsing add-on (Public Preview) offers high-quality table recognition, improved reading order, and more accurate text recognition ⟨Parse & chunk: Layout parser — add-ons⟩.

## Concepts & entities covered
Concepts: [[document-parsing]] · [[layout-aware-parsing]] · [[semantic-chunking]] · [[optical-character-recognition]] · [[retrieval-augmented-generation]]
Entities: [[org-google-cloud]]

---
title: "Docling (system)"
type: entity
subtype: system
aliases: []
tags: [doc-processing]
concepts: ["[[document-parsing]]"]
sources: ["[[docling]]"]
updated: 2026-08-10
---

# Docling (system)

## What it is
Docling is an MIT-licensed, self-contained open-source Python toolkit from IBM Research for
converting PDF and other document formats into a machine-processable representation. It runs a
linear pipeline of specialized AI models entirely on commodity hardware and produces a unified
DoclingDocument that can be exported to Markdown or JSON.

## Key facts
- Docling is an easy-to-use, self-contained, MIT-licensed open-source package for PDF document conversion, powered by specialized AI models for layout analysis and table-structure recognition, running efficiently on commodity hardware in a small resource budget ⟨docling: tech report abstract⟩
- Docling parses multiple document formats — including PDF, DOCX, PPTX, XLSX, HTML, EPUB, audio, and images — with advanced PDF understanding of page layout, reading order, table structure, code, formulas, and image classification ⟨docling: README⟩
- Docling implements a linear pipeline executed sequentially on each document: PDF backend parsing, per-page AI models (layout, table structure), then aggregation and post-processing ⟨docling: tech report §3⟩
- Docling provides a unified, expressive DoclingDocument representation and exports to Markdown, HTML, lossless JSON, DocTags, and WebVTT ⟨docling: README⟩
- Docling converts PDF documents to JSON or Markdown, understands detailed page layout and reading order, locates figures, recovers table structures, extracts metadata, and optionally applies OCR for scanned PDFs ⟨docling: tech report §1⟩
- The codebase is under the MIT license and hosted in the LF AI & Data Foundation; the project was started by the AI for knowledge team at IBM Research Zurich ⟨docling: README⟩

## Relations
- Realizes: [[document-parsing]]
- Defined in: [[docling]]
- Published by: [[org-ibm]]
- Related: [[tableformer]], [[doclaynet]]

## See also
[[document-parsing]] · [[tableformer]] · [[doclaynet]]

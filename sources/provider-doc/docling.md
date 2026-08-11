---
title: "Docling — Document Conversion Toolkit (Docs & Tech Report)"
type: source
kind: provider-doc
authority: vendor
subtype: system
aliases: ["Docling docs"]
publisher: IBM Research
url: https://github.com/docling-project/docling
version: "1.0"
published: 2024
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# Docling — Document Conversion Toolkit (Docs & Tech Report)

## Scope & purpose
Docling is an MIT-licensed, self-contained open-source Python package for converting PDF and
other document formats into a machine-processable representation, powered by specialized AI
models for layout analysis and table-structure recognition and designed to run entirely
locally on commodity hardware. This source combines the project's GitHub README with the
Docling Technical Report (arXiv:2408.09869, Deep Search / AI4K team, IBM Research, 2024),
covering the toolkit's capabilities, its linear processing pipeline, and its underlying
models and datasets.

## Structure
The Technical Report describes a **linear pipeline** of operations executed sequentially on
each document ⟨tech report §3⟩:
- **PDF backend** — parses the document to retrieve programmatic text tokens (string content + page coordinates) and to render a bitmap image of each page; the default is a custom qpdf-based parser (docling-parse), with pypdfium as an alternative backup backend ⟨tech report §3.1⟩
- **Layout analysis** — an object-detection model predicts bounding boxes and classes of page elements (paragraphs, section titles, list items, captions, figures, tables) ⟨tech report §3.2⟩
- **Table structure recognition** — TableFormer recovers the logical row/column structure and header/body classification of detected tables ⟨tech report §3.2⟩
- **OCR (optional)** — applied for scanned PDFs or bitmap images, relying initially on EasyOCR ⟨tech report §3.2⟩
- **Assembly / post-processing** — aggregates per-page predictions into a typed document object, augmenting metadata, detecting language, and inferring reading order, then serializes to JSON or Markdown ⟨tech report §3.3⟩

## Key points
- Docling is an easy-to-use, self-contained, MIT-licensed open-source package for PDF document conversion, powered by state-of-the-art specialized AI models for layout analysis (DocLayNet) and table-structure recognition (TableFormer), running efficiently on commodity hardware in a small resource budget ⟨tech report abstract⟩
- Docling parses multiple document formats — including PDF, DOCX, PPTX, XLSX, HTML, EPUB, audio (WAV, MP3), images (PNG, TIFF, JPEG), and more — with advanced PDF understanding covering page layout, reading order, table structure, code, formulas, and image classification ⟨README⟩
- Docling provides a unified, expressive DoclingDocument representation and exports to Markdown, HTML, lossless JSON, DocTags, and WebVTT, among other formats ⟨README⟩
- Docling implements a linear pipeline of operations executed sequentially on each document ⟨tech report §3⟩
- Each document is first parsed by a PDF backend, which retrieves programmatic text tokens (string content plus page coordinates) and renders a bitmap image of each page ⟨tech report §3.1⟩
- The default backend is a custom-built PDF parser based on the low-level qpdf library, open-sourced as docling-parse; an alternative backend relies on pypdfium as a backup for certain font encodings ⟨tech report §3.1⟩
- The layout analysis model is an object detector predicting bounding boxes and classes of page elements, its architecture derived from RT-DETR and re-trained on DocLayNet, with inference via onnxruntime on 72-dpi page images and sub-second latency on a single CPU ⟨tech report §3.2⟩
- Layout bounding-box proposals are post-processed and intersected with the PDF text tokens to group content into paragraphs, section titles, list items, captions, figures, and tables ⟨tech report §3.2⟩
- DocLayNet — the human-annotated layout dataset the model trains on (80,863 manually annotated pages) — reports a **human inter-annotator agreement of ~82–83 mAP@0.5-0.95**, and the report notes that object-detection models "fall approximately 10% behind the inter-annotator agreement," i.e. the human ceiling is itself well below 100% and the best models sit ~10 points under it ⟨tech report, DocLayNet (arXiv 2206.01062)⟩
- TableFormer is a vision-transformer model for table-structure recovery that predicts logical row/column structure and header/body classification, handling partial or absent borderlines, empty cells, spans, hierarchy, and inconsistent indentation; typical tables take 2–6 seconds on a standard CPU via PyTorch ⟨tech report §3.2⟩
- OCR is optional, applied for scanned PDFs or bitmap images; the initial release relies on EasyOCR (many languages), feeds a 216-dpi page image by default, and runs slowly on CPU (upwards of 30 s/page) ⟨tech report §3.2⟩
- The final assembly stage aggregates all per-page predictions into a well-defined datatype (docling-core), and a post-processing model augments features via language detection, reading-order correction, figure–caption matching, and metadata labelling (title, authors, references) ⟨tech report §3.3⟩
- Docling extracts metadata from the document, such as title, authors, references, and language ⟨tech report §1⟩
- The model pipeline is extensible: it can be fully customized by sub-classing BaseModelPipeline or cloning the default, with model classes satisfying a Python Callable interface that accepts an iterator over page objects and produces page objects augmented with predicted features (PagePredictions) ⟨tech report §3.4⟩
- On a 225-page reference set (3 arXiv papers + 2 IBM Redbooks) with OCR disabled, the native backend runs at roughly 1.27–1.34 pages/s on an Apple M3 Max and the pypdfium backend at 2.18–2.45 pages/s; pypdfium is faster and more memory-efficient but worse quality, especially for table-structure recovery ⟨tech report §4⟩
- Applications include enterprise document search, passage retrieval or classification, and knowledge-extraction pipelines; for RAG, the quackling open-source package uses Docling's output for document-native optimized embedding and chunking into LlamaIndex, and Docling is integrated within the IBM data prep kit ⟨tech report §5⟩
- The codebase is under the MIT license and hosted as a project in the LF AI & Data Foundation; the project was started by the AI for knowledge team at IBM Research Zurich ⟨README⟩

## Concepts & entities covered
Concepts: [[document-parsing]] · [[document-layout-analysis]] · [[table-structure-recognition]] · [[optical-character-recognition]] · [[reading-order-reconstruction]] · [[document-metadata-extraction]]
Entities: [[docling-system]] · [[tableformer]] · [[doclaynet]] · [[org-ibm]]

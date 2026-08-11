---
title: "Optical Character Recognition"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[document-parsing]]", "[[intelligent-document-processing]]"]
updated: 2026-08-10
---

# Optical Character Recognition

## What it is
Optical character recognition (OCR) is the recovery of machine-readable text from images of documents — scanned pages, photographs, or bitmap renders — where the characters are not already present as digital text. In document-processing pipelines it is the step that makes scanned or image-only content available to every later stage, and it is frequently combined with, or contrasted against, richer layout and entity understanding.

## How sources treat it
- **[[docling]]** _(provider-doc · vendor)_ — OCR is optional, applied for scanned PDFs or bitmap images; the initial release relies on EasyOCR (many languages), feeds a 216-dpi page image by default, and runs slowly on CPU (upwards of 30 s/page) ⟨tech report §3.2⟩
- **[[aws-textract]]** _(provider-doc · vendor)_ — Described as a machine learning service that goes beyond simple optical character recognition (OCR) to identify, understand, and extract specific data from scanned documents ⟨Textract overview: "Why Amazon Textract"⟩
- **[[aws-idp]]** _(provider-doc · vendor)_ — Names OCR as one of the constituent techniques — alongside computer vision, NLP, and machine learning — that IDP leverages to automate the processing of unstructured data ⟨IDP overview: Definition / technique⟩
- **[[google-document-ai]]** _(provider-doc · vendor)_ — Digitizes documents using OCR to obtain text and layout, with add-ons such as image-quality detection (readability) and deskewing ⟨Document AI overview: "Using Document AI"⟩
- **[[gcp-parse-chunk]]** _(provider-doc · vendor)_ — The OCR parser handles scanned PDFs and PDFs where text is part of an image; useNativeText=true merges machine-readable text with OCR output, it applies only to PDFs, and it parses the first 500 pages ⟨Parse & chunk: OCR parser for PDFs⟩

## Where sources differ
The sources agree that OCR converts document images to text but position it differently. [[docling]] and [[gcp-parse-chunk]] treat OCR as an optional or selectable parser applied only to scanned/image content, with concrete engine and page limits; [[aws-idp]] and [[google-document-ai]] treat it as one building block digitizing input for a larger platform; [[aws-textract]] explicitly positions its service as going "beyond simple OCR." These are complementary emphases — a discrete stage versus a component of a broader capability — not conflicting definitions.

## See also
[[document-parsing]] · [[document-layout-analysis]] · [[intelligent-document-processing]] · [[layout-aware-parsing]]

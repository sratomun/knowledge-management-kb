---
title: "Google Cloud Document AI — Overview"
type: source
kind: provider-doc
authority: vendor
subtype: system
aliases: ["Document AI overview"]
publisher: "Google Cloud"
url: https://cloud.google.com/document-ai/docs/overview
version: "current"
published: 2024-01
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# Google Cloud Document AI — Overview

## Scope & purpose
This page captures Google Cloud's Document AI overview at the technique level: it records
the document-processing capabilities the platform embodies (OCR digitization, layout and
entity extraction, and document classification/splitting) rather than cataloguing the
product's SKUs or pricing. Following the KB's technique-first framing, no vendor product
entity is created; the provider is referenced only in the trailer. Provider-specific
solution depth and cross-provider comparison are deferred to Wave 5.

## Key points
- Document AI is described as a document processing and understanding platform that takes unstructured data from documents and transforms it into structured data — specific fields suitable for a database — embodying intelligent document processing ⟨Document AI overview: intro⟩.
- It is built on top of products within Vertex AI with generative AI, presented as enabling scalable end-to-end cloud-based document processing without specialized ML expertise ⟨Document AI overview: intro⟩.
- The platform digitizes documents using OCR to obtain text and layout, with add-ons such as image-quality detection (readability) and deskewing ⟨Document AI overview: "Using Document AI"⟩.
- It extracts text and layout information from document files, normalizes entities, and identifies key-value pairs in structured forms and regular tables (e.g., "Name: Jill Smith") — document-metadata extraction over form and table content ⟨Document AI overview: "Using Document AI"⟩.
- It classifies document types to drive downstream processes such as extraction and storage, and can split and classify documents by type (e.g., a PDF containing multiple real documents) — document-element classification ⟨Document AI overview: "Using Document AI"⟩.
- A Document AI processor sits between the document file and an ML model that performs the processing/understanding action, and is used to classify, split, parse, or analyze a document ⟨Document AI overview: Processor⟩.
- Processor categories are Digitize (Enterprise Document OCR with image-quality analysis), Extract (Custom extractor, Form Parser for tables/KVP, Layout Parser, and pretrained parsers), and Classify (custom classifier and custom splitter); all processors can extract text and layout information ⟨Document AI overview: Processor categories⟩.
- The Layout Parser extracts text, tables, and lists and returns context-aware chunks, framing extraction output for downstream chunk-based consumption ⟨Document AI overview: Processor categories — Extract⟩.
- Document AI integrates with Cloud Storage, BigQuery, and Agent Search to store, search, organize, govern, and analyze documents and their metadata ⟨Document AI overview: "Using Document AI"⟩.
- For each processed request Document AI returns one or more Document objects containing the extracted, structured information ⟨Document AI overview: Steps to use⟩.

## Concepts & entities covered
Concepts: [[intelligent-document-processing]] · [[optical-character-recognition]] · [[document-element-classification]] · [[document-metadata-extraction]]
Entities: [[org-google-cloud]]

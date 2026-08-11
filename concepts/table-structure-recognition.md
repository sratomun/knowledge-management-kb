---
title: "Table Structure Recognition"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[document-layout-analysis]]", "[[document-parsing]]"]
updated: 2026-08-10
---

# Table Structure Recognition

## What it is
Table structure recognition is the recovery of a table's logical organization — rows, columns, spanning cells, and header-versus-body roles — from a detected table region, so tabular content can be represented as structured data rather than a flat block of text. It typically follows layout analysis (which locates the table) and is a distinct problem from reading the cell text.

## How sources treat it
- **[[docling]]** _(provider-doc · vendor)_ — TableFormer, a vision-transformer model, recovers logical row/column structure and header/body classification, handling partial or absent borderlines, empty cells, spans, hierarchy, and inconsistent indentation; typical tables take 2–6 seconds on a standard CPU via PyTorch ⟨tech report §3.2⟩
- **[[aws-textract]]** _(provider-doc · vendor)_ — Extracts tables and other structured data, framing table-structure recognition as part of the capability that goes beyond simple OCR ⟨Textract overview: "Why Amazon Textract"⟩

## Where sources differ
Both sources treat table structure recognition as a first-class capability distinct from plain text extraction, and the two are complementary. [[docling]] describes a specific named model (TableFormer) with its handling of borderless cells, spans, and hierarchy and reports per-table latency; [[aws-textract]] names table and structured-data extraction as a marketed product capability without exposing the underlying model. Neither is presented as authoritative over the other.

## See also
[[document-layout-analysis]] · [[document-parsing]] · [[optical-character-recognition]]

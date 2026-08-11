---
title: "DocLayNet"
type: entity
subtype: dataset
aliases: []
tags: [doc-processing]
concepts: ["[[document-layout-analysis]]"]
sources: ["[[docling]]"]
updated: 2026-08-10
---

# DocLayNet

## What it is
DocLayNet is a large human-annotated dataset for document-layout analysis. It is the training
data behind Docling's layout-analysis model, which detects and classifies page elements during
document conversion.

## Key facts
- DocLayNet is a large human-annotated dataset for document-layout analysis (KDD '22, arXiv:2206.01062) ⟨docling: tech report, Related key models/datasets⟩
- DocLayNet contains 80,863 manually annotated pages drawn from diverse sources — Financial, Manual, Scientific, Law, Patent, and Tender documents ⟨docling: tech report, Related key models/datasets⟩
- DocLayNet defines 11 distinct class labels: Caption, Footnote, Formula, List-item, Page-footer, Page-header, Picture, Section-header, Table, Text, and Title ⟨docling: tech report, Related key models/datasets⟩
- The dataset is provided in COCO format and includes inter-annotator agreement (mAP@0.5–0.95) ⟨docling: tech report, Related key models/datasets⟩
- Docling's layout-analysis model is an object detector whose architecture is derived from RT-DETR and re-trained on DocLayNet ⟨docling: tech report §3.2⟩
- Docling is powered by state-of-the-art specialized AI models for layout analysis (DocLayNet) and table-structure recognition (TableFormer) ⟨docling: tech report abstract⟩

## Relations
- Realizes: [[document-layout-analysis]]
- Defined in: [[docling]]
- Published by: [[org-ibm]]
- Related: [[docling-system]], [[tableformer]]

## See also
[[document-layout-analysis]] · [[docling-system]]

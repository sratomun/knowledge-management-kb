---
title: "TableFormer"
type: entity
subtype: model
aliases: []
tags: [doc-processing]
concepts: ["[[table-structure-recognition]]"]
sources: ["[[docling]]"]
updated: 2026-08-10
---

# TableFormer

## What it is
TableFormer is a vision-transformer model for table-structure recognition. It is one of the two
specialized AI models that power Docling's document-conversion pipeline, recovering the logical
structure of tables detected during layout analysis.

## Key facts
- TableFormer is a vision-transformer model for table-structure recovery that predicts the logical row/column structure and header/body classification of a table ⟨docling: tech report §3.2⟩
- TableFormer handles challenging tables with partial or absent borderlines, empty cells, spans, hierarchy, and inconsistent indentation ⟨docling: tech report §3.2⟩
- Inference runs via PyTorch, with typical tables taking 2–6 seconds on a standard CPU ⟨docling: tech report §3.2⟩
- Docling is powered by state-of-the-art specialized AI models for layout analysis (DocLayNet) and table-structure recognition (TableFormer) ⟨docling: tech report abstract⟩
- TableFormer's pre-trained weights are published on huggingface and its inference code ships as docling-ibm-models ⟨docling: tech report §3.2⟩
- TableFormer was introduced as table-structure understanding with transformers (CVPR 2022) ⟨docling: tech report, Related key models/datasets⟩

## Relations
- Realizes: [[table-structure-recognition]]
- Defined in: [[docling]]
- Published by: [[org-ibm]]
- Related: [[docling-system]], [[doclaynet]]

## See also
[[table-structure-recognition]] · [[docling-system]]

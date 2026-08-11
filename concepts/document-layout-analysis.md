---
title: "Document Layout Analysis"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[document-parsing]]", "[[reading-order-reconstruction]]", "[[vision-language-document-model]]"]
updated: 2026-08-10
---

# Document Layout Analysis

## What it is
Document layout analysis is the detection of a page's structural regions — paragraphs, titles, lists, captions, figures, tables — usually as bounding boxes with element classes, so a document's geometry is recovered before or alongside text. It supplies the spatial and structural scaffolding on which reading-order reconstruction, table recognition, and layout-aware parsing depend.

## How sources treat it
- **[[docling]]** _(provider-doc · vendor)_ — Uses an object-detection model (derived from RT-DETR, re-trained on DocLayNet) that predicts bounding boxes and classes of page elements — paragraphs, section titles, list items, captions, figures, tables — running via onnxruntime on 72-dpi page images with sub-second CPU latency ⟨tech report §3.2⟩
- **[[layoutlmv3]]** _(article · informational)_ — Frames document layout analysis as detecting layout regions with bounding boxes and categories (text, title, list, table, figure), parsing documents into a machine-readable format for downstream applications, and reaches an overall mAP of 95.1 on PubLayNet as a detector backbone ⟨arXiv:2204.08387, §3.4⟩
- **[[aws-textract]]** _(provider-doc · vendor)_ — Among the elements it extracts are layout elements, framing document-layout analysis as part of the capability that goes beyond simple OCR ⟨Textract overview: "Why Amazon Textract"⟩

## Where sources differ
The sources agree on the object-detection framing (regions as boxes with categories) but differ in role and depth. [[docling]] treats layout analysis as one stage of a fixed conversion pipeline whose proposals are intersected with PDF text tokens; [[layoutlmv3]] treats it as a benchmark task addressed by a pre-trained multimodal backbone inside a Cascade R-CNN detector; [[aws-textract]] names layout-element extraction as a marketed capability without describing the model. These are complementary views — a pipeline stage, a research task, and a product feature — rather than competing claims.

## See also
[[document-parsing]] · [[reading-order-reconstruction]] · [[table-structure-recognition]] · [[vision-language-document-model]] · [[layout-aware-parsing]]

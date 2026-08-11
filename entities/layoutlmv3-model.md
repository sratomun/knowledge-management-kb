---
title: "LayoutLMv3 (model)"
type: entity
subtype: model
aliases: []
tags: [doc-processing]
concepts: ["[[vision-language-document-model]]"]
sources: ["[[layoutlmv3]]"]
updated: 2026-08-10
---

# LayoutLMv3

## What it is
LayoutLMv3 is a multimodal Transformer for Document AI, pre-trained with unified text and image masking objectives plus a word-patch alignment objective. It is a general-purpose model for both text-centric tasks (form/receipt understanding, document visual question answering) and image-centric tasks (document image classification, document layout analysis).

## Key facts
- It is pre-trained with three unified objectives — Masked Language Modeling (MLM), Masked Image Modeling (MIM), and Word-Patch Alignment (WPA) — where WPA predicts whether the image patch corresponding to a text word is masked ⟨[[layoutlmv3]] §2.2⟩.
- It is the first multimodal Document AI model without a CNN or Faster R-CNN backbone, embedding document images as linear projections of image patches to save parameters and eliminate region annotations ⟨[[layoutlmv3]] §1 / §2.1⟩.
- The BASE model has 133M parameters (12 layers) and the LARGE model 368M (24 layers); the encoder is initialized from RoBERTa, the image tokenizer from DiT, and pre-training uses ~11M IIT-CDIP document images ⟨[[layoutlmv3]] §3.1 / §3.2 / Table 1⟩.
- It achieves state-of-the-art results on FUNSD, CORD, DocVQA, RVL-CDIP, and PubLayNet (overall mAP 95.1 for layout analysis) ⟨[[layoutlmv3]] Abstract / Table 1 / Table 2⟩.
- Code and models are publicly released at aka.ms/layoutlmv3 ⟨[[layoutlmv3]] Abstract⟩.

## Relations
- Realizes: [[vision-language-document-model]]
- Defined in: [[layoutlmv3]]
- Developed by: [[org-microsoft]]

## See also
[[vision-language-document-model]] · [[document-layout-analysis]] · [[layoutlmv3]]

---
title: "LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["LayoutLMv3 paper"]
publisher: "Huang, Lv, Cui, Lu, Wei (Sun Yat-sen University; Microsoft Research Asia)"
url: https://arxiv.org/abs/2204.08387
version: "arXiv:2204.08387v3; ACM MM '22"
published: 2022-07
effective_from: 2022-07
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking

## Scope & purpose
LayoutLMv3 is a self-supervised pre-training method that trains multimodal Transformers for Document AI using unified text and image masking objectives. It is designed as a general-purpose pre-trained model that performs both text-centric tasks (form/receipt understanding, document visual question answering) and image-centric tasks (document image classification, document layout analysis). The paper (ACM Multimedia 2022) was authored by Yupan Huang, Tengchao Lv, Lei Cui, Yutong Lu, and Furu Wei, with the work carried out at Microsoft Research Asia; code and models are released at aka.ms/layoutlmv3.

## Structure
The paper is organized around: (1) an introduction motivating unified text/image objectives and the elimination of CNN backbones; (2) the LayoutLMv3 model — architecture (text embedding, image patch embedding, multimodal Transformer) and three pre-training objectives MLM, MIM, and WPA; (3) experiments — model configurations, pre-training on IIT-CDIP, fine-tuning on multimodal benchmarks (FUNSD, CORD, RVL-CDIP, DocVQA), a vision task (PubLayNet layout analysis), and an ablation study; (4) related work; (5) conclusion; and an appendix on LayoutLMv3-Chinese and visual information extraction on EPHOIE.

## Key points
- LayoutLMv3 pre-trains a multimodal Transformer for Document AI with unified text and image masking, learning to reconstruct masked word tokens and masked image patch tokens symmetrically ⟨arXiv:2204.08387, Abstract / §2⟩.
- It is the first multimodal model in Document AI that does not rely on a pre-trained CNN or Faster R-CNN backbone; it represents document images with linear projections of image patches (inspired by ViT and ViLT), significantly saving parameters and eliminating region annotations ⟨arXiv:2204.08387, §1 / §2.1 Image Embedding⟩.
- Objective I — Masked Language Modeling (MLM): 30% of text tokens are masked with a span-masking strategy (span lengths from a Poisson distribution, λ=3), keeping layout information unchanged so the model links layout, text, and image context ⟨arXiv:2204.08387, §2.2 Objective I⟩.
- Objective II — Masked Image Modeling (MIM): about 40% of image tokens are masked blockwise and reconstructed; labels come from an image tokenizer (discrete VAE, visual vocabulary of 8,192), so MIM captures high-level layout structure rather than noisy low-level pixel detail ⟨arXiv:2204.08387, §2.2 Objective II⟩.
- Objective III — Word-Patch Alignment (WPA): a two-layer MLP head predicts, for each unmasked text token, whether its corresponding image patch is masked (aligned/unaligned), learning fine-grained cross-modal alignment; the full objective is L = L_MLM + L_MIM + L_WPA ⟨arXiv:2204.08387, §2.2 Objective III⟩.
- LayoutLMv3 adopts segment-level 2D layout positions (words in a segment share the same bounding-box position) instead of the word-level positions used by LayoutLM/LayoutLMv2 ⟨arXiv:2204.08387, §2.1 Text Embedding⟩.
- The BASE model uses a 12-layer / 12-head Transformer (133M parameters) and LARGE a 24-layer / 16-head Transformer (368M); the multimodal encoder is initialized from RoBERTa and the image tokenizer from DiT ⟨arXiv:2204.08387, §3.1 / §3.2 / Table 1⟩.
- Pre-training uses about 11 million document images from the IIT-CDIP Test Collection 1.0 ⟨arXiv:2204.08387, §3.2⟩.
- LayoutLMv3 achieves state-of-the-art results on text-centric benchmarks — FUNSD form understanding (F1 92.08, LARGE), CORD receipt understanding, and DocVQA — and on image-centric benchmarks RVL-CDIP document image classification and PubLayNet document layout analysis ⟨arXiv:2204.08387, Abstract / Table 1 / Table 2⟩.
- For document layout analysis, LayoutLMv3 is used as a feature backbone inside a Cascade R-CNN detector with FPN (Detectron2), modeling the task as object detection without text embedding, and reaches an overall mAP of 95.1 on PubLayNet ⟨arXiv:2204.08387, §3.4 / Table 2⟩.
- Document layout analysis is framed as detecting layout regions with bounding boxes and categories (text, title, list, table, figure), parsing documents into a machine-readable format for downstream applications ⟨arXiv:2204.08387, §3.4⟩.
- Ablation shows MIM is critical for vision tasks — without it the PubLayNet fine-tuning loss diverges — while the WPA objective consistently improves all evaluated tasks ⟨arXiv:2204.08387, §3.5 / Table 3⟩.
- A LayoutLMv3-Chinese model (BASE), pre-trained on 50 million Chinese document pages and initialized from XLM-R, reaches a state-of-the-art mean F1 of 99.21 on the EPHOIE visual information extraction dataset ⟨arXiv:2204.08387, Appendix A.1 / Table 4⟩.

## Concepts & entities covered
Concepts: [[vision-language-document-model]] · [[document-layout-analysis]] · [[document-element-classification]]
Entities: [[layoutlmv3-model]] · [[org-microsoft]]

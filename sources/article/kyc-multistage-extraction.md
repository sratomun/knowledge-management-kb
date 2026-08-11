---
title: "A Multistage Extraction Pipeline for Long Scanned Financial Documents: An Empirical Study in Industrial KYC Workflows"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["KYC multistage extraction"]
publisher: "Han, Zhang, Wang, Jin, Ke, Zhao (OCBC, Singapore)"
url: https://arxiv.org/abs/2604.26462
version: "arXiv:2604.26462v1 [cs.CV]"
published: 2026
effective_from: 2026-04
effective_to: ongoing
status: current
tags: [knowledge-processing]
updated: 2026-08-10
---

# A Multistage Extraction Pipeline for Long Scanned Financial Documents: An Empirical Study in Industrial KYC Workflows

## Scope & purpose
This paper presents a multistage extraction framework for structured information extraction from long, multilingual, non-machine-readable scanned financial documents in industrial Know-Your-Customer (KYC) and compliance workflows. The design separates page localization from multimodal reasoning: image preprocessing, multilingual OCR, hybrid page-level retrieval, and compact vision-language-model (VLM) structured extraction, followed by mandatory human review. The authors (an OCBC team, Singapore) evaluate it on 120 production KYC documents (~3000 pages) and report that it consistently outperforms direct PDF-to-VLM baselines.

## Structure
The paper is organized as: (1) an introduction motivating extraction for KYC onboarding, AML, and regulatory compliance and the impracticality of end-to-end VLM application; (3) methodology — the five-stage pipeline (preprocessing, OCR, page-level retrieval, compact-VLM extraction, human-in-the-loop review); (4) results on a production dataset with a module ablation and document-type analysis; (5) error analysis and limitations; and (6) conclusion.

## Key points
- The framework integrates image preprocessing, multilingual OCR, hybrid page-level retrieval, and compact VLM-based structured extraction, deliberately separating page localization from multimodal reasoning to reserve expensive VLM inference for relevant pages only ⟨arXiv:2604.26462, Abstract / §3⟩.
- Image preprocessing comprises segmentation (OpenCV edge detection / contour finding to remove blank areas and borders), two-stage skew and rotation correction (PaddleOCR document-orientation classifier for coarse rotation, then Hough transform for fine skew), and re-normalization (bicubic rescaling, CLAHE local contrast, light Gaussian denoising) ⟨arXiv:2604.26462, §3⟩.
- OCR uses multilingual engines (PaddleOCRv3, EasyOCR) for both printed and handwritten text ⟨arXiv:2604.26462, §3⟩.
- Page-level retrieval builds a predefined query per target field combining domain-specific financial terms, document-type location cues, and language-specific keywords, then applies hybrid retrieval — BM25 lexical matching (robust to noisy OCR) plus sentence-embedding semantic similarity — reducing the pages forwarded to the VLM by about 70% ⟨arXiv:2604.26462, §3⟩.
- Compact VLM extraction runs on the filtered high-relevance pages using a structured prompt with domain keywords, document-type cues, and output-format instructions, and emits a "remarks" field for ambiguity comments ⟨arXiv:2604.26462, §3⟩.
- In KYC, all extracted fields are subject to mandatory manual review, which the authors describe as a regulatory requirement rather than an added cost; reported accuracy reflects raw system outputs before manual intervention, and correction patterns iteratively refine field-specific prompts and retrieval queries ⟨arXiv:2604.26462, §3⟩.
- The authors report that the multistage pipeline consistently outperforms direct PDF-to-VLM baselines, improving field-level accuracy by up to 31.9 percentage points (a lift of 20.7–31.9 pp, over 50% relative gain) without increased latency ⟨arXiv:2604.26462, Abstract / §4⟩.
- The authors report the best configuration (PaddleOCR + MiniCPM-o-2.6) achieves 87.27% field-level accuracy and 92.81% on non-English content, and note MiniCPM-o-2.6 outperforming the larger Gemma-3-27B, which they attribute to its document-centric architecture (adaptive high-resolution encoding, high-density OCR tokenization) ⟨arXiv:2604.26462, §4⟩.
- The module ablation reports page-level retrieval as the most critical component (removal drops accuracy 16.8–24.0 pp), image preprocessing second (6.2–16.3 pp), and structured prompting modest overall but valuable for corner cases ⟨arXiv:2604.26462, §4⟩.
- The authors report the pipeline's gain is much larger for long financial statements (>40 pp) than for short standardized payslips (~8 pp), where structured prompting is the biggest contributor while retrieval and preprocessing matter little ⟨arXiv:2604.26462, §4⟩.
- Reported error sources and limitations include inconsistent financial terminology (revenue/income/sales) causing retrieval mismatch, OCR errors on low-quality scans and handwriting, currency-unit ambiguity in multilingual settings (IDR'000, ribuan, juta), per-field manual prompt/query specification limiting generalization, and prompt–model alignment bias toward PaddleOCR+MiniCPM ⟨arXiv:2604.26462, §5⟩.

## Concepts & entities covered
Concepts: [[extraction-verification]] · [[precise-retrieval]] · [[optical-character-recognition]] · [[human-in-the-loop-verification]] · [[intelligent-document-processing]]
Entities: [[kyc-multistage-pipeline]]

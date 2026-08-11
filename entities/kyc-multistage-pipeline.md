---
title: "KYC multistage extraction pipeline (OCBC)"
type: entity
subtype: technique
aliases: []
tags: [knowledge-processing]
concepts: ["[[extraction-verification]]", "[[precise-retrieval]]"]
sources: ["[[kyc-multistage-extraction]]"]
updated: 2026-08-10
---

# KYC multistage extraction pipeline (OCBC)

## What it is
The KYC multistage extraction pipeline is a five-stage framework, described by an OCBC team, for extracting structured fields from long, multilingual, non-machine-readable scanned financial documents in KYC and compliance workflows. It chains image preprocessing, multilingual OCR, hybrid page-level retrieval, compact vision-language-model (VLM) extraction, and mandatory human review, deliberately separating page localization from multimodal reasoning.

## Key facts
- The pipeline runs five stages: image preprocessing, multilingual OCR, hybrid page-level retrieval, compact-VLM structured extraction, and mandatory human-in-the-loop review ⟨[[kyc-multistage-extraction]] §3⟩.
- Page-level retrieval combines a per-field query (domain terms, document-type location cues, language-specific keywords) with hybrid BM25-plus-embedding matching, reducing the pages forwarded to the VLM by about 70% ⟨[[kyc-multistage-extraction]] §3⟩.
- All extracted fields undergo mandatory manual review, described as a regulatory requirement rather than an added cost; reported accuracy reflects raw outputs before that review ⟨[[kyc-multistage-extraction]] §3⟩.
- The authors report the pipeline improves field-level accuracy by up to 31.9 percentage points over direct PDF-to-VLM baselines without increased latency, with a best configuration (PaddleOCR + MiniCPM-o-2.6) of 87.27% ⟨[[kyc-multistage-extraction]] Abstract / §4⟩.
- The authors' module ablation reports page-level retrieval as the most critical component (removal drops accuracy 16.8–24.0 pp), ahead of image preprocessing (6.2–16.3 pp) and structured prompting ⟨[[kyc-multistage-extraction]] §4⟩.

## Relations
- Realizes: [[extraction-verification]] · [[precise-retrieval]]
- Defined in: [[kyc-multistage-extraction]]

## See also
[[extraction-verification]] · [[precise-retrieval]] · [[optical-character-recognition]] · [[human-in-the-loop-verification]] · [[kyc-multistage-extraction]]

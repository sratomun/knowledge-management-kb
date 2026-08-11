---
title: "IDP Accelerator: Agentic Document Intelligence from Extraction to Compliance Validation"
type: source
kind: article
authority: informational
subtype: system
aliases: ["IDP Accelerator"]
publisher: "Md Mofijul Islam et al. (Amazon Web Services)"
url: https://arxiv.org/abs/2602.23481
version: "arXiv:2602.23481v2 [cs.CL]"
published: 2026
effective_from: 2026-03
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-11
---

# IDP Accelerator: Agentic Document Intelligence from Extraction to Compliance Validation

## Scope & purpose
IDP (Intelligent Document Processing) Accelerator is an AWS-affiliated, open-source framework (github.com/aws-samples/sample-genai-idp) for agentic, end-to-end document intelligence spanning classification, extraction, analytics, and compliance validation. It is captured here technique-first, with provider specifics kept light. The framework has four components: DocSplit (a benchmark dataset plus multimodal classifier using BIO tagging to segment complex document packets), a configurable Extraction Module (multimodal LLMs to structured data), an MCP-compliant Agentic Analytics Module, and a Rule Validation Module that replaces deterministic engines with LLM-driven compliance logic.

## Structure
The paper motivates agentic IDP against traditional pipelines, describes the four components and a multi-layered confidence/human-review design, evaluates extraction on the RealKIE-FCC dataset with a reliability/failure-mode analysis, reports production deployment numbers, and closes with risks.

## Key points
- The framework is AWS-affiliated and open-source, enabling agentic end-to-end document intelligence across four components, motivated by the claim that unstructured data is ~80–90% of global data and that manual, rule-based, and raw-OCR approaches are inadequate ⟨arXiv:2602.23481, Abstract / Key technique points⟩.
- Multimodal document understanding processes documents as images through multimodal LLMs to capture spatial relationships and formatting, generating structured JSON conforming to user-defined schemas, with each field localized by bounding-box coordinates and few-shot learning without fine-tuning ⟨arXiv:2602.23481, Key technique points⟩.
- Confidence estimation is multi-layered: OCR per-line confidence (0–100%) plus a post-extraction LLM analysis of each attribute against OCR text and imagery producing granular confidence (0.0–1.0) with justifications and bounding boxes; when attribute-level confidence falls below a configurable threshold (default 0.8) it triggers human-in-the-loop review ⟨arXiv:2602.23481, Key technique points⟩.
- Rule validation operates in two steps — curate facts for each rule from individual document sections, then consolidate section-level findings and evaluate whether facts satisfy the rule conditions — and the authors state "this separation of fact extraction from rule evaluation improves precision and enables comprehensive analysis across very large documents" ⟨arXiv:2602.23481, Key technique points⟩.
- On RealKIE-FCC-Verified (75 FCC invoice documents), the authors report the best extraction score of 0.7991 for Claude Sonnet 4.5 (OCR+Image), ahead of Qwen3-VL (0.7805) and Opus 4.5 (0.7804) ⟨arXiv:2602.23481, Experimental evaluation⟩.
- The authors report that OCR-based input consistently outperforms image-only input across all models, with the gap most pronounced for smaller models (e.g. Gemma-3 0.7636 OCR vs 0.5359 image-only), while combining OCR+image yields only marginal gains over OCR-only ⟨arXiv:2602.23481, Experimental evaluation⟩.
- As a reliability/failure mode, open-source models (Qwen3-VL, Gemma-3) are competitive at much lower cost ($2.08, $1.64 vs Sonnet $7.18) but show high failure rates on image-only input (Gemma-3 failed 5/75, latency >200 min) "primarily attributed to invalid output structure, where model responses did not conform to the required JSON schema," which the authors say "underscore the importance of structured output enforcement" ⟨arXiv:2602.23481, Experimental evaluation⟩.
- The authors report a healthcare production deployment improving classification accuracy from 94% (legacy Amazon Comprehend baseline) to 98% with IDP plus Amazon Nova, alongside 77% lower operational cost and 80% reduced processing latency (about 300 hours/month saved) ⟨arXiv:2602.23481, Abstract / Real-world⟩.
- Stated risks include automation bias, the caution that "outputs should not be treated as ground truth without appropriate verification, particularly in high-stakes domains," and that IDP systems "transform rather than eliminate human roles," shifting effort from manual data entry to quality analysis and exception handling ⟨arXiv:2602.23481, Risks⟩.

## Concepts & entities covered
Concepts: [[agentic-extraction]] · [[schema-guided-extraction]] · [[extraction-self-verification]] · [[structured-output-generation]]
Entities: [[idp-accelerator-framework]]

---
title: "IDP Accelerator framework"
type: entity
subtype: system
aliases: []
tags: [doc-processing]
concepts: ["[[agentic-extraction]]", "[[schema-guided-extraction]]", "[[extraction-self-verification]]", "[[structured-output-generation]]"]
sources: ["[[idp-accelerator]]"]
updated: 2026-08-11
---

# IDP Accelerator framework

## What it is
IDP Accelerator is an AWS-affiliated, open-source framework for agentic, end-to-end intelligent document processing, spanning document classification, extraction, analytics, and compliance validation. It has four components: DocSplit (a benchmark dataset plus a multimodal BIO-tagging classifier for segmenting document packets), a configurable multimodal-LLM Extraction Module, an MCP-compliant Agentic Analytics Module, and a Rule Validation Module that replaces deterministic engines with LLM-driven compliance logic.

## Key facts
- The Extraction Module uses multimodal LLMs to process documents as images and emit structured JSON conforming to user-defined schemas, localizing each field with bounding-box coordinates via few-shot learning without fine-tuning ⟨[[idp-accelerator]] Key technique points⟩.
- Confidence is multi-layered — OCR per-line (0–100%) plus a post-extraction LLM per-attribute score (0.0–1.0) with justifications — and attribute confidence below a configurable threshold (default 0.8) routes the extraction to human-in-the-loop review ⟨[[idp-accelerator]] Key technique points⟩.
- The Rule Validation Module separates fact extraction from rule evaluation in two steps (curate facts per rule from sections, then evaluate whether facts satisfy the rule conditions), which the authors state "improves precision and enables comprehensive analysis across very large documents" ⟨[[idp-accelerator]] Key technique points⟩.
- On RealKIE-FCC-Verified (75 FCC invoices), the authors report a best extraction score of 0.7991 (Claude Sonnet 4.5, OCR+Image) and that OCR-based input consistently outperforms image-only input across all models ⟨[[idp-accelerator]] Experimental evaluation⟩.
- The authors report that lower-cost open models can fail at high rates on image-only input due to "invalid output structure … [not conforming] to the required JSON schema," which they say "underscore the importance of structured output enforcement" ⟨[[idp-accelerator]] Experimental evaluation⟩.
- The authors report a healthcare deployment reaching 98% classification accuracy (from a 94% legacy baseline) with 77% lower operational cost and 80% reduced latency ⟨[[idp-accelerator]] Abstract / Real-world⟩.

## Relations
- Realizes: [[agentic-extraction]] · [[schema-guided-extraction]] · [[extraction-self-verification]] · [[structured-output-generation]]
- Defined in: [[idp-accelerator]]

## See also
[[agentic-extraction]] · [[schema-guided-extraction]] · [[extraction-self-verification]] · [[structured-output-generation]] · [[idp-accelerator]]

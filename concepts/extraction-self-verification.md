---
title: "Extraction Self-Verification"
type: concept
subtype: ai-technique
aliases: []
tags: [doc-processing]
related: ["[[extraction-verification]]", "[[human-in-the-loop-verification]]", "[[agentic-extraction]]"]
updated: 2026-08-11
---

# Extraction Self-Verification

## What it is
Extraction self-verification is the mechanism by which an extraction system checks its own outputs before returning them — re-deriving answers, cross-checking values against source evidence, scoring confidence, and routing low-confidence items to repair or human review. It distinguishes an extraction that merely produces output from one that estimates whether that output is trustworthy. Sources implement it as multi-stage answer verification, per-attribute confidence estimation with thresholds, and grounding checks over an evidence store, and several tie it to escalation when confidence is low.

## How sources treat it
- **[[st-raptor]]** _(article · informational)_ — Uses two-stage verification to reduce hallucination: FORWARD verification checks the logic and execution trace of sub-operations, and BACKWARD verification rephrases the question and ensures answer consistency ⟨Core approach⟩
- **[[idp-accelerator]]** _(article · informational)_ — Multi-layered confidence combines OCR per-line confidence (0–100%) with a post-extraction LLM analysis of each attribute against OCR text and imagery producing granular confidence (0.0–1.0) with justifications and bounding boxes; when attribute-level confidence falls below a configurable threshold (default 0.8) it triggers human-in-the-loop review ⟨Key technique points⟩
- **[[idp-accelerator]]** _(article · informational)_ — Warns that "outputs should not be treated as ground truth without appropriate verification, particularly in high-stakes domains," framing verification as a guard against automation bias rather than a full replacement of human roles ⟨Risks⟩
- **[[ledgermind]]** _(article · informational)_ — Enforces verification structurally: grounding is checked at the entity level (ECC) and numeric level (NCC) against active ledger entries, and repair is limited to seven typed operators guaranteeing non-amplification, citing that LLMs largely cannot self-correct without external feedback; reports removing this ledger costs −15.39 overall on MMMU-Pro ⟨§3.1 / §3.2; Table 3⟩

## Where sources differ
The sources verify against different references. [[st-raptor]] verifies internally — re-checking its own execution trace and answer consistency by rephrasing — with no external evidence anchor. [[idp-accelerator]] verifies each extracted attribute against OCR text and imagery, emitting a numeric confidence and escalating to humans below a threshold, so verification feeds [[human-in-the-loop-verification]] rather than closing the loop autonomously. [[ledgermind]] makes verification a hard structural invariant over a provenance ledger, and both it and [[idp-accelerator]] (via the Huang et al. line of work) invoke the finding that unaided LLM self-correction is unreliable — [[ledgermind]] responding with external tool-grounded checks and [[idp-accelerator]] with human review. The KB records these as complementary designs, not a ranking.

## See also
[[extraction-verification]] · [[human-in-the-loop-verification]] · [[agentic-extraction]] · [[provenance-constrained-extraction]] · [[evidence-grounded-generation]]

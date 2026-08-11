---
title: "Human-in-the-loop verification"
type: concept
aliases: []
tags: [knowledge-processing]
related: ["[[extraction-verification]]"]
updated: 2026-08-10
---

# Human-in-the-loop verification

## What it is
Human-in-the-loop verification is the practice of routing an automated system's outputs through human review before they are accepted, especially where errors are costly or where regulation requires human accountability. It can be unconditional (every output reviewed) or confidence-gated (high-confidence outputs auto-accepted, low-confidence ones escalated), and the review signal can feed back to improve the system. In extraction and compliance settings it is often framed not as an add-on cost but as a mandated control, with reported system accuracy describing raw outputs before human correction.

## How sources treat it
- **[[kyc-multistage-extraction]]** _(article · informational)_ — makes all extracted fields subject to mandatory manual review, which the authors describe as a regulatory requirement rather than an added cost, and notes that reported accuracy reflects raw system outputs before manual intervention ⟨arXiv:2604.26462, §3⟩
- **[[kyc-multistage-extraction]]** _(article · informational)_ — describes correction patterns from review iteratively refining field-specific prompts and retrieval queries, so human feedback improves the pipeline over time ⟨arXiv:2604.26462, §3⟩

## Where sources differ
The KYC source treats human-in-the-loop verification as *unconditional* — every field is reviewed because KYC regulation demands it — and as a source of iterative improvement. Other sources in this domain describe *confidence-gated* variants of the same idea: [[euro-5k-obligation-extraction]] proposes provisionally accepting high-confidence predictions and referring lower-confidence cases for expert review ⟨§6.4⟩, and [[compliancenlp-gap-detection]] mandates analyst review only for findings whose source obligation involves ≥3 cross-references ⟨§6.1⟩. The divergence is descriptive — unconditional versus selective triggering of human review — and each design is attributed to its own source; the KB does not prescribe a policy.

## See also
[[extraction-verification]]

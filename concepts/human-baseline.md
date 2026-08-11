---
title: "Human baseline"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[inter-annotator-agreement]]", "[[expert-gold-standard]]"]
updated: 2026-08-10
---

# Human baseline

## What it is
A human baseline is a reference level of performance established by people — domain experts, trained annotators, or the agreement among them — against which an automated system's outputs are measured. It can take the form of a top-tier reference answer, a consensus label set, or a ceiling against which models are compared, and it is used to give model scores meaning relative to the professional standard the task actually demands. In this domain the baseline is itself contested: some sources treat human output as the standard to approximate, while others question whether human consensus is a valid ground truth at all.

## How sources treat it
- **[[euroexec]]** _(article · informational)_ — blindly-judged expert-written reference answers reach a near-ceiling 92.4% Solve Rate against the strongest model's 56.9%, and the human reference is preferred over every model response in 74.24% of direct rankings; the authors describe the experts as comfortably meeting the professional standard ⟨Table 4; §5⟩
- **[[euroexec]]** _(article · informational)_ — on a 33-question subset the question authors wrote an ideal answer that was blind-evaluated as a seventh "model," preserving the overall ranking and being preferred over all LLMs ⟨§4; Table 10⟩
- **[[cuad]]** _(article · informational)_ — establishes an expert-lawyer human baseline for contract review: dozens of legal experts plus law-student annotators trained 70–100 hours, each annotation verified by three additional annotators, a labeling effort the authors value conservatively at over $2 million ⟨§1; §3⟩
- **[[agreement-is-not-quality]]** _(article · informational)_ — challenges the presumption that human coding is the reference standard, reporting that a blind expert verifier preferred human coding in only 51.5% of decisive Human-vs-LLM pairs (binomial p = 0.537), i.e. no overall preference for the human baseline despite a large agreement gap ⟨RQ3; Discussion⟩
- **[[docling]]** _(provider-doc · vendor)_ — DocLayNet's human inter-annotator agreement is ~82–83 mAP@0.5-0.95 — a measured, sub-100% human ceiling that object-detection models fall ~10 points below ⟨tech report, DocLayNet (arXiv 2206.01062)⟩

## Where sources differ
The sources diverge on whether the human baseline is a stable ground truth. [[euroexec]] and [[cuad]] treat expert human work as the standard to be approximated and quantify how far models fall below it, while [[agreement-is-not-quality]] argues symmetrically that when two sources disagree and no ground truth exists, deviation from a human cannot distinguish a worse system from a different one. [[docling]] quantifies a human ceiling (~82–83 mAP) and the ~10-point gap models sit below it. The KB records these as differing framings of the same reference, not a ruling on which is correct.

## See also
[[inter-annotator-agreement]]
[[expert-gold-standard]]
[[human-parity]]

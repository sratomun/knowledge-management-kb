---
title: "Inter-annotator agreement"
type: concept
aliases: []
tags: [benchmarking]
related: ["[[human-baseline]]"]
updated: 2026-08-10
---

# Inter-annotator agreement

## What it is
Inter-annotator agreement (IAA) measures how consistently independent human annotators assign the same labels or judgments to the same items, typically via statistics such as Jaccard overlap, Cohen's or Fleiss' kappa, or an intraclass correlation. It is used as a reliability signal — high agreement is traditionally read as evidence that a task is well-defined and that human labels can serve as trustworthy ground truth, and it also bounds the ceiling that automated systems are expected to reach. A recurring theme in this domain is whether agreement, on its own, actually indicates quality.

## How sources treat it
- **[[agreement-is-not-quality]]** _(article · informational)_ — reports mean human-human Jaccard of ~0.52 against human-LLM 0.30, while LLM-LLM agreement (0.37–0.68) is comparable to human-human and intra-model re-run kappa (0.871–0.995) exceeds the human-human baseline, which the authors read as models sharing interpretive tendencies rather than producing noise ⟨RQ1⟩
- **[[agreement-is-not-quality]]** _(article · informational)_ — its central claim is that agreement is not quality: for several codes high human-human agreement encoded shared bias the verifier rejected (e.g. ELA Skills Development, human-human agreement 0.48, endorsed 61% when an LLM applied it but only 30% when a human did) ⟨Findings Pattern 2⟩
- **[[agreement-is-not-quality]]** _(article · informational)_ — cites prior work that models can produce consistent-but-biased outputs that standard metrics score as reliable, framing this as reliability without validity ⟨Related Work⟩
- **[[profbench]]** _(article · informational)_ — reports inter-annotator agreement of Fleiss' κ = 0.912 on a 1,127-pair re-annotation, described as excellent agreement and adopted as the human gold standard against which LLM-Judges are measured ⟨§4.1⟩
- **[[docling]]** _(provider-doc · vendor)_ — reports DocLayNet's human inter-annotator agreement at ~82–83 mAP@0.5-0.95 (a sub-100% human ceiling) and notes object-detection models "fall approximately 10% behind the inter-annotator agreement" ⟨tech report, DocLayNet (arXiv 2206.01062)⟩

## Where sources differ
[[profbench]] uses a high IAA figure (κ = 0.912) as positive evidence that its human labels are a reliable gold standard, whereas [[agreement-is-not-quality]] argues the opposite direction — that agreement, even when high, does not establish that the agreed answer is correct and can instead reflect shared bias. [[docling]] presupposes a human-agreed layout ground truth without measuring agreement. The KB surfaces both the "agreement as reliability" and "agreement is not quality" positions and leaves them standing.

## See also
[[human-baseline]]
[[expert-gold-standard]]

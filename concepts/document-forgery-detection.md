---
title: "Document forgery detection"
type: concept
aliases: []
tags: [knowledge-processing]
related: ["[[extraction-verification]]"]
updated: 2026-08-10
---

# Document forgery detection

## What it is
Document forgery detection is the practice of deciding whether a document — commonly an identity document — has been tampered with, and often localizing where the manipulation occurred. It is a verification step upstream of trusting any information extracted from the document, motivated by the threat forged documents pose to remote onboarding and Know-Your-Customer systems. Techniques combine image-forensics signals (device/camera fingerprints, noise residuals) with learned classifiers, and must contend with limited training data because genuine ID data is sensitive and personally identifiable.

## How sources treat it
- **[[edgedoc-id-forgery]]** _(article · informational)_ — performs simultaneous classification and forgery localization for ID documents, combining the TruFor framework with a custom lightweight EdgeNeXt-based hybrid CNN-transformer architecture, motivated by the threat forged documents pose to KYC and remote onboarding ⟨arXiv:2508.16284, Abstract / §2⟩
- **[[edgedoc-id-forgery]]** _(article · informational)_ — leverages a NoisePrint camera-model fingerprint (suppressing scene content to enhance camera-specific patterns) fused with the image as localized anomaly cues, and is designed to work with limited training samples given the sensitive nature of ID data ⟨arXiv:2508.16284, §2 / §2.1⟩
- **[[edgedoc-id-forgery]]** _(article · informational)_ — reports scoring 1.00 on accuracy, F1, ROC AUC, and MCC on the FantasyID public validation set (stated as superior to baselines such as TruFor and MMFusion) and third place in the ICCV 2025 DeepID Challenge, where fusion of EdgeDoc and TruFor is reported to improve generalization to unseen manipulations ⟨arXiv:2508.16284, §3⟩

## Where sources differ
Only one source treats document forgery detection directly, so the KB records no cross-source divergence. Its comparative claims — EdgeDoc scoring above TruFor and MMFusion on FantasyID, and fusion improving leaderboard aggregate F1 in the DeepID Challenge — are reported as the authors' own benchmark and competition results, not as KB conclusions. The authors note that larger, more diverse training data is expected to further improve performance.

## See also
[[extraction-verification]]

---
title: "EdgeDoc: Hybrid CNN-Transformer Model for Accurate Forgery Detection and Localization in ID Documents"
type: source
kind: article
authority: informational
subtype: technique
aliases: ["EdgeDoc paper"]
publisher: "George, Marcel (Idiap Research Institute, Switzerland)"
url: https://arxiv.org/abs/2508.16284
version: "arXiv:2508.16284v1 [cs.CV]"
published: 2025
effective_from: 2025-08
effective_to: ongoing
status: current
tags: [knowledge-processing]
updated: 2026-08-10
---

# EdgeDoc: Hybrid CNN-Transformer Model for Accurate Forgery Detection and Localization in ID Documents

## Scope & purpose
EdgeDoc is an approach for both detection and localization of forgeries in identity documents, motivated by the threat forged documents pose to Know-Your-Customer (KYC) and remote onboarding systems. Its architecture combines a lightweight convolutional transformer with auxiliary NoisePrint features to detect subtle manipulations, and it is designed to work with limited training samples given the sensitive, personally-identifiable nature of ID data. The authors (Idiap Research Institute) evaluate it on the FantasyID dataset and report a third-place finish in the ICCV 2025 DeepID Challenge.

## Structure
The paper is organized as: (1) an introduction on digital-KYC security risks, forgery-detection challenges (model generalization across regional ID designs, varied attack types, small tampered regions, constrained datasets); (2) method — NoisePrint/TruFor device-fingerprint fusion, the EdgeNeXt-based hybrid architecture, and training losses; (3) experiments on FantasyID and the ICCV 2025 DeepID Challenge; and (4) conclusion.

## Key points
- EdgeDoc performs simultaneous classification and forgery localization for ID documents, combining the TruFor framework with a custom lightweight architecture inspired by EdgeFace ⟨arXiv:2508.16284, Abstract / §2⟩.
- It leverages a NoisePrint representation (a camera-model fingerprint from Cozzolino & Verdoliva that suppresses scene content and enhances camera-specific patterns) as localized anomaly cues, fused with the original image for patch-wise interaction in a convolutional-transformer architecture ⟨arXiv:2508.16284, §2 / §2.1⟩.
- The architecture is based on the XXS variant of the EdgeNeXt backbone, feeding multi-scale feature maps into a U-Net-style decoder; classification uses a global-average-pooling bottleneck head and the segmentation mask is produced by a pointwise (1x1) convolution ⟨arXiv:2508.16284, §2.2 / §2.3⟩.
- The model input is two channels — the green channel of the ID image plus the NoisePrint feature map ⟨arXiv:2508.16284, §2.3⟩.
- Training uses BCE loss for classification and a composite BCE+Dice loss for localization (mask-loss weight lambda=3.0, total L_cls + lambda*L_mask), with AdamW, weight decay 5e-4, batch size 1, initial lr 3e-4 with cosine annealing over 20 epochs, selecting the lowest-validation-loss model ⟨arXiv:2508.16284, §2.4⟩.
- Evaluation uses FantasyID, a dataset for document forgery and presentation-attack detection in biometric KYC, comprising 786 genuine images (from 262 synthetically generated fantasy ID cards printed on plastic and captured with three devices) plus attack samples with digital and printed manipulations ⟨arXiv:2508.16284, §3⟩.
- On the public validation set of FantasyID the authors report EdgeDoc scoring 1.00 on accuracy, F1, ROC AUC, and MCC, which they state is superior to all baselines (e.g., TruFor 0.71 accuracy / 0.78 AUC; MMFusion 0.69 / 0.83), with a Fusion(EdgeDoc, TruFor) reaching 0.95 accuracy / 0.99 AUC ⟨arXiv:2508.16284, §3⟩.
- In the ICCV 2025 DeepID Challenge (the first competition focused on detecting synthetic manipulations / injection attacks in ID documents), inference used a fusion of EdgeDoc and TruFor; the authors report leaderboard aggregate F1 of 0.59 (EdgeDoc), 0.71 (TruFor), and 0.79 (Fusion), stating fusion significantly improves generalization to unseen manipulations, and EdgeDoc secured third place in the detection track ⟨arXiv:2508.16284, §3⟩.
- The authors state that larger, more diverse training data is expected to further improve performance; the work was funded by the Swiss Center for Biometrics Research and Testing ⟨arXiv:2508.16284, §4⟩.

## Concepts & entities covered
Concepts: [[document-forgery-detection]] · [[extraction-verification]]
Entities: [[edgedoc]]

---
title: "EdgeDoc"
type: entity
subtype: model
aliases: []
tags: [knowledge-processing]
concepts: ["[[document-forgery-detection]]"]
sources: ["[[edgedoc-id-forgery]]"]
updated: 2026-08-10
---

# EdgeDoc

## What it is
EdgeDoc is a lightweight hybrid CNN-transformer model, from an Idiap Research Institute team, for simultaneous detection and localization of forgeries in identity documents. It fuses the green channel of an ID image with auxiliary NoisePrint features to flag subtle manipulations, and is designed to train from limited samples given the sensitive nature of ID data.

## Key facts
- EdgeDoc combines the TruFor framework with a custom lightweight architecture inspired by EdgeFace, performing classification and forgery localization simultaneously ⟨[[edgedoc-id-forgery]] Abstract / §2⟩.
- The backbone is the XXS variant of EdgeNeXt feeding a U-Net-style decoder; classification uses a global-average-pooling bottleneck head and the segmentation mask is produced by a pointwise convolution ⟨[[edgedoc-id-forgery]] §2.2 / §2.3⟩.
- Its input is two channels — the green channel of the ID image plus a NoisePrint feature map used as localized anomaly cues ⟨[[edgedoc-id-forgery]] §2.1 / §2.3⟩.
- On the FantasyID public validation set the authors report EdgeDoc scoring 1.00 on accuracy, F1, ROC AUC, and MCC, which they state is superior to baselines such as TruFor and MMFusion ⟨[[edgedoc-id-forgery]] §3⟩.
- The authors report EdgeDoc secured third place in the detection track of the ICCV 2025 DeepID Challenge, with inference using a fusion of EdgeDoc and TruFor that they state improves generalization to unseen manipulations ⟨[[edgedoc-id-forgery]] §3⟩.

## Relations
- Realizes: [[document-forgery-detection]]
- Defined in: [[edgedoc-id-forgery]]

## See also
[[document-forgery-detection]] · [[extraction-verification]] · [[edgedoc-id-forgery]]

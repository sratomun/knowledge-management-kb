---
title: "spdx:Checksum"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[data-distribution]]"]
sources: ["[[dcat-3]]"]
updated: 2026-08-09
---

# spdx:Checksum

## What it is
An SPDX class adopted by DCAT 3 to provide a digest for a distribution, so consumers can verify that the contents of a file or package have not changed. It is the value of the `spdx:checksum` property on a `dcat:Distribution`.

## Key facts
- Class added in DCAT 3, reusing the SPDX vocabulary [SPDX] ⟨§6.17⟩
- Reached from a distribution via `spdx:checksum`, which "provides a mechanism that can be used to verify that the contents of a file or package have not changed" ⟨§6.8.20⟩
- Has property `spdx:algorithm` identifying the algorithm used to produce the checksum; SPDX 2.2 defines individuals for MD2, MD4, MD5, MD6, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 ⟨§6.17.1⟩
- Has property `spdx:checksumValue`, "a lowercase hexadecimal encoded digest value produced using a specific algorithm", with range `xsd:hexBinary` ⟨§6.17.2⟩

## Relations
- Realizes: [[data-distribution]]
- Defined in: [[dcat-3]]
- Related: [[dcat-distribution]]

## See also
[[data-distribution]] · [[dcat-distribution]]

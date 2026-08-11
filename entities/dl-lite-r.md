---
title: "DL-Lite_R"
type: entity
subtype: formalism
aliases: ["DL-Lite^H_core"]
tags: [obda]
concepts: ["[[first-order-rewritability]]", "[[ontology-based-data-access]]"]
sources: ["[[dl-lite-short-course]]"]
updated: 2026-08-10
---

# DL-Lite_R

## What it is
DL-Lite_R is the DL-Lite dialect that extends core DL-Lite with role inclusion assertions.
In the extended-family naming scheme of Artale et al. it is DL-Lite^H_core, and it is the
description logic at the basis of the OWL 2 QL profile.

## Key facts
- The original DL-Lite_R corresponds to DL-Lite^H_core — core concept inclusions together with role inclusions — and is the DL at the basis of OWL 2 QL ⟨§4.1⟩.
- The complexity results for logics of the form DL-Lite^H_α (including DL-Lite_R) do not depend on whether the UNA is adopted, because every model without the UNA can be "untangled" into one respecting it ⟨§4.1⟩.
- For DL-Lite^H_horn (the Horn extension over the same role inclusions) query answering is in AC0 for data complexity, i.e., first-order rewritable ⟨§7⟩.

## Relations
- Realizes: [[first-order-rewritability]]
- Realizes: [[ontology-based-data-access]]
- Defined in: [[dl-lite-short-course]]
- Related: [[dl-lite]] · [[dl-lite-a]] · [[owl2-ql]]

## See also
[[dl-lite]] · [[owl2-ql]] · [[first-order-rewritability]]

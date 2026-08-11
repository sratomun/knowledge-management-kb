---
title: "DL-Lite_A"
type: entity
subtype: formalism
aliases: []
tags: [obda]
concepts: ["[[first-order-rewritability]]", "[[ontology-based-data-access]]"]
sources: ["[[dl-lite-short-course]]"]
updated: 2026-08-10
---

# DL-Lite_A

## What it is
DL-Lite_A is a DL-Lite dialect (introduced by Poggi et al., 2008a) that keeps both role
inclusions and functionality/number restrictions in the language while restricting their
interaction, so that reasoning stays as tractable — and query answering as first-order
rewritable — as in the fragments that use only one of the two features.

## Key facts
- DL-Lite_A restricts the interaction between role inclusions and number restrictions in order to reduce reasoning complexity, while also adding limited qualified existential quantifiers, role disjointness, (a)symmetry and (ir)reflexivity constraints that raise expressive power without affecting computational properties ⟨§2.1⟩.
- The restriction is imposed by three conditions (A1)–(A3) on TBoxes: only positive occurrences of qualified number restrictions ≥q R.C are allowed (A1); if ≥q R.C occurs then no negative occurrence of ≥q′R or ≥q′inv(R) with q′≥2 is allowed (A2); and if R has a proper sub-role, no negative occurrence of ≥q R or ≥q inv(R) with q≥2 is allowed (A3) ⟨§2.1⟩.
- For the logics DL-Lite^{HF}_α and DL-Lite^{HN}_α whose interaction is limited by (A1)–(A3), reasoning complexity coincides with that of the role-inclusion-free fragments DL-Lite^F_α / DL-Lite^N_α and is independent of whether the UNA is adopted ⟨§9⟩.

## Relations
- Realizes: [[first-order-rewritability]]
- Realizes: [[ontology-based-data-access]]
- Defined in: [[dl-lite-short-course]]
- Related: [[dl-lite]] · [[dl-lite-r]] · [[owl2-ql]]

## See also
[[dl-lite]] · [[dl-lite-r]] · [[first-order-rewritability]]

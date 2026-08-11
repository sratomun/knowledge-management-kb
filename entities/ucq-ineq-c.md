---
title: "UCQ≠,C query class"
type: entity
subtype: formalism
aliases: ["UCQ-ineq-C"]
tags: [obda]
concepts: ["[[query-abstraction]]"]
sources: ["[[obda-query-abstractions]]"]
updated: 2026-08-10
---

# UCQ≠,C query class

## What it is
An extension of unions of conjunctive queries introduced to capture query abstractions in ontology-based data access. It adds two special predicates to UCQs: a restricted binary inequality (≠) and a unary predicate C asserting that its argument is a database constant. It is expressive enough to represent any minimally complete — and hence any perfect — abstraction of a source query, when such an abstraction exists.

## Key facts
- UCQ≠,C extends UCQ with a restricted inequality (≠) and a unary predicate C stating that its argument is a constant ⟨§3⟩
- In query abstraction, C marks variables in ontological queries that must be mapped to values coming from the database, while ≠ distinguishes different ways of matching query variables ⟨§3⟩
- By definition, all variables of a UCQ≠,C occur in standard atoms, and the terms of any ≠-atom must be constants, answer variables, or variables that occur in a C-atom ⟨§3⟩
- C is useless in source queries since databases are ground, but the same query class is kept at both the data and ontology levels for simplicity ⟨§3⟩
- Extending UCQ to UCQ≠,C does not increase the complexity of the problems of interest: verifying whether a candidate M-abstraction is perfect remains Π^P_2-complete ⟨§3⟩
- UCQ≠,C is able to express a minimally complete M- and Σ-abstraction of any source UCQ≠,C, minimal with respect to all ontological queries under certain-answer semantics ⟨§4⟩
- Consequently a perfect Σ-abstraction, when it exists, is expressible in UCQ≠,C, and UCQ≠,C is a minimal language with this property even when the source query is a plain UCQ ⟨§4⟩

## Relations
- Realizes: [[query-abstraction]]
- Defined in: [[obda-query-abstractions]]

## See also
[[query-abstraction]] · [[ontology-based-data-access]]

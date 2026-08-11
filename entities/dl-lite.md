---
title: "DL-Lite"
type: entity
subtype: formalism
aliases: []
tags: [obda]
concepts: ["[[first-order-rewritability]]", "[[ontology-based-data-access]]"]
sources: ["[[xiao-obda-survey]]", "[[dl-lite-short-course]]", "[[ontop-swj]]", "[[poggi-linking-data]]"]
updated: 2026-08-10
---

# DL-Lite

## What it is
DL-Lite is a family of lightweight description logics designed so that ontology reasoning
and conjunctive query answering stay computationally tractable, making it the logical
foundation for ontology-based data access over relational sources.

## Key facts
- DL-Lite is the family of lightweight description logics used to express OBDA ontologies ⟨IJCAI 2018, pp. 5511-5519⟩.
- DL-Lite is deliberately restricted so that conjunctive query answering is first-order rewritable, keeping data complexity in AC0 ⟨IJCAI 2018, pp. 5511-5519⟩.
- DL-Lite underpins the OWL 2 QL profile targeted at query answering over large data ⟨IJCAI 2018, pp. 5511-5519⟩.
- The "extended DL-Lite family" is classified along five orthogonal axes — role inclusions, the form of concept inclusions (core, Krom, Horn, Bool), numeric constraints (none / functionality / number restrictions), the unique name assumption, and standard role constraints — yielding 40 logics studied by Artale et al. ⟨dl-lite-short-course §1, §9⟩.
- For the original DL-Lite logics KB satisfiability is polynomial for combined complexity, while conjunctive query answering is in AC0 for data complexity ⟨dl-lite-short-course §1⟩.
- The natural logic-based characterization of the family is embeddability into the one-variable fragment of first-order logic without equality and function symbols ⟨dl-lite-short-course §1⟩.
- Under the UNA and without role inclusions, number restrictions can be added to the DL-Lite logics "for free," without changing computational complexity ⟨dl-lite-short-course §1⟩.
- Combining role inclusions with number restrictions pushes KB satisfiability to ExpTime-complete and data complexity of instance checking to P-complete (core/Horn) or coNP-complete (Krom/Bool) ⟨dl-lite-short-course §1, §9⟩.
- OWL 2 QL, the ontology language at the heart of Ontop, is based on the DL-Lite family of lightweight description logics, which is what guarantees that queries over the ontology can be rewritten into equivalent queries over the databases ⟨ontop-swj §2.1⟩.
- Ontop has its roots in the QuOnto reasoner, described as a reasoner for the description logic DL-Lite with plain conjunctive query answering ⟨ontop-swj §7⟩.
- DL-Lite_A is a member of the family that takes seriously the distinction between objects and values, adding attributes (binary relations between objects and values) alongside concepts, roles, and value-domains ⟨§2⟩.
- Ontology satisfiability, instance checking, and conjunctive query answering in the DL-Lite family can all be done in LogSpace with respect to data complexity, letting the data-dependent part of reasoning be delegated to a relational DBMS ⟨§2⟩.

## Relations
- Realizes: [[first-order-rewritability]]
- Realizes: [[ontology-based-data-access]]
- Defined in: [[xiao-obda-survey]]
- Defined in: [[dl-lite-short-course]]
- Defined in: [[ontop-swj]]
- Related: [[owl2-ql]] · [[dl-lite-r]] · [[dl-lite-a]]

## See also
[[owl2-ql]] · [[first-order-rewritability]]

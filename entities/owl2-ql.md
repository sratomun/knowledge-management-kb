---
title: "OWL 2 QL"
type: entity
subtype: specification-construct
aliases: []
tags: [obda]
concepts: ["[[first-order-rewritability]]"]
sources: ["[[xiao-obda-survey]]", "[[dl-lite-short-course]]", "[[ontop-swj]]", "[[owl2-overview]]", "[[owl2-profiles]]"]
updated: 2026-08-10
---

# OWL 2 QL

## What it is
OWL 2 QL is the OWL 2 profile tailored for query answering over large amounts of data,
based on the DL-Lite family of description logics.

## Key facts
- OWL 2 QL is the ontology-language profile used in OBDA, grounded in DL-Lite ⟨IJCAI 2018, pp. 5511-5519⟩.
- OWL 2 QL is restricted so that conjunctive query answering is first-order (FO) rewritable ⟨IJCAI 2018, pp. 5511-5519⟩.
- OWL 2 QL is based on the DL-Lite family of description logics, with DL-LiteR providing its logical underpinning; DL-LiteR does not require the unique name assumption ⟨§3⟩.
- OWL 2 QL is designed so that sound and complete query answering is in LOGSPACE (more precisely, in AC0) with respect to the size of the data (assertions) ⟨§3⟩.
- OWL 2 QL is one of the three OWL 2 profiles, aimed at applications with very large volumes of instance data where query answering is the most important reasoning task ⟨dl-lite-short-course §1, §4.1⟩.
- The DL at the basis of OWL 2 QL is DL-Lite^H_core, i.e., the original DL-Lite_R ⟨dl-lite-short-course §4.1⟩.
- OWL 2 QL excludes number restrictions (not even functionality) and keys, because — in the absence of the UNA, which OWL replaces with sameAs/differentFrom — those constructs would raise complexity and break first-order rewritability ⟨dl-lite-short-course §4.1⟩.
- OWL 2 QL is one of the two ontology languages (alongside RDFS) supported by Ontop, and being based on the DL-Lite family it guarantees that queries over the ontology can be rewritten into equivalent queries over the databases ⟨ontop-swj §2.1⟩.
- Because the common OBDA strategy is query rewriting, OWL 2 QL is the OWL profile most suitable for OBDA systems; to guarantee rewritability, features such as recursion and property chains are not allowed in OWL 2 QL ⟨ontop-swj §6⟩.

## Relations
- Realizes: [[first-order-rewritability]]
- Defined in: [[xiao-obda-survey]]
- Defined in: [[dl-lite-short-course]]
- Defined in: [[ontop-swj]]
- Related: [[dl-lite]] · [[dl-lite-r]] · [[owl2]] · [[owl2-el]] · [[owl2-rl]]

## See also
[[dl-lite]] · [[ontology-based-data-access]]

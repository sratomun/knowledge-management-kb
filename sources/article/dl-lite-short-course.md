---
title: "The DL-Lite Family and Relations"
type: source
kind: article
authority: informational
subtype: academic-paper
aliases: ["arXiv:1401.3487"]
publisher: arXiv
url: https://arxiv.org/abs/1401.3487
version: "arXiv:1401.3487"
published: 2014-01
effective_from: 2014-01
effective_to: ongoing
status: current
tags: [obda, semantic-web]
updated: 2026-08-10
---

# The DL-Lite Family and Relations

## Scope & purpose
A comprehensive, systematic study of inference in the "extended DL-Lite family" of
description logics — the lightweight DLs that underpin ontology-based data access and the
OWL 2 QL profile. The article maps how various DL-Lite constructs interact and how they
affect the computational complexity of reasoning, so that the boundary of "lite"-ness
(tractable combined complexity, first-order-rewritable query answering) can be located
precisely. By Artale, Calvanese, Kontchakov and Zakharyaschev; published in the Journal
of Artificial Intelligence Research 36 (2009), pp. 1–69, and posted to arXiv (1401.3487)
in January 2014.

## Structure
Nine sections: (1) Introduction and motivation; (2) definition of the extended DL-Lite
family — syntax, semantics, and its use for conceptual modeling; (3) reasoning problems,
complexity measures, and a summary of results (Table 2, Remark 3.1); (4) the landscape of
DL-Lite logics and the relationship to OWL 2 / OWL 2 QL; (5) combined complexity of
satisfiability; (6) data complexity of instance checking; (7) data complexity of query
answering; (8) reasoning without the unique name assumption; (9) conclusion. Results rest
on embedding DL-Lite logics into one-variable first-order logic.

## Key points
- The aim is a systematic investigation of inference in extensions of the original DL-Lite logics along five mutually orthogonal axes: (i) role inclusions, (ii) the form of concept inclusions (core, Krom, Horn, Bool), (iii) numeric constraints (none, global functionality only, or arbitrary number restrictions), (iv) adopting or dropping the unique name assumption, and (v) standard role constraints (disjointness, symmetry, asymmetry, reflexivity, irreflexivity, transitivity) ⟨§1⟩.
- 40 different logics are studied, analyzing the combined complexity of KB satisfiability and instance checking together with the data complexity of instance checking and of answering positive existential queries ⟨§9⟩.
- For the original DL-Lite logics, KB satisfiability is polynomial for combined complexity, while query answering is in AC0 for data complexity ⟨§1⟩.
- AC0 for data complexity means that, given a conjunctive query over a KB, the query and the TBox can be rewritten — independently of the ABox — into a union of conjunctive queries over the ABox alone ⟨§1⟩.
- The natural logic-based characterization identified for the DL-Lite family is embeddability into the one-variable fragment of first-order logic without equality and function symbols, which is used to derive most upper complexity bounds ⟨§1⟩.
- The DL-Lite family forms the basis of OWL 2 QL, one of the three OWL 2 profiles, aimed at applications that use very large volumes of instance data and where query answering is the most important reasoning task ⟨§1, §4.1⟩.
- The original DL-Lite_R corresponds to DL-Lite^H_core (core concept inclusions plus role inclusions) and is the DL at the basis of the OWL 2 QL profile ⟨§4.1⟩.
- DL-Lite_A (Poggi et al., 2008a) restricts the interaction between role inclusions and number restrictions via conditions (A1)–(A3), while adding constructs such as limited qualified existential quantifiers, role disjointness, (a)symmetry and (ir)reflexivity that raise expressive power without changing computational properties ⟨§2.1⟩.
- Number restrictions, even expressed locally rather than as global functionality, can be added to the original DL-Lite logics (under the UNA and without role inclusions) "for free," i.e., without changing their computational complexity ⟨§1⟩.
- Combining role inclusions with number restrictions (or even functionality) sharply raises complexity: KB satisfiability, NLogSpace-complete in the simplest core case, becomes ExpTime-complete, and data complexity of instance checking becomes P-complete for core/Horn and coNP-complete for Krom/Bool logics ⟨§1, §9⟩.
- Positive existential query answering is data-complete for coNP for DL-Lite^{HN}_bool, and data-complete for P for DL-Lite^{HF}_horn ⟨§7⟩.
- Theorem 7.1 establishes that positive existential query answering for DL-Lite^N_horn, DL-Lite^H_horn and DL-Lite^{HN}_horn is in AC0 for data complexity ⟨Th. 7.1⟩.
- For the logics DL-Lite^{HF}_α and DL-Lite^{HN}_α whose role-inclusion / number-restriction interaction is limited by (A1)–(A3), reasoning complexity coincides with that of the role-inclusion-free fragments and is independent of whether the UNA is adopted ⟨§9⟩.
- Dropping the UNA and allowing equality between object names (OWL's sameAs, ≈) raises the AC0 memberships to LogSpace-completeness and destroys first-order rewritability of query answering and instance checking; inequality constraints (differentFrom) do not affect complexity — which is why OWL 2 QL excludes number restrictions and keys ⟨§1, Remark 3.1, §8, §4.1⟩.
- Extending any DL-Lite logic with role transitivity constraints keeps the combined complexity of satisfiability unchanged but makes data complexity of instance checking and query answering NLogSpace-hard, replacing AC0 membership (and thus losing first-order rewritability) ⟨Remark 3.1, §5.4⟩.
- The first-order rewriting technique has been implemented in systems such as QuOnto — which queries data in any standard RDBMS relying on ontology-to-relational mappings — and Owlgres, which accesses an ABox stored in a Postgres database; the rewritten query can be substantially larger than the original ⟨§1, §9⟩.

## Concepts & entities covered
Concepts: [[description-logic]] · [[ontology-based-data-access]] · [[query-rewriting]] · [[query-unfolding]] · [[first-order-rewritability]]
Entities: [[dl-lite]] · [[dl-lite-r]] · [[dl-lite-a]] · [[owl2-ql]]

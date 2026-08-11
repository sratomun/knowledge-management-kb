---
title: "Description Logic"
type: concept
tags: [semantic-web, obda]
related: ["[[ontology-based-data-access]]", "[[first-order-rewritability]]", "[[certain-answer-semantics]]", "[[rdf-vocabulary-schema]]"]
updated: 2026-08-10
---

# Description Logic

## What it is
A family of formal logics for representing knowledge as classes (concepts), relationships (roles/properties), and individuals, with a precisely defined model-theoretic meaning that lets reasoners decide questions such as class consistency, subsumption, and instance membership. Different members of the family trade expressive power against the computational cost of reasoning; the ontology languages of the Semantic Web, and the ontology layer of ontology-based data access, are built on particular description logics chosen for their reasoning properties.

## How sources treat it
- **[[owl2-overview]]** _(standard · normative)_ — the Direct Semantics assigns meaning directly to ontology structures and is compatible with the model-theoretic semantics of the SROIQ description logic; ontologies satisfying the syntactic conditions for translation into a SROIQ knowledge base are called OWL 2 DL ontologies ⟨§2.3⟩
- **[[owl2-overview]]** _(standard · normative)_ — the two semantics (Direct and RDF-Based) are used by reasoners and other tools to answer class consistency, subsumption, and instance retrieval queries, linked by a correspondence theorem ⟨§2.3⟩
- **[[owl2-overview]]** _(standard · normative)_ — OWL 2 defines three profiles (EL, QL, RL), each a syntactic subset more restrictive than OWL DL, trading expressive power for computational and/or implementational benefits; OWL 2 EL enables polynomial-time reasoning and OWL 2 QL enables conjunctive queries answered in LogSpace (AC0) using standard relational database technology ⟨§2.4⟩
- **[[owl2-profiles]]** _(standard · normative)_ — a profile (fragment / sublanguage) is a trimmed-down version of OWL 2 that trades some expressive power for efficiency of reasoning; OWL 2 EL is based on the EL family of description logics and OWL 2 QL is based on the DL-Lite family, and none of the three profiles is a subset of another ⟨§1, §2.1, §3⟩
- **[[owl2-profiles]]** _(standard · normative)_ — OWL 2 QL's underpinning DL-LiteR does not require the unique name assumption (UNA), whereas more expressive variants such as DL-LiteA (with functional properties / keys) require UNA and further global restrictions to keep query answering in LogSpace ⟨§3⟩
- **[[owl2-profiles]]** _(standard · normative)_ — Table 10 records worst-case complexity: OWL 2 QL is In AC0 in data complexity, OWL 2 EL and OWL 2 RL are PTIME-complete for the standard problems, and OWL 2 under the RDF-Based Semantics is Undecidable ⟨§5⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — the DL-Lite family are the lightweight description logics that underpin ontology-based data access and the OWL 2 QL profile; the study systematically maps how DL-Lite constructs interact and how they affect the computational complexity of reasoning ⟨Scope, §1⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — the natural logic-based characterization of the DL-Lite family is embeddability into the one-variable fragment of first-order logic without equality and function symbols, which is used to derive most upper complexity bounds ⟨§1⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — the original DL-LiteR corresponds to DL-Lite^H_core (core concept inclusions plus role inclusions) and is the DL at the basis of the OWL 2 QL profile ⟨§4.1⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — combining role inclusions with number restrictions (or functionality) sharply raises complexity, and dropping the UNA (allowing OWL's sameAs / ≈) destroys first-order rewritability — which is why OWL 2 QL excludes number restrictions and keys ⟨§1, Remark 3.1, §4.1⟩

## Where sources differ
The sources agree that description logics underpin OWL 2 and its profiles and that expressive power is traded against reasoning complexity, but they operate at different levels. The OWL 2 Overview presents the family from the top down, identifying SROIQ behind OWL 2 DL and naming the three profiles and their headline complexity claims ⟨owl2-overview §2.3, §2.4⟩. The Profiles Recommendation specifies the fragments normatively, tying EL to the EL family, QL to DL-Lite, and giving the per-profile complexity table ⟨owl2-profiles §1, §5⟩. The DL-Lite short course studies the DL-Lite family itself in fine grain, charting how individual constructs (role inclusions, number restrictions, the UNA) move reasoning across the tractability boundary — a granularity the two standards do not reach ⟨dl-lite-short-course §1, Remark 3.1⟩.

## See also
[[ontology-based-data-access]] · [[first-order-rewritability]] · [[certain-answer-semantics]] · [[rdf-vocabulary-schema]]

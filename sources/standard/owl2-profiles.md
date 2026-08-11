---
title: "OWL 2 Web Ontology Language Profiles"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["OWL 2 Profiles"]
publisher: W3C
url: https://www.w3.org/TR/owl2-profiles/
version: "2 (2012-12-11)"
published: 2012-12
effective_from: 2012-12-11
effective_to: ongoing
status: current
tags: [semantic-web]
updated: 2026-08-10
---

# OWL 2 Web Ontology Language Profiles

## Scope & purpose

W3C Recommendation (11 December 2012, Second Edition) that specifies several profiles of OWL 2 — trimmed-down sublanguages (in logic, "fragments") that can be more simply and/or efficiently implemented. Three profiles are defined: OWL 2 EL, OWL 2 QL, and OWL 2 RL. Each trades some expressive power for efficiency of reasoning, achieves that efficiency in a different way, and targets different application scenarios: OWL 2 EL for ontologies with very large numbers of classes/properties; OWL 2 QL for very large volumes of instance data where query answering is the key task, enabling ontology-based access to data held in relational databases through query rewriting; and OWL 2 RL for scalable rule-based reasoning over OWL 2 and RDF(S). Profiles are specified by placing syntactic restrictions on the functional-style-syntax grammar, giving only the differing productions plus (in the Appendix) the full per-profile grammars. None of the three profiles is a subset of another. This document is descriptive of the language fragments; conformance is defined via the referenced OWL 2 Conformance specification.

## Structure

- §1 Introduction — profiles as fragments/sublanguages; overview of EL, QL, RL and their target scenarios; how profiles are defined by restricting the functional-style syntax; RFC 2119 keyword usage
- §2 OWL 2 EL — §2.1 Feature Overview; §2.2 Profile Specification (§2.2.1 Entities, §2.2.2 Property Expressions, §2.2.3 Class Expressions, §2.2.4 Data Ranges, §2.2.5 Axioms, §2.2.6 Global Restrictions)
- §3 OWL 2 QL — §3.1 Feature Overview; §3.2 Profile Specification (§3.2.1 Entities, §3.2.2 Property Expressions, §3.2.3 Class Expressions, §3.2.4 Data Ranges, §3.2.5 Axioms)
- §4 OWL 2 RL — §4.1 Feature Overview; §4.2 Profile Specification (§4.2.1 Entities … §4.2.5 Axioms); §4.3 Reasoning in OWL 2 RL and RDF Graphs using Rules (the OWL 2 RL/RDF rules; Theorem PR1)
- §5 Computational Properties — complexity measures and Table 10 (complexity of the profiles)
- §6 Appendix: Complete Grammars for Profiles (§6.1 EL, §6.2 QL, §6.3 RL)
- §7 Appendix: Change Log (Informative)
- §8 Acknowledgments
- §9 References (§9.1 Normative, §9.2 Nonnormative)

## Key points

- An OWL 2 profile (commonly called a fragment or sublanguage) is a trimmed-down version of OWL 2 that trades some expressive power for efficiency of reasoning; the document defines three profiles — EL, QL, RL — each achieving efficiency differently, and none of the profiles is a subset of another ⟨§1⟩.
- The italicized keywords must, must not, should, should not, and may specify normative features of OWL 2 documents and tools and are interpreted as specified in RFC 2119 ⟨§1⟩.
- OWL 2 QL is aimed at applications that use very large volumes of instance data and where query answering is the most important reasoning task; in OWL 2 QL, conjunctive query answering can be implemented using conventional relational database systems ⟨§1, §3⟩.
- OWL 2 QL is designed so that sound and complete query answering is in LOGSPACE (more precisely, in AC0) with respect to the size of the data (assertions), while providing many of the main features needed to express conceptual models such as UML class diagrams and ER diagrams; in particular the profile contains the intersection of RDFS and OWL 2 DL ⟨§3⟩.
- OWL 2 QL is designed so that data (assertions) stored in a standard relational database system can be queried through an ontology via a simple rewriting mechanism — rewriting the query into an SQL query that is then answered by the RDBMS, without any changes to the data; the QL acronym reflects that query answering can be implemented by rewriting queries into a standard relational Query Language ⟨§1, §3⟩.
- OWL 2 QL is based on the DL-Lite family of description logics; DL-LiteR provides the logical underpinning and does not require the unique name assumption (UNA), whose explicit axiomatization is thereby avoided; more expressive variants (e.g. DL-LiteA with functional properties/keys) require UNA and further global restrictions to keep query answering in LOGSPACE ⟨§3⟩.
- OWL 2 QL does not support individual equality assertions (SameIndividual): adding such axioms would increase the data complexity of query answering so that it is no longer first order rewritable, which means query answering could not be implemented directly using relational database technologies ⟨§3.1⟩.
- OWL 2 QL separates class expressions into subClassExpression and superClassExpression productions (Table 1), and does not support ObjectSomeValuesFrom in subclass position, ObjectHasSelf, ObjectHasValue/DataHasValue, enumerations, universal quantification, cardinality restrictions, disjunction, property chains, functional/inverse-functional/transitive properties, or keys ⟨§3.1, §3.2.3⟩.
- In OWL 2 QL the datatypes xsd:double, xsd:float, xsd:nonPositiveInteger, xsd:positiveInteger, xsd:negativeInteger, xsd:long, xsd:int, xsd:short, xsd:byte, the unsigned integer types, xsd:language, and xsd:boolean must not be used; OWL 2 QL does not support anonymous individuals; class assertions can involve only atomic classes; and each OWL 2 QL ontology must satisfy the global restrictions on axioms of Section 11 of the structural specification ⟨§3.2.1, §3.2, §3.2.5⟩.
- OWL 2 EL is designed for applications with ontologies defining very large numbers of classes and/or properties, for which ontology consistency, class expression subsumption, and instance checking can be decided in polynomial time; it is based on the EL family of description logics (providing only Existential quantification) and, for example, suffices to express the biomedical ontology SNOMED CT ⟨§2, §2.1⟩.
- OWL 2 EL supports existential quantification, self-restriction, single-individual/single-literal enumerations, intersections, property chains, and keys, but does not support universal quantification, cardinality restrictions, disjunction, class negation, inverse object properties, or (inverse-)functional/symmetric/asymmetric object properties; in OWL 2 EL certain datatypes (e.g. xsd:double, xsd:float, xsd:boolean) must not be used, and anonymous individuals are not supported ⟨§2.1, §2.2.1⟩.
- OWL 2 EL adds a global restriction: the axiom closure Ax of an OWL 2 EL ontology must obey the Section 11 restrictions and, if Ax contains a property-chain SubObjectPropertyOf axiom and imposes a range restriction to some class expression CE on the super-property, then Ax must impose a range restriction to CE on the chain's last property ⟨§2.2.6⟩.
- OWL 2 RL is aimed at applications requiring scalable reasoning without sacrificing too much expressive power, accommodating both OWL 2 applications that trade full expressivity for efficiency and RDF(S) applications needing some added expressivity; it can be implemented using rule-based reasoning engines, ontology consistency, class expression satisfiability/subsumption, instance checking, and conjunctive query answering are all solvable in polynomial time w.r.t. ontology size, and the RL acronym reflects implementability using a standard Rule Language ⟨§1, §4⟩.
- OWL 2 RL restricts constructs to certain syntactic positions (subClassExpression, superClassExpression, equivClassExpression; Table 2) so as to avoid inferring the existence of individuals not explicitly present and to avoid nondeterministic reasoning; it supports all OWL 2 axioms apart from DisjointUnion and ReflexiveObjectProperty, and the owl:real and owl:rational datatypes must not be used in OWL 2 RL ⟨§4.1, §4.2.1, §4.2.5⟩.
- §4.3 presents a partial axiomatization of the OWL 2 RDF-Based Semantics as universally quantified first-order implications over a ternary predicate T (the OWL 2 RL/RDF rules), a starting point for rule-based implementations; such an implementation may also be used with arbitrary RDF graphs, in which case completeness is no longer guaranteed although only correct entailments are still produced ⟨§4.3⟩.
- Table 10 summarizes worst-case complexity: for OWL 2 QL, ontology consistency/satisfiability/subsumption/instance checking are NLogSpace-complete (taxonomic) and In AC0 (data), and conjunctive query answering is In AC0 (data) / NP-complete (combined); OWL 2 EL and OWL 2 RL are PTIME-complete for the standard problems, whereas OWL 2 under the RDF-Based Semantics is Undecidable ⟨§5⟩.

## Concepts & entities covered
Concepts: [[description-logic]] · [[first-order-rewritability]] · [[ontology-based-data-access]]
Entities: [[owl2-ql]] · [[owl2-el]] · [[owl2-rl]]

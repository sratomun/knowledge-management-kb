---
title: "LegalRuleML Core Specification Version 1.0"
type: source
kind: standard
authority: normative
subtype: standard
aliases: ["LegalRuleML"]
publisher: OASIS
url: https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/os/legalruleml-core-spec-v1.0-os.html
version: "1.0"
published: 2021
effective_from: 2021-08-30
effective_to: ongoing
status: current
tags: [doc-processing]
updated: 2026-08-10
---

# LegalRuleML Core Specification Version 1.0

## Scope & purpose

LegalRuleML is an OASIS Standard that extends RuleML with formal features specific to legal norms, guidelines, policies, and reasoning, defining a specification (expressed with XML Schema and Relax NG) able to represent the particularities of legal normative rules with a rich, articulated markup language ⟨Abstract⟩. Its motivation is that legal texts — legislation, regulations, contracts, case law — are the source of norms but, as natural-language text, resist exchange, extraction, and automated processing; LegalRuleML provides machine-readable forms of that content to feed further interchange, comparison, evaluation, and reasoning ⟨§2.1⟩. Explicitly out of scope are the specifications of core or domain legal ontologies ⟨§2.2⟩. All text in the specification is normative unless labeled non-normative ⟨§1.4⟩; several structural chapters (Background, Functional Requirements, XML Design Principles, Examples) are marked non-normative, while the Vocabulary is determined by the normative schemas ⟨§3.1⟩.

## Structure

- §1 Introduction (IPR, Terminology, References, Typographical Conventions) ⟨§1⟩
- §2 Background, Motivation, Principles (non-normative) ⟨§2⟩
- §3 Vocabulary — namespaces, Node Elements, RuleML Node Elements, Edge Elements, attributes, metamodel ⟨§3⟩
- §4 Functional Requirements — modeling legal norms (defeasibility, constitutive/prescriptive, deontic), metadata, associations & context ⟨§4⟩
- §5 XML Design Principles — node/edge dichotomy, serializations, dialects, design patterns, schema derivation ⟨§5⟩
- §6 Comprehensive Examples; §7 Conformance; §8 Bibliography; Annexes A–G ⟨§6–§8⟩

## Key points

- The objective is to extend RuleML with formal features specific to legal norms, guidelines, policies, and reasoning ⟨§2.2⟩.
- LegalRuleML models defeasibility and defeasible logic, deontic operators (obligations, permissions, prohibitions, rights), semantic negation, temporal management, norm classification (constitutive, prescriptive), jurisdiction, isomorphism, identification of parts of norms, and authorial tracking ⟨§2.2⟩.
- A Legal Norm is defined as a binding directive from a Legal Authority to addressees (Bearers or Auxiliary Parties), and a Legal Rule is a formal representation of a Legal Norm ⟨§3.2⟩.
- Constitutive statements define concepts and do not prescribe behaviors, whereas prescriptive statements prescribe behaviors via permissions, obligations, or prohibitions on states, actions, or courses of action ⟨§3.4⟩.
- Deontic Specifications indicate what states are legal or illegal and include Obligation, Permission, Prohibition, and SuborderList, plus Boolean combinations ⟨§3.2⟩.
- Multiple Semantic Annotations is a main principle: a legal rule may carry multiple annotations representing different legal interpretations, each in a separate block with parameters for provenance, jurisdiction, and logical interpretation ⟨§2.3⟩.
- Isomorphism seeks a one-to-one correspondence between collections of formal rules and the units of (controlled) natural-language text expressing them in the original legal sources, easing validation and maintenance ⟨§4.1 R4⟩.
- An IRI-based linking mechanism supports many-to-many (N:M) relationships between rules and textual provisions, managed in the metadata block to avoid redundancy and association errors ⟨§2.3⟩.
- LegalRuleML represents temporal issues unambiguously: a rule has parameters that vary over time such as its status (strict, defeasible, defeater), validity (repealed, annulled, suspended), and jurisdiction ⟨§2.3⟩.
- LegalRuleML is independent from any legal ontology and logic framework but includes an IRI-based mechanism for pointing to reusable classes of an external ontology or framework ⟨§2.3⟩.
- LegalRuleML is mappable to RDF triples for Linked Data reuse ⟨§2.3⟩.
- Defeasible reasoning is sceptical: given conflicting rules concluding `head` and `-head`, it refrains from either conclusion unless a conflict-resolution mechanism applies, avoiding ex falso quodlibet ⟨§4.2.1⟩.
- Three rule strengths are distinguished — strict rules (`->`, the head always holds when the body holds), defeasible rules (`=>`, typically holds unless there are reasons otherwise), and defeaters (`~>`, which only block the opposite conclusion) ⟨§4.2.1⟩.
- Conflicts are resolved by methods including specificity (most specific rule prevails), salience/weight, and a preference (superiority) relation over rules ⟨§4.2.1⟩.
- The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL are to be interpreted as described in RFC 2119 ⟨§1.1⟩.
- The normalized serialization uses a "striped" node/edge syntax where children of Node elements are edge elements (leaf or containing one Node); the compact serialization is derived by deleting skippable edge tags ⟨§3.8⟩.

## Concepts & entities covered

Concepts: [[machine-readable-legal-norms]]

Entities: [[org-oasis]]

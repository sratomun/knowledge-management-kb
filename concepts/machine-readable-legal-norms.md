---
title: "Machine-Readable Legal Norms"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[legislative-document-model]]"]
updated: 2026-08-10
---

# Machine-Readable Legal Norms

## What it is
Machine-readable legal norms are formal representations of the rules and obligations expressed in legal texts — obligations, permissions, prohibitions, defeasibility, and their temporal and jurisdictional conditions — captured so that machines can interchange, compare, evaluate, and reason over them. This is distinct from modeling a legal document's structure: it targets the normative content (the rules) rather than the document container.

## How sources treat it
- **[[legalruleml]]** _(standard · normative)_ — An OASIS Standard that extends RuleML with formal features specific to legal norms, guidelines, policies, and reasoning, providing machine-readable forms of legal content to feed interchange, comparison, evaluation, and reasoning ⟨§2.2⟩
- **[[legalruleml]]** _(standard · normative)_ — Models defeasibility and defeasible logic, deontic operators (obligations, permissions, prohibitions, rights), semantic negation, temporal management, norm classification (constitutive, prescriptive), jurisdiction, isomorphism, identification of parts of norms, and authorial tracking ⟨§2.2⟩
- **[[legalruleml]]** _(standard · normative)_ — Defines a Legal Norm as a binding directive from a Legal Authority to addressees and a Legal Rule as a formal representation of a Legal Norm, and supports multiple semantic annotations so one rule may carry different legal interpretations ⟨§3.2⟩

## Where sources differ
Only one source treats this concept, so there is no divergence to report. [[legalruleml]] consistently frames machine-readable legal norms as a rule-representation layer that is deliberately independent of any particular legal ontology or logic framework while providing an IRI-based mechanism to point to external ones, and mappable to RDF triples for Linked Data reuse ⟨§2.3⟩. It also isolates isomorphism — a one-to-one correspondence between formal rules and the textual provisions expressing them — as the anchor to the underlying legal text ⟨§4.1 R4⟩.

## See also
[[legislative-document-model]] · [[legal-resource-identifier]]

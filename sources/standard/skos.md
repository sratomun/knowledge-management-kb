---
title: "SKOS Simple Knowledge Organization System Reference"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["SKOS", "Simple Knowledge Organization System"]
publisher: W3C
url: https://www.w3.org/TR/skos-reference/
version: "1.0"
published: 2009-08
effective_from: 2009-08-18
effective_to: ongoing
status: current
tags: [semantic-web, knowledge-organization]
updated: 2026-08-09
---

# SKOS Simple Knowledge Organization System Reference

## Scope & purpose

SKOS is a common data model for sharing and linking knowledge organization systems (KOS) — thesauri, taxonomies, classification schemes and subject heading systems — via the Web ⟨Abstract⟩. It captures the structure these families share and makes it explicit to enable data and technology sharing across diverse applications, providing a standard, low-cost migration path for porting existing KOS to the Semantic Web ⟨Abstract⟩. It may be used on its own or in combination with formal knowledge representation languages such as OWL ⟨Abstract⟩. This document is the normative specification, intended for readers involved in designing and implementing information systems who already understand RDF and OWL ⟨Abstract⟩. The SKOS data model is formally defined as an OWL Full ontology; SKOS data are expressed as RDF triples and may be encoded in any concrete RDF syntax (RDF/XML, Turtle, etc.) ⟨§1.2⟩. SKOS is a data-modeling language for representing KOS "as-is", **not** a formal knowledge representation language: the "concepts" of a thesaurus are modeled as individuals, and links between them as facts about those individuals, never as class or property axioms ⟨§1.3⟩. The open-world assumption is a fundamental premise: no conclusions can be drawn from missing data, and removing something never makes remaining data inconsistent ⟨§1.5⟩.

## Structure

- §1 Introduction — Background & Motivation (§1.1), SKOS Overview (§1.2), SKOS/RDF/OWL (§1.3), Consistency & Integrity (§1.4), Inference, Dependency & the Open-World Assumption (§1.5), Design Rationale (§1.6), How to Read (§1.7), Conformance (§1.8)
- §2 SKOS Namespace and Vocabulary
- §3 The skos:Concept Class
- §4 Concept Schemes
- §5 Lexical Labels
- §6 Notations
- §7 Documentation Properties (Note Properties)
- §8 Semantic Relations
- §9 Concept Collections
- §10 Mapping Properties
- §11 References; §12 Acknowledgments
- Appendix A SKOS Properties and Classes; Appendix B SKOS eXtension for Labels (SKOS-XL); Appendix C Namespace Documents; Appendix D SKOS Namespace historical note

## Key points

- The SKOS namespace URI is `http://www.w3.org/2004/02/skos/core#` (prefix `skos:`); all vocabulary URIs are formed by appending a local name to it ⟨§2⟩.
- `skos:Concept` is an instance of `owl:Class` (S1); a SKOS concept is "an idea or notion; a unit of thought," a definition meant to be suggestive rather than restrictive ⟨§3⟩.
- A concept scheme aggregates concepts and their links: `skos:ConceptScheme` is an `owl:Class` (S2), disjoint with `skos:Concept` (S9, an integrity condition); `skos:topConceptOf` is a sub-property of `skos:inScheme` (S7) and `owl:inverseOf skos:hasTopConcept` (S8) ⟨§4⟩.
- There is no way to close the boundary of a concept scheme: SKOS can describe a scheme but provides no mechanism to completely define one, and a concept may take part in zero, one, or more schemes ⟨§4.6.1⟩.
- Lexical labels (`skos:prefLabel`, `skos:altLabel`, `skos:hiddenLabel`) are each `owl:AnnotationProperty` and sub-properties of `rdfs:label` (S10, S11), with range the class of RDF plain literals (S12) ⟨§5⟩.
- Integrity conditions on labels: `skos:prefLabel`, `skos:altLabel` and `skos:hiddenLabel` are pairwise disjoint properties (S13), and "A resource has no more than one value of skos:prefLabel per language tag" (S14) ⟨§5.4⟩.
- `skos:notation` is an instance of `owl:DatatypeProperty` (S15); a notation is a string used to uniquely identify a concept within a scheme and is, by convention, used only with a typed literal whose datatype denotes a notation/classification system ⟨§6⟩.
- Seven documentation properties (`skos:note`, `skos:changeNote`, `skos:definition`, `skos:editorialNote`, `skos:example`, `skos:historyNote`, `skos:scopeNote`) are each `owl:AnnotationProperty` (S16); the six specific notes are each sub-properties of `skos:note` (S17) ⟨§7⟩.
- Semantic relations distinguish hierarchical (`skos:broader`/`skos:narrower`) from associative (`skos:related`) links; `skos:broader`/`skos:narrower` are, by convention, used only for direct (immediate) links and are deliberately **not** declared transitive ⟨§8.1⟩.
- `skos:semanticRelation` has domain and range `skos:Concept` (S19, S20); `skos:broaderTransitive`/`skos:narrowerTransitive`/`skos:related` are sub-properties of it (S21); `skos:broader` is a sub-property of `skos:broaderTransitive` (S22); `skos:related` is symmetric (S23); the transitive properties are `owl:TransitiveProperty` (S24) ⟨§8.3⟩.
- Semantic-relation integrity condition: "skos:related is disjoint with the property skos:broaderTransitive" (S27) — so hierarchical and associative links between the same pair clash ⟨§8.4⟩.
- Collections: `skos:Collection` and `skos:OrderedCollection` are each `owl:Class` (S28), `OrderedCollection` a sub-class of `Collection` (S29); `skos:memberList` is an `owl:FunctionalProperty` (S35) with range `rdf:List` (S34); integrity condition S37 — `skos:Collection` is disjoint with each of `skos:Concept` and `skos:ConceptScheme` ⟨§9⟩.
- Mapping properties (`skos:closeMatch`, `skos:exactMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`) link concepts across schemes; all are sub-properties of `skos:mappingRelation`, itself a sub-property of `skos:semanticRelation` (S39, S40); `skos:exactMatch` is transitive and a sub-property of `skos:closeMatch` (S45, S42), while `skos:closeMatch` is deliberately **not** transitive to avoid compound errors ⟨§10⟩.
- Mapping integrity condition S46: "skos:exactMatch is disjoint with each of the properties skos:broadMatch and skos:relatedMatch" ⟨§10.4⟩.
- SKOS-XL (optional extension, namespace `http://www.w3.org/2008/05/skos-xl#`) reifies labels as instances of `skosxl:Label`, each with exactly one `skosxl:literalForm` (S52); two labels with the same literal form are not necessarily the same individual, and property chains (`skosxl:prefLabel`, `skosxl:literalForm`) are sub-properties of the corresponding `skos:prefLabel` etc. (S55–S57) ⟨App. B⟩.
- The specification defines no formal notion of conformance, but an RDF graph is inconsistent with SKOS if it and the SKOS data model together lead to a logical contradiction ⟨§1.8⟩.

## Concepts & entities covered

Concepts: [[controlled-vocabulary]] · [[concept-scheme]] · [[lexical-labeling]] · [[notation]] · [[semantic-relation]] · [[scheme-mapping]] · [[concept-collection]]

Entities: [[skos-concept]] · [[skos-conceptscheme]] · [[skos-inscheme]] · [[skos-hastopconcept]] · [[skos-topconceptof]] · [[skos-preflabel]] · [[skos-altlabel]] · [[skos-hiddenlabel]] · [[skos-notation]] · [[skos-note]] · [[skos-semanticrelation]] · [[skos-broader]] · [[skos-narrower]] · [[skos-broadertransitive]] · [[skos-narrowertransitive]] · [[skos-related]] · [[skos-collection]] · [[skos-orderedcollection]] · [[skos-member]] · [[skos-memberlist]] · [[skos-mappingrelation]] · [[skos-exactmatch]] · [[skos-closematch]] · [[skos-broadmatch]] · [[skos-narrowmatch]] · [[skos-relatedmatch]] · [[skosxl-label]] · [[skosxl-literalform]] · [[skosxl-preflabel]] · [[skosxl-labelrelation]]

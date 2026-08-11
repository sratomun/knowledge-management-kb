---
title: "gist — Minimalist Upper Ontology"
type: source
kind: whitepaper
authority: informational
subtype: upper-ontology
aliases: ["gist ontology"]
publisher: Semantic Arts
url: https://www.semanticarts.com/gist/
version: "current"
published: 2024-01
effective_from: 2024-01
effective_to: ongoing
status: current
tags: [ontology-engineering]
updated: 2026-08-10
---

# gist — Minimalist Upper Ontology

## Scope & purpose

gist is Semantic Arts' minimalist upper (foundational) ontology for the enterprise, designed to provide the maximum coverage of typical business concepts with the fewest primitives and the least ambiguity ⟨semanticarts.com/gist⟩. It is domain-independent and intended as a foundation on which more specialized enterprise or application ontologies are built, facilitating interoperability and integration of knowledge across domains ⟨semanticarts.com/gist⟩. gist is distributed free under the Creative Commons Attribution 4.0 International license, requiring only attribution to the source ⟨semanticarts.com/gist⟩.

## Structure

gist defines a small number of top-level concepts on which everything else is based, both within gist and within downstream ontologies that use it as a foundation ⟨semanticarts.com/gist⟩. The current release (14.1.0, April 2026) defines roughly 100 classes and about the same number of object and data properties, plus a set of named individuals used as reference values (e.g., altitude, area, balance, duration, mass, monetary value, probability, volume) ⟨gist-doc WIDOCO 14.1.0, §Overview⟩. Coverage is often summarized graphically as the "Periodic Table of gist," organizing classes into abstract conceptual clusters ⟨semanticarts.com/gist⟩. Top-level classes span business essentials such as Organization, Person, Agreement, Commitment, Event, Task, Content, Category, Magnitude, Unit of Measure, Geographic Location, and Intellectual Property ⟨gist-doc WIDOCO 14.1.0, §Classes⟩.

## Key points

- gist is described as a minimalist upper ontology for the enterprise providing "maximum coverage of typical business concepts with the fewest number of primitives and the least amount of ambiguity" ⟨semanticarts.com/gist⟩
- Its primitives are deliberately everyday concepts with ordinary names (person, organization, agreement) rather than philosophical abstractions such as endurant, perdurant, or qualia ⟨semanticarts.com/gist⟩
- gist defines around 100 classes and about the same number of attributes and relationships, serving as a foundation for building more specialized ontologies ⟨semanticarts.com/gist⟩
- It is designed to be domain-independent so it can be applied across a wide spectrum of domains, supporting interoperability and knowledge integration ⟨semanticarts.com/gist⟩
- gist uses extensive and fine-grained disjointness at the highest level so that a reasoner surfaces logical inconsistencies (e.g., a thing typed as both a government organization and an intergovernmental organization) ⟨semanticarts.com/gist⟩
- gist specifies domain and range sparingly to keep properties broadly applicable ⟨semanticarts.com/gist⟩
- As a deliberate design decision, gist does not define inverse properties, to eliminate redundancy and reduce cognitive load; class definitions use "inverse <property>" expressions instead ⟨semanticarts.com/gist⟩; ⟨gist-doc WIDOCO 14.1.0, §Object Properties⟩
- Subclasses are typically defined by a pattern (OWL equivalent-class restrictions) specifying how they specialize their superclass — e.g., an Account is "an Agreement having a balance" ⟨semanticarts.com/gist⟩; ⟨gist-doc WIDOCO 14.1.0, §Account⟩
- gist is distributed free under CC BY 4.0; users must keep gist terms in the gist namespace (https://w3id.org/semanticarts/ns/ontology/gist/) and not define their own terms within it ⟨semanticarts.com/gist⟩
- The core ontology is serialized as Turtle, RDF/XML, and JSON-LD, with supplementary ontologies of RDFS annotations and materialized subclass inferences for varied reasoners ⟨semanticarts.com/gist⟩
- gist 14.0.0 (Oct 31 2025) introduced a KnowledgeConcept class for expressing knowledge that arises from the distillation of experience, and an Assignment class (with predicates) for task, pay-rate, and supervisor assignments ⟨semanticarts.com/gist⟩
- gist 14.1.0 is a minor, backward-compatible release that clarified annotations and deprecated several classes and properties (e.g., Building, Landmark, Language, Schema Meta Data, prevents) in preparation for removal, to keep gist small and manageable ⟨semanticarts.com/gist⟩; ⟨gist-doc WIDOCO 14.1.0, §Description⟩
- gist supports a fine-grained temporal model, distinguishing actual vs. planned and multiple precisions of start/end datetimes, plus classes such as Time Interval, Scheduled Event, Historical Event, and Contemporary Event ⟨gist-doc WIDOCO 14.1.0, §Data Properties⟩
- Semantic Arts markets gist as the basis for enterprise knowledge graphs and offers industry extensions (cybersecurity, pharmaceuticals, accounting, HR, professional services) plus gistBFO, a public bridge ontology aligning gist with the Basic Formal Ontology (BFO) ⟨semanticarts.com/gist⟩

## Concepts & entities covered

Concepts: [[upper-ontology]]
Entities: [[gist]] · [[gistbfo]] · [[gist-14-0-0]] · [[gist-14-1-0]]

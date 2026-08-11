---
title: "gist"
type: entity
subtype: formalism
aliases: ["gist ontology (entity)"]
tags: [ontology-engineering]
concepts: ["[[upper-ontology]]"]
sources: ["[[gist]]"]
updated: 2026-08-10
---

# gist

## What it is
gist is Semantic Arts' minimalist upper (foundational) ontology for the enterprise, expressed in OWL, designed to provide maximum coverage of typical business concepts with the fewest primitives and least ambiguity. It is domain-independent and serves as a foundation on which more specialized enterprise or application ontologies are built.

## Key facts
- gist defines around 100 classes and about the same number of attributes and relationships, serving as a foundation for building more specialized ontologies ⟨semanticarts.com/gist⟩.
- Its top-level primitives are everyday concepts with ordinary names such as person, organization, and agreement, rather than philosophical abstractions such as endurant, perdurant, or qualia ⟨semanticarts.com/gist⟩.
- gist uses extensive and fine-grained disjointness at the highest level so a reasoner surfaces logical inconsistencies (e.g., a thing typed as both a government organization and an intergovernmental organization) ⟨semanticarts.com/gist⟩.
- gist uses domain and range specifications sparingly to keep properties broadly applicable, and — as a deliberate design decision — does not define inverse properties, to eliminate redundancy and reduce cognitive load ⟨semanticarts.com/gist⟩.
- Subclasses are typically defined by an OWL equivalent-class pattern specifying how they specialize their superclass (e.g., Account ≡ an Agreement having a balance) ⟨gist-doc WIDOCO 14.1.0, §Account⟩.
- gist is distributed free under the Creative Commons Attribution 4.0 International license; users must keep gist terms in the gist namespace (https://w3id.org/semanticarts/ns/ontology/gist/) and not define their own terms within it ⟨semanticarts.com/gist⟩.
- The core ontology is serialized as Turtle, RDF/XML, and JSON-LD, with supplementary ontologies of RDFS annotations and materialized subclass inferences to support varied reasoners ⟨semanticarts.com/gist⟩.
- The current release is 14.1.0 (April 2026), with version IRI https://w3id.org/semanticarts/ontology/gistCore14.1.0 ⟨gist-doc WIDOCO 14.1.0, §Overview⟩.

## Relations
- Realizes: [[upper-ontology]]
- Defined in: [[gist]]
- Published by: [[org-semantic-arts]]
- Related: [[gistbfo]] · [[gist-14-1-0]] · [[gist-14-0-0]]

## See also
[[upper-ontology]] [[gistbfo]]

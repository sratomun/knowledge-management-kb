---
title: "Upper Ontology"
type: concept
subtype: ontology-kind
aliases: ["foundational ontology", "top-level ontology"]
tags: [ontology-engineering]
related: ["[[top-level-ontology-categories]]", "[[semantic-interoperability]]"]
updated: 2026-08-10
---

# Upper Ontology

## What it is

An upper (or foundational, or top-level) ontology is a small, domain-independent set of the most general categories and relations — things like object, event, quality, agreement — on which more specialized domain and application ontologies are built. Its job is to supply a shared conceptual backbone so that independently developed vocabularies stay integrable and interoperable, rather than to model any particular subject matter itself.

## How sources treat it

- **[[gist]]** _(whitepaper · informational)_ — Positions gist as a minimalist upper (foundational) ontology for the enterprise, designed to give "maximum coverage of typical business concepts with the fewest number of primitives and the least amount of ambiguity," domain-independent and intended as a foundation for more specialized ontologies ⟨semanticarts.com/gist⟩
- **[[gist]]** _(whitepaper · informational)_ — Its primitives are deliberately everyday business concepts with ordinary names (person, organization, agreement) rather than philosophical abstractions such as endurant, perdurant, or qualia ⟨semanticarts.com/gist⟩
- **[[gist]]** _(whitepaper · informational)_ — Defines roughly 100 classes plus about as many properties, and offers a public bridge ontology, gistBFO, aligning gist with the Basic Formal Ontology ⟨gist-doc WIDOCO 14.1.0, §Overview⟩
- **[[bfo]]** _(standard · normative)_ — Describes BFO as "a small, upper level ontology that is designed for use in supporting information retrieval, analysis and integration in scientific and other domains," positioned as a "genuine upper ontology" — a domain-neutral, top-level ontology rather than a domain vocabulary ⟨basic-formal-ontology.org / Home⟩
- **[[bfo]]** _(standard · normative)_ — Because it is a genuine upper ontology, "it does not contain physical, chemical, biological or other terms which would properly fall within the coverage domains of the special sciences" ⟨basic-formal-ontology.org / Home⟩
- **[[bfo]]** _(standard · normative)_ — Is standardized as ISO/IEC 21838-2:2021, one of the "Top-level ontologies (TLO)," and is offered in both an OWL and a first-order-logic axiomatization ⟨basic-formal-ontology.org / fol.html⟩

## Where sources differ

The two sources share the core definition — a small, domain-neutral foundation that specialized ontologies extend — but differ sharply in orientation and idiom. [[gist]] is pragmatic and business-facing: it minimizes primitives, names them in ordinary business language (person, organization, agreement), and explicitly avoids philosophical categories like endurant/perdurant to reduce cognitive load. [[bfo]] is philosophically rigorous and scientifically oriented: it is grounded in a realist theory developed by Barry Smith and Pierre Grenon, carries a formal FOL axiomatization, is standardized through ISO/IEC, and targets scientific integration (its user base is heavily biomedical). The two are not framed as rivals in the corpus — gist ships gistBFO precisely to bridge the two.

## See also
[[top-level-ontology-categories]] · [[semantic-interoperability]]

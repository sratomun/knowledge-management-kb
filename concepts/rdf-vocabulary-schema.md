---
title: "RDF Vocabulary Schema"
type: concept
tags: [semantic-web]
related: ["[[rdf-vocabulary-namespace]]", "[[rdf-data-model]]", "[[entailment-equivalence]]", "[[description-logic]]", "[[constraint-validation]]"]
updated: 2026-08-10
---

# RDF Vocabulary Schema

## What it is
A lightweight data-modelling layer on top of RDF that lets one describe groups of related resources as classes, and the relationships between resources as properties, using terms that are themselves RDF. Rather than defining a class by the properties its instances may have, this style is property-centric: it describes properties in terms of the classes to which they apply, chiefly through domain and range statements, and adds sub-class / sub-property hierarchies as the basis for simple inference.

## How sources treat it
- **[[rdf-schema-11]]** _(standard · normative)_ — RDF Schema is a data-modelling vocabulary and a semantic extension of the basic RDF vocabulary, providing mechanisms for describing groups of related resources and the relationships between them, and is itself written in RDF using the terms it describes ⟨Abstract, §1⟩
- **[[rdf-schema-11]]** _(standard · normative)_ — the core vocabulary sits in the namespace conventionally prefixed `rdfs:` and identified by the IRI `http://www.w3.org/2000/01/rdf-schema#`, with `rdf:` used for `http://www.w3.org/1999/02/22-rdf-syntax-ns#` ⟨§1⟩
- **[[rdf-schema-11]]** _(standard · normative)_ — the design is property-centric: rather than defining a class by the properties its instances may have, it describes properties in terms of the classes of resource to which they apply, letting anyone extend the description of existing resources without re-defining them ⟨§1⟩
- **[[rdf-schema-11]]** _(standard · normative)_ — resources may be divided into classes whose members are their instances; classes are themselves resources, `rdf:type` states that a resource is an instance of a class, and each class has a class extension, so two classes may share all instances yet be distinct ⟨§2, §3.3⟩
- **[[rdf-schema-11]]** _(standard · normative)_ — `rdfs:range` "is used to state that the values of a property are instances of one or more classes"; where a property has more than one range, objects are instances of all stated classes ⟨§3.1⟩
- **[[rdf-schema-11]]** _(standard · normative)_ — `rdfs:domain` "is used to state that any resource that has a given property is an instance of one or more classes"; multiple domains conjoin so subjects are instances of all stated classes ⟨§3.2⟩
- **[[rdf-schema-11]]** _(standard · normative)_ — `rdfs:subClassOf` states that all instances of one class are instances of another and is transitive with domain and range both `rdfs:Class`; `rdfs:subPropertyOf` is likewise transitive over `rdf:Property`, and the specification "does not define a top property that is the super-property of all properties" ⟨§3.4, §3.5⟩
- **[[rdf-schema-11]]** _(standard · normative)_ — RDF Schema "provides a mechanism for describing this information, but does not say whether or how an application should use it": domain and range assertions are descriptive, and validators, editors, and reasoners may act on them differently ⟨§4⟩
- **[[rdf-schema-11]]** _(standard · normative)_ — the basic facilities of `rdfs:domain` and `rdfs:range` "do not provide any direct way to indicate property restrictions that are local to a class"; richer ontology languages such as OWL and inference-rule languages provide such direct support ⟨§3 NOTE, §1⟩

## Where sources differ
Only one source in this KB, the normative RDF Schema 1.1 Recommendation, treats the vocabulary-schema layer directly, so no cross-source disagreement is recorded here. The page notes internally that RDFS positions itself as a floor: it describes domain/range and sub-class/sub-property but leaves how applications act on those descriptions open, and explicitly points to OWL and rule languages for the class-local restrictions and richer constraints it does not provide ⟨rdf-schema-11 §4, §3 NOTE⟩.

## See also
[[rdf-vocabulary-namespace]] · [[description-logic]] · [[constraint-validation]] · [[entailment-equivalence]]

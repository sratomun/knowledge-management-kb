---
title: "RDF Schema 1.1"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["RDFS", "RDF Schema 1.1 (spec)"]
publisher: W3C
url: https://www.w3.org/TR/rdf-schema/
version: "1.1 (2014-02-25)"
published: 2014-02
effective_from: 2014-02-25
effective_to: ongoing
status: current
tags: [semantic-web]
updated: 2026-08-10
---

# RDF Schema 1.1

## Scope & purpose

RDF Schema provides a data-modelling vocabulary for RDF data and is a semantic extension of the basic RDF vocabulary. It supplies mechanisms for describing groups of related resources (classes) and the relationships between resources (properties), and is itself written in RDF using the terms it describes. Its class-and-property system resembles the type systems of object-oriented languages, but is property-centric: instead of defining a class by the properties its instances may have, RDF Schema describes properties in terms of the classes to which they apply, via the domain and range mechanisms. It is a W3C Recommendation (25 February 2014), an edited RDF 1.1 revision of the 2004 RDF Schema Recommendation with unchanged technical content; where it disagrees with the RDF Semantics specification [RDF11-MT], that specification is to be taken as correct.

## Structure

- §1 Introduction — purpose, property-centric approach, the `rdfs:` namespace (`http://www.w3.org/2000/01/rdf-schema#`) and `rdf:` namespace (`http://www.w3.org/1999/02/22-rdf-syntax-ns#`).
- §2 Classes — §2.1 rdfs:Resource, §2.2 rdfs:Class, §2.3 rdfs:Literal, §2.4 rdfs:Datatype, §2.5 rdf:langString, §2.6 rdf:HTML, §2.7 rdf:XMLLiteral, §2.8 rdf:Property.
- §3 Properties — §3.1 rdfs:range, §3.2 rdfs:domain, §3.3 rdf:type, §3.4 rdfs:subClassOf, §3.5 rdfs:subPropertyOf, §3.6 rdfs:label, §3.7 rdfs:comment.
- §4 Using the Domain and Range vocabulary (non-normative).
- §5 Other vocabulary — §5.1 Containers (rdfs:Container, rdf:Bag, rdf:Seq, rdf:Alt, rdfs:ContainerMembershipProperty, rdfs:member), §5.2 RDF Collections (rdf:List, rdf:first, rdf:rest, rdf:nil), §5.3 Reification (rdf:Statement, rdf:subject, rdf:predicate, rdf:object), §5.4 Utility properties (rdfs:seeAlso, rdfs:isDefinedBy, rdf:value).
- §6 RDF Schema summary — §6.1 RDF classes, §6.2 RDF properties.
- §A Acknowledgments; §B Changes since the 2004 Recommendation; §C References (normative / informative).

## Key points

- RDF Schema is a data-modelling vocabulary and a semantic extension of the basic RDF vocabulary; it provides mechanisms for describing groups of related resources and the relationships between them, and is written in RDF using the terms it describes ⟨Abstract, §1⟩.
- The core vocabulary sits in the namespace conventionally prefixed `rdfs:` and identified by the IRI `http://www.w3.org/2000/01/rdf-schema#`; the specification also uses the `rdf:` prefix for `http://www.w3.org/1999/02/22-rdf-syntax-ns#` ⟨§1⟩.
- The design is property-centric: rather than defining a class by the properties its instances may have, RDF Schema describes properties in terms of the classes of resource to which they apply, which lets anyone extend the description of existing resources without re-defining them ⟨§1⟩.
- Resources may be divided into classes; the members of a class are its instances; classes are themselves resources; `rdf:type` may be used to state that a resource is an instance of a class, and each class has a class extension (the set of its instances), so two classes may share all instances yet be distinct ⟨§2, §3.3⟩.
- `rdfs:Resource` is the class of everything: all things described by RDF are instances of it and all other classes are subclasses of it; `rdfs:Resource` is an instance of `rdfs:Class` ⟨§2.1⟩.
- `rdfs:Class` is the class of resources that are RDF classes and is an instance of itself; `rdf:Property` is the class of RDF properties and is an instance of `rdfs:Class` ⟨§2.2, §2.8⟩.
- `rdfs:Literal` is the class of literal values, an instance of `rdfs:Class` and a subclass of `rdfs:Resource`; `rdfs:Datatype` is the class of datatypes, both an instance of and a subclass of `rdfs:Class`, and each of its instances is a subclass of `rdfs:Literal` ⟨§2.3–2.4⟩.
- `rdfs:range` "is used to state that the values of a property are instances of one or more classes": in `P rdfs:range C`, objects of triples with predicate P are instances of C; where P has more than one range, objects are instances of all stated classes ⟨§3.1⟩.
- `rdfs:domain` "is used to state that any resource that has a given property is an instance of one or more classes": in `P rdfs:domain C`, subjects of triples with predicate P are instances of C; multiple domains conjoin (subjects are instances of all stated classes) ⟨§3.2⟩.
- `rdfs:subClassOf` is used to state that all the instances of one class are instances of another; `C1 rdfs:subClassOf C2` makes C1 a subclass of C2; the property is transitive, and its domain and range are both `rdfs:Class` ⟨§3.4⟩.
- `rdfs:subPropertyOf` is used to state that all resources related by one property are also related by another; it is transitive, with domain and range `rdf:Property`; the specification "does not define a top property that is the super-property of all properties" ⟨§3.5⟩.
- `rdf:type` states that a resource is an instance of a class (domain `rdfs:Resource`, range `rdfs:Class`); `rdfs:subClassOf`/`rdfs:subPropertyOf`, `rdfs:domain` and `rdfs:range` together form the core inference vocabulary ⟨§3.3⟩.
- `rdfs:label` "may be used to provide a human-readable version of a resource's name" and `rdfs:comment` "may be used to provide a human-readable description of a resource"; both have domain `rdfs:Resource` and range `rdfs:Literal`, and support multilingual values via RDF language tagging ⟨§3.6–3.7⟩.
- RDF Schema "provides a mechanism for describing this information, but does not say whether or how an application should use it": domain and range assertions are descriptive, and different applications (validators, editors, reasoners) may act on them differently ⟨§4⟩.
- The basic facilities of `rdfs:domain` and `rdfs:range` "do not provide any direct way to indicate property restrictions that are local to a class"; richer ontology languages such as OWL, inference-rule languages, and other formalisms provide such direct support ⟨§3 NOTE, §1⟩.
- Non-normative "other vocabulary" (§5) supplies container classes (`rdfs:Container`, `rdf:Bag`, `rdf:Seq`, `rdf:Alt`, `rdfs:ContainerMembershipProperty`, `rdfs:member`), collection terms (`rdf:List`, `rdf:first`, `rdf:rest`, `rdf:nil`), a reification vocabulary (`rdf:Statement`, `rdf:subject`, `rdf:predicate`, `rdf:object`), and utility properties (`rdfs:seeAlso`, `rdfs:isDefinedBy`, `rdf:value`) ⟨§5⟩.

## Concepts & entities covered

Concepts: [[rdf-vocabulary-schema]] · [[rdf-data-model]] · [[rdf-vocabulary-namespace]] · [[literal-datatyping]]

Entities: [[rdfs-class]] · [[rdfs-resource]] · [[rdfs-literal]] · [[rdfs-datatype]] · [[rdfs-subclassof]] · [[rdfs-subpropertyof]] · [[rdfs-domain]] · [[rdfs-range]] · [[rdfs-label]] · [[rdfs-comment]] · [[rdfs-type]] · [[rdfs-property]]

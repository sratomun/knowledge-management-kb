---
title: "PROV-O: The PROV Ontology"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["PROV-O", "PROV Ontology"]
publisher: W3C
url: https://www.w3.org/TR/prov-o/
version: "1.0"
published: 2013-04
effective_from: 2013-04-30
effective_to: ongoing
status: current
tags: [semantic-web, governance]
updated: 2026-08-09
---

# PROV-O: The PROV Ontology

## Scope & purpose

PROV-O is the W3C Recommendation (30 April 2013) that expresses the PROV Data Model (PROV-DM) using the OWL2 Web Ontology Language, providing a set of classes, properties, and restrictions to represent and interchange provenance information generated in different systems and under different contexts ⟨Abstract⟩. It can be specialized to create new classes and properties for modeling provenance in different applications and domains ⟨Abstract⟩. The namespace for all PROV-O terms is `http://www.w3.org/ns/prov#` ⟨Abstract⟩. It is a lightweight ontology that, with the exception of five axioms, conforms to the OWL-RL profile ⟨§1⟩. Together with PROV-AQ and PROV-DM it forms a framework for provenance information interchange in domain-specific Web-based applications ⟨§1⟩. The normative sections are 1.1, 1.2, 3, 4, and Appendix B ⟨§1.1⟩.

## Structure

PROV-O terms are grouped into three incremental categories, described in Section 3 (The PROV-O Ontology Description) and cross-referenced in Section 4:

- **Starting Point Terms** (§3.1 / §4.1) — the small set of classes and properties providing the basis for the rest of the ontology: `prov:Entity`, `prov:Activity`, `prov:Agent`; and the properties `prov:wasGeneratedBy`, `prov:used`, `prov:wasInformedBy`, `prov:wasDerivedFrom`, `prov:wasAttributedTo`, `prov:wasAssociatedWith`, `prov:actedOnBehalfOf`, `prov:startedAtTime`, `prov:endedAtTime` ⟨§2⟩⟨§3.1⟩.
- **Expanded Terms** (§3.2 / §4.2) — additional terms relating the starting-point classes: subclasses of Agent (`prov:Person`, `prov:Organization`, `prov:SoftwareAgent`) and of Entity (`prov:Collection`, `prov:Bundle`, `prov:Plan`); the superproperty `prov:wasInfluencedBy`; derivation subproperties `prov:wasQuotedFrom`, `prov:wasRevisionOf`, `prov:hadPrimarySource`; abstraction links `prov:specializationOf`, `prov:alternateOf`; and lifetime/location terms (`prov:generatedAtTime`, `prov:invalidatedAtTime`, `prov:wasInvalidatedBy`, `prov:wasStartedBy`, `prov:wasEndedBy`, `prov:atLocation`, `prov:hadMember`, `prov:value`, etc.) ⟨§2⟩⟨§3.2⟩.
- **Qualified Terms** (§3.3 / §4.3) — the result of applying the Qualification Pattern to the unqualified relations, using an intermediate influence class annotated with additional attributes: classes such as `prov:Influence`, `prov:Generation`, `prov:Usage`, `prov:Derivation`, `prov:Association`, `prov:Attribution`, `prov:Communication`, `prov:Delegation`, `prov:Start`, `prov:End`, `prov:Invalidation`, `prov:Revision`, `prov:Quotation`, `prov:PrimarySource`, `prov:Plan`, `prov:Role`, `prov:InstantaneousEvent`; and qualification properties such as `prov:qualifiedGeneration`, `prov:qualifiedUsage`, `prov:qualifiedAssociation`, etc. ⟨§2⟩⟨§3.3⟩.

## Key points

- An `prov:Entity` is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary ⟨§3.1⟩.
- An `prov:Activity` is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities ⟨§3.1⟩.
- An `prov:Agent` is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity ⟨§3.1⟩.
- Activities start and end at particular points in time (`prov:startedAtTime`, `prov:endedAtTime`) and during their lifespan can use and generate entities (`prov:used`, `prov:wasGeneratedBy`) ⟨§3.1⟩.
- An Activity `prov:wasInformedBy` another Activity to provide dependency information without explicitly providing start and end times, allowing provenance chains comprising only Activities ⟨§3.1⟩.
- A derivation is a transformation of one entity into another; provenance chains comprising only Entities can be formed using `prov:wasDerivedFrom` ⟨§3.1⟩.
- An Agent's responsibility for an Activity or Entity is described using `prov:wasAssociatedWith` and `prov:wasAttributedTo`, respectively; in delegation the influencing Agent `prov:actedOnBehalfOf` another Agent that also bears responsibility ⟨§3.1⟩.
- A `prov:Collection` is an Entity that provides a structure (e.g. set, list) to some constituents which are themselves Entities; `prov:hadMember` asserts membership in a collection ⟨§3.2⟩.
- A `prov:Bundle` is a named set of provenance descriptions, which may itself have provenance; a Bundle of PROV-O assertions is an abstract set of RDF triples, and adding or removing a triple creates a new distinct Bundle ⟨§3.2⟩.
- A `prov:Plan` is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals ⟨§3.2⟩.
- `prov:wasInfluencedBy` is a superproperty that relates any influenced Entity, Activity, or Agent to any other influencing Entity, Activity, or Agent that had an effect on its characteristics ⟨§3.2⟩.
- `prov:wasQuotedFrom` cites a potentially larger Entity from which a new Entity was created by repeating some or all of the original; `prov:wasRevisionOf` indicates the derived Entity contains substantial content from the original; `prov:hadPrimarySource` cites a preceding Entity produced by some agent with direct experience and knowledge about the topic ⟨§3.2⟩.
- `prov:specializationOf` links a more specific Entity to a more general one, while `prov:alternateOf` links Entities that present aspects of the same thing but not necessarily the same aspects or at the same time ⟨§3.2⟩.
- The Qualified Terms category is the result of applying the Qualification Pattern to the simple (unqualified) relations; the Qualification Pattern restates an unqualified influence relation using an intermediate class that represents the influence between two resources, which can then be annotated with additional descriptions ⟨§3.3⟩.
- Seven Starting Point relations and seven Expanded relations can be further described using the Qualification Pattern, per the normative Tables 2 and 3 ⟨§3.3⟩.
- All influence classes (e.g. `prov:Association`, `prov:Usage`) are extensions of `prov:Influence` and either `prov:EntityInfluence`, `prov:ActivityInfluence`, or `prov:AgentInfluence`, which determine the property used to cite the influencing resource (`prov:entity`, `prov:activity`, or `prov:agent`, respectively); the most specific subclasses should be used when applicable ⟨§3.3⟩.
- Consuming applications should recognize both qualified and unqualified forms, and treat the qualified form as implying the unqualified form; because the qualified form is more verbose, the unqualified form should be favored where additional properties are not provided ⟨§3.3⟩.
- The `prov:atTime` property can be used to describe any `prov:InstantaneousEvent` (including `prov:Start`, `prov:Generation`, `prov:Usage`, `prov:Invalidation`, and `prov:End`) ⟨§3.3⟩.

## Concepts & entities covered
Concepts: [[provenance]] · [[provenance-influence]] · [[derivation]] · [[qualification-pattern]]
Entities: [[prov-entity]] · [[prov-activity]] · [[prov-agent]] · [[prov-wasgeneratedby]] · [[prov-used]] · [[prov-wasderivedfrom]] · [[prov-wasattributedto]] · [[prov-wasassociatedwith]] · [[prov-wasinformedby]] · [[prov-actedonbehalfof]] · [[prov-bundle]] · [[prov-collection]] · [[prov-wasrevisionof]] · [[prov-wasquotedfrom]] · [[prov-hadprimarysource]] · [[prov-specializationof]] · [[prov-alternateof]] · [[prov-plan]] · [[prov-influence]] · [[prov-generation]] · [[prov-usage]] · [[prov-derivation]] · [[prov-association]] · [[prov-attribution]]

---
title: "JSON-LD 1.1"
type: source
kind: standard
authority: normative
subtype: w3c-recommendation
aliases: ["JSON-LD", "JSON-LD 1.1"]
publisher: W3C
url: https://www.w3.org/TR/json-ld11/
version: "1.1"
published: 2020-07
effective_from: 2020-07-16
effective_to: ongoing
status: current
tags: [semantic-web]
updated: 2026-08-09
---
# JSON-LD 1.1

## Scope & purpose

JSON-LD 1.1 is a W3C Recommendation (16 July 2020) defining a JSON-based syntax to
serialize Linked Data. It is designed to integrate into deployed systems already using
JSON and to provide a smooth upgrade path from plain JSON to Linked Data, letting existing
JSON be interpreted as Linked Data with minimal change. It adds to JSON a universal
identifier mechanism (IRIs), a `@context` mechanism for disambiguating keys, remote
references, language annotation, datatyping, and expression of one or more directed
graphs. It is one of three JSON-LD 1.1 Recommendations from the JSON-LD Working Group
(this Syntax document, the Processing Algorithms and API, and Framing), and supersedes
JSON-LD 1.0 (2014) while remaining a superset compatible with it. The document is
descriptive of a serialization format; it does not rank or adjudicate usage.

## Structure

- §1 Introduction — design goals, data model overview, syntax tokens and keywords (§1.4 Terminology, §1.5 Design Goals, §1.6 Data Model Overview, §1.7 Syntax Tokens and Keywords)
- §2 Conformance — BCP 14 modality, namespace prefixes used
- §3 Basic Concepts — the context (§3.1), IRIs (§3.2), node identifiers (§3.3), uses of JSON objects (§3.4), specifying the type (§3.5)
- §4 Advanced Concepts — advanced context usage (§4.1: processing mode, default vocabulary, base IRI, compact IRIs, aliasing keywords, scoped/imported contexts, protected terms), describing values (§4.2: typed values, JSON literals, type coercion, string internationalization), value ordering/lists/sets (§4.3), nested properties (§4.4), embedding (§4.5), indexed values (§4.6), included nodes (§4.7), reverse properties (§4.8), named graphs (§4.9), loading documents (§4.10)
- §5 Forms of JSON-LD — expanded (§5.1), compacted (§5.2), flattened (§5.3), framed (§5.4)
- §6 Modifying Behavior with Link Relationships — interpreting JSON as JSON-LD (§6.1), alternate document location (§6.2)
- §7 Embedding JSON-LD in HTML Documents (§7.1–§7.3)
- §8 Data Model
- §9 JSON-LD Grammar — terms, node/frame/graph/value objects, language/index/id/type maps, included blocks, property nesting, context definitions (§9.15), keywords (§9.16)
- §10 Relationship to RDF — serializing/deserializing (§10.1), the rdf:JSON datatype (§10.2), the i18n namespace (§10.3), rdf:CompoundLiteral (§10.4)
- §11 Security Considerations; §12 Privacy Considerations; §13 Internationalization Considerations
- Appendices A–J — image descriptions, relationship to other Linked Data formats (Turtle, RDFa, Microdata) (§B), IANA considerations (§C), open issues (§D), changes (§E–§H), acknowledgements (§I), references (§J)

## Key points

- JSON-LD is a lightweight syntax to serialize Linked Data in JSON; its design allows existing JSON to be interpreted as Linked Data with minimal changes ⟨§1⟩.
- A JSON-LD document is always a valid JSON document, ensuring standard JSON libraries work with it (Compatibility design goal) ⟨§1.5⟩.
- A context maps terms to IRIs; it is introduced with the `@context` key and may appear within a node object or a value object, and may be embedded or referenced by URL ⟨§3.1⟩.
- The key words MAY, MUST, MUST NOT, RECOMMENDED, SHOULD, and SHOULD NOT are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals ⟨§2⟩.
- A JSON-LD document serializes an RDF Dataset, a collection of graphs comprising exactly one default graph and zero or more named graphs; the default graph does not have a name and MAY be empty ⟨§8⟩.
- Each named graph is a pair of a graph name (IRI or blank node identifier) and a graph; whenever practical, the graph name SHOULD be an IRI, and a directed-arc SHOULD be labeled with an IRI ⟨§8⟩.
- JSON-LD is a concrete RDF syntax; a JSON-LD document is both an RDF document and a JSON document, and JSON-LD extends the RDF data model to optionally serialize generalized RDF Datasets (properties may be IRIs or blank nodes) ⟨§10⟩.
- New features defined in JSON-LD 1.1 are available unless the processing mode is set to `json-ld-1.0`; setting the processing mode explicitly to `json-ld-1.1` is RECOMMENDED to prevent a 1.0 processor from producing different results ⟨§4.1.1⟩.
- Each JSON-LD keyword except `@context` MAY be aliased to an application-specific keyword to reuse existing JSON keys; all keys, keywords, and values in JSON-LD are case-sensitive ⟨§1.7⟩.
- In JSON-LD 1.1 a term may be used as a compact IRI prefix when expanding or compacting only if a simple term definition ends with a URI gen-delim character, or its expanded term definition contains a `@prefix` entry with value true ⟨§4.1.5⟩.
- The value of the `@reverse` key MUST be an IRI reference or a compact IRI (including blank node identifiers); `@reverse` MAY be aliased and MAY be used as a key in a node object ⟨§9.16⟩.
- A JSON literal is a literal whose datatype IRI is `rdf:JSON` (`http://www.w3.org/1999/02/22-rdf-syntax-ns#JSON`), represented in a value object with `@type` set to `@json`; its lexical space is UNICODE strings conforming to the JSON Grammar of [RFC8259] ⟨§10.2⟩.
- Expansion applies a context so that all IRIs, types, and values are expanded and the `@context` is no longer necessary; flattening collects all properties of a node into a single map and labels all blank nodes ⟨§5.1⟩ ⟨§5.3⟩.
- Framing shapes data using an example frame document that both matches the flattened data and shows how the resulting data should be shaped, per the JSON-LD 1.1 Framing specification ⟨§5.4⟩.
- Ordinary JSON can be interpreted as JSON-LD by providing an explicit context, e.g. referencing a context document via an HTTP Link Header, without changing the document ⟨§6.1⟩.
- JSON-LD can be embedded in HTML by placing it in a `script` element with `type` attribute set to `application/ld+json`, creating a data block ⟨§7⟩.

## Concepts & entities covered
Concepts: [[linked-data-serialization]] · [[iri-identity]] · [[rdf-dataset]] · [[rdf-data-model]]
Entities: [[jsonld-context]] · [[jsonld-id]] · [[jsonld-type]] · [[jsonld-value]] · [[jsonld-graph]] · [[jsonld-list]] · [[jsonld-set]] · [[jsonld-reverse]] · [[jsonld-container]] · [[jsonld-vocab]] · [[jsonld-base]] · [[jsonld-language]] · [[jsonld-nest]] · [[jsonld-json]] · [[jsonld-import]] · [[jsonld-protected]] · [[jsonld-expanded-form]] · [[jsonld-compacted-form]] · [[jsonld-flattened-form]] · [[jsonld-framed-form]] · [[jsonld-10]] · [[jsonld-rdf-json]]

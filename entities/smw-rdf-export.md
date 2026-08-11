---
title: "SMW RDF/OWL export"
type: entity
subtype: technique
aliases: []
tags: [semantic-wiki]
concepts: ["[[semantic-wiki]]", "[[structured-knowledge-base]]"]
sources: ["[[semantic-mediawiki]]"]
updated: 2026-08-10
---

# SMW RDF/OWL export

## What it is
SMW RDF/OWL export is Semantic MediaWiki's capability to serialize the data annotated
in wiki pages as Semantic Web formats (RDF/OWL), so external systems can consume the
wiki's knowledge as linked data. [gen: the specific RDF/OWL serialization and OWL
vocabulary mapping are documented on the Help namespace, which was unreachable at
capture; the homepage confirms export/publication "via the Semantic Web".]

## Key facts
- All data created within Semantic MediaWiki can easily be exported or published via the Semantic Web, allowing other systems to use this data seamlessly ⟨smw: homepage/intro⟩
- The export renders wiki annotations as RDF/OWL, mapping SMW properties and their typed values into a Semantic Web vocabulary [gen: RDF/OWL specifics from general SMW knowledge; homepage confirms Semantic Web export] ⟨smw: homepage/intro (Semantic Web export) · [gen] RDF/OWL detail not on captured homepage⟩
- Export turns the wiki into a data source for other systems, supporting interoperability beyond human reading ⟨smw: homepage/intro⟩

## Relations
- Realizes: [[structured-knowledge-base]]
- Defined in: [[semantic-mediawiki]]
- Maintained by: [[org-smw-project]]
- Related: [[smw-property]]

## See also
[[semantic-wiki]]

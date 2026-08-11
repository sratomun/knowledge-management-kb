---
title: "Syntax encoding scheme"
type: concept
aliases: []
tags: [metadata]
related: ["[[vocabulary-encoding-scheme]]", "[[descriptive-metadata]]", "[[value-domain]]"]
updated: 2026-08-09
---

# Syntax encoding scheme

## What it is
A syntax encoding scheme (SES) specifies the datatype or string syntax that a metadata value must follow — for example, an ISO 8601 date, an IETF language tag, or a URI. Where a vocabulary encoding scheme names *which controlled set* a value comes from, a syntax encoding scheme fixes *how the value is formatted*, so that values are machine-parseable and unambiguous.

## How sources treat it
- **[[dcmi-terms]]** _(standard · normative)_ — Syntax Encoding Schemes (datatypes) specify value syntaxes: Box, ISO3166, ISO639-2, ISO639-3, Period, Point, RFC1766, RFC3066, RFC4646, RFC5646, URI, W3CDTF ⟨§5 Syntax Encoding Schemes⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — Successive language-tag RFCs are cross-linked by supersession: RFC 5646 obsoletes RFC 4646, which obsoletes RFC 3066, which obsoleted RFC 1766 ⟨§5 Syntax Encoding Schemes⟩.
- **[[dcmi-terms]]** _(standard · normative)_ — Recommended practice points property values at datatype syntaxes such as ISO 8601 / W3CDTF / EDTF for dates and ISO 639 / BCP 47 for language ⟨§2 Properties in /terms/⟩.

## Where sources differ
Only DCMI Terms, among the specifications sourced for this concept, defines the syntax-encoding-scheme construct by name, so there is no cross-source divergence to report. DCMI itself keeps the syntax encoding scheme (a value's datatype/format) distinct from the vocabulary encoding scheme (the controlled vocabulary a value is drawn from) ⟨§5 Syntax Encoding Schemes⟩⟨§4 Vocabulary Encoding Schemes⟩.

## See also
[[vocabulary-encoding-scheme]] · [[descriptive-metadata]] · [[value-domain]]

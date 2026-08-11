---
title: "Reading Order Reconstruction"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[document-layout-analysis]]", "[[document-parsing]]"]
updated: 2026-08-10
---

# Reading Order Reconstruction

## What it is
Reading order reconstruction is the determination of the sequence in which a document's detected blocks should be read, recovering the linear narrative flow from a spatial arrangement of regions. It matters most for multi-column, richly formatted, or interleaved layouts, where naive top-to-bottom or left-to-right extraction scrambles meaning; it typically consumes the output of layout analysis.

## How sources treat it
- **[[docling]]** _(provider-doc · vendor)_ — The final assembly stage aggregates all per-page predictions into a well-defined datatype, and a post-processing model augments features via language detection, reading-order correction, figure–caption matching, and metadata labelling ⟨tech report §3.3⟩
- **[[document-parsing-rag-omdena]]** _(blog · practitioner)_ — Describes reconstructing reading flow in multi-column layouts as clustering text blocks by spatial coordinates, identifying column regions, ordering blocks top-to-bottom within each column, and merging columns in correct sequence, calling accurate reading order essential to preserve meaning ⟨Omdena, Reconstructing reading flow⟩

## Where sources differ
The two sources are complementary and do not conflict. [[docling]] places reading-order correction inside a post-processing model that runs after per-page prediction, treating it as one augmentation among several; [[document-parsing-rag-omdena]] gives an algorithmic sketch specific to multi-column layouts (cluster by coordinates, order within columns, merge columns) and frames accurate reading order as essential to preserving meaning. One is a pipeline placement, the other a method description.

## See also
[[document-layout-analysis]] · [[document-parsing]] · [[layout-aware-parsing]]

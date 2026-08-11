---
title: <Entity name>
type: entity
subtype: <emergent — e.g. regulation-article, vendor-product, organization, control, standard-edition>
aliases: [<alt name>, <identifier>]
tags: [<domain>]
# temporal — fill when the entity's referent is time-bound (e.g. a control edition)
published: <YYYY-MM or empty>
effective_from: <YYYY-MM-DD or empty>
effective_to: <YYYY-MM-DD or ongoing>
supersedes: [[<entity>]]
superseded_by: [[<entity>]]
status: <current | superseded | draft>   # derived from dates/links, convenience only
# relations
concepts: [[<concept>]]
sources: [[<source-id>]]
updated: <YYYY-MM-DD>
---

# <Entity name>

## What it is
<What this named thing is — a specific regulation article, product, org, control,
or standard edition. 1–3 sentences.>

## Key facts
<Cited facts about the entity. Preserve modality verbatim for normative referents.>

- <fact> ⟨§<clause> / Art. <n> / <url>⟩

## Relations
- Realizes / relates to: [[<concept>]]
- Defined in: [[<source-id>]]
- Supersession: supersedes [[<entity>]] · superseded by [[<entity>]]

## See also
[[<related-entity>]]

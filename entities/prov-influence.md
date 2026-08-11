---
title: "prov:Influence"
type: entity
subtype: vocabulary-term
aliases: []
tags: [metadata]
concepts: ["[[provenance-influence]]", "[[qualification-pattern]]"]
sources: ["[[prov-o]]"]
updated: 2026-08-09
---

# prov:Influence

## What it is
A Qualified term: the broad root class from which all qualified influence classes extend, representing the capacity of one thing to have an effect on another.

## Key facts
- "All influence classes (e.g. prov:Association, prov:Usage) are extensions of prov:Influence and either prov:EntityInfluence, prov:ActivityInfluence, or prov:AgentInfluence, which determine the property used to cite the influencing resource (either prov:entity, prov:activity, or prov:agent, respectively)." ⟨§3.3⟩
- "Because prov:Influence is a broad relation, its most specific subclasses (e.g. prov:Communication, prov:Delegation, prov:End, prov:Revision, etc.) should be used when applicable." ⟨§3.3⟩
- Qualifies prov:wasInfluencedBy via prov:qualifiedInfluence, with the influencer cited by prov:influencer. ⟨§3.3 Table 3⟩

## Relations
- Realizes: [[provenance-influence]]
- Defined in: [[prov-o]]
- Related: [[prov-generation]], [[prov-usage]], [[prov-derivation]], [[prov-association]], [[prov-attribution]]

## See also
[[qualification-pattern]] [[provenance-influence]]

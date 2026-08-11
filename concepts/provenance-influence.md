---
title: "Provenance influence"
type: concept
aliases: []
tags: [governance]
related: ["[[provenance]]", "[[derivation]]", "[[qualification-pattern]]"]
updated: 2026-08-09
---

# Provenance influence

## What it is
Influence is the most general provenance relation: the fact that one entity, activity, or agent had some effect on the character of another, without yet saying exactly how. It is the common root under which more specific provenance relations — generation, usage, derivation, attribution, association, and so on — are organized.

## How sources treat it
- **[[prov-o]]** _(standard · normative)_ — `prov:wasInfluencedBy` is a superproperty that relates any influenced Entity, Activity, or Agent to any other influencing Entity, Activity, or Agent that had an effect on its characteristics ⟨§3.2⟩.
- **[[prov-o]]** _(standard · normative)_ — All influence classes (e.g. `prov:Association`, `prov:Usage`) are extensions of `prov:Influence` and of one of `prov:EntityInfluence`, `prov:ActivityInfluence`, or `prov:AgentInfluence`, which determine whether the influencing resource is cited with `prov:entity`, `prov:activity`, or `prov:agent`; the most specific subclasses should be used when applicable ⟨§3.3⟩.
- **[[prov-o]]** _(standard · normative)_ — The Qualification Pattern restates an unqualified influence relation using an intermediate class that represents the influence between two resources, which can then be annotated with additional descriptions ⟨§3.3⟩.

## Where sources differ
Only PROV-O is sourced for this concept, so there is no cross-source divergence to report. Within PROV-O, `prov:wasInfluencedBy` is deliberately broad — the specification notes that more specific subproperties should be used when applicable rather than the generic influence relation ⟨§3.3⟩.

## See also
[[provenance]] · [[derivation]] · [[qualification-pattern]]

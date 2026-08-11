---
title: "First-Order Rewritability"
type: concept
tags: [obda]
aliases: ["FO-rewritability"]
related: ["[[query-rewriting]]", "[[ontology-based-data-access]]", "[[query-unfolding]]"]
updated: 2026-08-09
---

# First-Order Rewritability

## What it is
A property of an ontology language guaranteeing that answering a query over the ontology can always be reduced to evaluating a first-order (equivalently, SQL) query over the raw data alone. When a language is first-order rewritable, ontology reasoning can be compiled entirely into query rewriting, so the data source's relational engine does the work and data complexity stays very low.

## How sources treat it
- **[[xiao-obda-survey]]** _(article · informational)_ — ontologies are expressed in lightweight description logics of the DL-Lite family, which underpin the OWL 2 QL profile ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — DL-Lite / OWL 2 QL is deliberately restricted so that conjunctive query answering is first-order (FO) rewritable, keeping data complexity in AC0 ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[xiao-obda-survey]]** _(article · informational)_ — open challenges include richer ontology languages beyond FO-rewritable fragments, handling of aggregation and analytics, updates, and mapping management ⟨IJCAI 2018, pp. 5511-5519⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — first-order rewritability is defined as the possibility of rewriting a query q and TBox T into a single first-order query q′ that returns the certain answers to q over (T, A) for every ABox A, which ensures query answering is in AC0 for data complexity ⟨Remark 3.1⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — FO-rewritability is fragile: it is lost when the UNA is dropped and equality (sameAs) is allowed (complexity rises to LogSpace-completeness) and when role transitivity constraints are added (data complexity becomes NLogSpace-hard) ⟨§1, Remark 3.1, §5.4, §8⟩
- **[[dl-lite-short-course]]** _(article · informational)_ — the one-variable first-order embedding of the DL-Lite logics is what links each variant's reasoning complexity to known descriptive-complexity results and thus determines whether it stays first-order rewritable ⟨§1⟩

## Where sources differ
Both cited sources present first-order rewritability as the property that motivates the DL-Lite / OWL 2 QL restriction, enabling rewriting-based query answering in AC0 data complexity ⟨xiao-obda-survey — IJCAI 2018, pp. 5511-5519⟩ ⟨dl-lite-short-course Remark 3.1⟩. The survey treats it as a design target and boundary for future extension ⟨xiao-obda-survey — IJCAI 2018, pp. 5511-5519⟩; the DL-Lite family paper maps the boundary precisely, showing which combinations of constructs (role inclusions with number restrictions, dropping the UNA with equality, transitivity) push a logic out of the AC0 / FO-rewritable region ⟨dl-lite-short-course §1, §9⟩.

## See also
[[query-rewriting]] · [[ontology-based-data-access]] · [[query-unfolding]]

---
title: "rr:R2RMLView"
type: entity
subtype: vocabulary-term
aliases: ["R2RML view"]
tags: [obda]
concepts: ["[[logical-source-abstraction]]"]
sources: ["[[r2rml]]"]
updated: 2026-08-09
---

# rr:R2RMLView

## What it is
The R2RML vocabulary class for a logical table whose contents are the result of a SQL query supplied in the mapping. It emulates a SQL view for transformation, computation, or filtering without modifying the input database.

## Key facts
- An R2RML view is represented by a resource that has exactly one rr:sqlQuery property, whose value is a literal with a lexical form that is a valid SQL query ⟨§5.2⟩
- The result of the query execution MUST NOT have duplicate column names; columns derived by projecting an expression SHOULD be named ⟨§5.2⟩
- An R2RML view MAY have one or more SQL version identifiers, represented as values of the rr:sqlVersion property; unlike real SQL views it can not be used as an input table in further SQL queries ⟨§5.2⟩

## Relations
- Realizes: [[logical-source-abstraction]]
- Defined in: [[r2rml]]
- Related: [[r2rml-logicaltable]], [[r2rml-sql2008]], [[r2rml-inverseexpression]]

## See also
[[r2rml-basetableorview]] · [[org-w3c]]

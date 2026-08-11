---
title: "Logical Source Abstraction"
type: concept
tags: [semantic-web]
related: ["[[reference-formulation]]", "[[rdb-to-rdf-mapping]]", "[[term-map]]"]
updated: 2026-08-09
---

# Logical Source Abstraction

## What it is
The indirection layer in a mapping that names the input data a set of mapping rules draws from, decoupling the rules from the physical source. In relational mapping this is a "logical table" (a base table, a view, or a SQL query); in the generalized case it is a "logical source" that points at a data source together with how to iterate over it, so the same rule structure can target many source formats.

## How sources treat it
- **[[r2rml]]** _(standard · normative)_ — a logical table is a SQL base table or view (represented by exactly one rr:tableName) or an R2RML view; every logical table has an effective SQL query, and for a base table that query is SELECT * FROM {table} ⟨§5.1⟩
- **[[r2rml]]** _(standard · normative)_ — an R2RML view has exactly one rr:sqlQuery whose value is a valid SQL SELECT query; the result MUST NOT have duplicate column names, projected-expression columns SHOULD be named, and the view MAY carry one or more rr:sqlVersion identifiers ⟨§5.2⟩
- **[[r2rml]]** _(standard · normative)_ — a triples map MUST have exactly one rr:logicalTable and exactly one subject map ⟨§6⟩
- **[[rml]]** _(standard · normative)_ — a logical source (rml:LogicalSource) extends R2RML's logical table; it must be a base source (rml:BaseSource) pointing to the data to be mapped ⟨§3, §4, §4.1⟩
- **[[rml]]** _(standard · normative)_ — a base source is a resource with exactly one rml:source, exactly one logical iterator rml:iterator, and zero or one rml:referenceFormulation — this replaces R2RML's database-only table/query addressing ⟨§4.1⟩

## Where sources differ
R2RML's abstraction is the logical table, addressed through a SQL table name or an R2RML view's SQL SELECT query, with an effective SQL query behind every logical table ⟨r2rml §5.1⟩. RML defines the logical source as an extension of the logical table, and represents R2RML's rr:BaseTableOrView as a subclass of rml:BaseSource ⟨rml §2, §3⟩. Where R2RML iterates rows only, RML's base source carries an explicit rml:iterator and an optional rml:referenceFormulation so the abstraction can address CSV records, XML elements, or JSON objects, not just database rows ⟨rml §4.1⟩.

## See also
[[reference-formulation]] · [[rdb-to-rdf-mapping]] · [[term-map]]

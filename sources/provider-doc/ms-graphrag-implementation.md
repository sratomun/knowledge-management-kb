---
title: "microsoft/graphrag — GraphRAG Implementation"
type: source
kind: provider-doc
authority: vendor
subtype: system
aliases: ["microsoft/graphrag repository"]
publisher: "Microsoft Research"
tags: [graph-rag]
url: https://github.com/microsoft/graphrag
published: 2024
effective_from: 2024-01
effective_to: ongoing
status: current
updated: 2026-08-10
---

# microsoft/graphrag — GraphRAG Implementation

## Scope & purpose
microsoft/graphrag is the open-source implementation of GraphRAG published by Microsoft
Research: a data pipeline and transformation suite that uses LLMs to extract structured
data from unstructured text and to build knowledge-graph memory structures that enhance
an LLM's ability to reason over a private dataset. This page captures the repository's
README and its Responsible AI (RAI) transparency FAQ, which describe the system's
intended use, evaluation, and limitations. The repository is presented as a demonstration
methodology and is explicitly not an officially supported Microsoft offering.

## Structure
The captured material has two parts. The README covers the project overview, quickstart,
repository guidance, prompt tuning, and versioning/migration guidance. The
RAI_TRANSPARENCY.md ("Responsible AI FAQ") is a Q&A document covering what GraphRAG is and
can do, its intended uses, how it was evaluated (metrics), its limitations, and the
operational factors and settings for effective and responsible use. External pointers
include the Microsoft Research blog post, the hosted docs (microsoft.github.io/graphrag),
and the GraphRAG arXiv paper (arxiv.org/pdf/2404.16130).

## Key points
- GraphRAG is described as a data pipeline and transformation suite that extracts meaningful, structured data from unstructured text using the power of LLMs ⟨README, Overview⟩.
- The repository presents a methodology for using knowledge-graph memory structures to enhance LLM outputs, and states the provided code is a demonstration and not an officially supported Microsoft offering ⟨README, Repository Guidance⟩.
- ⚠️ WARNING: GraphRAG indexing can be an expensive operation; the README instructs users to read all documentation to understand the process and costs involved, and to start small ⟨README, Repository Guidance⟩.
- Using GraphRAG out of the box may not yield the best results, and Microsoft strongly recommends fine-tuning prompts by following the Prompt Tuning Guide ⟨README, Prompt Tuning⟩.
- Users should run `graphrag init --root [path] --force` between minor version bumps to get the latest config format, and run the provided migration notebook between major version bumps to avoid re-indexing prior datasets ⟨README, Versioning⟩.
- GraphRAG is an AI-based content interpretation and search capability that uses LLMs to parse data into a knowledge graph and answer user questions about a user-provided private dataset ⟨RAI FAQ, What is GraphRAG⟩.
- It can connect information across large volumes of data to answer questions whose answers span many documents, as well as thematic questions such as "what are the top themes in this dataset?", which are difficult or impossible for keyword and vector-based search ⟨RAI FAQ, What can GraphRAG do⟩.
- Intended use is critical information discovery and analysis where the needed insight spans many documents, is noisy, or is mixed with mis/disinformation, and where questions are more abstract or thematic than the underlying data can directly answer ⟨RAI FAQ, Intended uses⟩.
- GraphRAG is designed for users already trained in responsible analytic approaches; human analysis by a domain expert is needed to verify and augment its generated responses ⟨RAI FAQ, Intended uses⟩.
- GraphRAG itself does not collect user data, but users are encouraged to verify the data-privacy policies of the LLM they configure it with ⟨RAI FAQ, Intended uses⟩.
- Evaluation focused on four primary concerns: accurate representation of the dataset, transparency/groundedness of responses, resilience to prompt and data-corpus injection attacks, and low hallucination rates ⟨RAI FAQ, How was GraphRAG evaluated⟩.
- Accurate representation was tested by manual inspection and automated testing against a "gold answer" from randomly selected subsets of a test corpus; hallucination rates were evaluated via claim-coverage metrics, manual answer/source inspection, and adversarial forced-hallucination attacks ⟨RAI FAQ, How was GraphRAG evaluated⟩.
- GraphRAG depends on well-constructed indexing examples; effective indexing on unique datasets can depend on proper identification of domain-specific concepts, and a best practice is to first test on a small dataset in the target domain because indexing is relatively expensive ⟨RAI FAQ, Limitations⟩.
- GraphRAG yields the most effective results on natural-language text that is collectively focused on an overall topic or theme and that is entity-rich (people, places, things, or objects that can be uniquely identified) ⟨RAI FAQ, Operational factors⟩.
- Although evaluated for resilience to injection attacks and probed for specific harms, the user-configured LLM may still produce inappropriate or offensive content, so developers should assess outputs and use available safety classifiers, model-specific safety filters, or custom solutions ⟨RAI FAQ, Operational factors⟩.

## Concepts & entities covered
Concepts: [[graphrag]] · [[retrieval-augmented-generation]]
Entities: [[microsoft-graphrag]] · [[org-microsoft]]

---
title: "Intelligent Document Processing"
type: concept
aliases: []
tags: [doc-processing]
related: ["[[document-parsing]]", "[[optical-character-recognition]]", "[[document-element-classification]]"]
updated: 2026-08-10
---

# Intelligent Document Processing

## What it is
Intelligent document processing (IDP) is the automated transformation of unstructured documents into structured, usable data by combining several document-understanding techniques — optical character recognition, computer vision, natural-language processing, and machine learning — often orchestrated end to end. It is an umbrella capability rather than a single technique: it names the pipeline that ingests documents and emits fields, classifications, and insights suitable for downstream systems.

## How sources treat it
- **[[aws-idp]]** _(provider-doc · vendor)_ — Defines IDP as leveraging optical character recognition (OCR), computer vision, natural language processing (NLP), and machine learning to automate the processing of unstructured data such as documents, audio, video, and images ⟨IDP overview: Definition / technique⟩
- **[[aws-idp]]** _(provider-doc · vendor)_ — With the integration of large language models (LLMs) and generative AI, IDP can not only extract and classify information from unstructured data but also generate concise summaries and derive actionable insights ⟨IDP overview: Definition / technique⟩
- **[[google-document-ai]]** _(provider-doc · vendor)_ — Describes Document AI as a document processing and understanding platform that takes unstructured data from documents and transforms it into structured data — specific fields suitable for a database — embodying intelligent document processing ⟨Document AI overview: intro⟩
- **[[google-document-ai]]** _(provider-doc · vendor)_ — Presents the platform as built on top of products within Vertex AI with generative AI, enabling scalable end-to-end cloud-based document processing without specialized ML expertise ⟨Document AI overview: intro⟩

## Where sources differ
The two sources are complementary vendor framings of the same umbrella capability. [[aws-idp]] emphasizes the composition of techniques (OCR, computer vision, NLP, ML) and the addition of LLMs/generative AI for summarization and insight generation; [[google-document-ai]] emphasizes the input-to-output transformation (unstructured documents to database-ready fields) and its grounding in a generative-AI platform. Neither is presented as more authoritative; both describe IDP as an end-to-end pipeline built from lower-level document-processing techniques.

## See also
[[document-parsing]] · [[optical-character-recognition]] · [[document-element-classification]] · [[document-metadata-extraction]]

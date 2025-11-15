---
title: Multimodal Search Demo
layout: default
modules: [search-hybrid, embed-openai, embed-codebert, embed-clip, embed-audio]
---

## Header
# Multimodal Search Demo
**Hybrid RRF** | **4 Modalities**

## Container
### Search Input

## SearchBar
placeholder: "Search across text, code, images, audio..."
button: "Search"

## Container
### Modality Selection

## CheckboxGroup
- **Text** - ISA standards, documentation
- **Code** - PLC, Ladder Logic, Structured Text
- **Images** - P&ID, HMI screens, diagrams
- **Audio** - ISA educational songs

## Container
### Results

## ResultsList
Empty state: No results yet. Try searching for "ISA-95 Level 3" or "PLC code"

## Container
### How It Works

**Reciprocal Rank Fusion (RRF)**

```
RRF_score(doc) = Σ (1 / (k + rank_i(doc)))
```

Where:
- `k` = 60 (RRF constant)
- `rank_i(doc)` = rank in modality i

## Container
### Example Queries

- "ISA-95 Level 3 MES integration"
- "PLC ladder logic timer example"
- "P&ID symbols standard"
- "ISA-5.1 instrumentation song"

## Footer
Powered by Qdrant + OpenAI + CodeBERT + CLIP + CLAP

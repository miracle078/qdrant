# Hybrid Multimodal Search
**UUID:** a3f2b8c9-7d1e-4f5a-9b2c-8e3d6f1a4c7b
**AutoArray** | Reciprocal Rank Fusion (RRF)

Multimodal hybrid search combining text, code, image, and audio with RRF fusion.

```javascript
const HybridSearch = {
  kRRF: 60, // RRF constant

  async search(query, mode = 't', k = 10) {
    // Mode: t=text, c=code, i=image, a=audio
    const collectionMap = {
      't': 'isa',
      'c': 'code',
      'i': 'img',
      'a': 'aud',
      'd': 'doc'
    };

    const collection = collectionMap[mode] || 'isa';

    // Get appropriate embedding
    let embedding;
    if (mode === 't' || mode === 'd') {
      embedding = await EmbedOpenAI.embed(query);
    } else if (mode === 'c') {
      embedding = await EmbedCodeBERT.embed(query);
    } else if (mode === 'i') {
      embedding = await EmbedCLIP.embedText(query);
    } else if (mode === 'a') {
      embedding = await EmbedAudio.embedText(query);
    }

    // Search Qdrant
    if (window.SearchAPI) {
      const results = await SearchAPI.search(query, collection, k);
      return results.results;
    }

    return [];
  },

  async hybridSearch(query, kPerMode = 5, modes = ['t', 'c', 'i', 'a']) {
    // Search all modalities in parallel
    const searchPromises = modes.map(mode => this.search(query, mode, kPerMode));
    const resultSets = await Promise.all(searchPromises);

    // Apply Reciprocal Rank Fusion
    const fused = this.reciprocalRankFusion(resultSets);

    console.log(`Hybrid search: ${fused.length} fused results from ${modes.length} modalities`);
    return fused;
  },

  reciprocalRankFusion(resultSets, k = null) {
    k = k || this.kRRF;
    const scores = new Map();
    const pointData = new Map();

    // Calculate RRF scores
    resultSets.forEach(resultSet => {
      resultSet.forEach((hit, rank) => {
        const pointId = hit.id;
        const score = 1 / (k + rank + 1);

        if (!scores.has(pointId)) {
          scores.set(pointId, 0);
          pointData.set(pointId, hit);
        }

        scores.set(pointId, scores.get(pointId) + score);
      });
    });

    // Sort by fused score
    const sortedIds = Array.from(scores.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(([id]) => id);

    // Build fused results
    return sortedIds.map(pointId => ({
      id: pointId,
      score: scores.get(pointId),
      payload: pointData.get(pointId).payload,
      originalScore: pointData.get(pointId).score
    }));
  },

  // FemtoLLM sparse array (mock implementation)
  femtoArray: new Map(),

  spawnFemto(x, y, z) {
    const coord = `${x},${y},${z}`;

    if (!this.femtoArray.has(coord)) {
      this.femtoArray.set(coord, {
        coord: [x, y, z],
        weights: new Array(16).fill(0).map(() => Math.random() * 0.1),
        process: (text) => `[Processed@${coord}: ${text.slice(0, 50)}...]`
      });
    }

    return this.femtoArray.get(coord);
  }
};

window.HybridSearch = HybridSearch;
```

## Reciprocal Rank Fusion (RRF)

RRF fuses multiple ranked lists using:

```
RRF_score(doc) = Σ (1 / (k + rank_i(doc)))
```

Where:
- `k` = constant (default 60)
- `rank_i(doc)` = rank of document in list i

## Usage

```javascript
// Single modality search
const textResults = await HybridSearch.search('ISA-95 Level 3', 't', 10);

// Hybrid multimodal search
const hybridResults = await HybridSearch.hybridSearch('ISA-95 Level 3', 5);

// Search specific modalities
const custom = await HybridSearch.hybridSearch('PLC code', 3, ['t', 'c']);

// Spawn FemtoLLM at sparse coordinates
const femto = HybridSearch.spawnFemto(0, 1, 2);
console.log(femto.process('test input'));
```

## Modalities

- **t** - Text (ISA standards, documentation)
- **c** - Code (PLC, Ladder Logic, Structured Text)
- **i** - Images (P&ID, HMI screens, diagrams)
- **a** - Audio (ISA educational songs)
- **d** - Documents (general text)

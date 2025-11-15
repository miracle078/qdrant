# LAION CLAP Audio Embeddings
**UUID:** 72434101-4bde-4431-9e6f-53e3560566af
**Model:** LAION CLAP (512 dim)

Audio embeddings for ISA educational songs and educational content.

```javascript
const EmbedAudio = {
  model: null,
  dimension: 512,
  cache: new Map(),

  async init() {
    // Note: CLAP requires Python backend
    // Browser uses proxy to backend API
    console.log('✓ Audio embeddings (CLAP proxy mode)');
    return this;
  },

  async embedAudio(audioUrl) {
    const cacheKey = `audio:${audioUrl}`;

    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }

    try {
      // Proxy to backend
      const response = await fetch('/api/embed/audio', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ audio_url: audioUrl })
      });

      if (!response.ok) {
        console.error('Audio embedding failed:', response.statusText);
        return new Array(this.dimension).fill(0);
      }

      const data = await response.json();
      const embedding = data.embedding;

      this.cache.set(cacheKey, embedding);

      if (window.DatabaseManager?.db) {
        DatabaseManager.cacheEmbedding(
          '72434101-4bde-4431-9e6f-53e3560566af',
          audioUrl,
          embedding,
          'laion-clap',
          this.dimension
        );
      }

      return embedding;
    } catch (error) {
      console.error('CLAP audio error:', error);
      return new Array(this.dimension).fill(0);
    }
  },

  async embedText(text) {
    // Text-to-audio search (CLAP supports text queries)
    const cacheKey = `text:${text}`;

    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }

    try {
      const response = await fetch('/api/embed/audio-text', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ text })
      });

      const data = await response.json();
      const embedding = data.embedding;

      this.cache.set(cacheKey, embedding);
      return embedding;
    } catch (error) {
      console.error('CLAP text error:', error);
      return new Array(this.dimension).fill(0);
    }
  }
};

window.EmbedAudio = EmbedAudio;
```

## Features

- 512-dimensional audio embeddings
- Text-to-audio search (query audio with text)
- Backend proxy (CLAP requires Python)
- Caching for performance

## Usage

```javascript
await EmbedAudio.init();

// Embed audio file
const audioEmbed = await EmbedAudio.embedAudio('/audio/isa-song.mp3');

// Text-to-audio search
const textEmbed = await EmbedAudio.embedText('ISA-95 Level 3 explained');
```

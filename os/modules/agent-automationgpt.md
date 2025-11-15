# AutomationGPT Agent
**UUID:** 59ae07f8-57f7-47e3-a6e1-08bbc0847f4b
**RAG Pipeline** | Claude + Qdrant + ISA Standards

Expert system for ISA-95/88/18.2 with hybrid search and conversation memory.

```javascript
const AutomationGPT = {
  apiKey: null,
  memory: [],
  maxMemory: 20,

  systemPrompt: `You are AutomationGPT, an ISA standards expert.

Specialties:
- ISA-95: Enterprise-Control Integration (L0-L4)
- ISA-88: Batch Control
- ISA-18.2: Alarm Management

Use CONTEXT from retrieved documents. Cite sources as [std:sec].`,

  init(anthropicKey) {
    this.apiKey = anthropicKey || localStorage.getItem('anthropic_api_key');
    return this;
  },

  async query(question, mode = 'hybrid', maxContext = 5) {
    const startTime = Date.now();

    // 1. RETRIEVE context
    let contextResults;

    if (window.SearchAPI) {
      const searchResult = await SearchAPI.search(question, 'isa', maxContext);
      contextResults = searchResult.results;
    } else {
      contextResults = [];
    }

    // 2. FORMAT context
    const contextStr = this.formatContext(contextResults);

    // 3. BUILD prompt
    const prompt = this.buildPrompt(question, contextStr);

    // 4. GENERATE answer
    const answer = await this.generateAnswer(prompt);

    // 5. UPDATE memory
    this.memory.push({
      question,
      answer,
      context: contextResults.slice(0, 3),
      timestamp: Date.now(),
      mode
    });

    if (this.memory.length > this.maxMemory) {
      this.memory = this.memory.slice(-this.maxMemory);
    }

    return {
      answer,
      sources: contextResults,
      mode,
      retrievalTime: Date.now() - startTime,
      contextCount: contextResults.length
    };
  },

  formatContext(results) {
    if (!results.length) return 'No relevant context found.';

    return results.map((r, i) => {
      const p = r.payload;

      if (p.std) return `[${p.std}:${p.sec}] ${p.txt?.slice(0, 300)}`;
      if (p.code) return `[CODE:${p.lang}/${p.fn}]\n${p.code.slice(0, 200)}`;
      if (p.desc) return `[DIAGRAM:${p.type}] ${p.desc}`;

      return `[DOC] ${p.txt?.slice(0, 300) || JSON.stringify(p).slice(0, 300)}`;
    }).join('\n\n');
  },

  buildPrompt(question, context) {
    return `${this.systemPrompt}\n\nCONTEXT:\n${context}\n\nQUESTION: ${question}\n\nANSWER:`;
  },

  async generateAnswer(prompt) {
    if (!this.apiKey) {
      return 'Error: Anthropic API key not set';
    }

    try {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'x-api-key': this.apiKey,
          'anthropic-version': '2023-06-01',
          'content-type': 'application/json'
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 2000,
          messages: [{ role: 'user', content: prompt }]
        })
      });

      const data = await response.json();
      return data.content[0].text;
    } catch (error) {
      console.error('Claude API error:', error);
      return `Error: ${error.message}`;
    }
  },

  clearMemory() {
    this.memory = [];
  }
};

window.AutomationGPT = AutomationGPT;
```

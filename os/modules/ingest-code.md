# Code Ingestion
**PLC Samples** | Ladder/ST

Ingest PLC code samples into Qdrant.

```javascript
const IngestCode = {
  samples: [
    { code: "IF PV > SP THEN\n  CV := 100;\nELSE\n  CV := 0;\nEND_IF;", lang: "ST", plat: "codesys", isa_pat: "95-L1", fn: "control" },
    { code: "LD %I0.0\nAND %I0.1\nOUT %Q0.0", lang: "ladder", plat: "rslogix", isa_pat: "95-L1", fn: "interlock" },
    { code: "FUNCTION_BLOCK PID\nVAR_INPUT\n  PV: REAL;\n  SP: REAL;\nEND_VAR\nVAR_OUTPUT\n  CV: REAL;\nEND_VAR\nEND_FUNCTION_BLOCK", lang: "ST", plat: "codesys", isa_pat: "95-L1", fn: "PID" }
  ],

  async run() {
    console.log('🚀 Ingesting code samples...');

    const points = [];
    for (let i = 0; i < this.samples.length; i++) {
      const data = this.samples[i];
      const vector = await EmbedCode.embed(data.code, data.lang);

      points.push({
        id: crypto.randomUUID(),
        vector,
        payload: data
      });
    }

    await QdrantClient.upsert('code', points);
    console.log(`✅ Ingested ${points.length} code samples`);

    return { count: points.length, collection: 'code' };
  }
};

window.IngestCode = IngestCode;
```

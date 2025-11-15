# ISA Standards Ingestion
**Data Pipeline** | Sample Standards

Ingest ISA-95/88/18.2 sample data into Qdrant.

```javascript
const IngestISA = {
  standards: [
    { txt: "ISA-95 L0: Field devices - sensors, actuators, physical processes", std: "ISA-95", sec: "1.0", lvl: 0, diff: "beginner" },
    { txt: "ISA-95 L1: Control - PLC, DCS, regulatory control", std: "ISA-95", sec: "1.1", lvl: 1, diff: "beginner" },
    { txt: "ISA-95 L2: Supervisory - SCADA, HMI, batch management", std: "ISA-95", sec: "1.2", lvl: 2, diff: "intermediate" },
    { txt: "ISA-95 L3: Operations - MES, quality, scheduling", std: "ISA-95", sec: "1.3", lvl: 3, diff: "intermediate" },
    { txt: "ISA-95 L4: Business - ERP, supply chain, logistics", std: "ISA-95", sec: "1.4", lvl: 4, diff: "advanced" },
    { txt: "ISA-88 PackML: IDLE → STARTING → EXECUTE → COMPLETE", std: "ISA-88", sec: "2.0", lvl: 1, diff: "intermediate" },
    { txt: "ISA-18.2 Alarm priorities: Critical, High, Medium, Low", std: "ISA-18.2", sec: "3.0", lvl: 2, diff: "advanced" }
  ],

  async run() {
    console.log('🚀 Ingesting ISA standards...');

    const points = [];
    for (let i = 0; i < this.standards.length; i++) {
      const data = this.standards[i];
      const vector = await EmbedText.embed(data.txt);

      points.push({
        id: crypto.randomUUID(),
        vector,
        payload: data
      });
    }

    await QdrantClient.upsert('isa', points);
    console.log(`✅ Ingested ${points.length} standards`);

    return { count: points.length, collection: 'isa' };
  }
};

window.IngestISA = IngestISA;
```

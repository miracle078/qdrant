# Database Manager
**UUID:** d6f529de-e759-49f9-abcd-cd30e902626a
**SQLite Persistence** | ISA-95 L3: Data Layer

Database management for file registry, embeddings cache, and metadata.

```javascript
const DatabaseManager = {
  db: null,
  dbPath: 'automationgpt.db',

  async init() {
    // IndexedDB for browser-based SQLite
    const SQL = await initSqlJs({
      locateFile: file => `https://sql.js.org/dist/${file}`
    });

    // Check if DB exists in localStorage
    const saved = localStorage.getItem('automationgpt_db');

    if (saved) {
      const arr = new Uint8Array(JSON.parse(saved));
      this.db = new SQL.Database(arr);
    } else {
      this.db = new SQL.Database();
      await this.loadSchema();
    }

    return this;
  },

  async loadSchema() {
    const response = await fetch('/schema.sql');
    const schema = await response.text();

    this.db.run(schema);
    this.save();
  },

  query(sql, params = []) {
    return this.db.exec(sql, params);
  },

  run(sql, params = []) {
    this.db.run(sql, params);
    this.save();
  },

  save() {
    const data = this.db.export();
    const arr = Array.from(data);
    localStorage.setItem('automationgpt_db', JSON.stringify(arr));
  },

  // File registry
  registerFile(uuid, path, type, moduleName) {
    this.run(
      'INSERT OR REPLACE INTO files (uuid, path, type, module_name) VALUES (?, ?, ?, ?)',
      [uuid, path, type, moduleName]
    );
  },

  getFile(uuid) {
    const result = this.query('SELECT * FROM files WHERE uuid = ?', [uuid]);
    return result[0]?.values[0];
  },

  // Embeddings cache
  cacheEmbedding(fileUuid, text, vector, model, dimension) {
    const blob = new Float32Array(vector).buffer;
    this.run(
      'INSERT INTO embeddings (file_uuid, text, vector, model, dimension) VALUES (?, ?, ?, ?, ?)',
      [fileUuid, text, blob, model, dimension]
    );
  },

  getEmbedding(text, model) {
    const result = this.query(
      'SELECT vector FROM embeddings WHERE text = ? AND model = ? LIMIT 1',
      [text, model]
    );
    return result[0]?.values[0]?.[0];
  }
};

window.DatabaseManager = DatabaseManager;
```

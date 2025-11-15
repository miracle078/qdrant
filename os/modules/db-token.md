# Token Database
**UUID:** b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e
**Token-Dense Storage** | Module & Dependency Management

Database operations for token-dense module storage.

```javascript
const TokenDB = {
  db: null,

  async init() {
    // Initialize SQL.js (browser) or better-sqlite3 (Node.js)
    if (typeof SQL !== 'undefined') {
      // Browser with sql.js
      this.db = new SQL.Database();
    } else if (typeof require !== 'undefined') {
      // Node.js with better-sqlite3
      const Database = require('better-sqlite3');
      this.db = new Database('./data/sql/tokens.db');
    }

    await this.createSchema();
    return this;
  },

  async createSchema() {
    const schema = await fetch('../data/sql/token-schema.sql');
    const sql = await schema.text();

    // Extract SQL statements
    const statements = sql.match(/CREATE TABLE[\s\S]*?;/g) || [];
    statements.forEach(stmt => this.exec(stmt));

    // Extract indexes
    const indexes = sql.match(/CREATE INDEX[\s\S]*?;/g) || [];
    indexes.forEach(idx => this.exec(idx));
  },

  exec(sql, params = []) {
    if (this.db.exec) {
      return this.db.exec(sql, params);
    } else {
      return this.db.prepare(sql).run(...params);
    }
  },

  query(sql, params = []) {
    if (this.db.exec) {
      const result = this.db.exec(sql, params);
      return result[0]?.values || [];
    } else {
      return this.db.prepare(sql).all(...params);
    }
  },

  async insertModule(module) {
    const sql = `
      INSERT INTO modules (uuid, name, path, category, token_count, content_hash, metadata)
      VALUES (?, ?, ?, ?, ?, ?, ?)
    `;
    return this.exec(sql, [
      module.uuid,
      module.name,
      module.path,
      module.category,
      module.tokenCount,
      module.contentHash,
      JSON.stringify(module.metadata || {})
    ]);
  },

  async addDependency(moduleId, dependsOnId, type = 'requires') {
    const sql = `
      INSERT OR IGNORE INTO dependencies (module_id, depends_on_id, dependency_type)
      VALUES (?, ?, ?)
    `;
    return this.exec(sql, [moduleId, dependsOnId, type]);
  },

  async getModulesByCategory(category) {
    const sql = `SELECT * FROM modules WHERE category = ? ORDER BY name`;
    return this.query(sql, [category]);
  },

  async getDependencies(moduleId) {
    const sql = `
      SELECT m.*, d.dependency_type
      FROM modules m
      JOIN dependencies d ON m.id = d.depends_on_id
      WHERE d.module_id = ?
    `;
    return this.query(sql, [moduleId]);
  },

  async getArchitectureGraph() {
    const sql = `
      SELECT * FROM architecture_graph
      ORDER BY layer, x_pos, y_pos
    `;
    return this.query(sql);
  },

  async getTokenStats() {
    const sql = `
      SELECT
        category,
        COUNT(*) as module_count,
        SUM(token_count) as total_tokens,
        AVG(token_count) as avg_tokens
      FROM modules
      GROUP BY category
      ORDER BY total_tokens DESC
    `;
    return this.query(sql);
  },

  export() {
    if (this.db.export) {
      return this.db.export();
    }
    return null;
  }
};

window.TokenDB = TokenDB;
```

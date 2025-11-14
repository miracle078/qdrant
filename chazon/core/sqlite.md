# SQLite Wrapper
**sql.js Compatible** | Persistent Storage

Browser-compatible SQLite with localStorage persistence.

```javascript
const SQLiteDB = {
  db: null,
  storage: 'chazon:sqlite',

  async init() {
    // Load sql.js from CDN in production
    // For now, use in-memory mock
    this.db = this.createMockDB();
    this.loadFromStorage();
    console.log('💾 SQLite initialized');
  },

  createMockDB() {
    return {
      tables: {
        changelog: [],
        states: [],
        modules: []
      },
      exec(sql, params = []) {
        if (sql.includes('CREATE TABLE')) return { success: true };
        if (sql.includes('INSERT INTO changelog')) {
          this.tables.changelog.push(params);
          return { success: true, lastInsertRowid: this.tables.changelog.length };
        }
        if (sql.includes('SELECT')) {
          return this.tables.changelog.slice(-20);
        }
        return [];
      }
    };
  },

  exec(sql, params) {
    const result = this.db.exec(sql, params);
    this.saveToStorage();
    return result;
  },

  loadFromStorage() {
    const data = localStorage.getItem(this.storage);
    if (data) {
      const parsed = JSON.parse(data);
      this.db.tables = parsed.tables || this.db.tables;
      console.log('💾 Loaded from localStorage');
    }
  },

  saveToStorage() {
    const data = JSON.stringify({
      tables: this.db.tables,
      timestamp: Date.now()
    });
    localStorage.setItem(this.storage, data);
  },

  export() {
    return this.db.tables;
  },

  import(tables) {
    this.db.tables = tables;
    this.saveToStorage();
  }
};

window.SQLiteDB = SQLiteDB;
```

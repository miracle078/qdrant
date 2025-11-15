# Query Embeddings Cache
**UUID:** c66ed51a-f1e5-496b-9bd7-0ba1ce08877b
**Executable Query** | embeddings.db

Query the embeddings cache for model statistics and lookups.

```python
#!/usr/bin/env python3
import sqlite3
import hashlib
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'databases' / 'embeddings.db'

def connect():
    return sqlite3.connect(DB_PATH)

def hash_text(text):
    """Generate hash for text lookup"""
    return hashlib.sha256(text.encode()).hexdigest()

def find_embedding(text, model='text-embedding-3-large'):
    """Find cached embedding by text"""
    conn = connect()
    text_hash = hash_text(text)

    cursor = conn.execute("""
        SELECT id, dimension, created_at
        FROM embeddings
        WHERE text_hash = ? AND model = ?
    """, (text_hash, model))

    row = cursor.fetchone()

    if row:
        print(f"✓ Found cached embedding:")
        print(f"  ID: {row[0]}")
        print(f"  Dimension: {row[1]}")
        print(f"  Model: {model}")
        print(f"  Created: {row[2]}")
    else:
        print(f"✗ No cached embedding found for this text with model {model}")

    conn.close()

def stats_by_model():
    """Get statistics by model"""
    conn = connect()

    cursor = conn.execute("""
        SELECT model, dimension, COUNT(*) as count,
               MIN(created_at) as first_cached,
               MAX(created_at) as last_cached
        FROM embeddings
        GROUP BY model
        ORDER BY count DESC
    """)

    print("📊 Embeddings Cache Statistics:")
    print("-" * 80)
    for row in cursor.fetchall():
        model, dim, count, first, last = row
        print(f"{model:30} | {dim:4}d | {count:6} embeddings | {first} → {last}")

    conn.close()

def total_size():
    """Estimate total cache size"""
    conn = connect()

    cursor = conn.execute("""
        SELECT SUM(dimension * 4) / 1024.0 / 1024.0 as size_mb
        FROM embeddings
    """)

    size_mb = cursor.fetchone()[0] or 0

    print(f"\n💾 Estimated cache size: {size_mb:.2f} MB")
    print("   (assuming 4 bytes per float32 dimension)")

    conn.close()

def recent(limit=10):
    """Show recently cached embeddings"""
    conn = connect()

    cursor = conn.execute("""
        SELECT text, model, dimension, created_at
        FROM embeddings
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))

    print(f"\n🕐 {limit} Most Recent Embeddings:")
    print("-" * 80)
    for text, model, dim, created in cursor.fetchall():
        text_preview = text[:60] + '...' if len(text) > 60 else text
        print(f"{created} | {model:20} | {dim:4}d | {text_preview}")

    conn.close()

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'find' and len(sys.argv) > 2:
            text = ' '.join(sys.argv[2:])
            find_embedding(text)
        elif command == 'stats':
            stats_by_model()
            total_size()
        elif command == 'recent':
            limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            recent(limit)
        else:
            print("Usage: python query-embeddings.md <command> [args]")
            print("Commands:")
            print("  find <text>     - Find cached embedding")
            print("  stats           - Show statistics by model")
            print("  recent [n]      - Show n recent embeddings")
    else:
        stats_by_model()
        total_size()
```

## JavaScript Version

```javascript
const EmbeddingQueries = {
  dbPath: '/collab/databases/embeddings.db',
  db: null,

  async init() {
    const response = await fetch(this.dbPath);
    const buffer = await response.arrayBuffer();
    this.db = new window.SQL.Database(new Uint8Array(buffer));
    return this;
  },

  async hashText(text) {
    const encoder = new TextEncoder();
    const data = encoder.encode(text);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  },

  async findEmbedding(text, model = 'text-embedding-3-large') {
    const hash = await this.hashText(text);

    const result = this.db.exec(`
      SELECT id, dimension, created_at
      FROM embeddings
      WHERE text_hash = ? AND model = ?
    `, [hash, model]);

    return result[0]?.values[0] || null;
  },

  statsByModel() {
    const result = this.db.exec(`
      SELECT model, dimension, COUNT(*) as count
      FROM embeddings
      GROUP BY model
      ORDER BY count DESC
    `);

    return result[0]?.values || [];
  }
};

window.EmbeddingQueries = EmbeddingQueries;
```

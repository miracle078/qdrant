# Databases Directory
**UUID:** 4f26b35b-dac6-4f66-98b3-82115372e1d0
**SQLite Persistence Layer** | ISA-95 L1-L3

Initialized SQLite databases for project persistence.

## 📊 Database Files

### automationgpt.db (86 KB)
**Main database with complete schema**

Tables:
- `files` - File registry with UUIDs and metadata
- `dependencies` - Module dependency graph
- `embeddings` - Embedding cache with vectors
- `collections` - Qdrant collection metadata
- `points` - Qdrant point tracking
- `builds` - Build/CI log
- `isa_standards` - ISA compliance tracking

```sql
-- Example queries
SELECT COUNT(*) FROM files;
SELECT * FROM files WHERE type = 'module';
SELECT * FROM dependencies WHERE from_uuid = '...';
```

### modules.db (8 KB)
**Module registry and dependency tracking**

Tables:
- `modules` - UUID, name, path, type, isa_level
- `dependencies` - from_uuid, to_uuid, dep_type

```sql
-- Get all modules
SELECT uuid, name, type, isa_level FROM modules;

-- Get module dependencies
SELECT m.name
FROM dependencies d
JOIN modules m ON d.to_uuid = m.uuid
WHERE d.from_uuid = (SELECT uuid FROM modules WHERE name = 'AutomationGPT');
```

### embeddings.db (8 KB)
**Embedding cache for all models**

Tables:
- `embeddings` - text_hash, text, model, dimension, vector, created_at

```sql
-- Get cache statistics
SELECT model, COUNT(*), AVG(dimension)
FROM embeddings
GROUP BY model;

-- Find embedding
SELECT * FROM embeddings WHERE text_hash = '...';
```

### qdrant.db (8 KB)
**Qdrant metadata and sync tracking**

Tables:
- `collections` - name, dimension, vector_count
- `points` - point_id, collection, payload, synced_at

```sql
-- Collection statistics
SELECT name, dimension, vector_count FROM collections;

-- Recent points
SELECT * FROM points ORDER BY synced_at DESC LIMIT 10;
```

### agents.db (8 KB)
**Multi-agent coordination**

Tables:
- `agents` - id, name, type, status, current_task, metadata
- `tasks` - id, agent_id, task_type, status, result
- `messages` - from_agent, to_agent, message, timestamp

```sql
-- Active agents
SELECT id, name, status, current_task FROM agents WHERE status != 'stopped';

-- Pending tasks
SELECT * FROM tasks WHERE status = 'pending';

-- Agent messages
SELECT * FROM messages ORDER BY timestamp DESC LIMIT 20;
```

## 🔧 Database Schema

All databases follow the schema defined in `/schema.sql`.

To view schema:
```bash
python3 -c "
import sqlite3
conn = sqlite3.connect('collab/databases/automationgpt.db')
schema = conn.execute('SELECT sql FROM sqlite_master WHERE type=\"table\"').fetchall()
for s in schema: print(s[0])
"
```

## 💾 Backup & Restore

### Backup
```bash
# Single database
cp collab/databases/automationgpt.db collab/databases/automationgpt.db.backup

# All databases
tar -czf collab-databases-backup.tar.gz collab/databases/*.db
```

### Restore
```bash
# Single database
cp collab/databases/automationgpt.db.backup collab/databases/automationgpt.db

# All databases
tar -xzf collab-databases-backup.tar.gz
```

## 🔍 Querying

### Python
```python
import sqlite3

conn = sqlite3.connect('collab/databases/modules.db')
cursor = conn.execute('SELECT * FROM modules')
for row in cursor:
    print(row)
conn.close()
```

### Browser (via sql.js)
```javascript
await ModuleLoader.load('db-manager');
await DatabaseManager.init();

const result = DatabaseManager.query('SELECT * FROM files');
console.log(result);
```

### Executable Queries
```bash
# Use pre-built query scripts
python collab/queries/query-modules.md list
python collab/queries/query-embeddings.md stats
```

## 📈 Monitoring

Use the Database Management Agent:
```bash
# Check health
python collab/agents/agent-database.md monitor

# Daemon mode
python collab/agents/agent-database.md daemon
```

## 🔒 Security

- Databases are local SQLite files (no network exposure)
- No authentication required (filesystem permissions only)
- For production: consider encrypting sensitive databases

## 🚀 Initialization

Databases are pre-initialized with schemas. To reinitialize:

```python
import sqlite3

# Reinitialize
conn = sqlite3.connect('collab/databases/automationgpt.db')
with open('schema.sql') as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
```

## 📝 Best Practices

1. **Always close connections**: Use context managers
   ```python
   with sqlite3.connect('db.db') as conn:
       conn.execute('SELECT ...')
   ```

2. **Use parameterized queries**: Prevent SQL injection
   ```python
   conn.execute('SELECT * FROM modules WHERE name = ?', (name,))
   ```

3. **Regular backups**: Automated daily backups via agent

4. **Optimize regularly**: VACUUM and ANALYZE
   ```python
   conn.execute('VACUUM')
   conn.execute('ANALYZE')
   ```

5. **Monitor size**: Check database growth
   ```bash
   du -h collab/databases/*.db
   ```

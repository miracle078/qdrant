# Queries Directory
**UUID:** fd3c57a4-1e8c-45dc-bb2c-661f1c27e34a
**Executable SQL Queries** | ISA-95 L2-L3

Executable markdown files that query SQLite databases with both Python and JavaScript.

## 📋 Available Queries

### 1. Query Modules
**File:** `query-modules.md`
**UUID:** 67befcb1-c033-43a7-876c-41af2c5c2451
**Database:** modules.db

Query the module registry for dependencies, statistics, and metadata.

**Commands:**
```bash
# List all modules
python collab/queries/query-modules.md list

# Show dependencies for a module
python collab/queries/query-modules.md deps AutomationGPT

# Show what depends on a module
python collab/queries/query-modules.md dependents PackML

# Get statistics
python collab/queries/query-modules.md stats
```

**Output Example:**
```
📦 All Modules:
--------------------------------------------------------------------------------
L4 | ModuleRegistry                | c16e00c3... | registry
L3 | AutomationGPT                 | 59ae07f8... | agent
L3 | DatabaseManager               | d6f529de... | database
L2 | PackML                        | a9504de3... | core
```

### 2. Query Embeddings
**File:** `query-embeddings.md`
**UUID:** c66ed51a-f1e5-496b-9bd7-0ba1ce08877b
**Database:** embeddings.db

Query the embeddings cache for model statistics and cached vectors.

**Commands:**
```bash
# Find cached embedding by text
python collab/queries/query-embeddings.md find "ISA-95 Level 3"

# Show statistics by model
python collab/queries/query-embeddings.md stats

# Show recent embeddings
python collab/queries/query-embeddings.md recent 10
```

**Output Example:**
```
📊 Embeddings Cache Statistics:
--------------------------------------------------------------------------------
text-embedding-3-large        | 1536d |     45 embeddings | 1731628800 → 1731715200
codebert-base                 |  768d |     23 embeddings | 1731628900 → 1731715100
clip-vit-base-patch32         |  512d |     12 embeddings | 1731629000 → 1731715000

💾 Estimated cache size: 2.15 MB
   (assuming 4 bytes per float32 dimension)
```

## 🔧 Query Features

### Dual-Mode Execution

All queries support both Python (server/CLI) and JavaScript (browser):

**Python:**
```python
#!/usr/bin/env python3
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'databases' / 'modules.db'

def query():
    conn = sqlite3.connect(DB_PATH)
    result = conn.execute('SELECT * FROM modules').fetchall()
    conn.close()
    return result
```

**JavaScript:**
```javascript
const ModuleQueries = {
  async init() {
    const response = await fetch('/collab/databases/modules.db');
    const buffer = await response.arrayBuffer();
    this.db = new SQL.Database(new Uint8Array(buffer));
  },

  query() {
    return this.db.exec('SELECT * FROM modules');
  }
};
```

### Executable Markdown

All query files are executable:

```bash
# Make executable
chmod +x collab/queries/query-modules.md

# Run directly (shebang: #!/usr/bin/env python3)
./collab/queries/query-modules.md list
```

## 📊 Common Queries

### Get All Modules by ISA Level
```sql
SELECT uuid, name, isa_level
FROM modules
WHERE isa_level IS NOT NULL
ORDER BY isa_level DESC, name;
```

### Find Module Dependencies
```sql
SELECT m.name AS module, d.name AS depends_on
FROM modules m
JOIN dependencies dep ON m.uuid = dep.from_uuid
JOIN modules d ON dep.to_uuid = d.uuid
WHERE m.name = 'AutomationGPT';
```

### Embedding Cache Hit Rate
```sql
SELECT
  model,
  COUNT(*) as cached_count,
  SUM(dimension * 4) / 1024.0 / 1024.0 as size_mb
FROM embeddings
GROUP BY model;
```

### Recent Agent Activity
```sql
SELECT a.name, t.task_type, t.status, t.created_at
FROM tasks t
JOIN agents a ON t.agent_id = a.id
ORDER BY t.created_at DESC
LIMIT 20;
```

## 🎯 Use Cases

### 1. Dependency Analysis
```bash
# Find circular dependencies
python collab/queries/query-modules.md deps AutomationGPT
python collab/queries/query-modules.md dependents EmbedOpenAI
```

### 2. Cache Efficiency
```bash
# Check embedding cache utilization
python collab/queries/query-embeddings.md stats

# Find frequently embedded text
python collab/queries/query-embeddings.md recent 50 | grep -o "ISA-95" | wc -l
```

### 3. Module Discovery
```bash
# List all L3 modules
python collab/queries/query-modules.md list | grep "L3"

# Count modules by type
python collab/queries/query-modules.md stats
```

### 4. Performance Monitoring
```bash
# Database size tracking
python collab/agents/agent-database.md monitor | grep "Size:"

# Agent task throughput
python -c "
import sqlite3
conn = sqlite3.connect('collab/databases/agents.db')
print('Completed tasks:', conn.execute('SELECT COUNT(*) FROM tasks WHERE status=\"completed\"').fetchone()[0])
"
```

## 🛠️ Creating New Queries

### Template

```markdown
# Query [Database Name]
**UUID:** [new-uuid]
**Executable Query** | [database].db

Description of query purpose.

\`\`\`python
#!/usr/bin/env python3
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'databases' / '[database].db'

def connect():
    return sqlite3.connect(DB_PATH)

def my_query():
    conn = connect()
    cursor = conn.execute("""
        SELECT ...
        FROM ...
        WHERE ...
    """)

    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'myquery':
            my_query()
    else:
        my_query()
\`\`\`

## JavaScript Version

\`\`\`javascript
const MyQueries = {
  dbPath: '/collab/databases/[database].db',
  db: null,

  async init() {
    const response = await fetch(this.dbPath);
    const buffer = await response.arrayBuffer();
    this.db = new SQL.Database(new Uint8Array(buffer));
  },

  myQuery() {
    return this.db.exec('SELECT ... FROM ...');
  }
};

window.MyQueries = MyQueries;
\`\`\`
```

### Best Practices

1. **Always use parameterized queries** to prevent SQL injection
2. **Close connections** after use
3. **Provide both Python and JavaScript** versions
4. **Include usage examples** in comments
5. **Handle errors gracefully**
6. **Support command-line arguments** for flexibility
7. **Format output** for readability

## 📈 Performance Tips

### Indexes
Ensure proper indexes for fast queries:
```sql
CREATE INDEX idx_modules_isa_level ON modules(isa_level);
CREATE INDEX idx_dependencies_from ON dependencies(from_uuid);
CREATE INDEX idx_embeddings_text_hash ON embeddings(text_hash);
```

### Query Optimization
```sql
-- Use EXPLAIN QUERY PLAN to analyze
EXPLAIN QUERY PLAN
SELECT * FROM modules WHERE isa_level = 3;

-- Add indexes for frequently queried columns
CREATE INDEX IF NOT EXISTS idx_modules_type ON modules(type);
```

### Caching
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_module_deps(module_name):
    # Query cached in memory
    pass
```

## 🔗 Integration

### With Agents
```python
# Agent uses queries for monitoring
from collab.queries.query_modules import stats_by_type

agent = ModuleAgent()
module_stats = stats_by_type()
agent.report(module_stats)
```

### With Module System
```javascript
// Load query module in browser
await ModuleLoader.load('module-queries');

const stats = await ModuleQueries.stats();
console.log(stats);
```

### With API
```python
# API endpoint uses query
from fastapi import FastAPI
from collab.queries import query_modules

app = FastAPI()

@app.get("/api/modules")
def list_modules():
    return query_modules.list_all()
```

## 📚 References

- Database schemas: `/collab/databases/README.md`
- Agent documentation: `/collab/agents/README.md`
- Main README: `/collab/README.md`
- SQL reference: https://www.sqlite.org/lang.html

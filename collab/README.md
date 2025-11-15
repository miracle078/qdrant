# Collaboration Directory
**UUID:** 62f4f814-7ec6-4c52-973a-c6b350c36046
**Multi-Agent System** | ISA-95 L3-L4

Autonomous agent collaboration workspace for Chazon with SQLite databases and executable queries.

## 📁 Structure

```
collab/
├── agents/                 # Autonomous agents
│   ├── agent-database.md  # Database management agent
│   ├── agent-module.md    # Module development agent
│   └── README.md
│
├── databases/             # SQLite databases
│   ├── automationgpt.db  # Main database (all tables)
│   ├── modules.db        # Module registry & dependencies
│   ├── embeddings.db     # Embedding cache
│   ├── qdrant.db         # Qdrant metadata
│   ├── agents.db         # Agent coordination
│   └── README.md
│
├── queries/              # Executable query scripts
│   ├── query-modules.md
│   ├── query-embeddings.md
│   └── README.md
│
└── README.md             # This file
```

## 🤖 Agents

### Database Management Agent
**UUID:** d66a2866-a53f-402e-a21f-176cef24fd83

Monitors database health, optimizes performance, and maintains indexes.

```bash
# Monitor all databases
python collab/agents/agent-database.md monitor

# Run as daemon (continuous monitoring)
python collab/agents/agent-database.md daemon
```

### Module Management Agent
**UUID:** d60b9ca5-8f6f-4864-b47f-86c2d15135a5

Scans modules, tracks dependencies, validates structure, and generates templates.

```bash
# Scan and register all modules
python collab/agents/agent-module.md scan

# Generate module report
python collab/agents/agent-module.md report
```

## 💾 Databases

| Database | Size | Purpose | Tables |
|----------|------|---------|--------|
| automationgpt.db | ~86 KB | Main database | files, dependencies, embeddings, collections, points, builds, isa_standards |
| modules.db | ~8 KB | Module registry | modules, dependencies |
| embeddings.db | ~8 KB | Embedding cache | embeddings |
| qdrant.db | ~8 KB | Qdrant metadata | collections, points |
| agents.db | ~8 KB | Agent coordination | agents, tasks, messages |

## 🔍 Queries

### Query Modules
**UUID:** 67befcb1-c033-43a7-876c-41af2c5c2451

```bash
# List all modules
python collab/queries/query-modules.md list

# Show dependencies
python collab/queries/query-modules.md deps AutomationGPT

# Get statistics
python collab/queries/query-modules.md stats
```

### Query Embeddings
**UUID:** c66ed51a-f1e5-496b-9bd7-0ba1ce08877b

```bash
# Find cached embedding
python collab/queries/query-embeddings.md find "ISA-95 Level 3"

# Show statistics
python collab/queries/query-embeddings.md stats

# Recent embeddings
python collab/queries/query-embeddings.md recent 10
```

## 🚀 Quick Start

### Initialize Databases

Databases are already initialized with schemas. To verify:

```bash
# Check database health
python collab/agents/agent-database.md monitor
```

### Register Modules

```bash
# Scan and register all modules
python collab/agents/agent-module.md scan

# View report
python collab/agents/agent-module.md report
```

### Run Agents in Parallel

Terminal 1:
```bash
# Database monitoring agent (daemon mode)
python collab/agents/agent-database.md daemon
```

Terminal 2:
```bash
# Module management agent (one-time scan)
python collab/agents/agent-module.md scan
```

## 📊 Multi-Agent Communication

Agents communicate through the `agents.db` database:

### Agent Registration
```python
# Each agent registers on startup
agent_id = 'my-agent-001'
conn.execute("""
    INSERT INTO agents (id, name, type, status, metadata)
    VALUES (?, ?, ?, ?, ?)
""", (agent_id, name, type, 'idle', metadata_json))
```

### Task Queue
```python
# Agent creates task
task_id = conn.execute("""
    INSERT INTO tasks (agent_id, task_type, description)
    VALUES (?, ?, ?)
""", (agent_id, 'optimize', 'Optimize modules.db')).lastrowid

# Complete task
conn.execute("""
    UPDATE tasks
    SET status = 'completed', result = ?
    WHERE id = ?
""", (result_json, task_id))
```

### Message Passing
```python
# Send message to another agent
conn.execute("""
    INSERT INTO messages (from_agent, to_agent, message)
    VALUES (?, ?, ?)
""", ('agent-1', 'agent-2', message_json))
```

## 🏗️ Architecture

### ISA-95 Hierarchy

- **L4 (Business)**: Multi-agent orchestration, planning
- **L3 (MES)**: Database agents, module agents, data management
- **L2 (Supervisory)**: Query execution, monitoring
- **L1 (Control)**: Database operations, CRUD
- **L0 (Field)**: Raw data storage

### PackML State Machine

All agents follow ISA-88 PackML states:
- `IDLE` → `STARTING` → `EXECUTE` → `COMPLETING` → `COMPLETE`
- Error handling: `ABORTING` → `ABORTED` → `CLEARING`

### Agent Lifecycle

```
┌─────────────┐
│ REGISTER    │  Agent registers in agents.db
└──────┬──────┘
       ↓
┌─────────────┐
│ IDLE        │  Waiting for tasks
└──────┬──────┘
       ↓
┌─────────────┐
│ WORKING     │  Executing task
└──────┬──────┘
       ↓
┌─────────────┐
│ IDLE        │  Task complete, ready for next
└─────────────┘
```

## 📝 Creating New Agents

```python
from pathlib import Path
import sqlite3
import time

class MyAgent:
    def __init__(self, agent_id='my-agent-001'):
        self.agent_id = agent_id
        self.agent_db = Path(__file__).parent.parent / 'databases' / 'agents.db'
        self.register()

    def register(self):
        conn = sqlite3.connect(self.agent_db)
        conn.execute("""
            INSERT OR REPLACE INTO agents (id, name, type, status, started_at)
            VALUES (?, ?, ?, ?, ?)
        """, (self.agent_id, 'My Agent', 'custom', 'idle', int(time.time())))
        conn.commit()
        conn.close()

    def run(self):
        # Agent logic here
        pass

if __name__ == '__main__':
    agent = MyAgent()
    agent.run()
```

## 🧪 Testing

```bash
# Test database connectivity
python -c "import sqlite3; print(sqlite3.connect('collab/databases/automationgpt.db').execute('SELECT COUNT(*) FROM files').fetchone())"

# Test agent registration
python collab/agents/agent-database.md monitor

# Test query execution
python collab/queries/query-modules.md stats
```

## 📚 Documentation

- See `databases/README.md` for database schema details
- See `agents/README.md` for agent development guide
- See `queries/README.md` for query examples
- See root `MANIFEST.md` for project overview

## 🔗 Integration

All components integrate with the main module system:

```javascript
// In browser console
await ModuleLoader.load('db-manager');
await DatabaseManager.init();

// Query from browser
const modules = await DatabaseManager.query('SELECT * FROM files');
```

## 🎯 Use Cases

1. **Automated Testing**: Database agent monitors integrity, module agent validates structure
2. **CI/CD Pipeline**: Agents coordinate build, test, and deployment tasks
3. **Documentation**: Module agent scans and generates documentation
4. **Performance**: Database agent optimizes queries and indexes
5. **Dependency Management**: Module agent tracks and resolves dependencies

# Agents Directory
**UUID:** f5c60952-c50b-4259-b526-8a10b798dd8c
**Multi-Agent System** | ISA-95 L3-L4

Autonomous agents for database management, module development, and system maintenance.

## 🤖 Available Agents

### 1. Database Management Agent
**File:** `agent-database.md`
**UUID:** d66a2866-a53f-402e-a21f-176cef24fd83
**Type:** Database Administrator
**ISA Level:** L3 (MES/Data Layer)

**Capabilities:**
- Monitor database health and integrity
- Optimize database performance (VACUUM, ANALYZE)
- Maintain indexes
- Generate health reports
- Task queue management

**Usage:**
```bash
# Monitor all databases
python collab/agents/agent-database.md monitor

# Check specific database
python collab/agents/agent-database.md health automationgpt.db

# Optimize database
python collab/agents/agent-database.md optimize modules.db

# Run as daemon (continuous monitoring every 60s)
python collab/agents/agent-database.md daemon
```

**Example Output:**
```
🔍 Database Monitoring Report
Generated: 2025-11-15T01:30:00
================================================================================

✓ automationgpt.db
  Size: 0.08 MB
  Tables: 8
  Integrity: ok

✓ modules.db
  Size: 0.01 MB
  Tables: 2
  Integrity: ok
```

### 2. Module Management Agent
**File:** `agent-module.md`
**UUID:** d60b9ca5-8f6f-4864-b47f-86c2d15135a5
**Type:** Module Developer/Maintainer
**ISA Level:** L3-L4 (MES/Business)

**Capabilities:**
- Scan and register modules automatically
- Extract UUIDs from markdown headers
- Track module dependencies
- Validate module structure (UUID, exports, token count)
- Generate module templates
- Build dependency graph
- ISA level classification

**Usage:**
```bash
# Scan and register all modules
python collab/agents/agent-module.md scan

# Validate a module
python collab/agents/agent-module.md validate modules/my-module.md

# Track dependencies
python collab/agents/agent-module.md deps AutomationGPT

# Generate new module template
python collab/agents/agent-module.md generate MyNewModule

# Generate module report
python collab/agents/agent-module.md report
```

**Example Output:**
```
📊 Module Report
================================================================================
Total modules: 92

By Type:
  core                  17 modules
  embedding              6 modules
  api                    6 modules
  agent                  5 modules

By ISA Level:
  L4: 12 modules
  L3: 45 modules
  L2: 20 modules
```

## 🏗️ Agent Architecture

### Registration
Every agent registers in `agents.db` on startup:

```python
conn.execute("""
    INSERT OR REPLACE INTO agents (id, name, type, status, started_at, metadata)
    VALUES (?, ?, ?, ?, ?, ?)
""", (agent_id, name, type, 'idle', timestamp, metadata_json))
```

### Status Updates
Agents update status during operation:

```python
def update_status(self, status, task=None):
    conn.execute("""
        UPDATE agents SET status = ?, current_task = ? WHERE id = ?
    """, (status, task, self.agent_id))
```

### Task Management
Agents create and complete tasks:

```python
# Create task
task_id = conn.execute("""
    INSERT INTO tasks (agent_id, task_type, description)
    VALUES (?, ?, ?)
""", (agent_id, 'optimize', 'Optimize database')).lastrowid

# Complete task
conn.execute("""
    UPDATE tasks SET status = 'completed', result = ?, completed_at = ?
    WHERE id = ?
""", (result_json, timestamp, task_id))
```

## 🔄 Agent Communication

Agents communicate via the `messages` table:

```python
# Send message
conn.execute("""
    INSERT INTO messages (from_agent, to_agent, message)
    VALUES (?, ?, ?)
""", ('db-agent-001', 'module-agent-001', json.dumps({
    'type': 'request',
    'action': 'validate_all'
})))

# Receive messages
messages = conn.execute("""
    SELECT from_agent, message, timestamp
    FROM messages
    WHERE to_agent = ?
    ORDER BY timestamp DESC
""", (agent_id,)).fetchall()
```

## 🎯 Multi-Agent Orchestration

### Parallel Execution

Terminal 1:
```bash
python collab/agents/agent-database.md daemon
```

Terminal 2:
```bash
python collab/agents/agent-module.md scan
```

### Sequential Tasks

```python
# Database agent optimizes first
db_agent = DatabaseAgent()
db_agent.optimize('modules.db')

# Module agent scans after optimization
module_agent = ModuleAgent()
module_agent.scan_modules()
```

### Coordinated Workflow

```python
# 1. Database agent checks health
db_result = db_agent.check_health('modules.db')

# 2. If healthy, module agent scans
if db_result['status'] == 'ok':
    module_agent.scan_modules()

# 3. Module agent validates all
for module in modules:
    module_agent.validate_module(module)

# 4. Database agent optimizes after changes
db_agent.optimize('modules.db')
```

## 🛠️ Creating New Agents

### Template

```python
#!/usr/bin/env python3
import sqlite3
import time
import json
from pathlib import Path

class MyAgent:
    """
    Agent description and purpose
    """

    def __init__(self, agent_id='my-agent-001'):
        self.agent_id = agent_id
        self.agent_db = Path(__file__).parent.parent / 'databases' / 'agents.db'
        self.status = 'idle'
        self.register()

    def register(self):
        """Register agent in agents.db"""
        conn = sqlite3.connect(self.agent_db)
        conn.execute("""
            INSERT OR REPLACE INTO agents (id, name, type, status, started_at, metadata)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            self.agent_id,
            'My Agent Name',
            'agent_type',
            self.status,
            int(time.time()),
            json.dumps({'version': '1.0', 'capabilities': []})
        ))
        conn.commit()
        conn.close()

    def update_status(self, status, task=None):
        """Update agent status"""
        self.status = status
        conn = sqlite3.connect(self.agent_db)
        conn.execute("""
            UPDATE agents SET status = ?, current_task = ? WHERE id = ?
        """, (status, task, self.agent_id))
        conn.commit()
        conn.close()

    def run(self):
        """Main agent logic"""
        self.update_status('working', 'main_task')

        # Do work here

        self.update_status('idle')

if __name__ == '__main__':
    agent = MyAgent()
    agent.run()
```

### Best Practices

1. **Always register on startup**
2. **Update status during operations**
3. **Use task queue for trackability**
4. **Log to agents.db messages**
5. **Handle errors gracefully**
6. **Support daemon mode for long-running agents**
7. **Implement graceful shutdown (SIGINT)**

## 📊 Agent Monitoring

Query active agents:
```python
import sqlite3

conn = sqlite3.connect('collab/databases/agents.db')
agents = conn.execute("""
    SELECT id, name, status, current_task
    FROM agents
    WHERE status != 'stopped'
""").fetchall()

for agent in agents:
    print(f"{agent[0]}: {agent[1]} - {agent[2]} ({agent[3]})")
```

Query agent tasks:
```python
tasks = conn.execute("""
    SELECT agent_id, task_type, status, description
    FROM tasks
    ORDER BY created_at DESC
    LIMIT 20
""").fetchall()
```

## 🎨 ISA-88 PackML States

All agents follow PackML state machine:

```
IDLE → STARTING → EXECUTE → COMPLETING → COMPLETE → IDLE
                      ↓
                  ABORTING → ABORTED → CLEARING → IDLE
```

Implementation:
```python
class AgentStateMachine:
    states = ['idle', 'starting', 'execute', 'completing', 'complete',
              'aborting', 'aborted', 'clearing']

    def transition(self, new_state):
        if new_state in self.states:
            self.update_status(new_state)
```

## 🔗 Integration

Agents integrate with the module system:

```javascript
// Browser-based agent control
await ModuleLoader.load('agent-controller');

const controller = AgentController.init();
controller.startAgent('db-agent-001');
controller.getStatus('db-agent-001');
```

## 📚 References

- Main README: `/collab/README.md`
- Database schemas: `/collab/databases/README.md`
- Query examples: `/collab/queries/README.md`
- Project manifest: `/MANIFEST.md`

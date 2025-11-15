# Database Management Agent
**UUID:** d66a2866-a53f-402e-a21f-176cef24fd83
**Agent Type:** Database Administrator
**ISA Level:** L3 (MES/Data Layer)

Autonomous agent for database maintenance, optimization, and monitoring.

```python
#!/usr/bin/env python3
import sqlite3
import time
import json
from pathlib import Path
from datetime import datetime

class DatabaseAgent:
    """
    Autonomous agent for database management
    - Monitor database health
    - Optimize queries
    - Maintain indexes
    - Report statistics
    """

    def __init__(self, agent_id='db-agent-001'):
        self.agent_id = agent_id
        self.db_dir = Path(__file__).parent.parent / 'databases'
        self.agent_db = self.db_dir / 'agents.db'
        self.status = 'idle'
        self.current_task = None

        self.register()

    def register(self):
        """Register agent in agents.db"""
        conn = sqlite3.connect(self.agent_db)
        conn.execute("""
            INSERT OR REPLACE INTO agents (id, name, type, status, started_at, metadata)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            self.agent_id,
            'Database Management Agent',
            'database_admin',
            self.status,
            int(time.time()),
            json.dumps({'version': '1.0', 'capabilities': ['monitor', 'optimize', 'backup']})
        ))
        conn.commit()
        conn.close()

        print(f"✓ Agent {self.agent_id} registered")

    def update_status(self, status, task=None):
        """Update agent status"""
        self.status = status
        self.current_task = task

        conn = sqlite3.connect(self.agent_db)
        conn.execute("""
            UPDATE agents
            SET status = ?, current_task = ?
            WHERE id = ?
        """, (status, task, self.agent_id))
        conn.commit()
        conn.close()

    def create_task(self, task_type, description):
        """Create a task in task queue"""
        conn = sqlite3.connect(self.agent_db)
        cursor = conn.execute("""
            INSERT INTO tasks (agent_id, task_type, description, status)
            VALUES (?, ?, ?, 'pending')
        """, (self.agent_id, task_type, description))
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return task_id

    def complete_task(self, task_id, result):
        """Mark task as completed"""
        conn = sqlite3.connect(self.agent_db)
        conn.execute("""
            UPDATE tasks
            SET status = 'completed', result = ?, completed_at = ?
            WHERE id = ?
        """, (json.dumps(result), int(time.time()), task_id))
        conn.commit()
        conn.close()

    def check_health(self, db_name):
        """Check database health"""
        self.update_status('working', f'health_check:{db_name}')

        db_path = self.db_dir / db_name

        if not db_path.exists():
            return {'status': 'error', 'message': 'Database not found'}

        conn = sqlite3.connect(db_path)

        # Run integrity check
        cursor = conn.execute("PRAGMA integrity_check")
        integrity = cursor.fetchone()[0]

        # Get database size
        size_bytes = db_path.stat().st_size

        # Count tables
        cursor = conn.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
        table_count = cursor.fetchone()[0]

        conn.close()

        result = {
            'status': 'ok' if integrity == 'ok' else 'error',
            'integrity': integrity,
            'size_mb': size_bytes / 1024 / 1024,
            'tables': table_count,
            'checked_at': datetime.now().isoformat()
        }

        self.update_status('idle')
        return result

    def optimize(self, db_name):
        """Optimize database"""
        self.update_status('working', f'optimize:{db_name}')
        task_id = self.create_task('optimize', f'Optimizing {db_name}')

        db_path = self.db_dir / db_name
        conn = sqlite3.connect(db_path)

        # Run VACUUM
        conn.execute("VACUUM")

        # Analyze for query optimization
        conn.execute("ANALYZE")

        conn.close()

        result = {'optimized': db_name, 'timestamp': datetime.now().isoformat()}
        self.complete_task(task_id, result)
        self.update_status('idle')

        return result

    def monitor_all(self):
        """Monitor all databases"""
        print(f"\n🔍 Database Monitoring Report")
        print(f"Generated: {datetime.now().isoformat()}")
        print("=" * 80)

        for db_file in self.db_dir.glob('*.db'):
            health = self.check_health(db_file.name)

            status_icon = '✓' if health['status'] == 'ok' else '✗'
            print(f"\n{status_icon} {db_file.name}")
            print(f"  Size: {health['size_mb']:.2f} MB")
            print(f"  Tables: {health['tables']}")
            print(f"  Integrity: {health['integrity']}")

    def run(self, mode='once'):
        """Run agent"""
        print(f"🤖 Starting {self.agent_id} in {mode} mode")

        if mode == 'once':
            self.monitor_all()
        elif mode == 'daemon':
            print("Daemon mode: monitoring every 60 seconds (Ctrl+C to stop)")
            try:
                while True:
                    self.monitor_all()
                    time.sleep(60)
            except KeyboardInterrupt:
                print("\n👋 Agent stopped")
                self.update_status('stopped')

if __name__ == '__main__':
    import sys

    agent = DatabaseAgent()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'monitor':
            agent.monitor_all()
        elif command == 'health' and len(sys.argv) > 2:
            result = agent.check_health(sys.argv[2])
            print(json.dumps(result, indent=2))
        elif command == 'optimize' and len(sys.argv) > 2:
            result = agent.optimize(sys.argv[2])
            print(json.dumps(result, indent=2))
        elif command == 'daemon':
            agent.run('daemon')
        else:
            print("Usage: python agent-database.md <command> [args]")
            print("Commands:")
            print("  monitor              - Monitor all databases")
            print("  health <db>         - Check specific database")
            print("  optimize <db>       - Optimize database")
            print("  daemon              - Run in daemon mode")
    else:
        agent.run('once')
```

## Features

- ✅ Health monitoring
- ✅ Automatic optimization
- ✅ Task queue management
- ✅ Status reporting
- ✅ Daemon mode for continuous monitoring

## Usage

```bash
# Monitor all databases
python collab/agents/agent-database.md monitor

# Check specific database health
python collab/agents/agent-database.md health automationgpt.db

# Optimize database
python collab/agents/agent-database.md optimize modules.db

# Run as daemon (continuous monitoring)
python collab/agents/agent-database.md daemon
```

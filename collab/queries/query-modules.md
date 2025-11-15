# Query Modules Database
**UUID:** 67befcb1-c033-43a7-876c-41af2c5c2451
**Executable Query** | modules.db

Query the module registry database for dependencies and metadata.

## Quick Queries

```python
#!/usr/bin/env python3
import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'databases' / 'modules.db'

def connect():
    """Connect to modules database"""
    return sqlite3.connect(DB_PATH)

def list_all_modules():
    """List all registered modules"""
    conn = connect()
    cursor = conn.execute("""
        SELECT uuid, name, path, type, isa_level
        FROM modules
        ORDER BY isa_level DESC, name
    """)

    print("📦 All Modules:")
    print("-" * 80)
    for row in cursor.fetchall():
        uuid, name, path, mtype, level = row
        print(f"L{level or '?'} | {name:30} | {uuid[:8]}... | {mtype or 'unknown'}")

    conn.close()

def get_dependencies(module_name):
    """Get dependencies for a module"""
    conn = connect()

    # Get module UUID
    cursor = conn.execute("SELECT uuid FROM modules WHERE name = ?", (module_name,))
    row = cursor.fetchone()

    if not row:
        print(f"Module '{module_name}' not found")
        return

    module_uuid = row[0]

    # Get dependencies
    cursor = conn.execute("""
        SELECT m.name, d.dep_type
        FROM dependencies d
        JOIN modules m ON d.to_uuid = m.uuid
        WHERE d.from_uuid = ?
    """, (module_uuid,))

    print(f"\n🔗 Dependencies for {module_name}:")
    print("-" * 40)
    for dep_name, dep_type in cursor.fetchall():
        print(f"  → {dep_name} ({dep_type})")

    conn.close()

def get_dependents(module_name):
    """Get modules that depend on this module"""
    conn = connect()

    cursor = conn.execute("SELECT uuid FROM modules WHERE name = ?", (module_name,))
    row = cursor.fetchone()

    if not row:
        print(f"Module '{module_name}' not found")
        return

    module_uuid = row[0]

    cursor = conn.execute("""
        SELECT m.name, d.dep_type
        FROM dependencies d
        JOIN modules m ON d.from_uuid = m.uuid
        WHERE d.to_uuid = ?
    """, (module_uuid,))

    print(f"\n⬅️  Modules depending on {module_name}:")
    print("-" * 40)
    for dep_name, dep_type in cursor.fetchall():
        print(f"  ← {dep_name} ({dep_type})")

    conn.close()

def stats():
    """Get database statistics"""
    conn = connect()

    module_count = conn.execute("SELECT COUNT(*) FROM modules").fetchone()[0]
    dep_count = conn.execute("SELECT COUNT(*) FROM dependencies").fetchone()[0]

    # Count by ISA level
    cursor = conn.execute("""
        SELECT isa_level, COUNT(*)
        FROM modules
        WHERE isa_level IS NOT NULL
        GROUP BY isa_level
        ORDER BY isa_level DESC
    """)

    print("\n📊 Module Statistics:")
    print("-" * 40)
    print(f"Total modules: {module_count}")
    print(f"Total dependencies: {dep_count}")
    print("\nBy ISA Level:")
    for level, count in cursor.fetchall():
        print(f"  L{level}: {count} modules")

    conn.close()

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'list':
            list_all_modules()
        elif command == 'deps' and len(sys.argv) > 2:
            get_dependencies(sys.argv[2])
        elif command == 'dependents' and len(sys.argv) > 2:
            get_dependents(sys.argv[2])
        elif command == 'stats':
            stats()
        else:
            print("Usage: python query-modules.md <command> [args]")
            print("Commands:")
            print("  list                  - List all modules")
            print("  deps <module>        - Show dependencies")
            print("  dependents <module>  - Show dependents")
            print("  stats                - Show statistics")
    else:
        stats()
        print()
        list_all_modules()
```

## JavaScript Version

```javascript
// For browser-based queries
const ModuleQueries = {
  dbPath: '/collab/databases/modules.db',
  db: null,

  async init() {
    if (!window.SQL) {
      const SQL = await initSqlJs({
        locateFile: file => `https://sql.js.org/dist/${file}`
      });
      window.SQL = SQL;
    }

    const response = await fetch(this.dbPath);
    const buffer = await response.arrayBuffer();
    this.db = new window.SQL.Database(new Uint8Array(buffer));

    return this;
  },

  listAll() {
    const result = this.db.exec(`
      SELECT uuid, name, path, type, isa_level
      FROM modules
      ORDER BY isa_level DESC, name
    `);

    return result[0]?.values || [];
  },

  getDependencies(moduleName) {
    const result = this.db.exec(`
      SELECT m.name, d.dep_type
      FROM dependencies d
      JOIN modules m ON d.to_uuid = m.uuid
      WHERE d.from_uuid = (SELECT uuid FROM modules WHERE name = ?)
    `, [moduleName]);

    return result[0]?.values || [];
  },

  stats() {
    const moduleCount = this.db.exec("SELECT COUNT(*) FROM modules")[0].values[0][0];
    const depCount = this.db.exec("SELECT COUNT(*) FROM dependencies")[0].values[0][0];

    return { modules: moduleCount, dependencies: depCount };
  }
};

window.ModuleQueries = ModuleQueries;
```

## Example Usage

```bash
# List all modules
python collab/queries/query-modules.md list

# Show dependencies
python collab/queries/query-modules.md deps AutomationGPT

# Show what depends on a module
python collab/queries/query-modules.md dependents PackML

# Get statistics
python collab/queries/query-modules.md stats
```

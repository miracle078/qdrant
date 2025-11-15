# Module Management Agent
**UUID:** d60b9ca5-8f6f-4864-b47f-86c2d15135a5
**Agent Type:** Module Developer/Maintainer
**ISA Level:** L3-L4 (MES/Business)

Autonomous agent for module management, dependency tracking, and code generation.

```python
#!/usr/bin/env python3
import sqlite3
import json
import time
import re
from pathlib import Path
from datetime import datetime

class ModuleAgent:
    """
    Autonomous agent for module management
    - Register new modules
    - Track dependencies
    - Validate module structure
    - Generate module templates
    """

    def __init__(self, agent_id='module-agent-001'):
        self.agent_id = agent_id
        self.project_root = Path(__file__).parent.parent.parent
        self.modules_dir = self.project_root / 'modules'
        self.modules_db = self.project_root / 'collab' / 'databases' / 'modules.db'
        self.agent_db = self.project_root / 'collab' / 'databases' / 'agents.db'
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
            'Module Management Agent',
            'module_developer',
            self.status,
            int(time.time()),
            json.dumps({
                'version': '1.0',
                'capabilities': ['register', 'validate', 'track_deps', 'generate']
            })
        ))
        conn.commit()
        conn.close()

        print(f"✓ Agent {self.agent_id} registered")

    def scan_modules(self):
        """Scan modules directory and register in database"""
        print(f"🔍 Scanning {self.modules_dir}...")

        conn = sqlite3.connect(self.modules_db)
        registered = 0

        for md_file in self.modules_dir.glob('*.md'):
            content = md_file.read_text()

            # Extract UUID from header
            uuid_match = re.search(r'\*\*UUID:\*\*\s*`?([a-f0-9-]{36})`?', content)
            uuid = uuid_match.group(1) if uuid_match else None

            # Extract module name from window export
            name_match = re.search(r'window\.(\w+)\s*=', content)
            module_name = name_match.group(1) if name_match else md_file.stem

            # Determine ISA level
            isa_match = re.search(r'ISA-95\s+L(\d)', content)
            isa_level = int(isa_match.group(1)) if isa_match else None

            # Determine type
            module_type = 'unknown'
            if 'agent' in md_file.name:
                module_type = 'agent'
            elif 'api-' in md_file.name:
                module_type = 'api'
            elif 'embed-' in md_file.name:
                module_type = 'embedding'
            elif 'regulatory-' in md_file.name:
                module_type = 'regulatory'
            elif 'chazon-' in md_file.name:
                module_type = 'core'

            if uuid:
                try:
                    conn.execute("""
                        INSERT OR REPLACE INTO modules (uuid, name, path, type, isa_level)
                        VALUES (?, ?, ?, ?, ?)
                    """, (uuid, module_name, str(md_file.relative_to(self.project_root)),
                          module_type, isa_level))
                    registered += 1
                except sqlite3.Error as e:
                    print(f"⚠️  Error registering {module_name}: {e}")

        conn.commit()
        conn.close()

        print(f"✓ Registered {registered} modules")
        return registered

    def validate_module(self, module_path):
        """Validate module structure"""
        md_file = Path(module_path)

        if not md_file.exists():
            return {'valid': False, 'error': 'File not found'}

        content = md_file.read_text()
        issues = []

        # Check UUID
        if not re.search(r'\*\*UUID:\*\*\s*`?[a-f0-9-]{36}`?', content):
            issues.append('Missing UUID header')

        # Check JavaScript export
        if not re.search(r'window\.\w+\s*=', content):
            issues.append('No window export found')

        # Check code block
        if '```javascript' not in content and '```js' not in content:
            issues.append('No JavaScript code block')

        # Estimate token count (rough)
        words = len(content.split())
        if words > 250:
            issues.append(f'Exceeds 250 token limit (~{words} words)')

        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'words': words,
            'path': str(md_file)
        }

    def track_dependencies(self, module_name):
        """Track module dependencies by analyzing imports"""
        conn = sqlite3.connect(self.modules_db)

        # Get module info
        cursor = conn.execute("SELECT uuid, path FROM modules WHERE name = ?", (module_name,))
        row = cursor.fetchone()

        if not row:
            print(f"Module {module_name} not found in database")
            return

        module_uuid, module_path = row

        # Read module content
        content = (self.project_root / module_path).read_text()

        # Find dependencies (references to window.OtherModule)
        deps = re.findall(r'window\.(\w+)', content)
        deps = [d for d in set(deps) if d != module_name]

        # Clear existing dependencies
        conn.execute("DELETE FROM dependencies WHERE from_uuid = ?", (module_uuid,))

        # Add new dependencies
        for dep_name in deps:
            cursor = conn.execute("SELECT uuid FROM modules WHERE name = ?", (dep_name,))
            dep_row = cursor.fetchone()

            if dep_row:
                dep_uuid = dep_row[0]
                conn.execute("""
                    INSERT OR IGNORE INTO dependencies (from_uuid, to_uuid, dep_type)
                    VALUES (?, ?, 'requires')
                """, (module_uuid, dep_uuid))

        conn.commit()
        conn.close()

        print(f"✓ Tracked {len(deps)} dependencies for {module_name}")
        return deps

    def generate_template(self, module_name, module_type='core', isa_level=3):
        """Generate module template"""
        import uuid

        new_uuid = str(uuid.uuid4())

        template = f"""# {module_name}
**UUID:** {new_uuid}
**{module_type.title()} Module** | ISA-95 L{isa_level}

Description of {module_name} module.

```javascript
const {module_name} = {{
  init() {{
    console.log('{module_name} initialized');
    return this;
  }},

  // Add methods here
}};

window.{module_name} = {module_name};
```

## Usage

```javascript
// Initialize
await ModuleLoader.load('{module_name.lower()}');

// Use
{module_name}.init();
```
"""

        output_path = self.modules_dir / f"{module_name.lower().replace('_', '-')}.md"

        if output_path.exists():
            print(f"⚠️  Module {output_path.name} already exists")
            return None

        output_path.write_text(template)
        print(f"✓ Generated template: {output_path}")

        return str(output_path)

    def report(self):
        """Generate module report"""
        conn = sqlite3.connect(self.modules_db)

        # Total modules
        total = conn.execute("SELECT COUNT(*) FROM modules").fetchone()[0]

        # By type
        cursor = conn.execute("""
            SELECT type, COUNT(*)
            FROM modules
            GROUP BY type
            ORDER BY COUNT(*) DESC
        """)

        print(f"\n📊 Module Report")
        print("=" * 80)
        print(f"Total modules: {total}\n")
        print("By Type:")
        for mtype, count in cursor.fetchall():
            print(f"  {mtype:20} {count:3} modules")

        # By ISA level
        cursor = conn.execute("""
            SELECT isa_level, COUNT(*)
            FROM modules
            WHERE isa_level IS NOT NULL
            GROUP BY isa_level
            ORDER BY isa_level DESC
        """)

        print("\nBy ISA Level:")
        for level, count in cursor.fetchall():
            print(f"  L{level}: {count} modules")

        # Most dependencies
        cursor = conn.execute("""
            SELECT m.name, COUNT(d.to_uuid) as dep_count
            FROM modules m
            LEFT JOIN dependencies d ON m.uuid = d.from_uuid
            GROUP BY m.uuid
            ORDER BY dep_count DESC
            LIMIT 5
        """)

        print("\nMost Dependencies:")
        for name, count in cursor.fetchall():
            print(f"  {name:30} {count} deps")

        conn.close()

if __name__ == '__main__':
    import sys

    agent = ModuleAgent()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'scan':
            agent.scan_modules()
        elif command == 'validate' and len(sys.argv) > 2:
            result = agent.validate_module(sys.argv[2])
            print(json.dumps(result, indent=2))
        elif command == 'deps' and len(sys.argv) > 2:
            agent.track_dependencies(sys.argv[2])
        elif command == 'generate' and len(sys.argv) > 2:
            agent.generate_template(sys.argv[2])
        elif command == 'report':
            agent.report()
        else:
            print("Usage: python agent-module.md <command> [args]")
            print("Commands:")
            print("  scan                  - Scan and register all modules")
            print("  validate <path>      - Validate module structure")
            print("  deps <module>        - Track module dependencies")
            print("  generate <name>      - Generate module template")
            print("  report               - Generate module report")
    else:
        agent.scan_modules()
        agent.report()
```

## Features

- ✅ Automatic module scanning and registration
- ✅ UUID extraction and tracking
- ✅ Dependency graph construction
- ✅ Module validation (structure, size, exports)
- ✅ Template generation
- ✅ ISA level classification

## Usage

```bash
# Scan and register all modules
python collab/agents/agent-module.md scan

# Validate a module
python collab/agents/agent-module.md validate modules/my-module.md

# Track dependencies
python collab/agents/agent-module.md deps AutomationGPT

# Generate new module template
python collab/agents/agent-module.md generate MyNewModule

# Get module report
python collab/agents/agent-module.md report
```

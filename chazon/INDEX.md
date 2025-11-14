# 🌌 Chazon OS - Complete Index

**φ-Balanced Computing | ISA-Compliant | Client-Side Framework**

## Architecture Overview

```
chazon/
├── core/           # OS kernel, compiler, CLI, state management (5 files)
├── agents/         # CI/CD agents with ISA-95 L0-L4 (4 files)
├── ui/             # Desktop environment (7 files)
├── isa/            # Standards & compliance (2 files)
└── programs/       # Sample programs (8 files)
```

**Total: 27 markdown files | ~6,500 tokens | All < 250 tokens**

---

## Module Breakdown

### Core Framework (5 files)

| File | Tokens | ISA Level | Purpose |
|------|--------|-----------|---------|
| os.md | ~158 | L4 | OS kernel, module loading, event bus |
| mdcompiler.md | ~183 | L3 | Markdown → JavaScript compiler |
| cli.md | ~244 | L2 | Command-line interface |
| state.md | ~202 | L1 | Persistent state via localStorage |
| index.md | ~214 | - | Core architecture documentation |

### CI/CD Agents (4 files)

| File | Tokens | ISA Level | Purpose |
|------|--------|-----------|---------|
| ci.md | ~234 | L0-L4 | Complete agent hierarchy |
| test.md | ~193 | L1 | Unit testing with ISA-18.2 alarms |
| deploy.md | ~184 | L4 | Deployment with ISA-88 batch control |
| index.md | ~235 | - | Pipeline documentation |

### UI System (7 files)

| File | Tokens | ISA Level | Purpose |
|------|--------|-----------|---------|
| desktop.md | ~109 | - | Desktop foundation |
| windows.md | ~243 | - | Window manager with φ-cascade |
| icons.md | ~146 | - | Desktop icon grid |
| taskbar.md | ~165 | - | App management & live clock |
| theme.md | ~165 | - | 3 color themes |
| index.md | ~157 | - | UI orchestrator |
| README.md | - | - | Complete UI documentation |

### Programs (8 files)

| File | Tokens | ISA Level | Purpose |
|------|--------|-----------|---------|
| hello.md | ~40 | L0 | Hello World, basic execution |
| calculator.md | ~70 | L1 | Math operations, object methods |
| data.md | ~83 | L1 | Functional programming, transformations |
| search.md | ~89 | L2 | Mock Qdrant vector search |
| events.md | ~71 | L2 | Event-driven architecture |
| neural.md | ~78 | L3 | φ-balanced neural network |
| cicd.md | ~95 | L3-L4 | Complete CI/CD pipeline |
| index.md | ~129 | - | Program catalog |

### ISA Standards (2 files)

| File | Tokens | ISA Level | Purpose |
|------|--------|-----------|---------|
| standards.md | ~134 | - | ISA-95, ISA-88, ISA-18.2 definitions |
| compliance.md | ~160 | - | 21 CFR Part 11, EU Annex 11 checking |

---

## Bootstrap Sequence

```javascript
// 1. Load Compiler (first, needed for all others)
MDCompiler

// 2. Load Core
ChazonOS → ChazonCLI → StateManager

// 3. Load Agents
ChazonAgents → TestAgent → DeployAgent

// 4. Load UI
ChazonUI → WindowManager → IconManager → Taskbar → ThemeSystem → ChazonUISystem

// 5. Load Standards
ISAStandards → ComplianceChecker

// 6. Load Programs
hello.md, calculator.md, data.md, search.md, events.md, neural.md, cicd.md
```

---

## φ-Balanced Design

Golden ratio (φ = 1.618) applied throughout:

- **Window cascade**: `left = 50 + n × 30 × φ`
- **Icon spacing**: `20 + row × 100 × φ`
- **Compiler timeout**: `1618ms` (φ × 1000)
- **State cache**: `161 items` (φ × 100)
- **Color schemes**: φ-aesthetic principles
- **File sizes**: Target ~160 tokens (φ × 100)

---

## ISA Standards Compliance

**ISA-95 Automation Hierarchy:**
- L4: Business Planning (os.md, deploy.md)
- L3: MES/Control (mdcompiler.md, neural.md, cicd.md)
- L2: Supervisory (cli.md, search.md, events.md)
- L1: Basic Control (state.md, test.md, calculator.md, data.md)
- L0: Physical Process (hello.md, ci.md)

**ISA-88 Batch Control:**
- Deployment phases in deploy.md
- Prepare → Execute → Complete → Abort

**ISA-18.2 Alarm Management:**
- Priority levels (HIGH, MEDIUM, LOW)
- Alarm types (TEST_FAILURE)
- Integrated in test.md

---

## Usage

**Bootstrap:**
```bash
open chazon.html
```

**CLI Commands:**
```
help              - Show commands
ls                - List programs
run hello.md      - Run program
cat calculator.md - View source
demo              - Run demo programs
clear             - Clear terminal
```

**Direct API:**
```javascript
// Run program
const results = MDCompiler.compile(markdown);

// Execute via CLI
ChazonCLI.exec('run neural.md');

// Spawn CI/CD agent
ChazonAgents.spawn('L4_Deploy', task);

// Check compliance
ComplianceChecker.check(program, '21_CFR_11');
```

---

## File Locations

All files: `/home/user/qdrant/chazon/`

Bootstrap: `/home/user/qdrant/chazon.html`

Landing: `/home/user/qdrant/index.html`

---

## GitHub Pages

**Live URLs:**
- Landing: `https://teslasolar.github.io/qdrant/`
- Chazon OS: `https://teslasolar.github.io/qdrant/chazon.html`
- AutomationGPT: `https://teslasolar.github.io/qdrant/automationgpt.html`

**Setup:**
1. Enable GitHub Pages in repo settings
2. Source: Branch `claude/automation-gpt-multimodal-search-013LkL58AK8txgYpiizQcrsA`
3. All files are client-side ready

---

**Built with φ-balance for the automation community** 🌌

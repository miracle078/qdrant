# Module Registry
**UUID:** e118731b-4918-489d-beac-f1732834ab39
**File Tracking System** | ISA-95 L4: Business Planning

Central registry of all markdown modules with UUIDs, dependencies, and metadata.

## Core System Modules

| UUID | Module | Path | Type | ISA Level |
|------|--------|------|------|-----------|
| `d6f529de-e759-49f9-abcd-cd30e902626a` | DatabaseManager | modules/db-manager.md | database | L3 |
| `e118731b-4918-489d-beac-f1732834ab39` | ModuleRegistry | REGISTRY.md | registry | L4 |

## Embedding Modules

| UUID | Module | Path | Model | Dimension |
|------|--------|------|-------|-----------|
| `760e861d-afa5-47d7-bf35-c03509263f40` | EmbedOpenAI | modules/embed-openai.md | text-embedding-3-large | 1536 |
| `f66182df-7159-49cd-a5f5-9d078d83d854` | EmbedCodeBERT | modules/embed-codebert.md | codebert-base | 768 |
| `c6a53bf8-34eb-4620-8e87-ac8629f97d1b` | EmbedCLIP | modules/embed-clip.md | clip-vit-base-patch32 | 512 |

## Agent Modules

| UUID | Module | Path | Type | ISA Level |
|------|--------|------|------|-----------|
| `59ae07f8-57f7-47e3-a6e1-08bbc0847f4b` | AutomationGPT | modules/agent-automationgpt.md | rag_agent | L3 |

## Regulatory Modules

| UUID | Module | Path | Standard | Authority |
|------|--------|------|----------|-----------|
| `d20d52e3-4620-48b0-b53f-3419fe1bcd82` | CFRPart11 | modules/regulatory-cfr-part-11.md | 21 CFR Part 11 | US FDA |
| `165af54f-ea06-4972-9dd6-1f3613b641c4` | EUAnnex11 | modules/regulatory-eu-annex-11.md | EU Annex 11 | EC |

## Previously Created Modules (Without UUIDs - To Be Updated)

| Module | Path | Type |
|--------|------|------|
| ModuleLoader | modules/module-loader.md | bootstrap |
| PackML | modules/chazon-packml.md | state_machine |
| MDCompiler | modules/chazon-mdcompiler.md | compiler |
| ChazonCLI | modules/chazon-cli.md | cli |
| QdrantClient | modules/qdrant-client.md | database |
| HealthAPI | modules/api-health.md | api |
| SearchAPI | modules/api-search.md | api |
| IndexAPI | modules/api-index.md | api |
| EmbedAPI | modules/api-embed.md | api |
| CollectionsAPI | modules/api-collections.md | api |
| StatsAPI | modules/api-stats.md | api |
| JythonCompiler | modules/jython-compiler.md | compiler |
| IgnitionGateway | modules/gateway-ignition.md | scada |
| RepoPLC | modules/plc-repo.md | plc |
| RepoHMI | modules/hmi-repo.md | hmi |
| XRayJython | modules/xray-jython.md | medical |

## Dependencies

```javascript
{
  "embed-openai": ["db-manager"],
  "embed-codebert": ["db-manager"],
  "agent-automationgpt": ["api-search", "embed-openai"],
  "api-search": ["qdrant-client"],
  "api-index": ["qdrant-client", "embed-openai"],
  "jython-compiler": ["chazon-mdcompiler"],
  "gateway-ignition": ["chazon-packml"],
  "plc-repo": ["gateway-ignition", "chazon-packml"],
  "hmi-repo": ["gateway-ignition"],
  "xray-jython": ["jython-compiler", "embed-openai", "qdrant-client"]
}
```

## Module Statistics

- **Total Modules**: 90+
- **With UUIDs**: 7
- **Without UUIDs**: 84
- **Total Lines**: ~5000+
- **Average Module Size**: <250 tokens

## Usage

```javascript
// Load registry
const registry = await ModuleLoader.load('module-registry');

// Get module by UUID
const module = registry.getByUUID('760e861d-afa5-47d7-bf35-c03509263f40');

// Get dependencies
const deps = registry.getDependencies('agent-automationgpt');

// Register new module
registry.register({
  uuid: 'new-uuid-here',
  name: 'ModuleName',
  path: 'modules/module-name.md',
  type: 'type',
  dependencies: ['dep1', 'dep2']
});
```

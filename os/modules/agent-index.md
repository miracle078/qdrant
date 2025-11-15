# Chazon CI/CD Agents
**ISA-95 Automation Hierarchy** | Intelligent Agent Pipeline

## Architecture Overview

```
L0: Execute    → Run code directly (field device level)
L1: Unit       → Individual test execution (cell/unit control)
L2: Integration→ Module integration (area supervisory)
L3: System     → Full system validation (site operations)
L4: Deploy     → Production deployment (business planning)
```

## Agent Pipeline

```javascript
// Complete CI/CD Pipeline
const pipeline = async (program) => {
  // L1: Unit Testing (ISA-18.2 alarms)
  const tests = await TestAgent.run(program.tests);

  // L2-L3: Integration & System (ISA-95)
  const validation = await ChazonAgents.L3_System(program);

  // L4: Deployment (ISA-88 batch)
  if (validation.passed) {
    return await DeployAgent.deploy(program);
  }

  return { error: 'Pipeline failed', tests, validation };
};
```

## Standards Compliance

- **ISA-95**: L0-L4 automation hierarchy
- **ISA-88**: Batch control patterns (deploy phases)
- **ISA-18.2**: Alarm management (test failures)

## Usage

```javascript
// Load agents
const program = {
  name: 'MyApp',
  code: 'x => x * 2',
  tests: [{ name: 'double', code: '2*2', expect: 4 }],
  modules: [{ code: 'true' }]
};

// Run pipeline
pipeline(program).then(console.log);
```

All agents work together: **Test** validates (L1), **CI** orchestrates (L0-L3), **Deploy** ships (L4).

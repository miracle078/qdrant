# Deploy Agent
**ISA-95 L4** | Deployment Orchestration

Deploy programs to production after validation.

```javascript
const DeployAgent = {
  deploy(program) {
    console.log(`📦 Deploying: ${program.name}`);

    const validation = this.validate(program);
    if (!validation.passed) {
      console.error('❌ Validation failed:', validation.errors);
      return { deployed: false, errors: validation.errors };
    }

    const deployment = {
      name: program.name,
      version: program.version || '1.0.0',
      timestamp: new Date().toISOString(),
      status: 'deployed',
      url: `chazon://programs/${program.name}`
    };

    console.log(`✅ Deployed ${program.name} v${deployment.version}`);
    return deployment;
  },

  validate(program) {
    const errors = [];

    if (!program.name) errors.push('Missing program name');
    if (!program.code && !program.content) errors.push('Missing code/content');
    if (program.isa_level > 4) errors.push('Invalid ISA level');

    return {
      passed: errors.length === 0,
      errors
    };
  },

  rollback(program) {
    console.log(`⏪ Rolling back: ${program.name}`);
    return { rolledBack: true, reason: 'Manual rollback' };
  }
};

window.DeployAgent = DeployAgent;
```

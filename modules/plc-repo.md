# Repository PLC Controller
**Repo Logic Control** | ISA-95 L1

PLC-style controller for GitHub repository operations using ladder logic patterns.

```javascript
const RepoPLC = {
  state: PackML.create('RepoPLC'),
  scan: 100, // ms
  program: {},

  init() {
    PackML.setState(this.state, 'STARTING');
    this.loadProgram();
    this.startScan();
    PackML.setState(this.state, 'EXECUTE');
  },

  loadProgram() {
    // Ladder logic for repo control
    this.program = {
      // Rung 1: File change detection
      rung1() {
        const fileChanged = IgnitionGateway.readTag('[Repo]FileCount').value > 70;
        if (fileChanged) {
          IgnitionGateway.writeTag('[Production]ModulesBuilt', 1);
        }
      },

      // Rung 2: Build trigger
      rung2() {
        const needsBuild = IgnitionGateway.readTag('[Repo]CommitRate').value > 0;
        const buildStatus = IgnitionGateway.readTag('[Repo]BuildStatus').value;

        if (needsBuild && buildStatus !== 'Running') {
          console.log('⚙️ PLC: Triggering build');
          IgnitionGateway.writeTag('[Repo]BuildStatus', 'Running');
        }
      },

      // Rung 3: Quality check
      rung3() {
        const quality = IgnitionGateway.readTag('[Production]QualityScore').value;

        if (quality < 80) {
          IgnitionGateway.raiseAlarm('Quality below threshold', 'High');
        }
      },

      // Rung 4: Component assembly
      rung4() {
        const modulesBuilt = IgnitionGateway.readTag('[Production]ModulesBuilt').value;

        if (modulesBuilt > 0) {
          const current = IgnitionGateway.readTag('[Production]ComponentsAssembled').value;
          IgnitionGateway.writeTag('[Production]ComponentsAssembled', current + 1);
        }
      }
    };
  },

  startScan() {
    setInterval(() => {
      if (PackML.getState(this.state) === 'EXECUTE') {
        this.scanProgram();
      }
    }, this.scan);
  },

  scanProgram() {
    // Execute all rungs in sequence
    Object.values(this.program).forEach(rung => {
      try {
        rung();
      } catch (err) {
        console.error('PLC Fault:', err);
        PackML.setState(this.state, 'ABORTED');
      }
    });
  }
};

window.RepoPLC = RepoPLC;
```

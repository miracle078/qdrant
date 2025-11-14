# ISA Standards
**ISA-95, ISA-88, ISA-18.2** | Automation Hierarchy Definitions

Define ISA automation levels and standards mappings.

```javascript
const ISAStandards = {
  'ISA-95': {
    name: 'Enterprise-Control System Integration',
    levels: {
      L4: { name: 'Business Planning', scope: 'Enterprise/ERP' },
      L3: { name: 'Manufacturing Operations', scope: 'MES' },
      L2: { name: 'Supervisory Control', scope: 'SCADA/HMI' },
      L1: { name: 'Basic Control', scope: 'PLC/DCS' },
      L0: { name: 'Physical Process', scope: 'Sensors/Actuators' }
    }
  },

  'ISA-88': {
    name: 'Batch Control',
    hierarchy: ['Process', 'Unit', 'Operation', 'Phase', 'Step'],
    modes: ['Manual', 'Semi-Auto', 'Auto']
  },

  'ISA-18.2': {
    name: 'Alarm Management',
    priorities: ['Critical', 'High', 'Medium', 'Low'],
    states: ['Unacknowledged', 'Acknowledged', 'Cleared']
  },

  mapLevel(task) {
    if (task.includes('deploy')) return 4;
    if (task.includes('test')) return 3;
    if (task.includes('control')) return 2;
    if (task.includes('execute')) return 1;
    return 0;
  },

  getLevel(num) {
    return this['ISA-95'].levels[`L${num}`];
  }
};

window.ISAStandards = ISAStandards;
```

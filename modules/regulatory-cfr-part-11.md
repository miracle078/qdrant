# 21 CFR Part 11
**UUID:** d20d52e3-4620-48b0-b53f-3419fe1bcd82
**21 CFR Part 11** | Electronic Records & Signatures (FDA)

US FDA regulation for GMP systems with ISA-95 mapping.

```javascript
const CFRPart11 = {
  regulation: '21 CFR Part 11',
  authority: 'US FDA',
  year: 1997,
  scope: 'Electronic records & signatures in FDA-regulated activities',

  // Subpart B: Electronic Records (11.10)
  controls: {
    '11.10a': {
      control: 'System Validation',
      desc: 'IQ/OQ/PQ protocols for system accuracy and reliability',
      isaLevel: 'L3',
      implementation: ['IQ', 'OQ', 'PQ']
    },
    '11.10b': {
      control: 'Audit Trail',
      desc: 'Immutable audit trail: who, what, when, why',
      isaLevel: 'L2-L3',
      fields: ['timestamp', 'user_id', 'action', 'old_value', 'new_value', 'reason'],
      immutable: true
    },
    '11.10c': {
      control: 'Authority Checks',
      desc: 'RBAC for enforcing authorized access',
      isaLevel: 'L3',
      tech: ['LDAP', 'Active_Directory', 'MFA']
    },
    '11.10d': {
      control: 'Device Checks',
      desc: 'Device authentication and validation',
      isaLevel: 'L1-L2',
      tech: ['certificates', 'device_fingerprinting']
    },
    '11.10e': {
      control: 'Training',
      desc: 'Document training with annual refresher',
      isaLevel: 'L4',
      frequency: 'annual'
    },
    '11.10f': {
      control: 'Data Integrity',
      desc: 'Checksums, hash validation, backup/recovery',
      isaLevel: 'L2-L3',
      tech: ['SHA-256', 'MD5', 'CRC']
    },
    '11.200': {
      control: 'Two-Component E-Signature',
      desc: 'ID + password/biometric required',
      isaLevel: 'L3',
      components: ['user_id', 'password_or_biometric']
    },
    '11.300': {
      control: 'Password Management',
      desc: 'Unique IDs, periodic change, session timeout',
      isaLevel: 'L3',
      requirements: ['uniqueness', 'periodic_change', 'complexity', 'session_timeout']
    }
  },

  // Get requirements for ingestion
  getRequirements() {
    return Object.entries(this.controls).map(([sec, ctrl]) => ({
      txt: `21 CFR Part 11 ${sec}: ${ctrl.control} - ${ctrl.desc}`,
      std: '21 CFR Part 11',
      sec,
      type: ctrl.control.toLowerCase().replace(/\s+/g, '_'),
      isa_level: parseInt(ctrl.isaLevel.replace('L', '').split('-')[0]),
      control: ctrl.control,
      diff: 'advanced'
    }));
  }
};

window.CFRPart11 = CFRPart11;
```

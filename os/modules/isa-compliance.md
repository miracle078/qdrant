# Compliance Checker
**21 CFR Part 11, EU Annex 11** | Regulatory Validation

Check programs for regulatory compliance.

```javascript
const ComplianceChecker = {
  regulations: {
    '21_CFR_11': {
      name: '21 CFR Part 11',
      authority: 'US FDA',
      requirements: ['audit_trail', 'e_signature', 'validation', 'access_control']
    },
    'EU_ANNEX_11': {
      name: 'EU Annex 11',
      authority: 'European Commission',
      requirements: ['risk_management', 'validation', 'data_integrity']
    }
  },

  check(program, regulation) {
    const reg = this.regulations[regulation];
    if (!reg) return { compliant: false, error: 'Unknown regulation' };

    const checks = reg.requirements.map(req => ({
      requirement: req,
      passed: this.validate(program, req)
    }));

    const passed = checks.every(c => c.passed);

    return {
      regulation: reg.name,
      compliant: passed,
      checks,
      isa_level: program.isa_level || 3
    };
  },

  validate(program, requirement) {
    const validators = {
      audit_trail: p => p.logging === true,
      e_signature: p => p.auth === true,
      validation: p => p.tested === true,
      access_control: p => p.permissions !== undefined,
      risk_management: p => p.risk_level !== undefined,
      data_integrity: p => p.checksum !== undefined
    };

    return validators[requirement] ? validators[requirement](program) : false;
  }
};

window.ComplianceChecker = ComplianceChecker;
```

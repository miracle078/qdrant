# EU Annex 11
**UUID:** 165af54f-ea06-4972-9dd6-1f3613b641c4
**EU Annex 11** | Computerised Systems (EudraLex Vol 4)

EU GMP regulation for pharma manufacturing with risk-based approach.

```javascript
const EUAnnex11 = {
  regulation: 'EU Annex 11',
  fullName: 'EudraLex Volume 4, Annex 11: Computerised Systems',
  authority: 'European Commission',
  year: 2011,
  scope: 'Computerised systems in GMP for medicinal products',
  approach: 'risk_based',

  sections: {
    '1': {
      title: 'Risk Management',
      desc: 'GAMP 5 categories throughout lifecycle',
      isaLevel: 'L4',
      gamp: {1: 'Infrastructure', 3: 'Non-configured', 4: 'Configured', 5: 'Custom'}
    },
    '2': {
      title: 'Validation',
      desc: 'Documented evidence system does what it purports',
      isaLevel: 'L3',
      lifecycle: ['plan', 'specify', 'test', 'approve', 'review']
    },
    '4': {
      title: 'Accuracy Checks',
      desc: 'Second-person or electronic validation for critical data',
      isaLevel: 'L2',
      methods: ['second_person_check', 'electronic_validation']
    },
    '9': {
      title: 'Audit Trail',
      desc: 'Risk-based audit trail: who, what, when, why',
      isaLevel: 'L3',
      fields: ['who', 'what', 'when', 'why'],
      riskBased: true
    },
    '12.1': {
      title: 'Physical Security',
      desc: 'Physical/logical controls for access restriction',
      isaLevel: 'L3',
      controls: ['access_badges', 'locks', 'surveillance']
    },
    '12.4': {
      title: 'Electronic Signature',
      desc: 'Unique e-signatures cryptographically linked to records',
      isaLevel: 'L3',
      requirements: ['uniqueness', 'cryptographic_linking', 'legal_equivalence']
    },
    '13': {
      title: 'Change Control',
      desc: 'Impact assessment for all system changes',
      isaLevel: 'L3',
      process: ['request', 'assess', 'approve', 'test', 'implement', 'verify']
    },
    '15': {
      title: 'Business Continuity',
      desc: 'Backup, disaster recovery, manual procedures',
      isaLevel: 'L4',
      requirements: ['backup_systems', 'disaster_recovery', 'manual_fallback']
    },
    '17': {
      title: 'Batch Release',
      desc: 'Qualified Person only for batch certification',
      isaLevel: 'L3',
      isaMapping: 'isa-88-batch-record',
      requirements: ['qualified_person_only', 'electronic_record', 'print_capability']
    }
  },

  getRequirements() {
    return Object.entries(this.sections).map(([sec, s]) => ({
      txt: `EU Annex 11 Section ${sec}: ${s.title} - ${s.desc}`,
      std: 'EU Annex 11',
      sec,
      type: s.title.toLowerCase().replace(/\s+/g, '_'),
      isa_level: parseInt(s.isaLevel.replace('L', '')),
      diff: 'advanced'
    }));
  }
};

window.EUAnnex11 = EUAnnex11;
```

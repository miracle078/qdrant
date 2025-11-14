"""
EU Annex 11 - Computerised Systems (EudraLex Volume 4)
EU GMP Regulation - Pharma Manufacturing

Structured as ISA-style UDTs (User Defined Types)
"""

from typing import Dict, List, Any

# EU Annex 11 UDT - ISA Style Structure
EU_ANNEX_11_UDT = {
    "regulation": "EU Annex 11",
    "full_name": "EudraLex Volume 4, Annex 11: Computerised Systems",
    "authority": "European Commission (EC)",
    "year": 2011,
    "scope": "Computerised systems in GMP activities for medicinal products",
    "applicability": ["pharma_manufacturing", "clinical_trials"],
    "approach": "risk_based",

    # Principle
    "principle": {
        "statement": "This annex applies to all forms of computerised systems used as part of a GMP regulated activity.",
        "risk_management": "A risk management approach should determine the extent of validation and data integrity controls.",
        "isa_mapping": "isa-95-L2-L3-L4"
    },

    # Section 1: Risk Management
    "risk_management": {
        "name": "Risk Management",
        "requirements": {
            "risk_assessment": {
                "requirement": "Risk management should be applied throughout lifecycle",
                "level": "isa-95-L4",
                "approach": "GAMP 5 categories",
                "categories": {
                    "1": "Infrastructure software (low risk)",
                    "3": "Non-configured products (medium risk)",
                    "4": "Configured products (medium-high risk)",
                    "5": "Custom applications (high risk)"
                }
            },
            "criticality": {
                "requirement": "Assess impact on product quality and patient safety",
                "level": "isa-95-L3",
                "factors": ["gxp_impact", "patient_safety", "data_integrity"]
            }
        }
    },

    # Section 2-12: Project Phase
    "project_phase": {
        "name": "Project Phase",
        "sections": {
            "2_validation": {
                "title": "Validation",
                "requirement": "Documented evidence that system does what it purports to do",
                "level": "isa-95-L3",
                "lifecycle": ["planning", "specification", "testing", "approval", "review"],
                "isa_mapping": "isa-95-L3-MES"
            },
            "3_system_design": {
                "title": "System",
                "requirement": "System should be designed to facilitate data review",
                "level": "isa-95-L3",
                "requirements": {
                    "data_retention": "Allow complete data review",
                    "audit_trail": "Record changes and deletions",
                    "interfaces": "Validated interfaces to other systems"
                }
            },
            "4_accuracy_checks": {
                "title": "Accuracy Checks",
                "requirement": "Input/output checks for critical data",
                "level": "isa-95-L2-L3",
                "isa_mapping": "isa-95-L2-supervisory-control",
                "example": "Recipe parameter range checks"
            }
        }
    },

    # Section 13-17: Operational Phase
    "operational_phase": {
        "name": "Operational Phase",
        "sections": {
            "5_security": {
                "title": "Security",
                "requirement": "Physical and logical security",
                "level": "isa-95-L3",
                "controls": ["access_control", "data_protection", "virus_protection"]
            },
            "6_incident_management": {
                "title": "Incident Management",
                "requirement": "Procedures to handle system failures and data errors",
                "level": "isa-95-L3",
                "isa_mapping": "isa-18.2-alarm-management",
                "response": ["investigation", "corrective_action", "preventive_action"]
            },
            "7_electronic_signature": {
                "title": "Electronic Signature",
                "requirement": "E-signatures should be linked to their respective record",
                "level": "isa-95-L3",
                "equivalence": "Same legal standing as handwritten signatures",
                "difference_from_cfr": "Less prescriptive than 21 CFR Part 11"
            },
            "8_batch_release": {
                "title": "Batch Release",
                "requirement": "Electronic records for batch release must be accurate and complete",
                "level": "isa-95-L3",
                "isa_mapping": "isa-88-batch-record",
                "requirements": ["traceability", "integrity", "accessibility"]
            },
            "9_business_continuity": {
                "title": "Business Continuity",
                "requirement": "Alternative arrangements for systems critical to product quality",
                "level": "isa-95-L4",
                "requirements": ["backup", "disaster_recovery", "manual_procedures"]
            },
            "10_change_control": {
                "title": "Change and Configuration Management",
                "requirement": "Changes should not affect product quality or data integrity",
                "level": "isa-95-L3",
                "process": ["change_request", "impact_assessment", "approval", "testing", "implementation"]
            },
            "11_periodic_evaluation": {
                "title": "Periodic Evaluation",
                "requirement": "Regular evaluation to confirm continued fitness for use",
                "level": "isa-95-L4",
                "frequency": "periodic",
                "scope": ["performance", "compliance", "improvements"]
            }
        }
    },

    # Section 12: Security
    "security_detailed": {
        "physical_security": {
            "requirement": "Protect systems from unauthorized access",
            "level": "isa-95-L3",
            "measures": ["access_badges", "server_room_locks", "cctv"]
        },
        "logical_security": {
            "requirement": "Restrict system access to authorized individuals",
            "level": "isa-95-L3",
            "measures": ["user_authentication", "rbac", "session_management"]
        }
    },

    # Audit Trail (Detailed - similar to 21 CFR 11.10(b) but less prescriptive)
    "audit_trail": {
        "requirement": "Consider use of audit trails based on risk assessment",
        "level": "isa-95-L3",
        "when_required": "For GMP critical data",
        "contents": ["who", "what", "when", "why"],
        "review": "Audit trails should be reviewed regularly"
    }
}

# Detailed requirements for ingestion
eu_annex_11_requirements: List[Dict[str, Any]] = [
    {
        "txt": "EU Annex 11 Section 1: Risk Management - Apply risk management throughout the computerised system lifecycle. Use GAMP 5 categories to assess system criticality.",
        "std": "EU Annex 11",
        "sec": "1",
        "type": "risk_management",
        "isa_level": 4,
        "approach": "GAMP_5",
        "diff": "advanced"
    },
    {
        "txt": "EU Annex 11 Section 2: Validation - Documented evidence that the computerised system does what it purports to do. Lifecycle approach: planning, specification, testing, approval, review.",
        "std": "EU Annex 11",
        "sec": "2",
        "type": "validation",
        "isa_level": 3,
        "lifecycle": ["plan", "specify", "test", "approve", "review"],
        "diff": "advanced"
    },
    {
        "txt": "EU Annex 11 Section 4: Accuracy Checks - For critical data entered manually, there should be an additional check on the accuracy of the data. This can be done by a second operator or validated electronic means.",
        "std": "EU Annex 11",
        "sec": "4",
        "type": "data_accuracy",
        "isa_level": 2,
        "isa_mapping": "isa-95-L2-supervisory",
        "methods": ["second_person_check", "electronic_validation"],
        "diff": "intermediate"
    },
    {
        "txt": "EU Annex 11 Section 9: Audit Trail - Consider the need to build into the system the creation of a record of all GMP-relevant changes and deletions. Audit trail should include who, what, when, and why.",
        "std": "EU Annex 11",
        "sec": "9",
        "type": "audit_trail",
        "isa_level": 3,
        "risk_based": True,
        "fields": ["who", "what", "when", "why"],
        "review_frequency": "regular",
        "diff": "advanced"
    },
    {
        "txt": "EU Annex 11 Section 12.1: Physical Security - Physical and/or logical controls should be in place to restrict access to computerised system to authorised persons.",
        "std": "EU Annex 11",
        "sec": "12.1",
        "type": "physical_security",
        "isa_level": 3,
        "controls": ["access_badges", "locks", "surveillance"],
        "diff": "intermediate"
    },
    {
        "txt": "EU Annex 11 Section 12.4: Electronic Signature - The system should enforce uniqueness of each user's electronic signature over time. Electronic signatures must be linked to their respective record securely.",
        "std": "EU Annex 11",
        "sec": "12.4",
        "type": "e_signature",
        "isa_level": 3,
        "requirements": ["uniqueness", "cryptographic_linking", "legal_equivalence"],
        "diff": "advanced"
    },
    {
        "txt": "EU Annex 11 Section 13: Change Control - Changes to a computerised system should be controlled and documented. Impact assessment should evaluate effect on validation status and product quality.",
        "std": "EU Annex 11",
        "sec": "13",
        "type": "change_control",
        "isa_level": 3,
        "process": ["request", "assess", "approve", "test", "implement", "verify"],
        "diff": "intermediate"
    },
    {
        "txt": "EU Annex 11 Section 15: Business Continuity - For systems critical to product quality, alternative arrangements should be in place if the system fails. Include backup, disaster recovery, and manual procedures.",
        "std": "EU Annex 11",
        "sec": "15",
        "type": "business_continuity",
        "isa_level": 4,
        "requirements": ["backup_systems", "disaster_recovery", "manual_fallback"],
        "diff": "advanced"
    },
    {
        "txt": "EU Annex 11 Section 17: Batch Release - When a computerised system is used for electronic recording of batch certification, the system should allow only Qualified Persons to certify batches and print certificates.",
        "std": "EU Annex 11",
        "sec": "17",
        "type": "batch_release",
        "isa_level": 3,
        "isa_mapping": "isa-88-batch-record",
        "requirements": ["qualified_person_only", "electronic_record", "print_capability"],
        "diff": "advanced"
    }
]

# Comparison matrix for reference
COMPARISON_MATRIX = {
    "aspect": "Comparison",
    "items": {
        "type": {
            "cfr_part_11": "Federal regulation (legally binding)",
            "annex_11": "Guidance document (part of GMP guidelines)"
        },
        "scope": {
            "cfr_part_11": "Electronic records & signatures in all FDA-regulated activities",
            "annex_11": "Computerised systems in GMP activities for medicinal products"
        },
        "focus": {
            "cfr_part_11": "Prescriptive technical controls (e.g., two-component e-signatures)",
            "annex_11": "Risk-based approach, system lifecycle emphasis"
        },
        "applicability": {
            "cfr_part_11": "Pharma, biotech, medical devices",
            "annex_11": "Primarily pharma manufacturing"
        },
        "year": {
            "cfr_part_11": 1997,
            "annex_11": 2011
        }
    },
    "common_requirements": [
        "System validation",
        "Audit trails (who, what, when, why)",
        "Electronic signatures = handwritten equivalents",
        "Access controls & security",
        "Data integrity & traceability",
        "Training requirements",
        "Change control"
    ]
}

"""
21 CFR Part 11 - Electronic Records and Electronic Signatures
US FDA Regulation for GMP Systems

Structured as ISA-style UDTs (User Defined Types)
"""

from typing import Dict, List, Any

# 21 CFR Part 11 UDT - ISA Style Structure
CFR_PART_11_UDT = {
    "regulation": "21 CFR Part 11",
    "authority": "US FDA",
    "year": 1997,
    "scope": "Electronic records & signatures in FDA-regulated activities",
    "applicability": ["pharma", "biotech", "medical_devices"],
    "approach": "prescriptive",

    # Subpart A - General Provisions
    "subpart_a": {
        "name": "General Provisions",
        "sections": {
            "11.1": {
                "title": "Scope",
                "requirement": "Defines applicability to electronic records and signatures",
                "level": "isa-95-L3",
                "compliance_type": "system_scope"
            },
            "11.2": {
                "title": "Implementation",
                "requirement": "Validates electronic records and signatures",
                "level": "isa-95-L3",
                "compliance_type": "validation"
            },
            "11.3": {
                "title": "Definitions",
                "requirement": "Defines key terms",
                "level": "isa-95-L4",
                "compliance_type": "documentation"
            }
        }
    },

    # Subpart B - Electronic Records
    "subpart_b": {
        "name": "Electronic Records",
        "sections": {
            "11.10": {
                "title": "Controls for Closed Systems",
                "requirement": "Validation, audit trails, encryption, checksums",
                "level": "isa-95-L2-L3",
                "controls": {
                    "11.10a": {
                        "control": "System Validation",
                        "description": "Validate systems to ensure accuracy, reliability, and consistent intended performance",
                        "implementation": "IQ/OQ/PQ protocols",
                        "isa_mapping": "isa-95-L3-MES",
                        "audit_trail_required": True
                    },
                    "11.10b": {
                        "control": "Generate Audit Trail",
                        "description": "Secure audit trails that record who, what, when, why",
                        "implementation": "Immutable audit trail with timestamp, user, action, reason",
                        "isa_mapping": "isa-95-L2-L3",
                        "fields": ["timestamp", "user_id", "action", "old_value", "new_value", "reason"]
                    },
                    "11.10c": {
                        "control": "Authority Checks",
                        "description": "Operational system checks to enforce authorized access",
                        "implementation": "Role-based access control (RBAC)",
                        "isa_mapping": "isa-95-L3",
                        "technical": "LDAP, Active Directory, MFA"
                    },
                    "11.10d": {
                        "control": "Device Checks",
                        "description": "Determine validity of input source",
                        "implementation": "Device authentication and validation",
                        "isa_mapping": "isa-95-L1-L2",
                        "technical": "Certificate-based authentication, device fingerprinting"
                    },
                    "11.10e": {
                        "control": "Education and Training",
                        "description": "Document training on system use and security",
                        "implementation": "Training records with periodic refresher",
                        "isa_mapping": "isa-95-L4",
                        "frequency": "annual"
                    },
                    "11.10f": {
                        "control": "Data Integrity",
                        "description": "Ensure accuracy and completeness of data",
                        "implementation": "Checksums, hash validation, backup/recovery",
                        "isa_mapping": "isa-95-L2-L3",
                        "technical": "SHA-256, MD5, CRC"
                    },
                    "11.10g": {
                        "control": "Secure Storage",
                        "description": "Protect records from loss or damage",
                        "implementation": "Redundant storage, disaster recovery",
                        "isa_mapping": "isa-95-L3",
                        "backup_frequency": "daily"
                    },
                    "11.10h": {
                        "control": "Copy Authentication",
                        "description": "Accurate and complete copies of records",
                        "implementation": "Cryptographic signatures on exports",
                        "isa_mapping": "isa-95-L3",
                        "format": "PDF/A with embedded hash"
                    },
                    "11.10i": {
                        "control": "Record Retention",
                        "description": "Retention times specified in predicate rules",
                        "implementation": "Automated archival with retrieval capability",
                        "isa_mapping": "isa-95-L4",
                        "retention_period": "varies_by_product"
                    },
                    "11.10k": {
                        "control": "System Documentation",
                        "description": "Use of operational checks to enforce sequencing",
                        "implementation": "State machines for sequential operations",
                        "isa_mapping": "isa-88-phase-logic",
                        "example": "Batch record must complete phases in order"
                    }
                }
            },
            "11.30": {
                "title": "Controls for Open Systems",
                "requirement": "Additional measures like digital signatures for open systems",
                "level": "isa-95-L3",
                "additional_controls": ["encryption", "digital_signatures"]
            },
            "11.50": {
                "title": "Signature Manifestations",
                "requirement": "Signed records must contain info like name, date, meaning",
                "level": "isa-95-L3",
                "display_requirements": ["printed_name", "signature_date", "signature_meaning"]
            },
            "11.70": {
                "title": "Signature/Record Linking",
                "requirement": "E-signatures cannot be excised, copied, or transferred",
                "level": "isa-95-L3",
                "technical": "Cryptographically bind signature to record"
            }
        }
    },

    # Subpart C - Electronic Signatures
    "subpart_c": {
        "name": "Electronic Signatures",
        "sections": {
            "11.100": {
                "title": "General Requirements",
                "requirement": "Electronic signatures = handwritten signatures",
                "level": "isa-95-L3",
                "legal_equivalence": True
            },
            "11.200": {
                "title": "Electronic Signature Components",
                "requirement": "Two distinct identification components (e.g., ID + password)",
                "level": "isa-95-L3",
                "components": {
                    "component_1": "User ID or token",
                    "component_2": "Password or biometric",
                    "requirement": "Both required for valid signature"
                }
            },
            "11.300": {
                "title": "Controls for Identification Codes/Passwords",
                "requirement": "Unique to individuals, periodically checked",
                "level": "isa-95-L3",
                "controls": {
                    "uniqueness": "One ID per person",
                    "verification": "Periodic checks that IDs haven't been compromised",
                    "loss_management": "Report and deactivate lost tokens immediately",
                    "session_timeout": "Automatic logout after inactivity"
                }
            }
        }
    }
}

# Detailed requirements for ingestion
cfr_part_11_requirements: List[Dict[str, Any]] = [
    {
        "txt": "21 CFR Part 11.10(a): System Validation - Validate computerized systems to ensure accuracy, reliability, and consistent intended performance. Use IQ/OQ/PQ protocols.",
        "std": "21 CFR Part 11",
        "sec": "11.10(a)",
        "type": "validation",
        "isa_level": 3,
        "control": "System Validation",
        "implementation": ["IQ", "OQ", "PQ", "qualification_protocols"],
        "diff": "advanced"
    },
    {
        "txt": "21 CFR Part 11.10(b): Audit Trail - Generate secure, computer-generated audit trails that independently record who, what, when, and why for electronic record creation, modification, or deletion.",
        "std": "21 CFR Part 11",
        "sec": "11.10(b)",
        "type": "audit_trail",
        "isa_level": 3,
        "control": "Audit Trail",
        "fields": ["timestamp", "user_id", "action", "old_value", "new_value", "reason"],
        "immutable": True,
        "diff": "advanced"
    },
    {
        "txt": "21 CFR Part 11.10(c): Authority Checks - Use operational system checks to enforce permitted sequencing of steps and events, as appropriate.",
        "std": "21 CFR Part 11",
        "sec": "11.10(c)",
        "type": "access_control",
        "isa_level": 3,
        "control": "RBAC",
        "implementation": ["role_based_access", "LDAP", "Active_Directory"],
        "diff": "intermediate"
    },
    {
        "txt": "21 CFR Part 11.10(d): Device Checks - Use authority checks to ensure only authorized individuals can use the system, electronically sign a record, access the operation or device, alter a record, or perform the operation.",
        "std": "21 CFR Part 11",
        "sec": "11.10(d)",
        "type": "device_auth",
        "isa_level": 2,
        "control": "Device Authentication",
        "implementation": ["certificates", "device_fingerprinting", "MFA"],
        "diff": "intermediate"
    },
    {
        "txt": "21 CFR Part 11.10(e): Training - Establish and maintain education, training, and experience requirements for persons who develop, maintain, or use electronic record/signature systems.",
        "std": "21 CFR Part 11",
        "sec": "11.10(e)",
        "type": "training",
        "isa_level": 4,
        "control": "Training Records",
        "frequency": "annual",
        "documentation_required": True,
        "diff": "basic"
    },
    {
        "txt": "21 CFR Part 11.10(f): Data Integrity - Employ procedures and controls to ensure the accuracy, reliability, integrity, and consistent intended performance of all electronic records.",
        "std": "21 CFR Part 11",
        "sec": "11.10(f)",
        "type": "data_integrity",
        "isa_level": 3,
        "control": "Hash Validation",
        "implementation": ["SHA-256", "MD5", "CRC", "checksums"],
        "diff": "advanced"
    },
    {
        "txt": "21 CFR Part 11.200: Two-Component E-Signature - Electronic signatures shall employ at least two distinct identification components (e.g., ID + password).",
        "std": "21 CFR Part 11",
        "sec": "11.200",
        "type": "e_signature",
        "isa_level": 3,
        "control": "Two-Factor Authentication",
        "components": ["user_id", "password_or_biometric"],
        "diff": "intermediate"
    },
    {
        "txt": "21 CFR Part 11.300: Password Controls - Use unique identification codes and passwords that are periodically checked, recalled, or revised.",
        "std": "21 CFR Part 11",
        "sec": "11.300",
        "type": "password_policy",
        "isa_level": 3,
        "control": "Password Management",
        "requirements": ["uniqueness", "periodic_change", "complexity", "session_timeout"],
        "diff": "intermediate"
    }
]

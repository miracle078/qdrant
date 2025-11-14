"""
Sample data ingestion for demo/testing
Includes ISA standards excerpts, PLC code, and metadata
"""

import asyncio
import logging
from typing import List, Dict, Any
from qdrant_client.models import PointStruct

from ..qdrant_setup import QdrantManager
from ..embeddings import embed_text, embed_code
from ..regulatory.cfr_part_11 import cfr_part_11_requirements
from ..regulatory.eu_annex_11 import eu_annex_11_requirements

logger = logging.getLogger(__name__)


# Sample ISA-95 content
ISA_95_SAMPLES = [
    {
        "txt": "ISA-95 Level 0 defines the actual physical processes. This includes sensors, actuators, and the basic process equipment.",
        "std": "ISA-95",
        "sec": "1.0",
        "lvl": 0,
        "diff": "basic"
    },
    {
        "txt": "ISA-95 Level 1 covers sensing and manipulating the physical processes. This includes PLCs, DCS systems, and SCADA that directly control equipment.",
        "std": "ISA-95",
        "sec": "1.1",
        "lvl": 1,
        "diff": "basic"
    },
    {
        "txt": "ISA-95 Level 2 focuses on monitoring, supervisory control, and automated control of the production process. This is where real-time optimization happens.",
        "std": "ISA-95",
        "sec": "1.2",
        "lvl": 2,
        "diff": "intermediate"
    },
    {
        "txt": "ISA-95 Level 3 is the Manufacturing Execution System (MES) layer. It manages production workflows, tracks materials, and ensures quality compliance.",
        "std": "ISA-95",
        "sec": "1.3",
        "lvl": 3,
        "diff": "intermediate"
    },
    {
        "txt": "ISA-95 Level 4 represents business planning and logistics. This is the ERP layer that handles orders, schedules, and resource planning.",
        "std": "ISA-95",
        "sec": "1.4",
        "lvl": 4,
        "diff": "intermediate"
    },
    {
        "txt": "The ISA-95 standard defines a hierarchical model for integrating enterprise and control systems. It provides a common terminology and consistent information models.",
        "std": "ISA-95",
        "sec": "0.1",
        "lvl": -1,
        "diff": "basic"
    }
]

# Sample ISA-88 content
ISA_88_SAMPLES = [
    {
        "txt": "ISA-88 Batch Control standard defines models for batch manufacturing. The Physical Model describes equipment hierarchy: Enterprise, Site, Area, Process Cell, Unit, Equipment Module, Control Module.",
        "std": "ISA-88",
        "sec": "2.0",
        "lvl": -1,
        "diff": "intermediate"
    },
    {
        "txt": "ISA-88 Procedural Control Model includes Procedures, Unit Procedures, Operations, and Phases. A Recipe is the complete set of data and procedures to manufacture a batch.",
        "std": "ISA-88",
        "sec": "2.1",
        "lvl": -1,
        "diff": "intermediate"
    },
    {
        "txt": "ISA-88 defines four recipe types: General Recipe (product-independent), Site Recipe (site-specific), Master Recipe (approved formula), and Control Recipe (specific batch instance).",
        "std": "ISA-88",
        "sec": "2.2",
        "lvl": -1,
        "diff": "advanced"
    }
]

# Sample ISA-18.2 content
ISA_182_SAMPLES = [
    {
        "txt": "ISA-18.2 Alarm Management standard addresses the lifecycle of alarms. Key principles: alarms should be relevant, unique, timely, prioritized, and understandable.",
        "std": "ISA-18.2",
        "sec": "3.0",
        "lvl": -1,
        "diff": "intermediate"
    },
    {
        "txt": "ISA-18.2 defines alarm priorities: Critical (immediate operator action required), High (prompt operator action), Medium (operator awareness), Low (information only).",
        "std": "ISA-18.2",
        "sec": "3.1",
        "lvl": -1,
        "diff": "intermediate"
    },
    {
        "txt": "Alarm flooding occurs when operators receive more than 10 alarms per 10 minutes. ISA-18.2 recommends rationalization to reduce nuisance alarms and improve safety.",
        "std": "ISA-18.2",
        "sec": "3.2",
        "lvl": -1,
        "diff": "advanced"
    }
]

# Sample PLC code
PLC_CODE_SAMPLES = [
    {
        "code": """(* Interlock Logic - Safety System *)
IF Emergency_Stop = TRUE THEN
    Main_Motor := FALSE;
    Safety_Valve := TRUE;
ELSIF (Level_High = FALSE) AND (Pressure_OK = TRUE) THEN
    Main_Motor := TRUE;
    Safety_Valve := FALSE;
END_IF;""",
        "lang": "ST",
        "plat": "Codesys",
        "isa_pat": "95-L1",
        "fn": "interlock"
    },
    {
        "code": """(* PID Temperature Controller *)
PID_Controller(
    PV := Temperature_Sensor,
    SP := Temperature_Setpoint,
    KP := 1.5,
    KI := 0.02,
    KD := 0.1,
    OUT => Heater_Output
);

IF Heater_Output > 100.0 THEN
    Heater_Output := 100.0;
ELSIF Heater_Output < 0.0 THEN
    Heater_Output := 0.0;
END_IF;""",
        "lang": "ST",
        "plat": "Siemens",
        "isa_pat": "88-phase",
        "fn": "PID_control"
    },
    {
        "code": """(* Batch Phase - Filling *)
CASE Phase_State OF
    0: (* Idle *)
        IF Start_Fill THEN
            Phase_State := 1;
        END_IF;

    1: (* Opening Valve *)
        Fill_Valve := TRUE;
        Phase_State := 2;

    2: (* Filling *)
        IF Tank_Level >= Target_Level THEN
            Phase_State := 3;
        END_IF;

    3: (* Closing Valve *)
        Fill_Valve := FALSE;
        Phase_Complete := TRUE;
        Phase_State := 0;
END_CASE;""",
        "lang": "ST",
        "plat": "Rockwell",
        "isa_pat": "88-batch",
        "fn": "batch_phase"
    }
]

# Sample documentation
DOC_SAMPLES = [
    {
        "txt": "To implement ISA-95 integration, start by mapping your current systems to the 5 levels. Identify gaps between control systems (L0-L2) and business systems (L3-L4).",
        "type": "tutorial",
        "std": ["ISA-95"],
        "skill": "intermediate",
        "use": "implementation"
    },
    {
        "txt": "Common ISA-88 implementation challenge: Recipe management across multiple batches. Solution: Use master recipes with version control and implement proper phase state machines.",
        "type": "faq",
        "std": ["ISA-88"],
        "skill": "advanced",
        "use": "troubleshooting"
    }
]


async def ingest_sample_data(qdrant: QdrantManager) -> Dict[str, int]:
    """
    Ingest sample data into all collections

    Args:
        qdrant: QdrantManager instance

    Returns:
        Dictionary with count of items ingested per collection
    """
    counts = {}

    # 1. ISA Standards + Regulatory Requirements
    logger.info("Ingesting ISA standards and regulatory requirements...")
    isa_samples = ISA_95_SAMPLES + ISA_88_SAMPLES + ISA_182_SAMPLES

    # Add regulatory requirements (21 CFR Part 11 and EU Annex 11)
    regulatory_samples = cfr_part_11_requirements + eu_annex_11_requirements

    all_standards = isa_samples + regulatory_samples

    points = []
    for i, sample in enumerate(all_standards):
        embedding = await embed_text(sample['txt'])
        points.append(PointStruct(
            id=i,
            vector=embedding,
            payload=sample
        ))

    qdrant.client.upsert(
        collection_name='isa',
        points=points,
        wait=True
    )
    counts['isa'] = len(points)
    logger.info(f"✓ Ingested {len(points)} standards (ISA + 21 CFR Part 11 + EU Annex 11)")

    # 2. PLC Code
    logger.info("Ingesting PLC code samples...")
    code_points = []
    for i, sample in enumerate(PLC_CODE_SAMPLES):
        embedding = embed_code(sample['code'])
        code_points.append(PointStruct(
            id=i,
            vector=embedding,
            payload=sample
        ))

    qdrant.client.upsert(
        collection_name='code',
        points=code_points,
        wait=True
    )
    counts['code'] = len(code_points)
    logger.info(f"✓ Ingested {len(code_points)} code samples")

    # 3. Documentation
    logger.info("Ingesting documentation...")
    doc_points = []
    for i, sample in enumerate(DOC_SAMPLES):
        embedding = await embed_text(sample['txt'])
        doc_points.append(PointStruct(
            id=i,
            vector=embedding,
            payload=sample
        ))

    qdrant.client.upsert(
        collection_name='doc',
        points=doc_points,
        wait=True
    )
    counts['doc'] = len(doc_points)
    logger.info(f"✓ Ingested {len(doc_points)} documentation items")

    # 4. Placeholder for images and audio (would need actual files)
    logger.info("Image and audio collections created (empty)")
    counts['img'] = 0
    counts['aud'] = 0
    counts['vid'] = 0

    return counts


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    from ..qdrant_setup import get_qdrant_client

    async def main():
        # Initialize Qdrant
        qdrant = get_qdrant_client()
        qdrant.setup_collections()

        # Ingest data
        counts = await ingest_sample_data(qdrant)

        print("\n📊 Ingestion Complete:")
        for collection, count in counts.items():
            print(f"  {collection}: {count} items")

    asyncio.run(main())

"""
Regulatory Compliance Modules
21 CFR Part 11 (US FDA) and EU Annex 11 (EudraLex)
"""

from .cfr_part_11 import CFR_PART_11_UDT, cfr_part_11_requirements
from .eu_annex_11 import EU_ANNEX_11_UDT, eu_annex_11_requirements

__all__ = [
    'CFR_PART_11_UDT',
    'EU_ANNEX_11_UDT',
    'cfr_part_11_requirements',
    'eu_annex_11_requirements'
]

"""Data ingestion pipelines"""

from .isa_standards import ingest_isa_standards
from .code_samples import ingest_code_samples
from .audio_content import ingest_audio_content
from .sample_data import ingest_sample_data

__all__ = [
    'ingest_isa_standards',
    'ingest_code_samples',
    'ingest_audio_content',
    'ingest_sample_data'
]

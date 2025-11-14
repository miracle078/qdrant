"""
AutomationGPT Setup Script
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="automationgpt",
    version="1.0.0",
    author="AutomationGPT Team",
    description="Multimodal ISA Standards Search Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teslasolar/qdrant",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "qdrant-client>=1.7.0",
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",
        "anthropic>=0.7.0",
        "openai>=1.3.0",
        "sentence-transformers>=2.2.2",
        "transformers>=4.35.0",
        "torch>=2.1.0",
        "Pillow>=10.1.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "numpy>=1.24.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.11.0",
            "flake8>=6.1.0",
        ],
        "audio": [
            "laion-clap",
        ],
        "pdf": [
            "PyPDF2>=3.0.0",
            "pdfplumber>=0.10.0",
        ],
        "youtube": [
            "yt-dlp>=2023.11.0",
        ],
    },
)

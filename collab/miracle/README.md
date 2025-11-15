# Miracle's Workspace

This is Miracle's personal workspace for the Qdrant project.

Use this directory for your work, experiments, and notes.

x-ray datasets
https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/37178474737

Alz dataset reqs approval
https://adni.loni.usc.edu/

Cross-sectional MRI Data in Young, Middle Aged, Nondemented and Demented Older Adults
https://sites.wustl.edu/oasisbrains/home/oasis-1/




# Medical Imaging Datasets for AI/ML Analysis

## X-Ray Datasets (Chest/Thoracic)

### ChestX-ray14 (NIH)
- **Size**: 112,120 frontal-view chest X-rays from 30,805 patients
- **Labels**: 14 disease categories (pneumonia, atelectasis, cardiomegaly, etc.)
- **Access**: https://nihcc.app.box.com/v/ChestXray-NIHCC
- **Notes**: Most widely cited benchmark dataset

### MIMIC-CXR
- **Size**: 377,110 chest X-rays from 227,835 studies
- **Features**: Includes radiology reports for NLP tasks
- **Access**: PhysioNet (requires credentialed access)
- **Notes**: Current gold standard for research

### CheXpert (Stanford)
- **Size**: 224,316 chest radiographs from 65,240 patients
- **Features**: Uncertainty labels for ambiguous findings
- **Access**: Free download after registration
- **Notes**: Excellent for training robust classifiers

### PadChest
- **Size**: 160,000+ chest X-rays
- **Features**: Multiple projections, bilingual annotations
- **Access**: Free registration required
- **Notes**: Good for multi-view analysis

### COVID-19 Image Data Collection
- **Focus**: COVID-19 and pneumonia cases
- **Features**: Regularly updated, community-driven
- **Access**: Public GitHub repository
- **Notes**: Best for pandemic-related research

---

## Brain Imaging Datasets

### Alzheimer's Disease

#### ADNI (Alzheimer's Disease Neuroimaging Initiative)
- **Modalities**: MRI, PET, genetic data, clinical assessments
- **Features**: Longitudinal tracking of disease progression
- **Access**: http://adni.loni.usc.edu/ (requires application)
- **Notes**: Gold standard for Alzheimer's research

#### OASIS (Open Access Series of Imaging Studies)
- **OASIS-1**: 416 subjects, cross-sectional MRI
- **OASIS-3**: 1,378 participants, longitudinal data
- **Features**: Cognitive assessments included
- **Access**: https://www.oasis-brains.org/ (freely available)

#### AIBL (Australian Imaging, Biomarkers & Lifestyle)
- **Size**: 1,100+ participants (AD, MCI, healthy controls)
- **Modalities**: MRI, PET, cognitive tests, blood biomarkers
- **Access**: https://aibl.csiro.au/

### Autism Spectrum Disorder (ASD)

#### ABIDE (Autism Brain Imaging Data Exchange)
- **ABIDE I**: 1,112 subjects (539 ASD, 573 controls)
- **ABIDE II**: 1,114 additional subjects
- **Modalities**: Resting-state fMRI and structural MRI
- **Access**: http://fcon_1000.projects.nitrc.org/indi/abide/

#### EU-AIMS LEAP
- **Features**: Longitudinal European multi-site study
- **Modalities**: Multi-site MRI data
- **Access**: Requires data access agreement

### General Neuroimaging

#### UK Biobank
- **Size**: 100,000+ brain scans (ongoing)
- **Use Case**: Excellent for pre-training models
- **Access**: Requires approved research application
- **Notes**: Massive scale dataset

#### Human Connectome Project
- **Size**: 1,200+ healthy adults
- **Quality**: High-quality MRI data
- **Use Case**: Understanding normal brain structure
- **Notes**: Good for transfer learning baselines

---

## Important Technical Considerations

### X-Ray vs Brain Imaging
- **X-rays**: 2D grayscale images, simpler preprocessing
- **Brain MRI/PET**: 3D volumes, require complex preprocessing
- **File Sizes**: Brain scans are significantly larger
- **Architectures**: Brain imaging needs 3D CNNs or specialized networks

### Access Requirements
- Most datasets require registration and data use agreements
- Some require institutional affiliation
- HIPAA compliance may be necessary
- IRB approval needed for clinical research

### Preprocessing Tools
**For Brain Imaging:**
- FSL (FMRIB Software Library)
- FreeSurfer
- SPM (Statistical Parametric Mapping)
- ANTs (Advanced Normalization Tools)

**Common Steps:**
- Skull stripping
- Spatial normalization
- Image registration
- Intensity normalization

### ML Architecture Recommendations
- **X-rays**: ResNet, DenseNet, EfficientNet (2D CNNs)
- **Brain MRI**: 3D CNNs, U-Net for segmentation
- **fMRI**: Graph Neural Networks, RNNs for temporal data
- **Multi-modal**: Fusion architectures combining different scan types

---

## Quick Selection Guide

**For chest pathology detection**: MIMIC-CXR or ChestX-ray14  
**For Alzheimer's research**: ADNI or OASIS  
**For autism research**: ABIDE I & II  
**For pre-training/transfer learning**: UK Biobank or Human Connectome Project  
**For COVID-19 research**: COVID-19 Image Data Collection

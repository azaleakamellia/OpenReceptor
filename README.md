# Tropical Forest Cover EO Methodology: Borneo Case Study

**Author:** Azalea Kamellia Abdullah, Gs.  
**Domain:** Applied Vegetation Remote Sensing, Tropical Forest Environments, Natural Capital  

## Project Overview
This repository documents the methodological framework and code architecture used for large-scale tropical forest cover mapping and land-use change detection in Borneo. Originally developed during my tenure leading the Conservation GIS Unit at WWF-Malaysia, this methodology contributed directly to the **Malaysia Forest Cover 2020 Dashboard** and subsequent peer-reviewed publications.

This work is highly applicable to commercial natural capital applications, providing a robust, reproducible pipeline for assessing forest extent, degradation, and regeneration using multi-temporal satellite imagery.

## Methodological Framework

### 1. Data Acquisition & Preprocessing
- **Primary Data Sources:** Landsat 5/7/8/9 and Sentinel-2 time-series imagery via Google Earth Engine (GEE).
- **Preprocessing:** Automated cloud and shadow masking (using QA bands and Fmask algorithms), atmospheric correction, and harmonization across sensor generations to ensure consistent temporal analysis.

### 2. Feature Engineering & Spectral Indices
- Calculation of key vegetation and moisture indices to enhance class separability in tropical environments:
  - NDVI (Normalized Difference Vegetation Index)
  - EVI (Enhanced Vegetation Index)
  - NBR (Normalized Burn Ratio) for disturbance detection
  - Tasseled Cap transformations (Brightness, Greenness, Wetness)

### 3. Machine Learning Classification
- **Algorithm:** Random Forest and Gradient Boosting (XGBoost) classifiers, chosen for their robustness to noisy, high-dimensional remote sensing data.
- **Training Data:** Stratified random sampling of reference points, validated against high-resolution basemaps and field knowledge.
- **Output:** Continuous forest cover probability maps and discrete land-cover classifications (e.g., Primary Forest, Degraded Forest, Agriculture, Water).

### 4. Accuracy Assessment & Validation
- Generation of error matrices (Confusion Matrices).
- Calculation of Overall Accuracy, Producer’s/User’s Accuracy, and Kappa/F1-Scores to ensure the methodology meets commercial and scientific rigor standards.

## Relevance to Natural Capital Applications
This pipeline provides the foundational geospatial intelligence required for:
- Baseline forest carbon stock estimation.
- Monitoring deforestation and degradation (REDD+ applications).
- Biodiversity habitat connectivity modeling.
- ESG and TCFD physical risk reporting for assets in tropical regions.

## Publications & Outputs
- **Md Reba, M. N., Abdullah, A. K., et al. (2025).** Evaluating satellite gridded precipitation errors in the Sungai Sarawak basin: A triple collocation approach. *Proceedings of ACRS 2025*.
- **Abdullah, A. K., et al. (2021).** Deep forest cover classification of consecutive Landsat imageries over Borneo. *Warta Geologi Newsletter*, 47(1), 71.

## Contact & Collaboration
For inquiries regarding the adaptation of this methodology for commercial natural capital projects, please visit my portfolio:  
🌐 [azaleakamellia.github.io](https://azaleakamellia.github.io)  
✉️ [azaleakamellia.a@gmail.com](mailto:azaleakamellia.a@gmail.com)

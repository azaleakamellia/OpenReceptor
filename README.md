# OpenReceptor: Sensitive Receptor Detection for ESIA & TNFD

**OpenReceptor** is an automated geospatial pipeline designed for environmental consultants, ESG auditors, and project developers. It rapidly extracts and maps sensitive human and environmental receptors within a project Area of Interest (AOI) to accelerate baseline studies for ESIA, EIA/SIA, TNFD, ADB, and ESI reporting.

## 🎯 Purpose & Compliance
Traditional receptor identification requires manual digitization and cross-referencing of disparate datasets. OpenReceptor automates this by fusing live OpenStreetMap data with global environmental databases, ensuring compliance with:
- **TNFD (Taskforce on Nature-related Financial Disclosures):** Identifying sensitive biodiversity and ecosystem receptors.
- **ADB & IFC Performance Standards:** Mapping vulnerable communities, schools, and healthcare facilities.
- **ESIA / EIA / SIA:** Rapid scoping of physical, biological, and socio-economic sensitivities.
- **ESI (Environmental Sensitivity Index):** Baseline coastal and terrestrial sensitivity mapping.

## ️ How It Works
OpenReceptor operates in two parallel streams:

### 1. Social & Anthropogenic Receptors (Overpass API)
Queries live OpenStreetMap data via the Overpass API to extract:
- Healthcare facilities (Hospitals, Clinics)
- Educational institutions (Schools, Universities)
- Places of worship and cultural heritage sites
- Residential zones and critical infrastructure

### 2. Environmental & Ecological Receptors (Google Earth Engine)
Processes global spatial datasets via GEE to extract:
- IUCN Protected Areas (WDPA)
- Critical Habitats and Key Biodiversity Areas (KBAs)
- Hydrological features (Rivers, Wetlands, Water Bodies)
- Land cover sensitivities (Primary forests, Mangroves)

## 🚀 Quick Start
1. Install dependencies: `pip install earthengine-api geopandas requests shapely`
2. Authenticate GEE: `earthengine authenticate`
3. Define your project AOI as a GeoJSON bounding box or polygon.
4. Run `openreceptor_pipeline.py`.
5. Import the generated `social_receptors.gpkg` and `env_receptors.gpkg` directly into QGIS or ArcGIS Pro.

##  Licensing
This tool is released under the AGPLv3 license for open scientific and educational use. For commercial, closed-door integration into proprietary ESIA workflows, please contact the author for an Enterprise License.

**Author:** Azalea Kamellia Abdullah, Gs.  
**Portfolio:** [azaleakamellia.github.io](https://azaleakamellia.github.io)

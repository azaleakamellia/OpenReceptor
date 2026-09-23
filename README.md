# 🌍 OpenReceptor: Dynamic Sensitive Receptor Detection

**Live Interactive Map:** [OpenReceptor](https://azaleakamellia.github.io/OpenReceptor/)

**OpenReceptor** is a dynamic, browser-based geospatial tool designed for environmental consultants and ESG auditors. Inspired by OpenInfraMap, it live-queries OpenStreetMap via the Overpass API to instantly extract and map sensitive human and environmental receptors within any user-defined Area of Interest (AOI).

## 🎯 Purpose & Compliance
Accelerates baseline studies for:
- **TNFD / ADB / IFC:** Identifying vulnerable communities, healthcare, and educational facilities.
- **ESIA / EIA / SIA:** Rapid scoping of physical, biological, and socio-economic sensitivities.
- **ESI (Environmental Sensitivity Index):** Baseline coastal and terrestrial sensitivity mapping.

## 🚀 How to Use
1. Open the [Live Web App](https://azaleakamellia.github.io/OpenReceptor/).
2. Pan and zoom the map to your project's Area of Interest (AOI).
3. Toggle the desired receptor categories in the sidebar (Hospitals, Schools, Protected Areas, etc.).
4. Click **"Update Map to Current View"**. The tool instantly queries the Overpass API and plots the receptors.
5. Export the data or use it to guide high-resolution validation.

## 🛠️ Technology Stack
- **Frontend:** Vanilla HTML/JS, Leaflet.js (for OpenInfraMap-style interactivity)
- **Data Source:** Live Overpass API (OpenStreetMap) + Google Earth Engine (for WDPA/environmental layers)
- **Hosting:** GitHub Pages (100% free, zero backend required)

**Author:** Azalea Kamellia Abdullah, Gs. | [Portfolio](https://azaleakamellia.github.io)

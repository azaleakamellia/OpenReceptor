# Tropical Forest EO Methodology Framework

A reproducible methodology for applied vegetation remote sensing in tropical environments, designed for natural capital applications and environmental baseline assessments.

## 🌍 Context
Tropical forest monitoring requires robust handling of persistent cloud cover, phenological variations, and multi-sensor data fusion. This repository outlines a standardized workflow using Google Earth Engine (GEE) and Python to derive reliable vegetation indices (NDVI/EVI) and detect land-use change.

## 🛠️ Methodology Components
1. **Multi-Sensor Harmonization:** Combining Landsat 8/9 and Sentinel-2 surface reflectance.
2. **Advanced Cloud & Shadow Masking:** Utilizing the `s2cloudless` algorithm and QA bands to ensure pixel-level integrity in high-precipitation zones.
3. **Time-Series Smoothing:** Applying Whittaker or Savitzky-Golay filters to reconstruct continuous vegetation trajectories.
4. **Change Detection:** Implementing Continuous Change Detection and Classification (CCDC) or breakpoint analysis for deforestation/degradation alerts.

## 💻 Representative Code Snippet (GEE Python API)
```python
import ee
ee.Initialize()

def mask_s2_clouds(image):
    """Masks clouds and cloud shadows in a Sentinel-2 image."""
    qa = image.select('QA60')
    cloud_bit_mask = 1 << 10
    cirrus_bit_mask = 1 << 11
    mask = qa.bitwiseAnd(cloud_bit_mask).eq(0).And(qa.bitwiseAnd(cirrus_bit_mask).eq(0))
    return image.updateMask(mask).divide(10000).select(['B2', 'B3', 'B4', 'B8', 'B11', 'B12'], 
                                                       ['blue', 'green', 'red', 'nir', 'swir1', 'swir2'])

# Define Area of Interest (e.g., Sarawak, Malaysia)
aoi = ee.Geometry.Rectangle([109.5, 1.0, 115.0, 5.0])

# Load Sentinel-2, apply masking, and calculate NDVI
collection = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
              .filterBounds(aoi)
              .filterDate('2023-01-01', '2023-12-31')
              .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
              .map(mask_s2_clouds)
              .map(lambda img: img.addBands(img.normalizedDifference(['nir', 'red']).rename('NDVI'))))

median_ndvi = collection.select('NDVI').median()

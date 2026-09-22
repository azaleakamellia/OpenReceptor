import ee
import geopandas as gpd
import requests
import json
from shapely.geometry import shape

# Initialize GEE
ee.Initialize()

def get_osm_receptors(aoi_geojson, receptor_type='amenity'):
    """
    Queries Overpass API to extract sensitive receptors from OpenStreetMap.
    """
    # Convert GeoJSON to Overpass QL bounding box or polygon (simplified for bbox here)
    # In production, use a proper polygon query.
    overpass_url = "http://overpass-api.de/api/interpreter"
    
    # Example: Extracting schools, hospitals, and places of worship
    query = f"""
    [out:json];
    (
      node["{receptor_type}"="school"]({aoi_geojson['bbox']});
      node["{receptor_type}"="hospital"]({aoi_geojson['bbox']});
      node["{receptor_type}"="place_of_worship"]({aoi_geojson['bbox']});
      way["landuse"="residential"]({aoi_geojson['bbox']});
    );
    out body;
    """
    
    response = requests.get(overpass_url, params={'data': query})
    data = response.json()
    
    # Convert to GeoDataFrame
    features = []
    for element in data['elements']:
        if 'lat' in element and 'lon' in element:
            features.append({
                'type': 'Feature',
                'geometry': {'type': 'Point', 'coordinates': [element['lon'], element['lat']]},
                'properties': element.get('tags', {})
            })
    return gpd.GeoDataFrame.from_features(features, crs="EPSG:4326")

def get_wdpa_protected_areas(aoi_geometry):
    """
    Queries GEE World Database on Protected Areas (WDPA).
    """
    aoi_ee = ee.Geometry(aoi_geometry)
    wdpa = ee.FeatureCollection("WCMC/WDPA/current/polygons")
    
    # Filter to AOI
    protected_areas = wdpa.filterBounds(aoi_ee)
    
    # Get first 100 features to avoid memory limits
    features = protected_areas.limit(100).getInfo()['features']
    return gpd.GeoDataFrame.from_features(features, crs="EPSG:4326")

# --- EXECUTION ---
# Define a dummy AOI (Replace with your actual project GeoJSON)
dummy_aoi = {
    "type": "Feature",
    "geometry": {"type": "Point", "coordinates": [101.6869, 3.1390]}, # Kuala Lumpur
    "bbox": "3.0, 101.6, 3.2, 101.8" # minLat, minLon, maxLat, maxLon
}

print("Extracting Social Receptors via Overpass API...")
social_receptors = get_osm_receptors(dummy_aoi)
print(f"Found {len(social_receptors)} social receptors.")

print("Extracting Environmental Receptors via GEE (WDPA)...")
env_receptors = get_wdpa_protected_areas(dummy_aoi['geometry'])
print(f"Found {len(env_receptors)} protected areas.")

# Save to GeoPackage for easy use in QGIS/ArcGIS
social_receptors.to_file("social_receptors.gpkg", layer='social', driver="GPKG")
env_receptors.to_file("env_receptors.gpkg", layer='environmental', driver="GPKG")
print("Export complete: social_receptors.gpkg and env_receptors.gpkg")

# 'dataset' holds the input data for this script

# Miradi-GeoJSON.py
# called from Power Query (Power BI) to convert GeoJSON features (in row data) to a single GeoJSON file.
# The Python script is written to be generic, so it can be applied to any Query with "Footprint" (spatial) data.
# Assumes a "Footprint Geojson Text" column exists in the input dataset (pandas dataframe, generated from the prior query step).
# The "Footprint Geojson Text" column should contain a geojson shape in text form.
# The geojson shape will be simplified if it is over 30,000 characters long.
# Adds a geojson property to each shape, to record the 'Footprint Name' and 'Resource Uri' columns, for data matching in the Azure Maps Power BI visual.
# This script writes a GeoJSON file with the collected geojson features from all rows. 
# Explodes rows with multiple objects in their geojson shape into multiple rows.

# Queries where this script is used: 
#   Direct Threat Footprints - GeoJSON
#   Program Footprints - GeoJSON
#   Project Footprints - GeoJSON
#   Target Footprints - GeoJSON

output_file_path = "C:/Dev/Miradi/GeoJSON/Miradi-Projects.geojson"
import pandas

# test harness for debugging outside Power Query. Delete this section when pasting into Power Query

# dataset = pandas.read_csv("C:/Dev/Miradi/GeoJSON/Miradi-GeoJSON-test.csv", sep="\t")
# dataset.to_csv("C:/Dev/Miradi/GeoJSON/Miradi-GeoJSON-test.csv", sep="\t", index=False)

# test harness ends

# 'dataset' holds the input data for this script

import geopandas
import json
import topojson

dataset_copy = dataset.copy()
dataset['Footprint Geojson Is Empty'] = ''
features_all_gdf = None
features_each_gdf_list = []

for idx in dataset_copy.index:
    try:
        features_each_text = str(dataset_copy.at[idx, 'Footprint Geojson Text'])
        features_each_json = json.loads(features_each_text)
        features_each_gdf = geopandas.GeoDataFrame.from_features(features_each_json["features"])
        if len ( features_each_text  ) > 30000:
            topo = topojson.Topology( features_each_gdf , prequantize=False)
            features_each_gdf = topo.toposimplify(0.01).to_gdf()
        features_each_gdf['Resource Uri'] =  str(dataset_copy.at[idx, 'Resource Uri'])
        features_each_gdf['Project Name'] =  str(dataset_copy.at[idx, 'Project Name'])
        dataset.at[idx, 'Footprint Geojson Is Empty'] = str(features_each_gdf.empty)
        if not(features_each_gdf.empty):
            features_each_gdf.set_crs('epsg:4326')
            features_each_gdf_list.append(features_each_gdf)
    except:
        do_nothing = ''

features_all_gdf = geopandas.GeoDataFrame(pandas.concat(features_each_gdf_list, ignore_index=True, sort=False))
features_all_gdf = features_all_gdf.set_crs(crs='epsg:4326', allow_override=True)
features_all_gdf.to_file(output_file_path, driver='GeoJSON', encoding="utf-8")

# test harness for debugging outside Power Query. Delete this section when pasting into Power Query

print(features_all_gdf) 

# test harness ends

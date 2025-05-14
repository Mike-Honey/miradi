# 'dataset' holds the input data for this script

# Miradi-WKT.py
# called from Power Query (Power BI) to convert GeoJSON shapes to WKT format.
# The Python script is written to be generic, so it can be applied to any Query with "Footprint" (spatial) data.
# Assumes a "Footprint Geojson Text" column exists in the input dataset (pandas dataframe, generated from the prior query step).
# The "Footprint Geojson Text" column should contain a geojson shape in text form.
# This script adds a "Footprint WKT" column with the geojson shape reformatted as WKT. 
# Explodes rows with multiple objects in their geojson shape into multiple rows.

# Queries where this script is used: 
#   Direct Threat Footprints - WKT
# Program Footprints - WKT - base
#   Project Footprints - WKT
#   Target Footprints - WKT

import pandas

# test harness for debugging outside Power Query. Delete this section when pasting into Power Query

dataset = pandas.read_csv("C:/Dev/Miradi/Miradi-WKT-test.csv", sep="\t")

# test harness ends

# 'dataset' holds the input data for this script

import geopandas
import json
import topojson

dataset_df_copy = dataset.copy()
dataset['Footprint WKT'] = ''
for idx in dataset_df_copy.index:
    try:
        features_each_text = str(dataset_df_copy.at[idx, 'Footprint Geojson Text'])
        features_each_json = json.loads(features_each_text)
        features_each_gdf = geopandas.GeoDataFrame.from_features(features_each_json["features"])
        if len ( features_each_text  ) > 30000:
            topo = topojson.Topology( features_each_gdf , prequantize=False)
            features_each_gdf = topo.toposimplify(0.01).to_gdf()
        wkt = [geom.wkt for geom in features_each_gdf.geometry]
        dataset.at[idx,'Footprint WKT'] = wkt
    except:
        do_nothing = ''
dataset = dataset.explode( 'Footprint WKT' )

# test harness for debugging outside Power Query. Delete this section when pasting into Power Query

print(dataset) 

# test harness ends

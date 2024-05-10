"""
Script to create geojson files ready for Mapbox, from the Miradi Program Dashboard (Power BI report)

Steps to use:
1. Open Miradi Program Dashboard (Power BI report, using Power BI Desktop), refresh from Miradi Share (described in detail elsewhere)
2. Go to the (hidden) page: Data Testing. Export the Project and Target tables as CSV
3. Copy the CSV files into datadir folder: C:/Dev/Miradi/Spatial/
4. Run this script. It will produce a geojson file for each input CSV file
5. Rename the output files - add the Miradi Program name as a suffix
6. Upload each as a tileset to Mapbox
7. Configure the Mapbox custom visuals (in the Power BI report) so their Choropleth properties match the uploaded tilesets.
"""

import os
import json
import geopandas
import datetime
import pandas

def processGeojson(datadir):
  """
  Read in all the csv files from the given directory then pass each for processing
  """
  
  for file in os.listdir(datadir):
    filename = os.fsdecode(file)
    # print (filename)
    if filename.endswith(".csv"): 
      #print(os.path.splitext(file)[0])
      processEachGeojson(datadir , filename)
      continue
    else:
      continue

  

def processEachGeojson(datadir , filename):
  """
  Read each input csv file, process and append it's updated features collection via features_all_in.
  """
  print ( str(datetime.datetime.now()) + ' Processing file: ' + filename)
  File_Name_Prefix = str.lower(filename.split("_")[0])
  Source_File_Name = filename.split(".")[0]

  # read the shapefile
  input_gdf = pandas.read_csv(datadir + filename, encoding="utf-8")
  features_all_gdf = None

  input_gdf_copy = input_gdf.copy()
  for idx in input_gdf_copy.index:
    features_each_text = str(input_gdf_copy.at[idx, 'Footprint Geojson Text'])
    if features_each_text.find("geometry"):
      features_each_json = json.loads(features_each_text)
      features_each_gdf = geopandas.GeoDataFrame.from_features(features_each_json["features"])
      features_each_gdf["Footprint Name"] =  str(input_gdf_copy.at[idx, input_gdf_copy.columns[0]])
      features_each_gdf["Resource Uri"] =  str(input_gdf_copy.at[idx, input_gdf_copy.columns[1]])
      features_all_gdf = geopandas.GeoDataFrame(pandas.concat([features_each_gdf, features_all_gdf], ignore_index=True, sort=False), crs='epsg:4326' )
  
  print ( str(datetime.datetime.now()) + ' features_all_gdf: ' + str(features_all_gdf.count))

  # write a new file, containing the appended features from all the input files, and a simplified copy (for Power BI query)
  full_file_path = datadir + str.replace(filename, '.csv', '.geojson')
  features_all_gdf.to_file(full_file_path, driver='GeoJSON', encoding="utf-8")
  print ( str(datetime.datetime.now()) + ' Finished writing file: ' + full_file_path)



def main():
  """
  Main - program execute
  """

  datadir = 'C:/Dev/Miradi/Spatial/' 
  
  processGeojson(datadir)

  print (str(datetime.datetime.now()) + ' Finished!')
  exit()

if __name__ == '__main__':
    main()

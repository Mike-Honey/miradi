# Miradi
Files to support analysis projects on the Miradi system www.miradi.org

## Results Chain Diagrams

Examples (from the Miradi sample projects) of diagrams exported from Miradi for access by Power BI custom visuals.  You could clone this project and upload your own results chain diagrams following the naming standard, then point the Power BI template for Miradi at your clone to view your own diagrams.

/ResultsChainDiagrams sub-folder naming standard is /[Project Name]. Special characters in Project Names have to be removed to meet github & file system constraints. 

Within each sub-folder, Results Chain diagrams should be named [Results Chain ID and Name].png (which is the default names given on export from Miradi Share. Those files can then be referred to by analysis tools e.g. Power BI.

# Spatial

This is a method to extract the spatial data stored in Miradi for Projects and Threats, and output each in a geojson file for integration with MapBox or similar. 

The instructions are provided at the top of the Python script.  Power BI Desktop is also required. Sample data files from the Miradi sample program are provided, also in the Spatial sub-folder.

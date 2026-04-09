# Program Management Dashboard for Miradi 
[Miradi](https://www.miradishare.org/) is project management software designed for conservation practitioners. It helps teams practice evidence-based conservation for projects or programs, while implementing the Open Standards for the Practice of Conservation.

I've been working with the technical team behind Miradi to develop a Power BI report template, which smoothly integrates with the Miradi API to jump-start analysis on any Miradi project or program.

Here's a sample Power BI report, using the data from the **Miradi Islands Seascape (Example Program)**:

[Link to interactive DataViz](https://app.powerbi.com/view?r=eyJrIjoiZDg4YzgyNzEtYzI2MC00NDM4LWEwM2QtYTA1MjI2NTczMTg5IiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D)

[![Click to view and interact with the report](https://github.com/Mike-Honey/miradi/blob/master/Miradi%20Program%20Dashboard%20-%20Miradi%20Islands%20Seascape%20(Example%20Program).png?raw=true)](https://app.powerbi.com/view?r=eyJrIjoiZDg4YzgyNzEtYzI2MC00NDM4LWEwM2QtYTA1MjI2NTczMTg5IiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D)

This [portfolio page](https://www.mangasolutions.com/conservation-analytics) on the Manga Solutions website gives an introduction to this project and explains some of the intended uses.

This article in the Miradi Help Centre describes their API and the Power BI template, and provides a link to get started.  
[Miradi API](https://help.miradishare.org/hc/en-us/articles/7651985079963-Miradi-API)

The [Power BI template](https://github.com/Mike-Honey/miradi/raw/master/Miradi%20Program%20Dashboard%20-%20Miradi%20Islands%20Seascape%20(Example%20Program).pbix) integrates and models the key data from Miradi, and presents a set of interactive pages to start exploring and analyzing. Note the sample report filters the Miradi projects shown on all pages, using the Project Access field. You can remove or edit that filter to suit your requirements, using Power BI.

[Power BI](https://www.microsoft.com/en-au/power-platform/products/power-bi/) provides a great platform to extend the template - to build alternative visuals or page layouts, or to integrate data from other sources. Power BI can automate the chores of keeping your report up-to-date and distributing it to the right audience.

While developing this template, I've been grateful for the help, support and guidance from teams at [Foundations of Success](https://fosonline.org/), [Bush Heritage Australia](https://www.bushheritage.org.au), [Our Common Place (formerly Conservation Management)](https://ourcommonplace.org.au/) and the [Gordon and Betty Moore Foundation](https://moore.org).

The template has already been deployed at several organisations, and I'm keen to see it widely used. Please feel free to contact me if you are interested or have any questions.

## python scripts

Python scripts are embedded in the Power BI queries. These require [python 3](https://www.python.org/downloads/) with the following libraries: pandas, bs4, geopandas, json, topojson.  The Power BI Desktop options must be configured to select your python home folder.

Python is required to translate the spatial shapes stored in Miradi for Projects, Threats and Targets from geojson objects to geojson files, required for the Azure Map visual. Python scripts calling the bs4 library are used to clean text fields of HTML tags and special characters.

Scheduled refresh scenarios with the Power BI web service and python require the [Power BI Gateway](https://www.microsoft.com/en-us/power-platform/products/power-bi/gateway) component in Personal Mode.

For ease of review and testing, the python scripts used are provided as .py files, with .csv files for test input. There are notes in each .py script for updating the test input files using your data.

## Results Chain Diagrams

Examples (from the Miradi sample projects) of diagrams exported from Miradi for access by Power BI custom visuals.  You could clone this project and upload your own results chain diagrams following the naming standard, then point the Power BI template for Miradi at your clone to view your own diagrams.

/ResultsChainDiagrams sub-folder naming standard is /[Project Name]. Special characters in Project Names have to be removed to meet github & file system constraints. 

Within each sub-folder, Results Chain diagrams should be named [Results Chain ID and Name].png (which is the default names given on export from Miradi Share. Those files can then be referred to by analysis tools e.g. Power BI.

# GeoJSON folder

The .geojson files in this folder are updated by python scripts embedded in the Power BI queries, at every data refresh. These convert the spatial data stored in Miradi for Programs, Projects, Threats and Targets and output each in a geojson file formatted for integration with the Azure Maps visuals.

Whenever the spatial data changes, you need to use Power BI Desktop to upload the updated .geojson file into each Azure Map visual, using that visual's **Format > Reference layer > Data source > Upload a file** feature. More automated scenarios are possible (using the **Data source: URL** setting for Azure Map visuals), but are outside the current scope of this project.

# Releases

## 2026-04 release

This release replaces the (discontinued) IconMap Custom Visual with Azure Maps, which are now a standard Power BI visual. Python scripts embedded in the Power BI queries produce geojson files in the required format.

## 2025-05 release

This update extends the python scripts to include calls to the bs4 library to strip HTML tags.  These replace embedded Power BI M functions, and resolve some bugs as well as requiring far fewer lines of code.

There were also many performance improvements made in measures, as well as new measures for % Complete and Progress Status.

## 2024-06 release

The June 2024 update includes:
- replacing the MapBox maps with the IconMap Custom Visual. Integration via Power Queries with embedded Python scripts - automates the extraction of shapes from any Miradi program
- Program Overview page: map now coloured by Overall Viability Status 
- Threats page: map added to show Threat Footprints
- Threat tooltips are now more informative
- Indicators .. Taxonomies tables added to the semantic model
- HTML Content custom visual was replaced with the certified HTML Content (lite) custom visual

## 🤝 Support

Contributions, issues, feature requests and sponsorship are all welcome!

Give a ⭐️ if you like this project!

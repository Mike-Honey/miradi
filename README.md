# Miradi
[Miradi](https://www.miradishare.org/) is project management software designed for conservation practitioners. It helps teams practice evidence-based conservation for projects or programs, while implementing the Open Standards for the Practice of Conservation.

I've been working with the technical team behind Miradi to develop a Power BI report template, which smoothly integrates with the Miradi API to jump-start analysis on any Miradi project or program.

Here's a sample Power BI report, using the data from the **Miradi Islands Seascape (Example Program)**:

[Link to interactive DataViz](https://app.powerbi.com/view?r=eyJrIjoiZDg4YzgyNzEtYzI2MC00NDM4LWEwM2QtYTA1MjI2NTczMTg5IiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D)

[![Click to view and interact with the report](https://github.com/Mike-Honey/miradi/blob/master/Miradi%20Program%20Dashboard%20-%20Miradi%20Islands%20Seascape%20(Example%20Program).png?raw=true)](https://app.powerbi.com/view?r=eyJrIjoiZDg4YzgyNzEtYzI2MC00NDM4LWEwM2QtYTA1MjI2NTczMTg5IiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D)


This article in the Miradi Help Centre describes their API and the Power BI template, and provides a link to get started.  
[Miradi API](https://help.miradishare.org/hc/en-us/articles/7651985079963-Miradi-API)

The [Power BI template](https://github.com/Mike-Honey/miradi/raw/master/Miradi%20Program%20Dashboard%20-%20Miradi%20Islands%20Seascape%20(Example%20Program).pbix) integrates and models the key data from Miradi, and presents a set of interactive pages to start exploring and analyzing. The June 2024 update includes:
- replacing the MapBox maps with the IconMap Custom Visual. Integration via Power Queries with embedded Python scripts - automates the extraction of shapes from any Miradi program
- Program Overview page: map now coloured by Overall Viability Status 
- Threats page: map added to show Threat Footprints
- Threat tooltips are now more informative
- Indicators .. Taxonomies tables added to the semantic model
- HTML Content custom visual was replaced with the HTML Content 

[Power BI](https://www.microsoft.com/en-au/power-platform/products/power-bi/) provides a great platform to extend the template - to build alternative visuals or page layouts, or to integrate data from other sources. Power BI can automate the chores of keeping your report up-to-date and distributing it to the right audience.

While developing this template, I've been grateful for the help, support and guidance from teams at [Foundations of Success](https://www.linkedin.com/company/foundations-of-success/), [ESA Sitka](https://www.linkedin.com/company/sitka-technology-group), [Bush Heritage Australia](https://www.linkedin.com/company/bush-heritage-australia), [Conservation Management](https://www.linkedin.com/company/bush-heritage-australia) and the [Gordon and Betty Moore Foundation](https://www.linkedin.com/company/moore-foundation).

The template has already been deployed at several organisations, and I'm keen to see it widely used. Please feel free to contact me if you are interested or have any questions.

## python scripts

Python scripts are embedded in the Power BI queries. These require [python 3](https://www.python.org/downloads/) with the following libraries: pandas, bs4, geopandas, json, topojson.  The Power BI Desktop options must be configured to select your python home folder.

Python is required to translate the spatial shapes from geojson to WKT, required for the IconMap custom visual. Python scripts calling the bs4 library have replaced the embedded Power BI M queries - they are more effective and far fewer lines of code.

Scheduled refresh scenarios with the Power BI web service and python require the [Power BI Gateway](https://www.microsoft.com/en-us/power-platform/products/power-bi/gateway) component in Personal Mode.

For ease of review and testing, the python scripts used are provided as .py files, with .csv files for test input.

## Results Chain Diagrams

Examples (from the Miradi sample projects) of diagrams exported from Miradi for access by Power BI custom visuals.  You could clone this project and upload your own results chain diagrams following the naming standard, then point the Power BI template for Miradi at your clone to view your own diagrams.

/ResultsChainDiagrams sub-folder naming standard is /[Project Name]. Special characters in Project Names have to be removed to meet github & file system constraints. 

Within each sub-folder, Results Chain diagrams should be named [Results Chain ID and Name].png (which is the default names given on export from Miradi Share. Those files can then be referred to by analysis tools e.g. Power BI.

# Spatial

This is a method to extract the spatial data stored in Miradi for Projects and Threats, and output each in a geojson file for integration with MapBox or similar. This method is no longer required, if you are happy with the integrated IconMap custom visuals.

The instructions are provided at the top of the Python script.  Power BI Desktop is also required. Sample data files from the Miradi sample program are provided, also in the Spatial sub-folder.

## 2025-05 release

This update extends the python scripts to include calls to the bs4 library to strip HTML tags.  These replace embedded Power BI M functions, and resolve some bugs as well as requiring far fewer lines of code.

There were also many performance improvements made in measures, as well as new measures for % Complete and Progress Status.

## 🤝 Support

Contributions, issues, feature requests and sponsorship are all welcome!

Give a ⭐️ if you like this project!

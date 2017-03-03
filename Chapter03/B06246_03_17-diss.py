# Dissolving Vector Shapes

# https://github.com/GeospatialPython/Learn/raw/master/GIS_CensusTract.zip

import processing

processing.runandload("qgis:dissolve","/qgis_data/census/GIS_CensusTract_poly.shp",False,"COUNTY_8","/qgis_data/census/dissovle.shp")
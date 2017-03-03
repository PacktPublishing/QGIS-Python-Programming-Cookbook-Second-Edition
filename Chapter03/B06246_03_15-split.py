# Splitting a Shapefile

# https://github.com/GeospatialPython/Learn/raw/master/GIS_CensusTract.zip

import processing
pth = "/qgis_data/census/"
processing.runalg("qgis:splitvectorlayer",pth + "GIS_CensusTract_poly.shp","COUNTY_8",pth)

# Generalizing a Vector Layer

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

import processing
processing.runandload("qgis:simplifygeometries","/qgis_data/ms/mississippi.shp",0.3,"/qgis_data/ms/generalize.shp")
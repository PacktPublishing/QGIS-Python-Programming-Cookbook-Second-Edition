# Clipping a Raster using a Shapefile

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

import processing

processing.runandload("gdalogr:cliprasterbymasklayer","/qgis_data/rasters/SatImage.tif","/qgis_data/hancock/hancock.shp",None,False,False,False,0,4,75,6,1,False,0,False,"",None)
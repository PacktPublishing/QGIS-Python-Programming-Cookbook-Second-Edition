# Creating Pyramids for a Raster

# https://github.com/GeospatialPython/Learn/raw/master/FalseColor.zip

import processing

processing.runalg("gdalogr:overviews","/qgis_data/rasters/FalseColor.tif","2 4 8 16",True,0,1)

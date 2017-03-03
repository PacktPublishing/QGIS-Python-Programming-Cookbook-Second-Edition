# Rasterizing a Vector Layer

# https://github.com/GeospatialPython/Learn/raw/master/contour.zip

import processing

processing.runalg("gdalogr:rasterize","/qgis_data/rasters/contour.shp","ELEV",1,100,100,"428212.21,465052.21,5566050.73,5595210.73",False,5,"",4,75,6,1,False,0,"","/.qgis2/processing/outputs/raster_contour.tif")
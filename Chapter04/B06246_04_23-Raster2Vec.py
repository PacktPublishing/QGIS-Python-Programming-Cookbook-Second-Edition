# Converting a Raster to a Vector

# https://github.com/GeospatialPython/Learn/raw/master/landuse_bay.zip

import processing

processing.runandload("gdalogr:polygonize","/qgis_data/rasters/landuse_bay.tif","DN",None)

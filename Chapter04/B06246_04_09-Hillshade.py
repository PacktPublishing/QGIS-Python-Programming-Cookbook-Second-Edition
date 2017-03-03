# Creating an Elevation Hillshade

# https://github.com/GeospatialPython/Learn/raw/master/dem.zip

import processing
rasterLyr = QgsRasterLayer("/qgis_data/rasters/dem.asc", "Hillshade")
rasterLyr.isValid()
# True
processing.runandload("gdalogr:hillshade", rasterLyr, 1, False, False, 1.0, 1.0, 315.0, 45.0, "/qgis_data/rasters/hillshade.tif")



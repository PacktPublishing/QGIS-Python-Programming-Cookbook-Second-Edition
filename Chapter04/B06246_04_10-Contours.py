# Creating Vector Contours from Elevation Data

# https://github.com/GeospatialPython/Learn/raw/master/dem.zip

import processing
rasterLyr = QgsRasterLayer("/qgis_data/rasters/dem.asc", "DEM")
rasterLyr.isValid()
# True
QgsMapLayerRegistry.instance().addMapLayers([rasterLyr])
processing.runandload("gdalogr:contour", rasterLyr, 50.0, "Elv", None, "/qgis_data/rasters/contours.shp")


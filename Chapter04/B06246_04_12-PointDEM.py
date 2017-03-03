# Adding Elevation Data to Line Vertices using a DEM

# https://github.com/GeospatialPython/Learn/raw/master/path.zip

import processing
from PyQt4.QtCore import *

pth = "/qgis_data/rasters/path/"
rasterPth = pth + "elevation.asc"
vectorPth = pth + "paths.shp"
pointsPth = pth + "points.shp"
elvPointsPth = pth + "elvPoints.shp" 

settings = QSettings()
originalSetting = settings.value("/Projections/defaultBehaviour", "prompt", type=str)
settings.setValue("/Projections/defaultBehaviour", "useProject")

rasterLyr = QgsRasterLayer(rasterPth, "Elevation")
crs = QgsCoordinateReferenceSystem()
crs.createFromSrid(4326)
rasterLyr.setCrs(crs)
settings.setValue( "/Projections/defaultBehaviour", originalSetting)

rasterLyr.isValid()
# True


vectorLyr = QgsVectorLayer(vectorPth, "Path", "ogr")
vectorLyr.isValid()
# True

QgsMapLayerRegistry.instance().addMapLayers([rasterLyr])

QgsMapLayerRegistry.instance().addMapLayers([vectorLyr, rasterLyr])
processing.runalg("saga:convertlinestopoints", vectorLyr, False, 1, pointsPth)
processing.runandload("saga:addgridvaluestopoints", pointsPth, rasterPth, 0, elvPointsPth)

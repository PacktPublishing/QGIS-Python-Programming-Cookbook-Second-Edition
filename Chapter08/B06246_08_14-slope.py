# Computing Road Slope using Elevation Data

# https://github.com/GeospatialPython/Learn/raw/master/road.zip

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import processing

dem = "/qgis_data/road/dem.asc"
road = "/qgis_data/road/road.shp"
slope = "/qgis_data/road/slope.tif"
segRoad = "/qgis_data/road/segRoad.shp"
steepness = "/qgis_data/road/steepness.shp"
hillshade = "/qgis_data/road/hillshade.tif"

demLyr = QgsRasterLayer(dem, "DEM")
roadLyr = QgsVectorLayer(road, "Road", "ogr")

ext = demLyr.extent()
xmin = ext.xMinimum()
ymin = ext.yMinimum()
xmax = ext.xMaximum()
ymax = ext.yMaximum()
demBox = "{},{},{},{}".format(xmin,xmax,ymin,ymax)

processing.runalg("grass7:r.slope",dem,0,False,1,0,demBox,0,slope)

ext = roadLyr.extent()
xmin = ext.xMinimum()
ymin = ext.yMinimum()
xmax = ext.xMaximum()
ymax = ext.yMaximum()
roadBox = "{},{},{},{}".format(xmin,xmax,ymin,ymax)

processing.runalg("grass7:v.split.length",road,500,roadBox,-1,0.0001,0,segRoad)


slopeLyr = QgsRasterLayer(slope, "Slope")
segRoadLyr = QgsVectorLayer(segRoad, "Segmented Road", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([segRoadLyr,slopeLyr], False)

processing.runalg("saga:addgridvaluestoshapes",segRoad,slope,0,steepness)
steepLyr = QgsVectorLayer(steepness, "Road Gradient", "ogr")

roadGrade = (
("Rolling Hill", 0.0, 20.0, "green"), 
("Steep", 20.0, 40.0, "yellow"),
("Very Steep", 40.0, 90.0, "red"))

ranges = []
for label, lower, upper, color in roadGrade:
    sym = QgsSymbolV2.defaultSymbol(steepLyr.geometryType())
    sym.setColor(QColor(color))
    sym.setWidth(3.0)
    rng = QgsRendererRangeV2(lower, upper, sym, label)
    ranges.append(rng)

field = "slopetif"
renderer = QgsGraduatedSymbolRendererV2(field, ranges)
steepLyr.setRendererV2(renderer)

processing.runalg("saga:analyticalhillshading",dem,0,158,45,4,hillshade)

hs = QgsRasterLayer(hillshade, "Terrain")

QgsMapLayerRegistry.instance().addMapLayers([steepLyr, hs])
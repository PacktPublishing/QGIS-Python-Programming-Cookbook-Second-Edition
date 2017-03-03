# Creating Tiles from a QGIS Map

# https://github.com/GeospatialPython/Learn/raw/master/countries.zip

# Requires QMetaTiles plugin

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import QMetaTiles
import random

def randomColor(mix=(255,255,255)):
    red = random.randrange(0,256)
    green = random.randrange(0,256)
    blue = random.randrange(0,256)
    r,g,b = mix
    red = (red + r) / 2
    green = (green + g) / 2
    blue = (blue + b) / 2
    return (red, green, blue)

def done():
    print "FINISHED!!"

shp = "/qgis_data/shapes/countries.shp"

dir = "/qgis_data/tilecache"

layer = QgsVectorLayer(shp, "Countries", "ogr")

field = 'CNTRY_NAME'

features = layer.getFeatures()

categories = []

for feature in features:
	country = feature[field]
	sym = QgsSymbolV2.defaultSymbol(layer.geometryType())
	r,g,b = randomColor()
	sym.setColor(QColor(r,g,b,255))
	category = QgsRendererCategoryV2(country, sym, country)
	categories.append(category)	

renderer = QgsCategorizedSymbolRendererV2(field, categories)
layer.setRendererV2(renderer)
QgsMapLayerRegistry.instance().addMapLayer(layer)	

canvas = iface.mapCanvas()
layers = canvas.mapSettings().layers()
extent = canvas.extent()
minZoom = 0
maxZoom = 5
width = 256
height = 256
transp = 100
quality = 70
format = "PNG"
outputPath = QFileInfo(dir)
rootDir = "countries"
antialiasing = False
tmsConvention = True
mapUrl = False
viewer = True

tt = QMetaTiles.tilingthread.TilingThread(layers, extent, minZoom, 
                                          maxZoom, width, height, 
                                          transp, quality, format, 
                                          outputPath, rootDir, antialiasing, 
                                          tmsConvention, mapUrl, viewer, 
                                          False, None, False, None)

tt.processFinished.connect(done)
                 
tt.start()

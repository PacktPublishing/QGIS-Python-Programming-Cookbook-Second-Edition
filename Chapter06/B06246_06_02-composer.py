# Using the Map Composer

# https://github.com/GeospatialPython/Learn/raw/master/hancock.zip

from PyQt4.QtGui import *
from PyQt4.QtCore import *

lyr = QgsVectorLayer("/qgis_data/hancock/hancock.shp", "Hancock", "ogr")
reg = QgsMapLayerRegistry.instance()
reg.addMapLayer(lyr)
lyrs = reg.mapLayers().keys()
mr = iface.mapCanvas().mapRenderer()
mr.setLayerSet(lyrs)
rect = QgsRectangle(lyr.extent())
rect.scale(1.2)
mr.setExtent(rect) 
c = QgsComposition(mr)
c.setPlotStyle(QgsComposition.Print)
c.setPaperSize(215.9, 279.4)
w, h = c.paperWidth() * .50, c.paperHeight() * .50
x = (c.paperWidth() - w) / 2
y = ((c.paperHeight() - h)) / 2 
composerMap = QgsComposerMap(c,x,y,w,h)
composerMap.setNewExtent(rect)
composerMap.setFrameEnabled(True)
c.addItem(composerMap)

# Set resolution
dpi = c.printResolution()
c.setPrintResolution(dpi)
dpmm = dpi / 25.4
width = int(dpmm * c.paperWidth())
height = int(dpmm * c.paperHeight())

# create output image and initialize it
image = QImage(QSize(width, height), QImage.Format_ARGB32)
image.setDotsPerMeterX(dpmm * 1000)
image.setDotsPerMeterY(dpmm * 1000)
image.fill(0)

# render the composition
imagePainter = QPainter(image)
sourceArea = QRectF(0, 0, c.paperWidth(), c.paperHeight())
targetArea = QRectF(0, 0, width, height)
c.render(imagePainter, targetArea, sourceArea)
imagePainter.end()

image.save("/qgis_data/map.jpg", "jpg")

# Symbolizing a Vector Layer

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

from PyQt4.QtGui import *

lyr = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")
QgsMapLayerRegistry.instance().addMapLayer(lyr)
symbols = lyr.rendererV2().symbols()
sym = symbols[0]
sym.setColor(QColor.fromRgb(255,0,0))
lyr.triggerRepaint()


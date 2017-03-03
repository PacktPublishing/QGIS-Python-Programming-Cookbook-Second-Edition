# Creating the Simplest Map Renderer

# https://github.com/GeospatialPython/Learn/raw/master/hancock.zip

from PyQt4.QtGui import *
from PyQt4.QtCore import *

lyr = QgsVectorLayer("/qgis_data/hancock/hancock.shp", "Hancock", "ogr")
reg = QgsMapLayerRegistry.instance()
reg.addMapLayer(lyr)
i = QImage(QSize(600,600), QImage.Format_ARGB32_Premultiplied)
c = QColor("white")
i.fill(c.rgb())
p = QPainter()
p.begin(i)
r = QgsMapRenderer()
lyrs = reg.mapLayers().keys()
r.setLayerSet(lyrs)
rect = QgsRectangle(r.fullExtent())
rect.scale(1.1)
r.setExtent(rect) 
r.setOutputSize(i.size(), i.logicalDpiX())
r.render(p)
p.end()
i.save("/qgis_data/map.jpg","jpg")
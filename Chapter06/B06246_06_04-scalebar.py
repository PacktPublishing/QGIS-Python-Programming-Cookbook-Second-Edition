# Adding a Scale Bar to a Map

# https://github.com/GeospatialPython/Learn/raw/master/MapComposer.py
# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import MapComposer

lyr = QgsVectorLayer("/qgis_data/ms/Mississippi.shp", "Mississippi", "ogr")
reg = QgsMapLayerRegistry.instance()
reg.addMapLayer(lyr)
mr = iface.mapCanvas().mapRenderer()	
qc = MapComposer.MapComposer(qmlr=reg, qmr=mr)
qc.scalebar = QgsComposerScaleBar(qc.c)
qc.scalebar.setStyle('Single Box')
qc.scalebar.setComposerMap(qc.composerMap)
qc.scalebar.applyDefaultSize()
sbw = qc.scalebar.rect().width()
sbh = qc.scalebar.rect().height()
mcw = qc.composerMap.rect().width()
mch = qc.composerMap.rect().height()
sbx = qc.x + (mcw - sbw)
sby = qc.y + mch	
qc.scalebar.setItemPosition(sbx, sby)
qc.c.addItem(qc.scalebar)

qc.output("/qgis_data/map.jpg", "jpg")
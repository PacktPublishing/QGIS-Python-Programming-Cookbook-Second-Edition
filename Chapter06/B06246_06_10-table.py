# Adding a Table to the Map

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
	
qc.table = QgsComposerAttributeTable(qc.c)
qc.table.setComposerMap(qc.composerMap)
qc.table.setVectorLayer(lyr)
mch = qc.composerMap.rect().height()	
qc.table.setItemPosition(qc.x, qc.y + mch + 20)
qc.c.addItem(qc.table)

qc.output("/qgis_data/map.jpg", "jpg")


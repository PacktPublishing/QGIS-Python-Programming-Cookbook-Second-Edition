# Adding Labels to a Map for Printing

# https://github.com/GeospatialPython/Learn/raw/master/MapComposer.py
# https://github.com/GeospatialPython/Learn/raw/master/hancock.zip

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MapComposer

lyr = QgsVectorLayer("/qgis_data/hancock/hancock.shp", "Hancock", "ogr")
reg = QgsMapLayerRegistry.instance()
reg.addMapLayer(lyr)
mr = iface.mapCanvas().mapRenderer()
qc = MapComposer.MapComposer(qmlr=reg, qmr=mr)
qc.label = QgsComposerLabel(qc.c)
qc.label.setText("Hancock County")
qc.label.adjustSizeToText()
qc.label.setFrameEnabled(True)
qc.label.setItemPosition(qc.x,qc.y-10)
qc.c.addItem(qc.label)	
qc.output("/qgis_data/map.jpg", "jpg")
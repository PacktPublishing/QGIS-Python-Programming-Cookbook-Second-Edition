# Adding a Vertical Legend to the Map

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

qc.legend = QgsComposerLegend(qc.c)
qc.legend.model().setLayerSet(qc.qmr.layerSet())
qc.legend.setItemPosition(5, qc.y)
qc.c.addItem(qc.legend)

qc.output("/qgis_data/map.jpg", "jpg")
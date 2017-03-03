# Adding a Horizontal Legend to the Map

# https://github.com/GeospatialPython/Learn/raw/master/MapComposer.py
# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip
# https://github.com/GeospatialPython/Learn/raw/master/MSCities_Geo_Pts.shp

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import MapComposer

lyr = QgsVectorLayer("/qgis_data/ms/Mississippi.shp", "Mississippi", "ogr")
lyr2 = QgsVectorLayer("/qgis_data/ms/MSCities_Geo_Pts.shp", "Cities", "ogr")
reg = QgsMapLayerRegistry.instance()
reg.addMapLayers([lyr2, lyr])
mr = iface.mapCanvas().mapRenderer()
qc = MapComposer.MapComposer(qmlr=reg, qmr=mr)

qc.legend = QgsComposerLegend(qc.c)
qc.legend.model().setLayerSet(qc.qmr.layerSet())
qc.legend.setItemPosition(50,50)
qc.legend.setColumnCount(2)
qc.c.addItem(qc.legend)

qc.output("/qgis_data/map.jpg", "jpg")
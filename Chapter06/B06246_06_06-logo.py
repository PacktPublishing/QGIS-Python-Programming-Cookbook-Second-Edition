# Adding a Logo to the Map

# https://github.com/GeospatialPython/Learn/raw/master/MapComposer.py
# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import MapComposer

lyr = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")
reg = QgsMapLayerRegistry.instance()
reg.addMapLayer(lyr)
mr = iface.mapCanvas().mapRenderer()	
qc = MapComposer.MapComposer(qmlr=reg, qmr=mr)

qc.logo = QgsComposerPicture(qc.c)
qc.logo.setPictureFile("/qgis_data/rasters/logo.png")
qc.logo.setSceneRect(QRectF(0,0,43,50))
lx = qc.x + 50
ly = qc.y - 50   
qc.logo.setItemPosition(lx, ly)
qc.c.addItem(qc.logo)

qc.output("/qgis_data/map.jpg", "jpg")	
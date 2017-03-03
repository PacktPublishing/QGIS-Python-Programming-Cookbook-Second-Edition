# Adding a North Arrow to the Map

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

mcw = qc.composerMap.rect().width()
mch = qc.composerMap.rect().height()
ax =  qc.x + mcw + 10
ay =  (qc.y + mch) - 10
afy = ay - 20
qc.arrow = QgsComposerArrow(QPointF(ax, ay), QPointF(ax,afy), qc.c)
qc.c.addItem(qc.arrow)	

f = QFont()
f.setBold(True)
f.setFamily("Times New Roman")
f.setPointSize(30)
qc.labelNorth = QgsComposerLabel(qc.c)
qc.labelNorth.setText("N")
qc.labelNorth.setFont(f)
qc.labelNorth.adjustSizeToText()
qc.labelNorth.setFrameEnabled(False)
qc.labelNorth.setItemPosition(ax - 5, ay)	
qc.c.addItem(qc.labelNorth)	

qc.output("/qgis_data/map.jpg", "jpg")	
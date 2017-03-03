# Adding a Custom Shape to the Map

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

red = {'color':'255,0,0,255','color_border':'0,0,0,255'}
redsym = QgsFillSymbolV2.createSimple(red)
blue = {'color':'0,0,255,255','color_border':'0,0,0,255'}
bluesym = QgsFillSymbolV2.createSimple(blue)
yellow = {'color':'255,255,0,255','color_border':'0,0,0,255'}
yellowsym = QgsFillSymbolV2.createSimple(yellow)
mch = qc.composerMap.rect().height()
sy = qc.y + mch
qc.shape1 = QgsComposerShape(10,sy-25,10,25,qc.c)
qc.shape1.setShapeType(1)
qc.shape1.setUseSymbolV2(True)
qc.c.addItem(qc.shape1)
qc.shape1.setShapeStyleSymbol(redsym)
qc.shape2 = QgsComposerShape(22,sy-18,10,18,qc.c)
qc.shape2.setShapeType(1)
qc.shape2.setUseSymbolV2(True)
qc.shape2.setShapeStyleSymbol(bluesym)
qc.c.addItem(qc.shape2)
qc.shape3 = QgsComposerShape(34,sy-12,10,12,qc.c)
qc.shape3.setShapeType(1)
qc.shape3.setUseSymbolV2(True)
qc.shape3.setShapeStyleSymbol(yellowsym)
qc.c.addItem(qc.shape3)

qc.output("/qgis_data/map.jpg", "jpg")

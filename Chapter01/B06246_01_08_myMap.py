# Standalone QGIS script
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QgsApplication([], True)
path = "C:/Program Files/QGIS2.18/apps/qgis"
app.setPrefixPath(path, True)
app.initQgis()
canvas = QgsMapCanvas()
title = "PyQGIS Standalone Application Example"
canvas.setWindowTitle(title)
canvas.setCanvasColor(Qt.white)
layer_info = 'LineString?crs=epsg:4326'
layer =  QgsVectorLayer(layer_info, 'MyLine' , "memory")
pr = layer.dataProvider()
linstr = QgsFeature()
wkt = "LINESTRING (1 1, 10 15, 40 35)"
geom = QgsGeometry.fromWkt(wkt)
linstr.setGeometry(geom)
pr.addFeatures([linstr])
layer.updateExtents()
QgsMapLayerRegistry.instance().addMapLayer(layer)
canvas.setExtent(layer.extent())
canvas.setLayerSet([QgsMapCanvasLayer(layer)])
canvas.zoomToFullExtent()
canvas.show()
exitcode = app.exec_()
QgsApplication.exitQgis()
sys.exit(exitcode)


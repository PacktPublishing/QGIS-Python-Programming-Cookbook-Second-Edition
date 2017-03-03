# Adding a Grid to the Map

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

# setGridAnnotationPosition method reference
setGridAnnoPos = qc.composerMap.setGridAnnotationPosition

# setGridAnnotationDir method reference
setGridAnnoDir = qc.composerMap.setGridAnnotationDirection

# QgsComposerMap
qcm = QgsComposerMap

# Create the map grid.
qc.composerMap.setGridEnabled(True)
qc.composerMap.setGridIntervalX(.75)
qc.composerMap.setGridIntervalY(.75)
qc.composerMap.setGridStyle(qcm.Solid)
qc.composerMap.setShowGridAnnotation(True)
qc.composerMap.setGridAnnotationPrecision(0)


# Top
setGridAnnoPos(qcm.OutsideMapFrame, qcm.Top)
setGridAnnoDir(qcm.Horizontal, qcm.Top)

# Bottom
setGridAnnoPos(qcm.OutsideMapFrame, qcm.Bottom)
setGridAnnoDir(qcm.Horizontal, qcm.Bottom)

# Left
setGridAnnoPos(qcm.OutsideMapFrame, qcm.Left)
setGridAnnoDir(qcm.Vertical, qcm.Left)

# Right
setGridAnnoPos(qcm.OutsideMapFrame, qcm.Right)
setGridAnnoDir(qcm.Vertical, qcm.Right)

qc.composerMap.setAnnotationFrameDistance(1)
qc.composerMap.setGridPenWidth(.2)
qc.composerMap.setGridPenColor(QColor(0, 0, 0))
qc.composerMap.setAnnotationFontColor(QColor(0, 0, 0))
qc.c.addComposerMap(qc.composerMap)

qc.output("/qgis_data/map.jpg", "jpg")	
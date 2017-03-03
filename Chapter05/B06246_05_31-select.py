# Building a Custom Selection Tool

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

from qgis.gui import *
from qgis.core import *
from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL, Qt
import sys, os

class MyWnd(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        QgsApplication.setPrefixPath("/Applications/QGIS.app/Contents/MacOS/", True)
        QgsApplication.initQgis()
        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(Qt.white)
        self.lyr = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "Mississippi", "ogr")
        QgsMapLayerRegistry.instance().addMapLayer(self.lyr)
        self.canvas.setExtent(self.lyr.extent())
        self.canvas.setLayerSet([QgsMapCanvasLayer(self.lyr)])
        
        self.setCentralWidget(self.canvas)
        actionZoomIn = QAction("Zoom in", self)
        actionZoomOut = QAction("Zoom out", self)
        actionPan = QAction("Pan", self)
        actionSelect = QAction("Select", self)
        
        actionZoomIn.setCheckable(True)
        actionZoomOut.setCheckable(True)
        actionPan.setCheckable(True)
        actionSelect.setCheckable(True)
        
        self.connect(actionZoomIn, SIGNAL("triggered()"), self.zoomIn)
        self.connect(actionZoomOut, SIGNAL("triggered()"), self.zoomOut)
        self.connect(actionPan, SIGNAL("triggered()"), self.pan)
        self.connect(actionSelect, SIGNAL("triggered()"), self.select)
                
        self.toolbar = self.addToolBar("Canvas actions")
        self.toolbar.addAction(actionZoomIn)
        self.toolbar.addAction(actionZoomOut)
        self.toolbar.addAction(actionPan)
        self.toolbar.addAction(actionSelect)
        
        # create the map tools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
        self.toolZoomIn.setAction(actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
        self.toolZoomOut.setAction(actionZoomOut)
        self.toolSelect = SelectMapTool(self.canvas, self.lyr) 
        self.toolSelect.setAction(actionSelect)
                
        self.select()
        
        
    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)
        
    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)
        
    def pan(self):
        self.canvas.setMapTool(self.toolPan)

    def select(self):
        self.canvas.setMapTool(self.toolSelect)

class SelectMapTool(QgsMapToolEmitPoint):
    def __init__(self, canvas, lyr):
        self.canvas = canvas
        self.lyr = lyr
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.rubberband = QgsRubberBand(self.canvas, QGis.Polygon)
        self.rubberband.setColor(QColor(255,255,0,50))
        self.rubberband.setWidth(1)
        self.point = None
        self.points = []
    
    def canvasPressEvent(self, e):
        self.point = self.toMapCoordinates(e.pos())
        m = QgsVertexMarker(self.canvas)
        m.setCenter(self.point)
        m.setColor(QColor(0,255,0))
        m.setIconSize(5)
        m.setIconType(QgsVertexMarker.ICON_BOX)
        m.setPenWidth(3) 
        self.points.append(self.point)
        self.isEmittingPoint = True
        self.selectPoly()

    def selectPoly(self):
        self.rubberband.reset(QGis.Polygon)
        for point in self.points[:-1]:
            self.rubberband.addPoint(point, False)
        self.rubberband.addPoint(self.points[-1], True)
        self.rubberband.show() 
        if len(self.points) > 2:
            g = self.rubberband.asGeometry()
            featsPnt = self.lyr.getFeatures(QgsFeatureRequest().setFilterRect(g.boundingBox()))
            for featPnt in featsPnt:
                if featPnt.geometry().within(g):
                    self.lyr.select(featPnt.id())                  
        
class MainApp(QApplication):
    def __init__(self):
        QApplication.__init__(self,[],True)
        wdg = MyWnd()
        wdg.show()
        self.exec_()

if __name__ == "__main__":
    import sys
    app = MainApp()


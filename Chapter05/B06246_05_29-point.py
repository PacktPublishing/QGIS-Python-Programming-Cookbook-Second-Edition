# A Map Tool to Draw Points on the Canvas

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
        self.lyr = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")
        QgsMapLayerRegistry.instance().addMapLayer(self.lyr)
        self.canvas.setExtent(self.lyr.extent())
        self.canvas.setLayerSet([QgsMapCanvasLayer(self.lyr)])
        
        self.setCentralWidget(self.canvas)
        actionZoomIn = QAction("Zoom in", self)
        actionZoomOut = QAction("Zoom out", self)
        actionPan = QAction("Pan", self)
        actionPoint = QAction("Point", self)
        
        actionZoomIn.setCheckable(True)
        actionZoomOut.setCheckable(True)
        actionPan.setCheckable(True)
        actionPoint.setCheckable(True)
        
        self.connect(actionZoomIn, SIGNAL("triggered()"), self.zoomIn)
        self.connect(actionZoomOut, SIGNAL("triggered()"), self.zoomOut)
        self.connect(actionPan, SIGNAL("triggered()"), self.pan)
        self.connect(actionPoint, SIGNAL("triggered()"), self.point)
                
        self.toolbar = self.addToolBar("Canvas actions")
        self.toolbar.addAction(actionZoomIn)
        self.toolbar.addAction(actionZoomOut)
        self.toolbar.addAction(actionPan)
        self.toolbar.addAction(actionPoint)
        
        # create the map tools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
        self.toolZoomIn.setAction(actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
        self.toolZoomOut.setAction(actionZoomOut)
        self.toolPoint = PointMapTool(self.canvas) 
        self.toolPoint.setAction(actionPoint)
                
        self.point()
        
        
    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)
        
    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)
        
    def pan(self):
        self.canvas.setMapTool(self.toolPan)

    def point(self):
        self.canvas.setMapTool(self.toolPoint)

class PointMapTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.point = None
    
    def canvasPressEvent(self, e):
        self.point = self.toMapCoordinates(e.pos())
        print self.point.x(), self.point.y()
        m = QgsVertexMarker(self.canvas)
        m.setCenter(self.point)
        m.setColor(QColor(0,255,0))
        m.setIconSize(5)
        m.setIconType(QgsVertexMarker.ICON_BOX) # or ICON_CROSS, ICON_X
        m.setPenWidth(3) 
        
class MainApp(QApplication):
    def __init__(self):
        QApplication.__init__(self,[],True)
        wdg = MyWnd()
        wdg.show()
        self.exec_()

if __name__ == "__main__":
    import sys
    app = MainApp()


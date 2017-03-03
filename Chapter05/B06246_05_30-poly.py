# A Map Tool to Draw Polygons or Lines on the Canvas

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
        actionPoly = QAction("Polygon", self)
        
        actionZoomIn.setCheckable(True)
        actionZoomOut.setCheckable(True)
        actionPan.setCheckable(True)
        actionPoly.setCheckable(True)
        
        self.connect(actionZoomIn, SIGNAL("triggered()"), self.zoomIn)
        self.connect(actionZoomOut, SIGNAL("triggered()"), self.zoomOut)
        self.connect(actionPan, SIGNAL("triggered()"), self.pan)
        self.connect(actionPoly, SIGNAL("triggered()"), self.poly)
                
        self.toolbar = self.addToolBar("Canvas actions")
        self.toolbar.addAction(actionZoomIn)
        self.toolbar.addAction(actionZoomOut)
        self.toolbar.addAction(actionPan)
        self.toolbar.addAction(actionPoly)
        
        # create the map tools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
        self.toolZoomIn.setAction(actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
        self.toolZoomOut.setAction(actionZoomOut)
        self.toolPoly = PolyMapTool(self.canvas) 
        self.toolPoly.setAction(actionPoly)
                
        self.poly()
        
        
    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)
        
    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)
        
    def pan(self):
        self.canvas.setMapTool(self.toolPan)

    def poly(self):
        self.canvas.setMapTool(self.toolPoly)

class PolyMapTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.rubberband = QgsRubberBand(self.canvas, QGis.Polygon)
        self.rubberband.setColor(Qt.red)
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
        self.showPoly()

    def showPoly(self):
        self.rubberband.reset(QGis.Polygon)
        for point in self.points[:-1]:
            self.rubberband.addPoint(point, False)
        self.rubberband.addPoint(self.points[-1], True)
        self.rubberband.show()         
        
class MainApp(QApplication):
    def __init__(self):
        QApplication.__init__(self,[],True)
        wdg = MyWnd()
        wdg.show()
        self.exec_()

if __name__ == "__main__":
    import sys
    app = MainApp()



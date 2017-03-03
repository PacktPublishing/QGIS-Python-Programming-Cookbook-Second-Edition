# Adding Standard Map Tools to the Canvas

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
        
        actionZoomIn.setCheckable(True)
        actionZoomOut.setCheckable(True)
        actionPan.setCheckable(True)
        
        self.connect(actionZoomIn, SIGNAL("triggered()"), self.zoomIn)
        self.connect(actionZoomOut, SIGNAL("triggered()"), self.zoomOut)
        self.connect(actionPan, SIGNAL("triggered()"), self.pan)
        
        self.toolbar = self.addToolBar("Canvas actions")
        self.toolbar.addAction(actionZoomIn)
        self.toolbar.addAction(actionZoomOut)
        self.toolbar.addAction(actionPan)
        
        # create the map tools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
        self.toolZoomIn.setAction(actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
        self.toolZoomOut.setAction(actionZoomOut)
        
        # Button selected when the application loads:
        self.pan()
        
    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)
        
    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)
        
    def pan(self):
        self.canvas.setMapTool(self.toolPan)
        
        
class MainApp(QApplication):
    def __init__(self):
        QApplication.__init__(self,[],True)
        wdg = MyWnd()
        wdg.show()
        self.exec_()

if __name__ == "__main__":
    import sys
    app = MainApp()

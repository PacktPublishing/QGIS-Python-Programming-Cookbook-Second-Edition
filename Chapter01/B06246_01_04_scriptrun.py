from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

def run_script(iface):
    """ Put your code here and remove the pass statement"""
    layer =  QgsVectorLayer('Polygon?crs=epsg:4326', 'Mississippi' , "memory")
    pr = layer.dataProvider()
    poly = QgsFeature()
    geom = QgsGeometry.fromWkt("""POLYGON ((-88.82 34.99,
                               -88.09 34.89,
                               -88.39 30.34,
                               -89.57 30.18,
                               -89.73 31,
                               -91.63 30.99,
                               -90.87 32.37,
                               -91.23 33.44,
                               -90.93 34.23,
                               -90.30 34.99,
                               -88.82 34.99))""")
    poly.setGeometry(geom)
    pr.addFeatures([poly])
    layer.updateExtents()
    QgsMapLayerRegistry.instance().addMapLayers([layer])

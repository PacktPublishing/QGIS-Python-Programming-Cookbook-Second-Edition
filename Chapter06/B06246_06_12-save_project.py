# Saving a Map to a Project

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

from PyQt4.QtCore import *

lyr = QgsVectorLayer("/qgis_data/ms/Mississippi.shp", "Mississippi", "ogr")
reg = QgsMapLayerRegistry.instance()
reg.addMapLayer(lyr)
f = QFileInfo("/qgis_data/myProject.qgs") 
p = QgsProject.instance() 
p.write(f)
# Loading a Map from a Project

from PyQt4.QtCore import *

f = QFileInfo("/qgis_data/myProject.qgs") 
p = QgsProject.instance() 
p.readPath("/qgis_data/")
p.read(f)
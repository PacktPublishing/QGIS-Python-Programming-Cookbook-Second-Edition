# Adding a World File to a Map Image

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

output = "/qgis_data/map"
qc.output(output + ".jpg", "jpg")

qc.c.setWorldFileMap(qc.composerMap)
qc.c.setGenerateWorldFile(True)
wf = qc.c.computeWorldFileParameters()
with open(output + ".jgw", "w") as f:
	f.write("%s\n" % wf[0])
	f.write("%s\n" % wf[1])
	f.write("%s\n" % wf[3])
	f.write("%s\n" % wf[4])
	f.write("%s\n" % wf[2])
	f.write("%s\n" % wf[5])




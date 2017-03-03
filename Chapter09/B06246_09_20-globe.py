# Visualizing Data on a globe

# https://github.com/GeospatialPython/Learn/raw/master/ufo.zip

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mmqgis import mmqgis_library as mmqgis
import platform
import os

pth = "/qgis_data/continental-us.shp"

lyrName = "continental-us"

lyr = QgsVectorLayer(pth, lyrName, "ogr")

QgsMapLayerRegistry.instance().addMapLayer(lyr, False)

output = "/qgis_data/us.kml"

nameAttr = "FIPS_CNTRY"

desc = "{{CNTRY_NAME}}"

mmqgis.mmqgis_kml_export(iface, lyrName, nameAttr, desc, True, output, False)

qds = QDesktopServices()
url = QUrl.fromLocalFile(output)
qds.openUrl(url)
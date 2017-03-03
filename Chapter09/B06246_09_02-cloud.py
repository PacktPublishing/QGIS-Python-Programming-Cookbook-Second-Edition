# Adding a layer to geojson.io

# Requires qgisio plugin (experimental)

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from tempfile import mkstemp
import os
from qgisio import geojsonio

layer = QgsVectorLayer("/qgis_data/shapes/building.shp", "Building", "ogr")

name = layer.name()

handle, tmpfile = mkstemp(suffix='.geojson')
os.close(handle)

crs = QgsCoordinateReferenceSystem(4326,
    QgsCoordinateReferenceSystem.PostgisCrsId)
error = QgsVectorFileWriter.writeAsVectorFormat(layer, tmpfile,
    "utf-8", crs, "GeoJSON", onlySelected=False)

if error != QgsVectorFileWriter.NoError:
    print "Unable to write geoJSON!"
    
with open(str(tmpfile), 'r') as f:
    contents = f.read()
    
os.remove(tmpfile)

url = geojsonio._create_gist(contents, "Layer exported from QGIS", name + ".geojson")

QDesktopServices.openUrl(QUrl(url))





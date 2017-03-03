# Using an outline for font markers

# https://github.com/GeospatialPython/Learn/raw/master/tourism_points.zip

from PyQt4.QtGui import *

src = "/qgis_data/ms/tourism_points.shp"

lyr = QgsVectorLayer(src, "Points of Interest", "ogr")

symLyr = QgsFontMarkerSymbolLayerV2(pointSize=16, color=QColor("cyan"))

symLyr.setFontFamily("'Arial'")
symLyr.setCharacter("@")
symLyr.setOutlineWidth(.5)
symLyr.setOutlineColor(QColor("black"))

lyr.rendererV2().symbols()[0].changeSymbolLayer(0, symLyr)

QgsMapLayerRegistry.instance().addMapLayer(lyr)
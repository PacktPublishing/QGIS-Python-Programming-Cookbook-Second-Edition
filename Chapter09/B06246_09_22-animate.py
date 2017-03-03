# Animating a layer

# https://github.com/GeospatialPython/Learn/raw/master/ufo.zip

# https://github.com/GeospatialPython/Learn/raw/master/alien_invasion.zip

from mmqgis import mmqgis_library as mmqgis

ufo_shp = "/qgis_data/ufo/alien_invasion.shp"
us_shp = "/qgis_data/ufo/continental-us.shp"

ufo = QgsVectorLayer(ufo_shp, "UFOs", "ogr")

us = QgsVectorLayer(us_shp, "US", "ogr")

QgsMapLayerRegistry.instance().addMapLayers([ufo, us])

mmqgis.mmqgis_animate_lines(iface, "UFOs", False, 50, "/qgis_data/ufo/video")
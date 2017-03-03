# Performing Nearest Neighbor Analysis

# Requires the MMQGIS Plugin

# https://github.com/GeospatialPython/Learn/raw/master/ufo.zip

from mmqgis import mmqgis_library as mmqgis

srcPath = "/qgis_data/ufo/ufo-sightings.shp"
dstPath = "/qgis_data/ufo/major-cities.shp"
usPath = "/qgis_data/ufo/continental-us.shp"
output = "/qgis_data/ufo/alien_invasion.shp"

srcName = "UFO Sightings"
dstName = "Major Cities"
usName = "Continental US"

source = QgsVectorLayer(srcPath, srcName, "ogr")
dest = QgsVectorLayer(dstPath, dstName, "ogr")
us = QgsVectorLayer(usPath, usName, "ogr")
QgsMapLayerRegistry.instance().addMapLayers([source, dest, us])

mmqgis.mmqgis_hub_distance(iface, srcName, dstName, "NAME", "Miles", True, output, False, True)
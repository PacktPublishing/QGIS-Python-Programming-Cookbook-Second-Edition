# Using a different Status Bar CRS than the Map

# https://github.com/GeospatialPython/Learn/raw/master/MSCities_Geo_Pts.zip

# Ensure "On the fly projection" is enabled in Project settings

pth = "/qgis_data/ms/MSCities_Geo_Pts.shp"
lyr = QgsVectorLayer(pth, "Cities", "ogr")
QgsMapLayerRegistry.instance().addMapLayer(lyr)
iface.mapCanvas().setDestinationCrs(QgsCoordinateReferenceSystem("EPSG:3815"))
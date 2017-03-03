# Iterating over Layers

# https://github.com/GeospatialPython/Learn/raw/master/MSCities_Geo_Pts.zip
# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

lyr_1 = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")
lyr_2 = QgsVectorLayer("/qgis_data/ms/MSCities_Geo_Pts.shp", "Cities", "ogr")
registry = QgsMapLayerRegistry.instance()
registry.addMapLayers([lyr_2, lyr_1])
layers = registry.mapLayers()
for l in layers:
	print l.title()

#Cities20140904160234792
#Mississippi20140904160234635


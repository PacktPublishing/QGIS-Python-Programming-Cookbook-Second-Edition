# Using an outline for font markers

# https://github.com/GeospatialPython/Learn/raw/master/countries.zip

# https://github.com/GeospatialPython/Learn/raw/master/human_migration_routes.zip

countries_shp = "/qgis_data/countries.shp"
routes_shp = "/qgis_data/human_migration_routes.shp"

countries = QgsVectorLayer(countries_shp, "Countries", "ogr")
routes = QgsVectorLayer(routes_shp, "Human Migration Routes", "ogr")

symLyr = QgsArrowSymbolLayer()

symLyr.setIsCurved(True)
symLyr.setIsRepeated(False)

routes.rendererV2().symbols()[0].changeSymbolLayer(0, symLyr)

QgsMapLayerRegistry.instance().addMapLayers([routes,countries])
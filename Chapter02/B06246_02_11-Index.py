# Creating a Spatial Index

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

lyr = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
fts = lyr.getFeatures()
first = fts.next()
index = QgsSpatialIndex()
index.insertFeature(first)
for f in fts:
  index.insertFeature(f)
QgsMapLayerRegistry.instance().addMapLayers([lyr])
hood = index.nearestNeighbor(first.geometry().asPoint(), 4)
lyr.setSelectedFeatures(hood)






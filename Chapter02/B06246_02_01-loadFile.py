# Loading a Vector Layer from a File

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

layer = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
if not layer.isValid():
  print("Layer {} did not load".format(layer.name()))
QgsMapLayerRegistry.instance().addMapLayers([layer])
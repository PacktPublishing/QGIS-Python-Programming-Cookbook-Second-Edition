# Set a feature color using a column in a CSV

# https://github.com/GeospatialPython/Learn/raw/master/point_colors.csv

uri = "file:///qgis_data/shapes/point_colors.csv?"
uri += "type=csv&"
uri += "xField=X&yField=Y&"
uri += "spatialIndex=no&"
uri += "subsetIndex=no&"
uri += "watchFile=no&"
uri += "crs=epsg:4326"
lyr = QgsVectorLayer(uri,"Points","delimitedtext")

sym = QgsSymbolV2.defaultSymbol(lyr.geometryType())
symLyr = sym.symbolLayer(0)
symLyr.setDataDefinedProperty("color", '"COLOR"')
lyr.rendererV2().symbols()[0].changeSymbolLayer(0, symLyr)

QgsMapLayerRegistry.instance().addMapLayers([lyr])
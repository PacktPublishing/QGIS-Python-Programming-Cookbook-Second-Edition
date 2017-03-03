# Loading Data from a Spreadsheet

# https://github.com/GeospatialPython/Learn/raw/master/tourism.csv

uri = "file:///Users/joellawhead/qgis_data/ms/tourism.csv?"
uri += "type=csv&"
uri += "xField=X&yField=Y&"
uri += "spatialIndex=no&"
uri += "subsetIndex=no&"
uri += "watchFile=no&"
uri += "crs=epsg:4326"
layer=QgsVectorLayer(uri,"Tourism Sites","delimitedtext")
QgsMapLayerRegistry.instance().addMapLayers([layer])

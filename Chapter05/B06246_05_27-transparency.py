# Change Map Layer Transparency

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

lyr = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")

lyr.setLayerTransparency(50)

QgsMapLayerRegistry.instance().addMapLayer(lyr)

# Setting Scale-Based Visibility for a Layer

# https://github.com/GeospatialPython/Learn/raw/master/GIS_CensusTract.zip

lyr = QgsVectorLayer("/qgis_data/census/GIS_CensusTract_poly.shp", "Census", "ogr")

lyr.toggleScaleBasedVisibility(True)

lyr.setMinimumScale(22945.0)
lyr.setMaximumScale(1000000.0)

QgsMapLayerRegistry.instance().addMapLayer(lyr)
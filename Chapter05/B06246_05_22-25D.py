# Using the 2.5D Renderer

# https://github.com/GeospatialPython/Learn/raw/master/buildings.zip

lyr = QgsVectorLayer("/qgis_data/hancock/buildings.shp", "Buildings", "ogr")
r = Qgs25DRenderer()
lyr.setRendererV2(r)
exp = QgsExpressionContextUtils()
exp.setLayerVariable(lyr, "qgis_25d_angle", 90)
exp.setLayerVariable(lyr, "qgis_25d_height", "HEIGHT")
QgsMapLayerRegistry.instance().addMapLayer(lyr)

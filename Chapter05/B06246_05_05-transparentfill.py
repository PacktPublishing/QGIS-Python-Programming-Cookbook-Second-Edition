# Setting a transparent layer fill

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

lyr = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")
QgsMapLayerRegistry.instance().addMapLayer(lyr)
properties = {}
properties["color"] = '#289e26'
properties["color_border"] = '#289e26'
properties["width_border"] = '2'
properties["style"] = 'no'
sym = QgsFillSymbolV2.createSimple(properties)
renderer = lyr.rendererV2()
renderer.setSymbol(sym)
lyr.triggerRepaint()

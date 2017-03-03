# Using a filled marker symbol

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

lyr = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")
QgsMapLayerRegistry.instance().addMapLayer(lyr)

marker_props = {}
marker_props["color"] = 'red'
marker_props["color_border"] = 'black'
marker_props["name"] = 'star'
marker_props["size"] = '3'

marker = QgsMarkerSymbolV2.createSimple(marker_props)

filled_marker = QgsPointPatternFillSymbolLayer()

filled_marker.setDistanceX(4.0)
filled_marker.setDistanceY(4.0)
filled_marker.setSubSymbol(marker)

renderer = lyr.rendererV2()
renderer.symbols()[0].changeSymbolLayer(0, filled_marker)

lyr.triggerRepaint()


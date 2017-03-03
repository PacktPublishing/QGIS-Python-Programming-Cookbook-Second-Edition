# Creating inverted polygon shapeburst fills

# https://github.com/GeospatialPython/Learn/raw/master/hancock_land_water.zip

from PyQt4.QtGui import *

land = QgsVectorLayer("/qgis_data/hancock/hancock_land.shp", "Land", "ogr")
water = QgsVectorLayer("/qgis_data/hancock/hancock_water.shp", "Water", "ogr")

land_sym = land.rendererV2().symbols()[0]
water_sym = water.rendererV2().symbols()[0]

fill = QgsSimpleFillSymbolLayerV2()
fill.setFillColor(QColor.fromRgb(201,204,149))
fill.setOutlineColor(QColor.fromRgb(175,179,138))

land_sym.changeSymbolLayer(0, fill)
	
color1 = QColor.fromRgb(95,243,248)
color2 = QColor.fromRgb(51,44,247)

shapeburst = QgsShapeburstFillSymbolLayerV2(color=color1, color2=color2)

water_sym.changeSymbolLayer(0, shapeburst)

QgsMapLayerRegistry.instance().addMapLayers([land, water])



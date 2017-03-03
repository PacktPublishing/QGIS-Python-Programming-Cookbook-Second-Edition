# Creating a Categorized Vector Layer Symbol

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

from PyQt4.QtGui import *

lyr = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")

sym = lyr.rendererV2().symbols()[0]

fill = QgsSimpleFillSymbolLayerV2()
fill.setFillColor(QColor.fromRgb(221,239,196))
fill.setOutlineColor(QColor.fromRgb(63,122,17))
	
inner_glow = QgsInnerGlowEffect()
inner_glow.setColor(QColor.fromRgb(46,129,4))
inner_glow.setSpread(5.0)
inner_glow_lyr = QgsSimpleFillSymbolLayerV2()
inner_glow_lyr.setPaintEffect(inner_glow)

drop_shadow = QgsDropShadowEffect()
drop_shadow_lyr = QgsSimpleFillSymbolLayerV2()
drop_shadow_lyr.setPaintEffect(drop_shadow)

sym.appendSymbolLayer(drop_shadow_lyr)
sym.appendSymbolLayer(fill)
sym.appendSymbolLayer(inner_glow_lyr)

QgsMapLayerRegistry.instance().addMapLayer(lyr)



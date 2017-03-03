# Rendering a Single Band Raster Using a Color-Ramp Algorithm

# https://github.com/GeospatialPython/Learn/raw/master/dem.zip

from PyQt4.QtGui import QColor

lyr = QgsRasterLayer("/qgis_data/rasters/dem.asc", "DEM")

s = QgsRasterShader()
c = QgsColorRampShader()
c.setColorRampType(QgsColorRampShader.INTERPOLATED)

i = []
i.append(c.ColorRampItem(400, QColor('#d7191c'), '400 meters'))
i.append(c.ColorRampItem(900, QColor('#fdae61'), '900 meters'))
i.append(c.ColorRampItem(1500, QColor('#ffffbf'), '1500 meters'))
i.append(c.ColorRampItem(2000, QColor('#abdda4'), '2000 meters'))
i.append(c.ColorRampItem(2500, QColor('#2b83ba'), '2500 meters'))

c.setColorRampItemList(i)

s.setRasterShaderFunction(c)

ps = QgsSingleBandPseudoColorRenderer(lyr.dataProvider(), 1,  s)

lyr.setRenderer(ps)

QgsMapLayerRegistry.instance().addMapLayer(lyr)
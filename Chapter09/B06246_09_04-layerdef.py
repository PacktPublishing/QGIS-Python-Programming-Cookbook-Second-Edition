# Creating a Layer Definition File

from PyQt4.QtCore import *
from PyQt4.QtGui import *

hs = QgsRasterLayer("/qgis_data/saveqml/hillshade.tif", "Hillshade")
dem = QgsRasterLayer("/qgis_data/saveqml/dem.asc", "DEM")

algorithm = QgsContrastEnhancement.StretchToMinimumMaximum
limits = QgsRaster.ContrastEnhancementMinMax

dem.setContrastEnhancement(algorithm, limits)

s = QgsRasterShader() 
c = QgsColorRampShader() 
c.setColorRampType(QgsColorRampShader.INTERPOLATED) 
i = [] 
qri = QgsColorRampShader.ColorRampItem
i.append(qri(356.334, QColor(63,159,152,255), '356.334')) 
i.append(qri(649.292, QColor(96,235,155,255), '649.292')) 
i.append(qri(942.25, QColor(100,246,174,255), '942.25')) 
i.append(qri(1235.21, QColor(248,251,155,255), '1235.21'))
i.append(qri(1528.17, QColor(246,190,39,255), '1528.17')) 
i.append(qri(1821.13, QColor(242,155,39,255), '1821.13'))
i.append(qri(2114.08, QColor(165,84,26,255), '2114.08'))
i.append(qri(2300, QColor(236,119,83,255), '2300'))
i.append(qri(2700, QColor(203,203,203,255), '2700'))
c.setColorRampItemList(i) 
s.setRasterShaderFunction(c) 
ps = QgsSingleBandPseudoColorRenderer(dem.dataProvider(), 1,  s)
ps.setOpacity(0.5) 
dem.setRenderer(ps) 

QgsMapLayerRegistry.instance().addMapLayers([dem, hs])

dem.saveNamedStyle("/qgis_data/saveqml/dem.qml")

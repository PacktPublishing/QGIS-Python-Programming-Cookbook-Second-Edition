# Creating an NDVI

# https://github.com/GeospatialPython/Learn/raw/master/farm-field.tif

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.analysis import *

rasterName = "farm"

raster = QgsRasterLayer("/qgis_data/rasters/farm-field.tif", rasterName)

ir = QgsRasterCalculatorEntry()
r = QgsRasterCalculatorEntry()

ir.raster = raster
r.raster = raster

ir.bandNumber = 2
r.bandNumber = 1

ir.ref = rasterName + "@2"
r.ref = rasterName + "@1"

references = (ir.ref, r.ref, ir.ref, r.ref)

exp = "1.0 * (%s - %s) / 1.0 + (%s + %s)" % references 

output = "/qgis_data/rasters/ndvi.tif"

e = raster.extent()
w = raster.width()
h = raster.height()

entries = [ir,r]

ndvi =  QgsRasterCalculator(exp, output, "GTiff", e, w, h, entries)

ndvi.processCalculation()


lyr = QgsRasterLayer(output, "NDVI")

algorithm = QgsContrastEnhancement.StretchToMinimumMaximum
limits = QgsRaster.ContrastEnhancementMinMax
  
lyr.setContrastEnhancement(algorithm, limits)

s = QgsRasterShader() 
c = QgsColorRampShader() 
c.setColorRampType(QgsColorRampShader.INTERPOLATED) 
i = [] 
qri = QgsColorRampShader.ColorRampItem
i.append(qri(0, QColor(0,0,0,0), 'NODATA')) 
i.append(qri(214, QColor(120,69,25,255), 'Lowest Biomass')) 
i.append(qri(236, QColor(255,178,74,255), 'Lower Biomass')) 
i.append(qri(258, QColor(255,237,166,255), 'Low Biomass'))
i.append(qri(280, QColor(173,232,94,255), 'Moderate Biomass')) 
i.append(qri(303, QColor(135,181,64,255), 'High Biomass'))
i.append(qri(325, QColor(3,156,0,255), 'Higher Biomass'))  
i.append(qri(400, QColor(1,100,0,255), 'Highest Biomass'))    
c.setColorRampItemList(i) 
s.setRasterShaderFunction(c) 
ps = QgsSingleBandPseudoColorRenderer(lyr.dataProvider(), 1,  s) 
lyr.setRenderer(ps) 

QgsMapLayerRegistry.instance().addMapLayer(lyr)


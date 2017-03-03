# Image Change Detection

# https://github.com/GeospatialPython/Learn/raw/master/change-detection.zip

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.analysis import *
from PyQt4.QtGui import *

before = "/qgis_data/rasters/change-detection/before.tif"
after = "/qgis_data/rasters/change-detection/after.tif"

beforeName = "Before"
afterName = "After"

beforeRaster = QgsRasterLayer(before, beforeName)
afterRaster = QgsRasterLayer(after, afterName)

beforeEntry = QgsRasterCalculatorEntry()
afterEntry = QgsRasterCalculatorEntry()

beforeEntry.raster = beforeRaster
afterEntry.raster = afterRaster

beforeEntry.bandNumber = 1
afterEntry.bandNumber = 2

beforeEntry.ref = beforeName + "@1"
afterEntry.ref = afterName + "@2"

entries = [afterEntry, beforeEntry]

exp = "%s - %s" % (afterEntry.ref, beforeEntry.ref) 

output = "/qgis_data/rasters/change-detection/change.tif"

e = beforeRaster.extent()
w = beforeRaster.width()
h = beforeRaster.height()

change = QgsRasterCalculator(exp, output, "GTiff", e, w, h, entries)

change.processCalculation()

lyr = QgsRasterLayer(output, "Change")

algorithm = QgsContrastEnhancement.StretchToMinimumMaximum
limits = QgsRaster.ContrastEnhancementMinMax

lyr.setContrastEnhancement(algorithm, limits)

s = QgsRasterShader()
c = QgsColorRampShader()
c.setColorRampType(QgsColorRampShader.INTERPOLATED) 
i = []
qri = QgsColorRampShader.ColorRampItem
i.append(qri(0, QColor(0,0,0,0), 'NODATA')) 
i.append(qri(-101, QColor(123,50,148,255), 'Significant Itensity Decrease')) 
i.append(qri(-42.2395, QColor(194,165,207,255), 'Minor Itensity Decrease')) 
i.append(qri(16.649, QColor(247,247,247,0), 'No Change'))
i.append(qri(75.5375, QColor(166,219,160,255), 'Minor Itensity Increase')) 
i.append(qri(135, QColor(0,136,55,255), 'Significant Itensity Increase'))
c.setColorRampItemList(i)
s.setRasterShaderFunction(c)
ps = QgsSingleBandPseudoColorRenderer(lyr.dataProvider(), 1, s) 
lyr.setRenderer(ps)

QgsMapLayerRegistry.instance().addMapLayer(lyr)




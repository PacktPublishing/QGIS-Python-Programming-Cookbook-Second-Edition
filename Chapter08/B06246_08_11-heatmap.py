# Creating a Heat Map

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import processing

countries = "https://raw.githubusercontent.com/johan/world.geo.json/"
countries += "master/countries.geo.json"

quakes = "https://github.com/GeospatialPython/Learn/"
quakes += "raw/master/quakes2014.geojson"

output = "/qgis_data/rasters/heat.tif"

basemap = QgsVectorLayer(countries, "World", "ogr")

quakeLyr = QgsVectorLayer(quakes, "2014 Earthquakes", "ogr")

QgsMapLayerRegistry.instance().addMapLayers([quakeLyr, basemap])

ext = quakeLyr.extent()
xmin = ext.xMinimum()
ymin = ext.yMinimum()
xmax = ext.xMaximum()
ymax = ext.yMaximum()
box = "%s,%s,%s,%s".format(xmin,xmax,ymin,ymax)

processing.runalg("saga:kerneldensityestimation",quakeLyr,"mag",10,1,box,1,0,output)

heat = QgsRasterLayer(output, "Earthquake Heatmap")

algorithm = QgsContrastEnhancement.StretchToMinimumMaximum
limits = QgsRaster.ContrastEnhancementMinMax
  
heat.setContrastEnhancement(algorithm, limits)

s = QgsRasterShader() 
c = QgsColorRampShader() 
c.setColorRampType(QgsColorRampShader.INTERPOLATED) 
i = [] 
qri = QgsColorRampShader.ColorRampItem
i.append(qri(0, QColor(255,255,178,255), 'Lowest Earthquake Impact')) 
i.append(qri(13, QColor(254,204,92,255), 'Lower Earthquake Impact')) 
i.append(qri(26, QColor(253,141,60,255), 'Moderate Earthquake Impact')) 
i.append(qri(38, QColor(240,59,32,255), 'Higher Earthquake Impact'))
i.append(qri(50, QColor(189,0,38,255), 'Highest Earthquake Impact')) 
c.setColorRampItemList(i) 
s.setRasterShaderFunction(c) 
ps = QgsSingleBandPseudoColorRenderer(heat.dataProvider(), 1,  s) 
heat.setRenderer(ps) 

QgsMapLayerRegistry.instance().addMapLayers([heat])


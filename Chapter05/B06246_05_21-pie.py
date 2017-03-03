# Using Pie Charts for Symbols

# https://github.com/GeospatialPython/Learn/raw/master/County10PopnHou.zip

from PyQt4.QtGui import *
from PyQt4.QtCore import *

# Layer
lyr = QgsVectorLayer("/qgis_data/ms/County10PopnHou.shp", "Population", "ogr")

# Attributes to feature in pie chart symbols
categories = [u'PCT_WHT', u'PCT_BLK', u'PCT_AMIND', u'PCT_ASIAN', u'PCT_HAW', u'PCT_ORA', u'PCT_MR', u'PCT_HISP']

# Colors - 1 for each attribute
colors = ['#3727fa','#01daae','#f849a6','#268605','#6810ff','#453990','#630f2f','#07dd45']

# Convert the colors to Qt QColor objects
qcolors = map(QColor, colors)

# set up our Pie Chart diagram symbol
diagram = QgsPieDiagram()

# Diagram settings
ds = QgsDiagramSettings() 
ds.font = QFont("Helvetica", 12)
ds.transparency = 0
ds.categoryColors = qcolors
ds.categoryAttributes = categories
ds.categoryLabels = categories
ds.size = QSizeF(100.0, 100.0)
ds.sizeType = 0 
ds.labelPlacementMethod = 1 
ds.scaleByArea = True 
ds.minimumSize = 0 
ds.BackgroundColor = QColor(255,255,255,0) 
ds.PenColor = QColor("black") 
ds.penWidth = 0

# Diagram Renderer
dr = QgsLinearlyInterpolatedDiagramRenderer()
dr.setLowerValue(0.0)
dr.setLowerSize(QSizeF(0.0, 0.0))
dr.setUpperValue(2000000)
dr.setUpperSize(QSizeF(40,40))
dr.setClassificationAttribute(6)
dr.setDiagram(diagram)
dr.setDiagramSettings(ds)
lyr.setDiagramRenderer(dr)

# Set layer-wide diagram settings
dls = QgsDiagramLayerSettings()
dls.dist = 0
dls.priority = 0
dls.xPosColumn = -1
dls.yPosColumn = -1
dls.placement = 0 
lyr.setDiagramLayerSettings(dls)

# Label settings - required regardless of use
label = QgsPalLayerSettings() 
label.readFromLayer(lyr) 
label.enabled = True 
label.writeToLayer(lyr)

# Delete any cached images and repaint
if hasattr(lyr, "setCacheImage"): 
    lyr.setCacheImage(None)

lyr.triggerRepaint()

# Display the layer and symbols
QgsMapLayerRegistry.instance().addMapLayer(lyr)
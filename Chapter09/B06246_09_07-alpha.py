# Using Alpha Values to Show Data Density

# Requires MMQGIS Plugin

# https://github.com/GeospatialPython/Learn/raw/master/bear-data.zip

import processing
from PyQt4.QtGui import *
from mmqgis import mmqgis_library as mmqgis

dir = "/qgis_data/ms/"
source = dir + "bear-data.shp"
grid = dir + "grid.shp"
clipped_grid = dir + "clipped_grid.shp"
output = dir + "ms-bear-sightings.shp"

layer = QgsVectorLayer(source, "bear data", "ogr")

e = layer.extent()
minx = e.xMinimum()
miny = e.yMinimum()
maxx = e.xMaximum()
maxy = e.yMaximum()
w = e.width()
h = e.height()

crs = layer.crs()

mmqgis.mmqgis_grid(iface, "Hexagons", crs, .1, .1, minx, miny, maxx, maxy, "Hexagon (polygon)", grid, False)

processing.runalg("qgis:clip",grid,source,clipped_grid)

processing.runalg("qgis:joinattributesbylocation",clipped_grid,source,['intersects'],0,0,"sum,mean,min,max,median",0,output)


bears = QgsVectorLayer(output, "Bear Sightings", "ogr")

# Label, expression, color, symbol alpha
rules = (
    ('RARE', '"BEARS" <= 5', (227,26,28,255), .2),
    ('UNCOMMON', '"BEARS" > 5 AND "BEARS" <= 15', (227,26,28,255), .4),
    ('OCCASIONAL', '"BEARS" > 15 AND "BEARS" <= 50', (227,26,28,255), .6),
    ('FREQUENT', '"BEARS" > 50', (227,26,28,255), 1),
)

# create a new rule-based renderer
sym_bears = QgsFillSymbolV2.createSimple({"outline_color":"white","outline_width":".26"}) 
rend_bears = QgsRuleBasedRendererV2(sym_bears)

# get the "root" rule
root_rule = rend_bears.rootRule()

for label, exp, color, alpha in rules:
    # create a clone (i.e. a copy) of the default rule
    rule = root_rule.children()[0].clone()
    # set the label, exp and color
    rule.setLabel(label)
    rule.setFilterExpression(exp)
    r,g,b,a = color
    rule.symbol().setColor(QColor(r,g,b,a))
    # set the transparency level
    rule.symbol().setAlpha(alpha)
    # append the rule to the list of rules
    root_rule.appendChild(rule)

# delete the default rule
root_rule.removeChildAt(0)

# apply the rend_rails to the rails
bears.setRendererV2(rend_bears)

QgsMapLayerRegistry.instance().addMapLayer(bears)



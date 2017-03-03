# Rendering Map Layers Based on Rules

# https://github.com/GeospatialPython/Learn/raw/master/ms_rails_mstm.zip

from PyQt4.QtGui import *

prefix = "/qgis_data/ms/"

rails = QgsVectorLayer(prefix + "ms_rails_mstm.shp", "Railways", "ogr")

# define some rules: label, exp, color name, (min scale, max scale)
rules = (
    ('Heavily Used', '"DEN09CODE" > 3', 'red', (0, 6000000)),
    ('Moderately Used', '"DEN09CODE" < 4 AND "DEN09CODE" > 1', 'orange', (0, 1500000)),
    ('Lightly Used', '"DEN09CODE" < 2', 'grey', (0, 250000)),
)

# create a new rule-based renderer
sym_rails = QgsSymbolV2.defaultSymbol(rails.geometryType())
rend_rails = QgsRuleBasedRendererV2(sym_rails)

# get the "root" rule
root_rule = rend_rails.rootRule()

for label, exp, color, scale in rules:
    # create a clone (i.e. a copy) of the default rule
    rule = root_rule.children()[0].clone()
    # set the label, exp and color
    rule.setLabel(label)
    rule.setFilterExpression(exp)
    rule.symbol().setColor(QColor(color))
    # set the scale limits if they have been specified
    if scale is not None:
        rule.setScaleMinDenom(scale[0])
        rule.setScaleMaxDenom(scale[1])
    # append the rule to the list of rules
    root_rule.appendChild(rule)

# delete the default rule
root_rule.removeChildAt(0)

# apply the rend_rails to the rails
rails.setRendererV2(rend_rails)

jax = QgsVectorLayer(prefix + "jackson.shp", "Jackson", "ogr")
jax_style = {}
jax_style['color'] = "#ffff00"
jax_style['name'] = 'regular_star'
jax_style['outline'] = '#000000'
jax_style['outline-width'] = '1'
jax_style['size'] = '8'
sym_jax = QgsSimpleMarkerSymbolLayerV2.create(jax_style)
jax.rendererV2().symbols()[0].changeSymbolLayer(0, sym_jax)

ms = QgsVectorLayer(prefix + "mississippi.shp", "Mississippi", "ogr")
ms_style = {}
ms_style['color'] = "#F7F5EB"
sym_ms = QgsSimpleFillSymbolLayerV2.create(ms_style)
ms.rendererV2().symbols()[0].changeSymbolLayer(0, sym_ms)

QgsMapLayerRegistry.instance().addMapLayers([jax, rails, ms])
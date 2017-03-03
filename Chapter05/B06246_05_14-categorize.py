# Creating a Categorized Vector Layer Symbol

# https://github.com/GeospatialPython/Learn/raw/master/landuse_shp.zip

from PyQt4.QtGui import QColor

lyr = QgsVectorLayer("/qgis_data/hancock/landuse.shp", "Land Use", "ogr")
	
landuse = {
	        "0":("yellow", "Developed"),
	        "1":("darkcyan", "Water"),
	        "2":("green", "Land")}

categories = []
for terrain, (color, label) in landuse.items():
	sym = QgsSymbolV2.defaultSymbol(lyr.geometryType())
	sym.setColor(QColor(color))
	category = QgsRendererCategoryV2(terrain, sym, label)
	categories.append(category)
	
field = "DN"
renderer = QgsCategorizedSymbolRendererV2(field, categories)
lyr.setRendererV2(renderer)
QgsMapLayerRegistry.instance().addMapLayer(lyr)



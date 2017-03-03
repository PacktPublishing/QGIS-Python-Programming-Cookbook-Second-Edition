# Creating a Graduated Vector Layer Symbol

# https://github.com/GeospatialPython/Learn/raw/master/MS_UrbanAnC10.zip

from PyQt4.QtGui import QColor

lyr = QgsVectorLayer("/qgis_data/ms/MS_UrbanAnC10.shp", "Urban Areas", "ogr")

population = (
("Village", 0.0, 3159.0, "cyan"), 
("Small town", 3160.0, 4388.0, "blue"),
("Town", 43889.0, 6105.0, "green"),
("City", 6106.0, 10481.0, "yellow"),
("Large City", 10482.0, 27165, "orange"),
("Metropolis", 27165.0, 1060061.0, "red"))

ranges = []
for label, lower, upper, color in population:
    sym = QgsSymbolV2.defaultSymbol(lyr.geometryType())
    sym.setColor(QColor(color))
    rng = QgsRendererRangeV2(lower, upper, sym, label)
    ranges.append(rng)

field = "POP"
renderer = QgsGraduatedSymbolRendererV2(field, ranges)
lyr.setRendererV2(renderer)
QgsMapLayerRegistry.instance().addMapLayer(lyr)

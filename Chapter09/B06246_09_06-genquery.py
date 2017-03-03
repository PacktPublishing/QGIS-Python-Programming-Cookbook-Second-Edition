# Using Generators for Layer Queries

# easy_install https://github.com/GeospatialPython/qquery/archive/master.zip

from query import query

pth = "/qgis_data/ms/MS_UrbanAnC10.shp"
layer = QgsVectorLayer(pth, "Urban Areas", "ogr")

q = (query(layer).where("POP > 50000").select('NAME10', "POP", "AREALAND", "POPDEN"))

q().next()


# Calculating the Area of a Polygon

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

lyr = QgsVectorLayer("/Users/joellawhead/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")
fts = lyr.getFeatures()
boundary = fts.next()
d = QgsDistanceArea()
m = d.measurePolygon(boundary.geometry().asPolygon()[0])
d.convertMeasurement(m, 2, 7, True)
# (42955.47889640281, 7)
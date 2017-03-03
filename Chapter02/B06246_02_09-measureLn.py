# Measuring Distance Along a Line

# https://github.com/GeospatialPython/Learn/raw/master/paths.zip

lyr = QgsVectorLayer("/Users/joellawhead/qgis_data/shapes/paths.shp", "Route", "ogr")
fts = lyr.getFeatures()
route = fts.next()
d = QgsDistanceArea()
d.setEllipsoidalMode(True)
m = d.measureLine(route.geometry().asPolyline())
d.convertMeasurement(m, 0, 7, False)

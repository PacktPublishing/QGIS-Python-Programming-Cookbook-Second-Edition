# Adding a Polygon Feature to a Vector Layer

# https://github.com/GeospatialPython/Learn/raw/master/polygon.zip

vectorLyr =  QgsVectorLayer('/qgis_data/polygon/polygon.shp', 'Polygon' , "ogr")
vectorLyr.isValid()
vpr = vectorLyr.dataProvider()

points = []
points.append(QgsPoint(-123.26072,49.06822))
points.append(QgsPoint(-127.19157,43.07367))
points.append(QgsPoint(-120.70567,35.21197))
points.append(QgsPoint(-115.89037,40.02726))
points.append(QgsPoint(-113.04051,48.47859))
points.append(QgsPoint(-123.26072,49.06822))

poly = QgsGeometry.fromPolygon([points])

f = QgsFeature()
f.setGeometry(poly)
vpr.addFeatures([f])
vectorLyr.updateExtents()

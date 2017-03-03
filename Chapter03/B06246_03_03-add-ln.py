# Adding a Line Feature to a Vector Layer

# https://github.com/GeospatialPython/Learn/raw/master/paths.zip

vectorLyr =  QgsVectorLayer('/qgis_data/paths/paths.shp', 'Paths' , "ogr")
vectorLyr.isValid()
vpr = vectorLyr.dataProvider()

points = []
points.append(QgsPoint(430841.61703,5589485.34838))
points.append(QgsPoint(432438.36523,5575114.61462))
points.append(QgsPoint(447252.64015,5567663.12304))

line = QgsGeometry.fromPolyline(points)

f = QgsFeature()
f.setGeometry(line)
vpr.addFeatures([f])
vectorLyr.updateExtents()


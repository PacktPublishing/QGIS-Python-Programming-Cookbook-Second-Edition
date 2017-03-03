# Adding a Point Feature to a Vector Layer

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

vectorLyr =  QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")

vpr = vectorLyr.dataProvider()

pnt = QgsGeometry.fromPoint(QgsPoint(-74.80,40.549))

f = QgsFeature()
f.setGeometry(pnt)
vpr.addFeatures([f])
vectorLyr.updateExtents()


# Adding a set of Attributes to a Vectory Layer

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

vectorLyr =  QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vectorLyr.isValid()
vpr = vectorLyr.dataProvider()

pnt = QgsGeometry.fromPoint(QgsPoint(-74.13401,40.62148))

fields = vpr.fields()

f = QgsFeature(fields)
f.setGeometry(pnt)

f.setAttribute(0,"Python Museum")

vpr.addFeatures([f])
vectorLyr.updateExtents()


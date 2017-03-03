# Creating a Dot Density Map

# https://github.com/GeospatialPython/Learn/raw/master/GIS_CensusTract.zip

import random

src = "/qgis_data/census/GIS_CensusTract_poly.shp"

tractLyr = QgsVectorLayer(src, "Census Tracts", "ogr")

popLyr =  QgsVectorLayer('Point?crs=epsg:4326', "Population" , "memory")

i = tractLyr.fieldNameIndex('POPULAT11')

features = tractLyr.getFeatures()

vpr = popLyr.dataProvider()

dotFeatures = []

for feature in features:
	pop = feature.attributes()[i]
	density = pop / 100
	found = 0
	dots = []
	g = feature.geometry()
	minx =  g.boundingBox().xMinimum()
	miny =  g.boundingBox().yMinimum()
	maxx =  g.boundingBox().xMaximum()
	maxy =  g.boundingBox().yMaximum()
	while found < density:
		x = random.uniform(minx,maxx)
		y = random.uniform(miny,maxy)
		pnt = QgsPoint(x,y)
		if g.contains(pnt):
			dots.append(pnt)
			found += 1
	geom = QgsGeometry.fromMultiPoint(dots)
	f = QgsFeature()
	f.setGeometry(geom)
	dotFeatures.append(f)

vpr.addFeatures(dotFeatures)
popLyr.updateExtents()

QgsMapLayerRegistry.instance().addMapLayers([popLyr,tractLyr]) 
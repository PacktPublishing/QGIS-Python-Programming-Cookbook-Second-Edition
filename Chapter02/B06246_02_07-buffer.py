# Buffering a Feature

# https://geospatialpython.googlecode.com/svn/NYC_MUSEUMS_GEO.zip

lyr = QgsVectorLayer("/Users/joellawhead/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([lyr])
fts = lyr.getFeatures()
ft = fts.next()
lyr.setSelectedFeatures([ft.id()])
buff = ft.geometry().buffer(.2,8)
buffLyr =  QgsVectorLayer('Polygon?crs=epsg:4326', 'Buffer' , "memory")
pr = buffLyr.dataProvider()
b = QgsFeature()
b.setGeometry(buff)
pr.addFeatures([b])
buffLyr.updateExtents()
buffLyr.setLayerTransparency(70)
QgsMapLayerRegistry.instance().addMapLayers([buffLyr])

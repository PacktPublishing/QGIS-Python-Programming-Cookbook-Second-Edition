# Filtering a Layer by Attributes

# https://geospatialpython.googlecode.com/svn/NYC_MUSEUMS_GEO.zip

lyrPts = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([lyrPts])
selection = lyrPts.getFeatures(QgsFeatureRequest().setFilterExpression(u'"ZIP" = 10002'))
lyrPts.setSelectedFeatures([s.id() for s in selection])
iface.mapCanvas().zoomToSelected()

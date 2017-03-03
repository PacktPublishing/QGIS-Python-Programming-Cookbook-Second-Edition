# Filtering a Layer by Geometry

# https://geospatialpython.googlecode.com/files/MSCities_Geo_Pts.zip

lyrPts = QgsVectorLayer("/qgis_data/ms/MSCities_Geo_Pts.shp", "MSCities_Geo_Pts", "ogr")
lyrPoly = QgsVectorLayer("/qgis_data/ms/GIS_CensusTract_poly.shp", "GIS_CensusTract_poly", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([lyrPoly,lyrPts])
ftsPoly = lyrPoly.getFeatures()
for feat in ftsPoly:
    geomPoly = feat.geometry()
    bbox = geomPoly.boundingBox()
    req = gsFeatureRequest()
    filterRect = req.setFilterRect(bbox)
    featsPnt = lyrPts.getFeatures(filterRect)
    for featPnt in featsPnt:
        if featPnt.geometry().within(geomPoly):
            print featPnt.id()
            lyrPts.select(featPnt.id())

iface.setActiveLayer(lyrPoly)
iface.zoomToActiveLayer() 
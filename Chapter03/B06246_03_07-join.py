# Join a Shapefile Attribute Table to a CSV File

# https://github.com/GeospatialPython/Learn/raw/master/census.zip
# See also: https://github.com/rldhont/Quantum-GIS/blob/master/python/plugins/processing/algs/qgis/JoinAttributes.py

vectorLyr = QgsVectorLayer("/qgis_data/census/hancock_tracts.shp", "Hancock", "ogr")
vectorLyr.isValid()
infoLyr = QgsVectorLayer("/qgis_data/census/ACS_12_5YR_S1901_with_ann.csv", "Census", "ogr")
infoLyr.isValid()
QgsMapLayerRegistry.instance().addMapLayers([vectorLyr,infoLyr], False)
info = QgsVectorJoinInfo()
info.joinLayerId = infoLyr.id()
info.joinFieldName = "GEOid2"
info.targetFieldName = "GEOID"
info.memoryCache = True
vectorLyr.addJoin(info)
QgsVectorFileWriter.writeAsVectorFormat(vectorLyr, "/qgis_data/census/joined.shp", "CP120", None, "ESRI Shapefile")
joinedLyr =  QgsVectorLayer("/qgis_data/census/joined.shp", "Joined", "ogr")
vectorLyr.dataProvider().fields().count()
# 12
joinedLyr.dataProvider().fields().count()
# 142
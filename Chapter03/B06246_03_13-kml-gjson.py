# Converting a Shapefile to KML

# https://github.com/GeospatialPython/Learn/raw/master/hancock.zip

vectorLyr =  QgsVectorLayer('/qgis_data/hancock/hancock.shp', 'Hancock' , "ogr")
vectorLyr.isValid()
dest_crs = QgsCoordinateReferenceSystem(4326) 
QgsVectorFileWriter.writeAsVectorFormat(vectorLyr, "/qgis_data/hancock/hancock.kml", "utf-8", dest_crs, "KML")

# Or we can write out GeoJSON
QgsVectorFileWriter.writeAsVectorFormat(vectorLyr, "/qgis_data/hancock/hancock.geojson", "utf-8", dest_crs, "GeoJSON")
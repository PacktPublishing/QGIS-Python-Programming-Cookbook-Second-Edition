# Deleting a Vector Layer Field

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

vectorLyr =  QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vectorLyr.isValid()
vectorLyr.dataProvider().deleteAttributes([1]) 
vectorLyr.updateFields()
# Changing a Vector Layer Attribute

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

vectorLyr =  QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vectorLyr.isValid()
feat_id = 22
attr = {1:"(555) 555-5555"}
vectorLyr.dataProvider().changeAttributeValues({feat_id : attr})

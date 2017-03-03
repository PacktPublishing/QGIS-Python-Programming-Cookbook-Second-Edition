# Moving Vector Layer Geometry

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

vectorLyr =  QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vectorLyr.isValid()
feat_id = 22
geom = QgsGeometry.fromPoint(QgsPoint(-74.20378,40.89642))
vectorLyr.dataProvider().changeGeometryValues({feat_id : geom})
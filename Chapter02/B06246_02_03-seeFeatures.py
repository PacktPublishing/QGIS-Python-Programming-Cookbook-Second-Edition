# Examining Vector Layer Features

# https://geospatialpython.googlecode.com/svn/NYC_MUSEUMS_GEO.zip

layer = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
features = layer.getFeatures()
f = features.next()
g = f.geometry()
g.asPoint()
# Output:
# (-74.0138,40.7038)
 

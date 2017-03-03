# Examining Vector Layer Attributes

# https://geospatialpython.googlecode.com/svn/NYC_MUSEUMS_GEO.zip

layer = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
features = layer.getFeatures()
f = features.next()
f.attributes()
# [u'Alexander Hamilton U.S. Custom House', u'(212) 514-3700', u'http://www.oldnycustomhouse.gov/', u'1 Bowling Grn', NULL, u'New York', 10004.0, -74.013756, 40.703817]
# To see field names:
# [c.name() for c in f.fields().toList()]
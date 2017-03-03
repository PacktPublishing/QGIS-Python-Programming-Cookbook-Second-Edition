# Accessing layer metadata

lyr = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([lyr])
m = layer.metadata()
lyr_cap = m.split(“Capabilities of this layer</p>\n<p>”)[1].split(“<”)[0].split(“,”)
lyr_cap = [x.strip() for x in lyr_cap]
# [u'Add Features', u'Delete Features', u'Change Attribute Values',
# u'Add Attributes', u'Delete Attributes', u'Rename Attributes',
# u'Create Spatial Index', u'Create Attribute Indexes',
# u'Fast Access to Features at ID', u'Change Geometries']


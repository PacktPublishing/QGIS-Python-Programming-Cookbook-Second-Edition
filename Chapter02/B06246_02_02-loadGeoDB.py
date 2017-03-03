# Loading a Vector Layer from a GeoDatabase

uri = QgsDataSourceURI()
uri.setConnection("spacialdb.com", "9999", "lzmjzm_hwpqlf", "lzmjzm_hwpqlf", "0e9fcc39")
uri.setDataSource("public", "islands", "wkb_geometry", "")
layer = QgsVectorLayer(uri.uri(), "Islands", "postgres")
if not layer.isValid():
  print "Layer %s did not load" % layer.name()
QgsMapLayerRegistry.instance().addMapLayers([layer])  

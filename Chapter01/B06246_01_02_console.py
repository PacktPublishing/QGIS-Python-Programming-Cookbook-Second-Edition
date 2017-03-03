# Run from the QGIS Python console

layer =  QgsVectorLayer('Point?crs=epsg:4326', 'MyPoint' , "memory")
pr = layer.dataProvider()
pt = QgsFeature()
point1 = QgsPoint(20,20)
pt.setGeometry(QgsGeometry.fromPoint(point1))
pr.addFeatures([pt])
layer.updateExtents()
QgsMapLayerRegistry.instance().addMapLayers([layer])

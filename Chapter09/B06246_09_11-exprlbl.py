# Using Expression-Based Labels

# https://github.com/GeospatialPython/Learn/raw/master/MS_UrbanAnC10.zip

pth = "/qgis_data/ms/MS_UrbanAnC10.shp"

lyr = QgsVectorLayer(pth, "Urban Areas", "ogr")

palyr = QgsPalLayerSettings()

palyr.readFromLayer(lyr)

palyr.fieldName = 'CASE WHEN "POP" > 50000 THEN NAME10 END'

palyr.isExpression = True

palyr.enabled = True 

palyr.writeToLayer(lyr)

QgsMapLayerRegistry.instance().addMapLayer(lyr)

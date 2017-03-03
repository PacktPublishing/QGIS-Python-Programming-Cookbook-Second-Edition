# Label Features

# https://github.com/GeospatialPython/Learn/raw/master/MSCities_Geo_Pts.zip

src = "/qgis_data/ms/MSCities_Geo_Pts.shp"

lyr = QgsVectorLayer(src, "Cities", "ogr")

label = QgsPalLayerSettings() 
label.readFromLayer(lyr) 

label.enabled = True 
label.fieldName = 'NAME10' 
label.placement= QgsPalLayerSettings.AroundPoint 
label.textFont.setPointSize(12)

label.writeToLayer(lyr) 

QgsMapLayerRegistry.instance().addMapLayers([lyr])
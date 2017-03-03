# Collecting Field Data

# Mobile field app: http://geospatialpython.github.io/qgis/fieldwork.html

wb = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
basemap = QgsVectorLayer(wb, "Countries", "ogr")
observations = QgsVectorLayer("http://bit.ly/QGISFieldApp", "Field Observations", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([observations, basemap])
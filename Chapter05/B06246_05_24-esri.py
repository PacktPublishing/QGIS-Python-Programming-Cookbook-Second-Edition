# Using X,Y,Z Tiled Map Services

arc_map_server = "http://server.arcgisonline.com/"
arc_map_server += "ArcGIS/rest/services/World_Imagery/MapServer?f=json"

arc_feature_server = "https://services5.arcgis.com/U8xJBTiAx2RGR2e2"
arc_feature_server += "/arcgis/rest/services/2011_Earthquakes/FeatureServer/0/"
arc_feature_server += "query?outFields=*&where=1%3D1&outSR=3857&f=json"

basemap = QgsRasterLayer(arc_map_server, "World Imagery")

earthquakes = QgsVectorLayer(arc_feature_server, "EarthQuakes", "ogr")

QgsMapLayerRegistry.instance().addMapLayers([earthquakes, basemap])
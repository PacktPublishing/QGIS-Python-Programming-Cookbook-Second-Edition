# Using OpenStreetMap Points of Interest in QGIS

# Requires QuickOSM QGIS plugin

# https://github.com/GeospatialPython/Learn/raw/master/MSCoast_geo.zip

import processing

lyr = QgsVectorLayer("/qgis_data/ms/MSCoast_geo.shp", "MS Coast", "ogr")
ext = lyr.extent()
w =  ext.xMinimum()
s =  ext.yMinimum()
e =  ext.xMaximum()
n =  ext.yMaximum()

bbox = "%s,%s,%s,%s".format(w,e,s,n)

factory = processing.runalg("quickosm:queryfactory","tourism","",True,"",25)

q = factory["OUTPUT_QUERY"]

results = processing.runalg("quickosm:queryoverpassapiwithastring","http://overpass-api.de/api/",q,bbox,"",None)

osm = results["OUTPUT_FILE"]

poly = "/qgis_data/ms/tourism_poly.shp"
multiline = "/qgis_data/ms/tourism_multil.shp"
line = "/qgis_data/ms/tourism_lines.shp"
points = "/qgis_data/ms/tourism_points.shp"

processing.runalg("quickosm:ogrdefault",osm,"","","","",poly,multiline,line,points)

tourism_points = QgsVectorLayer(points, "Points of Interest", "ogr")

QgsMapLayerRegistry.instance().addMapLayers([tourism_points, lyr])

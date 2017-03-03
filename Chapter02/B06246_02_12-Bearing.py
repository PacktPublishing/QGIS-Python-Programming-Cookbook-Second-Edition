# Calculating the Bearing of a line

# https://github.com/GeospatialPython/Learn/raw/master/paths.zip

import math
lyr = QgsVectorLayer("/qgis_data/shapes/paths.shp", "Route", "ogr")
fts = lyr.getFeatures()
route = fts.next()
d = QgsDistanceArea()
points = route.geometry().asPolyline()
first = points[0]
last = points[-1]
r = d.bearing(first, last)
b = math.degrees(r)
if b < 0:
    b += 360
print(b)
# 320.3356091875395


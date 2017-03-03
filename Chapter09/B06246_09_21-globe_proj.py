# Make a globe-like azimuthal orthographic projection

# https://github.com/GeospatialPython/Learn/raw/master/countries.zip

import processing

pth = "/qgis_data/countries.shp"

clipped = "/qgis_data/clipped_countries.shp"

warped = "/qgis_data/sphere.shp"

x = 22
y = 36

processing.runalg("cliptohemisphere:clipavectorlayertothehemispherecentredonauserspecifiedpoint",pth,y,x,500,clipped, progress=None)

processing.runandload("qgis:reprojectlayer",clipped,"EPSG:53032",warped)
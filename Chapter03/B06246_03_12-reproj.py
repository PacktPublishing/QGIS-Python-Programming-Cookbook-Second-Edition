# Reprojecting a Vector Layer

# https://github.com/GeospatialPython/Learn/raw/master/MSCities_MSTM.zip

import processing
processing.runalg("qgis:reprojectlayer", "/qgis_data/ms/MSCities_MSTM.shp", "epsg:4326", "/qgis_data/ms/MSCities_MSTM_4326.shp")
# Creating a Common Extent for Rasters

# https://github.com/GeospatialPython/Learn/raw/master/overlap.zip
# https://github.com/GeospatialPython/Learn/raw/master/unify_extents.zip

import processing

processing.runalg("script:unifyextentandresolution","/qgis_data/rasters/Image2.tif;/qgis_data/rasters/Image1.tif",-9999,"/qgis_data/rasters",True)
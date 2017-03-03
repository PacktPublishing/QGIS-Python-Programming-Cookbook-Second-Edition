# Classifying a Raster

# https://github.com/GeospatialPython/Learn/raw/master/FalseColor.zip

import processing
# OTB toolbox must be installed on Windows
processing.runandload("otb:unsupervisedkmeansimageclassification","/qgis_data/rasters/FalseColor.tif",128,None,100,3,1000,0.95,"/qgis_data/rasters/class.tif",None)


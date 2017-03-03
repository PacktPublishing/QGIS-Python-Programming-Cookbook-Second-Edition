# Merging Shapefiles

# https://github.com/GeospatialPython/Learn/raw/master/tiled_footprints.zip

# See also: processing.alghelp("qgis:mergevectorlayers")

import glob
import processing

pth = "/qgis_data/tiled_footprints/"
files = glob.glob(pth + "*.shp")
out = pth + "merged.shp"
processing.runandload("saga:mergelayers",";".join(files),"True", "True", out)


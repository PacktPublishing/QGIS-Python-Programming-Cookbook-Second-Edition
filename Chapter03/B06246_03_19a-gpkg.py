# Exporting a geopackage

# https://github.com/GeospatialPython/Learn/raw/master/rivers.zip

import os
from osgeo import ogr

# Path to the shapefiles
pth = "/qgis_data/rivers/"

# Create the base geopackage
gpkg = os.path.join(pth + "rivers.gpkg")
ds = ogr.GetDriverByName("GPKG").CreateDataSource(gpkg)

# Add the first shapefile
sf1 = ogr.Open(pth + "rivers.shp")
sf_lyr1 = sf1.GetLayerByIndex(0)
ds.CopyLayer(sf_lyr1, "rivers", [])

# Close the dataset
ds = None

# Reopen the dataset in update mode
ds = ogr.Open(gpkg, True)

# Add the second shapefile
sf2 = ogr.Open(pth + "junctions.shp")
sf_lyr2 = sf2.GetLayerByIndex(0)
ds.CopyLayer(sf_lyr2, "junctions", [])

# Close the dataset
ds = None




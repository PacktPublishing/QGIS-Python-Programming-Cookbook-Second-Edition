# Finding the Least Cost Path

# NOTE: Data must be projected

# https://github.com/GeospatialPython/Learn/raw/master/lcp.zip

import processing

path = "/qgis_data/rasters/lcp/"

# Digital Elevation Model
dem = path + "dem.asc"

# Starting point of our path
start = path + "start-point.shp"

# End of our path
finish = path + "end-point.shp"

# Get the DEM extent
demLyr = QgsRasterLayer(dem, "DEM")
ext = demLyr.extent()
xmin = ext.xMinimum()
ymin = ext.yMinimum()
xmax = ext.xMaximum()
ymax = ext.yMaximum()
box = "%s,%s,%s,%s".format(xmin,xmax,ymin,ymax)

a = QgsVectorLayer(start, "Start", "ogr")
b = QgsVectorLayer(finish, "End", "ogr")

# Cummulative cost raster to temp file
cost = path + "cost.tif"
tmpCost = processing.runalg("grass7:r.cost.points",dem,a,None,False,False,box,0,-1,0.0001,cost)


# Merge start and end point layers into one layer for SAGA least cost path algorithm
merge = path + "merge.shp"
tmpMerge = processing.runalg("qgis:mergevectorlayers","{};{}".format(start,finish),merge)

# Least cost path analysis
vLyr = QgsVectorLayer(merge, "Destination Points", "ogr")
rLyr = QgsRasterLayer(cost, "Accumulated Cost")
line = path + "path.shp"
points = path + "profilePts.shp"
results = processing.runalg("saga:leastcostpaths",vLyr,rLyr,dem,points,line)

lcp = QgsVectorLayer(line, "Least Cost Path", "ogr")
QgsMapLayerRegistry.instance().addMapLayers([vLyr, lcp, demLyr]) 
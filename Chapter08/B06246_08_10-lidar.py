# Converting LiDAR data to a DEM

# https://github.com/GeospatialPython/Learn/raw/master/lidar.zip

import processing

lidar = "/qgis_data/rasters/lidar.las"
output = "/qgis_data/rasters/lidar.tif"

processing.runalg("lidartools:las2dem",False,False,lidar,0,1,0,0,False,"",output)

lyr = QgsRasterLayer(output, "DEM")

QgsMapLayerRegistry.instance().addMapLayer(lyr)
# Reprojecting a Raster

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

import processing
rasterLyr = QgsRasterLayer("/qgis_data/rasters/SatImage.tif", "Reproject")
rasterLyr.isValid()
# True
processing.runalg("gdalogr:warpreproject","C:/qgis_data/rasters/SatImage.tif","EPSG:4326","EPSG:3722","0",0,1,None,None,0,4,75,6,1,False,0,False,"","/qgis_data/rasters/warped.tif")


# Resampling Raster Resolution  

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

import processing
rasterLyr = QgsRasterLayer("/qgis_data/rasters/SatImage.tif", "Resample")
rasterLyr.isValid()
# True
epsg = rasterLyr.crs().postgisSrid()
srs = "EPSG:%s" % epsg
res = rasterLyr.rasterUnitsPerPixelX() * 2
processing.runalg("gdalogr:warpreproject",rasterLyr,srs,srs,res,0,0,None,"EPSG:4326",5,4,75,6,1,False,0,False,"","/qgis_data/rasters/resampled.tif")


# Counting Raster Bands

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif", "Sat Image")
rasterLyr.isValid()
# True
rasterLyr.bandCount()
# 3

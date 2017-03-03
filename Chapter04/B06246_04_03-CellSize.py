# Get the Cell Size of a Raster Layer

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif", "Sat Image")
rasterLyr.isValid()
# True
rasterLyr.rasterUnitsPerPixelX()
# 0.00029932313140079714
rasterLyr.rasterUnitsPerPixelY()
# 0.00029932313140079714
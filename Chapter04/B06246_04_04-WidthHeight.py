# Obtaining the Width and Height of a Raster

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif", "Satellite Image")
rasterLyr.isValid()
# True
rasterLyr.width()
# 2592
rasterLyr.height()
# 2693
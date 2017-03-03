# Query the Value of a Raster at a Specified Point

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif", "Sat Image")
rasterLyr.isValid()
c = rasterLyr.extent().center()
qry = rasterLyr.dataProvider().identify(QgsPoint(*c), QgsRaster.IdentifyFormatValue)
qry.isValid()
#True
qry.results() 
# {1: 17.0, 2: 66.0, 3: 56.0}


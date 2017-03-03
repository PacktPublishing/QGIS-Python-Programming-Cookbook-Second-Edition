# Loading a Raster Layer

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif", "satimage")
rasterLyr.isValid()
# True
QgsMapLayerRegistry.instance().addMapLayers([rasterLyr])
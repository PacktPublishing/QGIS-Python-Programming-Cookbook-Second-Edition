# Swapping Raster Bands

https://github.com/GeospatialPython/Learn/raw/master/FalseColor.zip

rasterLyr = QgsRasterLayer("/qgis_data/rasters/FalseColor.tif", "Band Swap")
rasterLyr.isValid()
# True
ren = rasterLyr.renderer()
ren.setRedBand(2)
ren.setGreenBand(1)
QgsMapLayerRegistry.instance().addMapLayers([rasterLyr])
# Blue and green image


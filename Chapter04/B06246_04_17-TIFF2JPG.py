# Converting a TIFF Image to a JPEG Image

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

from osgeo import gdal
drv = gdal.GetDriverByName("JP2OpenJPEG")
src = gdal.Open("/qgis_data/rasters/satimage.tif")
tgt = drv.CreateCopy("/qgis_data/rasters/satimage.jp2", src)
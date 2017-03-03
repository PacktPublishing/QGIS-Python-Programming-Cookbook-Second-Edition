# Converting a Geospatial Coordinate to a Pixel Location

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

from osgeo import gdal

def world2Pixel(geoMatrix, x, y):
  ulX = geoMatrix[0]
  ulY = geoMatrix[3]
  xDist = geoMatrix[1]
  yDist = geoMatrix[5]
  rtnX = geoMatrix[2]
  rtnY = geoMatrix[4]
  pixel = int((x - ulX) / xDist)
  line = int((y - ulY) / yDist)
  return (pixel, line) 

src = gdal.Open("/qgis_data/rasters/satimage.tif")
geoTrans = src.GetGeoTransform()
world2Pixel(geoTrans, -89.59486002580364, 30.510227817850406)
# (1296, 1346)


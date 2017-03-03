# Converting a Pixel Location to a Geospatial Coordinate

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip 

from osgeo import gdal

def Pixel2world(geoMatrix, x, y):
    ulX = geoMatrix[0]
    ulY = geoMatrix[3]
    xDist = geoMatrix[1]
    yDist = geoMatrix[5]
    coorX = (ulX + (x * xDist))
    coorY = (ulY + (y * yDist))
    return (coorX, coorY)

src = gdal.Open("/qgis_data/rasters/satimage.tif")
geoTrans = src.GetGeoTransform()
centerX = src.RasterXSize/2
centerY = src.RasterYSize/2
Pixel2world(geoTrans, centerX, centerY) 
#(-89.59486002580364, 30.510227817850406) 


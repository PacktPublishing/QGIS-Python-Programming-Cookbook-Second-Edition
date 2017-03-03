# Creating a KML Image Overlay for a Raster

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

from osgeo import gdal
import zipfile

srcf = "/qgis_data/rasters/satimage.tif"
vfn = "/vsimem/satimage.jpg"
drv = gdal.GetDriverByName('JPEG')
src = gdal.Open(srcf)
tgt = drv.CreateCopy(vfn, src)
rasterLyr = QgsRasterLayer(srcf, "SatImage")
e = rasterLyr.extent()
kml = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>QGIS KML Example</name>
    <GroundOverlay>
        <name>SatImage</name>
        <drawOrder>30</drawOrder>
        <Icon>
          <href>SatImage.jpg</href>
        </Icon>
        <LatLonBox>
          <north>%s</north>
          <south>%s</south>
          <east>%s</east>
          <west>%s</west>
        </LatLonBox>
    </GroundOverlay>
  </Document>
</kml>""" %(e.yMaximum(), e.yMinimum(), e.xMaximum(), e.xMinimum())
vsifile = gdal.VSIFOpenL(vfn,'r')
gdal.VSIFSeekL(vsifile, 0, 2)
vsileng = gdal.VSIFTellL(vsifile)
gdal.VSIFSeekL(vsifile, 0, 0)           
z = zipfile.ZipFile("/qgis_data/rasters/satimage.kmz", "w", zipfile.ZIP_DEFLATED)
z.writestr("doc.kml", kml)
z.writestr("SatImage.jpg", gdal.VSIFReadL(1, vsileng, vsifile))
z.close()

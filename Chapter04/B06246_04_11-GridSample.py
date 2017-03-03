# Sampling Raster Dataset Using a Regular Grid

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

import numpy
from PyQt4.QtCore import *


spacing = .1
inset = .04
rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif", "Sat Image")
rasterLyr.isValid()
# True
rpr = rasterLyr.dataProvider()
epsg = rasterLyr.crs().postgisSrid()
ext = rasterLyr.extent()
vectorLyr = QgsVectorLayer('Point?crs=epsg:%s' % epsg, 'Grid' , "memory")
vpr = vectorLyr.dataProvider()
qd = QVariant.Double
vpr.addAttributes([QgsField("Red", qd), QgsField("Green", qd), QgsField("Blue", qd)])
vectorLyr.updateFields()
xmin = ext.xMinimum() + inset
xmax = ext.xMaximum()
ymin = ext.yMinimum() + inset
ymax = ext.yMaximum() - inset

pts = [(x,y) for x in (i for i in numpy.arange(xmin, xmax, spacing)) for y in (j for j in numpy.arange(ymin, ymax, spacing))]
feats = []
for x,y in pts:
  f = QgsFeature()
  p = QgsPoint(x,y)
  qry = rasterLyr.dataProvider().identify(p, QgsRaster.IdentifyFormatValue)
  r = qry.results()
  f.setAttribute(0, r[1])
  f.setAttribute(1, r[2])
  f.setAttribute(2, r[3])
  f.setGeometry(QgsGeometry.fromPoint(p))
  feats.append(f)
vpr.addFeatures(feats)
vectorLyr.updateExtents()
QgsMapLayerRegistry.instance().addMapLayers([vectorLyr, rasterLyr])
canvas = qgis.utils.iface.mapCanvas()
canvas.setExtent(rasterLyr.extent())
canvas.refresh()

  




##Vector=group
##Input_Raster_Directory=folder
##Output_Footprints_Vector=output vector

# QGIS Processing toolboox script to read
# a directory of rasters and output a 
# shapefile of their footprints as polygons.

# Sample data: https://github.com/GeospatialPython/Learn/raw/master/scenes.zip

import os
from qgis.core import *

files = os.listdir(Input_Raster_Directory)

footprints = []

crs = ""

for f in files:
    try:
        fn = os.path.join(Input_Raster_Directory, f)
        lyr = QgsRasterLayer(fn, "Input Raster")
        crs = lyr.crs()
        e = lyr.extent()
        ulx = e.xMinimum()
        uly = e.yMaximum()
        lrx = e.xMaximum()
        lry = e.yMinimum()
        ul = (ulx, uly)
        ur = (lrx, uly)
        lr = (lrx, lry)
        ll = (ulx, lry)
        fp = {}
        points = []
        points.append(QgsPoint(*ul))
        points.append(QgsPoint(*ur))
        points.append(QgsPoint(*lr)) 
        points.append(QgsPoint(*ll))   
        points.append(QgsPoint(*ul))
        fp["points"] = points
        fp["raster"] = fn
        footprints.append(fp)
    except:
        progress.setInfo("Warning: The file %s does not appear to be a valid raster file." % f)

vectorLyr =  QgsVectorLayer("Polygon?crs=%s&field=raster:string(100)" % crs, "Footprints" , "memory")

vpr = vectorLyr.dataProvider()

features = []

for fp in footprints:
    poly = QgsGeometry.fromPolygon([fp["points"]])
    print fp["points"]
    f = QgsFeature()
    f.setGeometry(poly)
    f.setAttributes([fp["raster"]])
    features.append(f)

vpr.addFeatures(features)
vectorLyr.updateExtents()

driver = "Esri Shapefile"

ct = QgsCoordinateTransform(crs, crs)

error = QgsVectorFileWriter.writeAsVectorFormat(vectorLyr, Output_Footprints_Vector, "utf-8", ct, driver)
if not QgsVectorFileWriter.NoError:
    progress.setInfo("Unable to output footprints.")

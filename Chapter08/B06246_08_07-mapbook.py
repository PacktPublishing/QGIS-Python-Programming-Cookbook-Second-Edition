# Creating a Mapbook

# https://github.com/GeospatialPython/Learn/raw/master/countries.zip

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import PyPDF2
import os

filenames = []
mapbook = "/qgis_data/atlas/mapbook.pdf"
coverage = "/qgis_data/shapes/countries.shp"
atlasPattern = "/qgis_data/atlas/output_"

vlyr = QgsVectorLayer(coverage, "Countries", "ogr")
QgsMapLayerRegistry.instance().addMapLayer(vlyr)

mr = QgsMapRenderer()
mr.setLayerSet([vlyr.id()])
mr.setProjectionsEnabled(True)
mr.setMapUnits(QGis.DecimalDegrees)
crs = QgsCoordinateReferenceSystem()
crs.createFromSrid(4326)
mr.setDestinationCrs(crs)

c = QgsComposition(mr)
c.setPaperSize(297, 210)

gray = { "color": "155,155,155" }
mapSym = QgsFillSymbolV2.createSimple(gray)
renderer = QgsSingleSymbolRendererV2(mapSym)
vlyr.setRendererV2(renderer)

atlasMap = QgsComposerMap(c, 20, 20, 130, 130)
atlasMap.setFrameEnabled(True)
c.addComposerMap(atlasMap)

atlas = c.atlasComposition()
atlas.setCoverageLayer(vlyr)
atlas.setHideCoverage(False)
atlas.setEnabled(True)
c.setAtlasMode(QgsComposition.ExportAtlas)

ov = QgsComposerMap(c, 180, 20, 50, 50)
ov.setFrameEnabled(True)
ov.setOverviewFrameMap(atlasMap.id())
c.addComposerMap(ov)
rect = QgsRectangle(vlyr.extent())
ov.setNewExtent(rect)

yellow = { "color": "255,255,0,255" }
ovSym = QgsFillSymbolV2.createSimple(yellow)
ov.setOverviewFrameMapSymbol(ovSym)

lbl = QgsComposerLabel(c)
c.addComposerLabel(lbl)
lbl.setText("[% \"CNTRY_NAME\" %]")
lbl.setFont(QgsFontUtils.getStandardTestFont())
lbl.adjustSizeToText()
lbl.setSceneRect(QRectF(150, 5, 60, 15))

atlasMap.setAtlasDriven(True)
atlasMap.setAtlasScalingMode(QgsComposerMap.Auto)
atlasMap.setAtlasMargin(0.10)

atlas.setFilenamePattern("'%s' || $feature" % atlasPattern)
atlas.beginRender()
for i in range(0, atlas.numFeatures()):
    atlas.prepareForFeature(i)
    filename = atlas.currentFilename() + ".pdf"
    print "Writing file %s" % filename
    filenames.append(filename)
    c.exportAsPDF(filename)  
atlas.endRender()

output = PyPDF2.PdfFileWriter()

for f in filenames:
    pdf = open(f, "rb")
    page = PyPDF2.PdfFileReader(pdf)
    output.addPage(page.getPage(0))
    os.remove(f)

print "Writing final mapbook..."
with open(mapbook, "wb") as book:
    output.write(book)

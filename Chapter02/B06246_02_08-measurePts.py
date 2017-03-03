# Measuring Distance Between Two Points

# https://geospatialpython.googlecode.com/svn/NYC_MUSEUMS_GEO.zip
from qgis.core import QGis

lyr = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
fts = lyr.getFeatures()
first = fts.next()
last = fts.next()
for f in fts:
  last = f
d = QgsDistanceArea()
m = d.measureLine(first.geometry().asPoint(), last.geometry().asPoint())
deg = QGis.DecimalDegrees
met = QGis.Meters
d.convertMeasurement(m, deg, met, False)
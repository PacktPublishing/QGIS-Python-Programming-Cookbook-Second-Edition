# Adding a Field to a Vector Layer

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

from PyQt4.QtCore import QVariant 

vectorLyr =  QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vectorLyr.isValid()
vpr = vectorLyr.dataProvider()
vpr.addAttributes([QgsField("Admission", QVariant.Double)])
vectorLyr.updateFields()
# Using NULL Values in PyQGIS

# https://github.com/GeospatialPython/Learn/raw/master/NullExample.zip

lyrPth = "/qgis_data/shapes/NullExample.shp"

lyr = QgsVectorLayer(lyrPth, "Null Field Example", "ogr")

features = lyr.getFeatures()

f = features.next()

value = f["SAMPLE"]

print "Check python value type:"
print type(value)
# <class 'PyQt4.QtCore.QPyNullVariant'>

print "Check python string representation:"
print value
# NULL

print "Check if value is None:"
print value is None
# False

print "Check if value == None:"
print value == None
# True

print "Check if value == NULL:"
print value == NULL
# True

print "Check if value is NULL:"
print value is NULL
# False

print "Check type(value) is type(NULL):"
print type(value) is type(NULL)
# True


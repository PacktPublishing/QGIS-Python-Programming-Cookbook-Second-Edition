# Calculate Length for all Selected Lines

# https://github.com/GeospatialPython/Learn/raw/master/ms_rails_mstm.zip

pth = "/qgis_data/ms/ms_rails_mstm.shp"
lyr = QgsVectorLayer(pth, "Railroads", "ogr")
total = 0
for f in lyr.getFeatures():
    geom = f.geometry()
    total += geom.length()   
    
print "{0:.2f} total kilometers of rails.".format(total / 1000)

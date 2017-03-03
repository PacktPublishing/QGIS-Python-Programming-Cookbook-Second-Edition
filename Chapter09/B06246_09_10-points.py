# Generating Points along a Line

# https://github.com/GeospatialPython/Learn/raw/master/path.zip

import processing

line = QgsVectorLayer("/qgis_data/shapes/path/path.shp", "Line", "ogr")

QgsMapLayerRegistry.instance().addMapLayer(line)

processing.runandload("grass7:v.to.points",line,"100",1,False,"435727.015026,458285.819185,5566442.32879,5591754.78979",-1,0.0001,0,None)

processing.runandload("qgis:randompointsinextent","435727.015026,458285.819185,5566442.32879,5591754.78979",100,100,None)


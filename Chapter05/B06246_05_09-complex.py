# Creating a Complex Vector Layer Symbol

# https://github.com/GeospatialPython/Learn/raw/master/paths.zip

lyr = QgsVectorLayer("/qgis_data/shapes/paths.shp", "Route", "ogr")

symbolList = lyr.rendererV2().symbols() 
symbol = symbolList[0]

symLyrReg = QgsSymbolLayerV2Registry

lineStyle = {'width':'0.26', 'color':'0,0,0'}

symLyr1Meta = symLyrReg.instance().symbolLayerMetadata("SimpleLine")

symLyr1 = symLyr1Meta.createSymbolLayer(lineStyle)

symbol.appendSymbolLayer(symLyr1)

markerStyle = {}
markerStyle['width'] = '0.26'
markerStyle['color'] = '0,0,0'
markerStyle['interval'] = '3'
markerStyle['interval_unit'] = 'MM'
markerStyle['placement'] = 'interval'
markerStyle['rotate'] = '1'

symLyr2Meta = symLyrReg.instance().symbolLayerMetadata("MarkerLine")

symLyr2 = symLyr2Meta.createSymbolLayer(markerStyle)

sybSym = symLyr2.subSymbol()

sybSym.deleteSymbolLayer(0)

railStyle = {'size':'2', 'color':'0,0,0', 'name':'line', 'angle':'0'}

railMeta = symLyrReg.instance().symbolLayerMetadata("SimpleMarker")

rail = railMeta.createSymbolLayer(railStyle)

sybSym.appendSymbolLayer(rail)

symbol.appendSymbolLayer(symLyr2)

QgsMapLayerRegistry.instance().addMapLayer(lyr)
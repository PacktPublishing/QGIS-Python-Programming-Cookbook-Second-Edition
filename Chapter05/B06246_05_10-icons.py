# Using Icons as Vector Layer Symbols

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

src = "/qgis_data/nyc/NYC_MUSEUMS_GEO.shp"

lyr = QgsVectorLayer(src, "Museums", "ogr")

fontStyle = {}
fontStyle['color'] = '#000000'
fontStyle['font'] = 'Webdings'
fontStyle['chr'] = 'G'
fontStyle['size'] = '6'

symLyr1 = QgsFontMarkerSymbolLayerV2.create(fontStyle)

lyr.rendererV2().symbols()[0].changeSymbolLayer(0, symLyr1)

QgsMapLayerRegistry.instance().addMapLayer(lyr)
# Using SVG for Layer Symbols

# https://github.com/GeospatialPython/Learn/raw/master/NYC_MUSEUMS_GEO.zip

src = "/qgis_data/nyc/NYC_MUSEUMS_GEO.shp"

lyr = QgsVectorLayer(src, "Museums", "ogr")

svgStyle = {}
svgStyle['fill'] = '#0000ff'
svgStyle['name'] = 'landmark/tourism=museum.svg'
svgStyle['outline'] = '#000000'
svgStyle['outline-width'] = '0'
svgStyle['size'] = '6'

symLyr1 = QgsSvgMarkerSymbolLayerV2.create(svgStyle)

lyr.rendererV2().symbols()[0].changeSymbolLayer(0, symLyr1)

QgsMapLayerRegistry.instance().addMapLayer(lyr)
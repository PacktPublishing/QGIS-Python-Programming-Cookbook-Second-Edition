# Using X,Y,Z Tiled Map Services

rasterLyr = QgsRasterLayer("type=xyz&url=http://c.tile.openstreetmap.org/{z}/{x}/{y}.png", "OSM", "wms")

QgsMapLayerRegistry.instance().addMapLayer(rasterLyr)

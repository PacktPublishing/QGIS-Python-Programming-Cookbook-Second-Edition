# Routing along Streets

# Requires the QGIS GeoSearch Plugin
# Also requries the OpenLayers Plugin

import qgis.utils
from GeoSearch import geosearchdialog, GoogleMapsApi

openLyrs = qgis.utils.plugins['openlayers_plugin']

g = geosearchdialog.GeoSearchDialog(iface)
g.SearchRoute([]) 
d = GoogleMapsApi.directions.Directions()

origin = "Boston, MA"
dest = "2517 Main Rd, Dedham, ME 04429"

route = d.GetDirections(origin, dest, mode = "driving", waypoints=None, avoid=None, units="imperial")

layerType = openLyrs._olLayerTypeRegistry.getById(4)
openLyrs.addLayer(layerType)

g.CreateVectorLayerGeoSearch_Route(route)
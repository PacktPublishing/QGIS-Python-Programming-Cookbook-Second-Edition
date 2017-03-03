# Creating HTML Map Tips in QGIS

from qgis.utils import qgsfunction
from qgis.core import QGis
import urllib
import os

@qgsfunction(0, "Python")
def googleStreetView(values, feature, parent):
    """
    Returns a path to a local Google Street View 
    image for the feature
    """
    x,y = feature.geometry().asPoint()
    baseurl = "https://maps.googleapis.com/maps/api/streetview?"
    w = 150
    h = 150
    fov = 90
    heading = 235
    pitch = 10
    params = "size={w}x{h}&".format(w,h)
    params += "location={y},{x}&".format(y,x)
    params += "fov={}&heading={}&pitch={}".format(fov, heading, pitch) 
    url = baseurl + params    
    tmpdir = "/qgis_data/tmp/"
    img = tmpdir + str(feature.id()) + ".jpg"
    if not os.path.isfile(img):
        urllib.urlretrieve(url, img)
    uri = "file://" + img
    return uri
    
pth = "/qgis_data/nyc/nyc_museums_geo.shp"
lyr = QgsVectorLayer(pth, "New York City Museums", "ogr")
lyr.setDisplayField('<img src="[%googleStreetView()%]"/>')

QgsMapLayerRegistry.instance().addMapLayer(lyr)
   
# QgsExpression.unregisterFunction("googleStreetView")
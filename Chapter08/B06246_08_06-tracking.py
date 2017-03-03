# Tracking a GPS

import urllib
import urllib2
import time

# Free NMEA Sample Generator
url = 'http://freenmea.net/api/emitnmea'
values = {'types' : 'default'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
results = []
for i in range(10):
    response = urllib2.urlopen(req)
    results.extend(response.read().split("\n"))

# World Boundaries data
wb = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
basemap = QgsVectorLayer(wb, "Countries", "ogr")
qmr = QgsMapLayerRegistry.instance()
qmr.addMapLayer(basemap)
vectorLyr = QgsVectorLayer('Point?crs=epsg:4326', 'GPS Point' , "memory")
vpr = vectorLyr.dataProvider()
cLat = None
cLon = None
canvas = iface.mapCanvas()
c = QgsNMEAConnection(None)
firstPt = True

for r in results:
    l = len(r)
    if "GGA" in r:
        c.processGGASentence(r,l)
    elif "RMC" in r:
        c.processRMCSentence(r,l)
    elif "GSV" in r:
        c.processGSVSentence(r,l)
    elif "VTG" in r:
        c.processVTGSentence(r,l)
    elif "GSA" in r:
        c.processGSASentence(r,l)
    i=c.currentGPSInformation()
    if i.latitude and i.longitude:
        lat = float(i.latitude)
        lon = float(i.longitude)
        if cLat is None:
            cLat = float(i.latitude)
            cLon = float(i.longitude)
        elif round(lat, 2)==round(cLat, 2) and round(lon, 2)==round(cLon, 2):
            continue    
        else:
            cLat = lat
            cLon = lon
        pnt = QgsGeometry.fromPoint(QgsPoint(lon,lat))
        if firstPt:
            firstPt = False
            f = QgsFeature()
            f.setGeometry(pnt)
            vpr.addFeatures([f])
            qmr.addMapLayer(vectorLyr)
        else:
            print lon, lat
            vectorLyr.startEditing()
            vectorLyr.changeGeometry(1,pnt)
            vectorLyr.commitChanges()
        vectorLyr.setCacheImage(None)
        vectorLyr.updateExtents()
        vectorLyr.triggerRepaint()
        canvas.refresh()
        time.sleep(2)


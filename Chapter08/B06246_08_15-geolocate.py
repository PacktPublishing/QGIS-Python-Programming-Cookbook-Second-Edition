# Geolocating Photos on the Map

# https://github.com/GeospatialPython/Learn/raw/master/photos.zip

import glob
import Image
from ExifTags import TAGS

def exif(img):
    exif_data = {}
    try:    
        i = Image.open(img)
        tags = i._getexif()
        for tag, value in tags.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
    except:
        pass
    return exif_data

def dms2dd(d, m, s, i):
    sec = float((m * 60) + s)
    dec = float(sec / 3600)
    deg = float(d + dec)
    if i.upper() == 'W':
        deg = deg * -1
    elif i.upper() == 'S':
        deg = deg * -1
    return float(deg)

def gps(exif):
    lat = None
    lon = None
    if exif['GPSInfo']:
        # Lat
        coords = exif['GPSInfo']
        i = coords[1]
        d = coords[2][0][0]
        m = coords[2][1][0]
        s = coords[2][2][0]
        lat = dms2dd(d, m ,s, i)
        # Lon
        i = coords[3]
        d = coords[4][0][0]
        m = coords[4][1][0]
        s = coords[4][2][0]
        lon = dms2dd(d, m ,s, i)
    return lat, lon

photos = {}
photo_dir = "/qgis_data/photos/"
files = glob.glob(photo_dir + "*.jpg")

for f in files:
    e = exif(f)
    lat, lon = gps(e)
    photos[f] = [lon, lat]

lyr_info = "Point?crs=epsg:4326&field=photo:string(75)"

vectorLyr =  QgsVectorLayer(lyr_info, "Geotagged Photos" , "memory")

vpr = vectorLyr.dataProvider()

features = []

for pth, p in photos.items():
    lon, lat = p
    pnt = QgsGeometry.fromPoint(QgsPoint(lon,lat))
    f = QgsFeature()
    f.setGeometry(pnt)
    f.setAttributes([pth])
    features.append(f)

vpr.addFeatures(features)
vectorLyr.updateExtents()

QgsMapLayerRegistry.instance().addMapLayer(vectorLyr)
iface.setActiveLayer(vectorLyr)
activeLyr = iface.activeLayer()
actions = activeLyr.actions() 
actions.addAction(QgsAction.OpenUrl, "Photos", '[% "photo" %]') 
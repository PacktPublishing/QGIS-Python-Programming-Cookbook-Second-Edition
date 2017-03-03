# Adjusting imprecise building footprints

# Algorithm by Jose Guerrero: 
# http://gis.stackexchange.com/questions/212003/how-to-modify-a-polygon-to-be-more-rectangular/212325#212325

# https://github.com/GeospatialPython/Learn/raw/master/irregular.zip


def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


def intercept(y, slope, x):
    return y - slope * x


def perpindicular(slope):
    return -1 / slope

pth = "/qgis_data/shapes/irregular.shp"

lyr = QgsVectorLayer(pth, "Footprints", "ogr")

epsg = lyr.crs().postgisSrid()

uri = "Polygon?crs=epsg:{}&field=id:integer&index=yes".format(epsg)

rectangle = QgsVectorLayer(uri, 'Rectangles', 'memory')

p = rectangle.dataProvider()

for f in lyr.getFeatures():
    g = f.geometry()
    xmin, ymin, xmax, ymax = g.boundingBox().toRectF().getCoords()
    pts = f.geometry().asPolygon()[0]
    # Find the top right point regardless of which direction
    # we are moving along the poly
    for i in range(len(pts)-1):
        if pts[i][1] == ymax and pts[i+1][1] < pts[i][1]:
            idx = i
        if pts[i][1] == ymax and pts[i-1][1] < pts[i][1]:
            idx = i-1
    #rectangle poly 
    r = []
    #first point coords
    x1 = pts[idx][0] 
    y1 = pts[idx][1]
    r.append(QgsPoint(x1,y1))
    #second point coords
    x2 = pts[idx+1][0] 
    y2 = pts[idx+1][1]
    r.append(QgsPoint(x2,y2))
    #first line slope
    s1 = slope(x1, y1, x2, y2)
    #first line origin intercept
    i1 = intercept(y1, s1, x1)
    #third point coords
    x3 = pts[idx+2][0] 
    y3 = pts[idx+2][1]
    #second line origin intercept
    i2 = intercept(y3, s1, x3)
    #first perpendicular slope
    s3 = perpindicular(s1)
    #second line origin intercept
    i3 = intercept(y2, s3, x2)
    #point intersect
    x4 = (i3 - i2)/(s1 - s3)
    y4 = s3 * x4 + i3
    r.append(QgsPoint(x4, y4))
    #second perpendicular slope
    s4 = perpindicular(s1)
    #second perpendicular origin intercept
    i4 = intercept(y1, s4, x1)
    #point intersect
    x5 = (i4 - i2)/(s1 - s4)
    y5 = s4 * x5 + i4
    r.extend([QgsPoint(x5, y5),QgsPoint(x1, y1)])
    poly = []
    poly.append(r)
    g = QgsGeometry.fromPolygon(poly)
    ft = QgsFeature()
    ft.setAttributes([i])
    ft.setGeometry(g)
    p.addFeatures([ft])

QgsMapLayerRegistry.instance().addMapLayers([rectangle, lyr])
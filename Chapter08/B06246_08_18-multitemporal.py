# Visualizing Multi-temporal data

# Example animation from this recipe: 
# http://geospatialpython.github.io/qgis/earthquake_loop.gif

from PyQt4.QtGui import *
from timemanager import *

iface.mapCanvas().setCanvasColor(QColor(196,229,248))
iface.mapCanvas().refresh()

countries = "https://raw.githubusercontent.com/"
countries += "johan/world.geo.json/master/countries.geo.json"

quakes = "https://raw.githubusercontent.com/GeospatialPython/Learn/"
quakes += "master/2011_Earthquakes.geojson"

basemap = QgsVectorLayer(countries, "World", "ogr")

gray = {"color": "220,221,222"}
mapSym = QgsFillSymbolV2.createSimple(gray)
renderer = QgsSingleSymbolRendererV2(mapSym)
basemap.setRendererV2(renderer)

quakeLyr = QgsVectorLayer(quakes, "2011 Earthquakes", "ogr")

quakeLyr.setLayerTransparency(30)

magnitude = (
("Light", 4.5, 4.7, "253,255,22", "2"), 
("Moderate", 4.7, 5.0, "253,190,22", "5"),
("Strong", 5.0, 5.4, "253,122,22", "7.5"),
("Major", 5.4, 6.2, "253,99,22", "9.75"),
("Great", 6.2, 7.2, "253,0,22", "12"))

ranges = []
for label, lower, upper, color, size in magnitude:
    props = {}
    props["color"] = color
    props["size"] = size
    props["outline_width"] = "0"
    props["outline_color"] ="0,0,0,0"
    sym = QgsMarkerSymbolV2.createSimple(props)
    rng = QgsRendererRangeV2(lower, upper, sym, label)
    ranges.append(rng)

field = "Magnitude"
renderer = QgsGraduatedSymbolRendererV2(field, ranges)
quakeLyr.setRendererV2(renderer)

QgsMapLayerRegistry.instance().addMapLayers([quakeLyr, basemap])


settings = layer_settings.LayerSettings()
settings.layer = quakeLyr
settings.startTimeAttribute = "Date"
settings.endTimeAttribute = "Date"
timeLayer = timevectorlayer.TimeVectorLayer(settings, iface=iface)

try:
    ctrl = qgis.utils.plugins['timemanager'].getController()
except:
    # MacOS needs the capitalized name
    ctrl = qgis.utils.plugins['TimeManager'].getController()

tlm = ctrl.getTimeLayerManager()
tlm.registerTimeLayer(timeLayer)
tlm.setTimeFrameType('months')
ctrl.setLoopAnimation(True)
start = time_util.str_to_datetime(timeLayer.getMinMaxValues()[0])
end = time_util.str_to_datetime(timeLayer.getMinMaxValues()[1])
tlm.setCurrentTimePosition(start)
ctrl.setAnimationFrameLength(1000)
ctrl.toggleAnimation()

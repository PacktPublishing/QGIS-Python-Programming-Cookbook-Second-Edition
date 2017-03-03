# Performing Network Analysis

# https://github.com/GeospatialPython/Learn/raw/master/network.zip

from qgis.core import *
from qgis.gui import *
from qgis.networkanalysis import *
from PyQt4.QtCore import *

network = QgsVectorLayer("/qgis_data/shapes/Network.shp", "Network Layer", "ogr")
waypoints = QgsVectorLayer("/qgis_data/shapes/NetworkPoints.shp", "Waypoints", "ogr")
director = QgsLineVectorLayerDirector(network, -1, '', '', '', 3)
properter = QgsDistanceArcProperter()
director.addProperter(properter)
crs = network.crs()
builder = QgsGraphBuilder(crs)

ptStart = QgsPoint(-0.8095638694, -0.1578175511)
ptStop = QgsPoint(0.8907435677, 0.4430834924)

tiePoints = director.makeGraph(builder, [ptStart, ptStop])
graph = builder.graph()

tStart = tiePoints[0]
tStop = tiePoints[1]

idStart = graph.findVertex(tStart)
idStop = graph.findVertex(tStop)

(tree, cost) = QgsGraphAnalyzer.dijkstra(graph, idStart, 0)

p = []
curPos = idStop
while curPos != idStart:
	p.append(graph.vertex(graph.arc(tree[curPos]).inVertex()).point())
	curPos = graph.arc(tree[curPos]).outVertex()

p.append(tStart)
QgsMapLayerRegistry.instance().addMapLayers([network,waypoints])
rb = QgsRubberBand(iface.mapCanvas())
rb.setColor(Qt.red)

for pnt in p:
	rb.addPoint(pnt)

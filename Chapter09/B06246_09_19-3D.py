# Visualizing Data in 3D with WebGL

from PyQt4.QtCore import QSize
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsPoint
from Qgis2threejs.api import Exporter

iface.mapCanvas().setCrsTransformEnabled(False)
iface.mapCanvas().setMapUnits(0)

demPth = "/qgis_data/rasters/dem.asc"

hillshadePth = "/qgis_data/rasters/hillshade.tif"

dem = QgsRasterLayer(demPth, "DEM")
hillshade = QgsRasterLayer(hillshadePth, "Hillshade")

algorithm = QgsContrastEnhancement.StretchToMinimumMaximum
limits = QgsRaster.ContrastEnhancementMinMax

dem.setContrastEnhancement(algorithm, limits)

s = QgsRasterShader() 
c = QgsColorRampShader() 
c.setColorRampType(QgsColorRampShader.INTERPOLATED) 
i = [] 
qri = QgsColorRampShader.ColorRampItem
i.append(qri(356.334, QColor(63,159,152,255), '356.334')) 
i.append(qri(649.292, QColor(96,235,155,255), '649.292')) 
i.append(qri(942.25, QColor(100,246,174,255), '942.25')) 
i.append(qri(1235.21, QColor(248,251,155,255), '1235.21'))
i.append(qri(1528.17, QColor(246,190,39,255), '1528.17')) 
i.append(qri(1821.13, QColor(242,155,39,255), '1821.13'))
i.append(qri(2114.08, QColor(165,84,26,255), '2114.08'))
i.append(qri(2300, QColor(236,119,83,255), '2300'))
i.append(qri(2700, QColor(203,203,203,255), '2700'))
c.setColorRampItemList(i) 
s.setRasterShaderFunction(c) 
ps = QgsSingleBandPseudoColorRenderer(dem.dataProvider(), 1,  s)
ps.setOpacity(0.5) 
dem.setRenderer(ps) 

QgsMapLayerRegistry.instance().addMapLayers([dem, hillshade])

outputPath = "/qgis_data/3D/3d.html"

props = {
  "DEM": {
    "checkBox_Clip": False, 
    "checkBox_Frame": False, 
    "checkBox_Shading": True, 
    "checkBox_Sides": True, 
    "checkBox_Surroundings": False, 
    "checkBox_TransparentBackground": False, 
    "comboBox_ClipLayer": None, 
    "comboBox_DEMLayer": dem.id(), 
    "comboBox_TextureSize": 100, 
    "horizontalSlider_DEMSize": 2, 
    "lineEdit_Color": "", 
    "lineEdit_ImageFile": "", 
    "lineEdit_centerX": "", 
    "lineEdit_centerY": "", 
    "lineEdit_rectHeight": "", 
    "lineEdit_rectWidth": "", 
    "radioButton_MapCanvas": True, 
    "radioButton_Simple": True, 
    "spinBox_Height": 4, 
    "spinBox_Roughening": 4, 
    "spinBox_Size": 5, 
    "spinBox_demtransp": 0, 
    "visible": True
  }, 
  "OutputFilename": outputPath, 
  "PluginVersion": "1.4.2", 
  "Template": "3DViewer(dat-gui).html"
}

e = Exporter(iface)
e.settings.loadSettings(props)
canvas = iface.mapCanvas()
e.setMapSettings(canvas.mapSettings())
e.export(outputPath, openBrowser=True)



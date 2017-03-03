from qgis.utils import iface
import datetime
c = iface.mapCanvas()
t = '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())
img_path = "<output directory>/map{}.png"
c.saveAsImage(img_path.format(t), None, "PNG")

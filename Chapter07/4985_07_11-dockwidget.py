# Creating a dockable widget

from PyQt4.QtCore import *
from PyQt4.QtGui import *

te = QTextEdit("<b>Project notes:</b>")
dw = QDockWidget("QGIS Sticky Notes")
dw.setWidget(te)
iface.addDockWidget(Qt.RightDockWidgetArea, dw)
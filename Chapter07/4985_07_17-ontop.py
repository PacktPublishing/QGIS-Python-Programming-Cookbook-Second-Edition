# Keeping Dialogs on Top

from PyQt4.QtGui import *
from PyQt4.QtCore import *

msg = "   This window will always stay on top."
lbl = QLabel(msg, None, Qt.WindowStaysOnTopHint)
lbl.resize(400,400)
lbl.show()
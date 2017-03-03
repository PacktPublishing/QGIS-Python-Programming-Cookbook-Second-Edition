# Creating a Combo Box

from PyQt4.QtGui import *

cb = QComboBox()
cb.addItems(["North", "South", "West", "East"])
cb.resize(200,35)
cb.show()
# Choose an option then execute:
print cb.currentText()

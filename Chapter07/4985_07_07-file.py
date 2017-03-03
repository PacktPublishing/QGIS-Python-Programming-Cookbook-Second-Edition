# Creating File Input Dialog

from PyQt4.QtGui import *

qfd = QFileDialog()
title = 'Open File'
path = "/Users/joellawhead/qgis_data"

f = QFileDialog.getOpenFileName(qfd, title, path)
print f

# Creating an Error Dialog

from PyQt4.QtGui import *

msg = QMessageBox()
msg.setText("This is an error!")
msg.setIcon(3)
msg.exec_()
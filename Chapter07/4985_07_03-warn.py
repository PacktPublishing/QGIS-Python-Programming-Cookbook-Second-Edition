# Creating a Warning Dialog

from PyQt4.QtGui import *

msg = QMessageBox()
msg.setText("This is a warning...")
msg.setIcon(2)
msg.exec_()



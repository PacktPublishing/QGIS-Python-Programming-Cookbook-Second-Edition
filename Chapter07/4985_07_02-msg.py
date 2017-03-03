# Creating a Simple Message Dialog

from PyQt4.QtGui import *

msg = QMessageBox()
msg.setText("This is a simple information message.")
msg.exec_()
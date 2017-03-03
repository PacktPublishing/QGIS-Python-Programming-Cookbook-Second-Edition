# Creating a Simple Text Input Dialog

from PyQt4.QtGui import *

qid = QInputDialog()
title = "Enter Your Name"
label = "Name: "
mode = QLineEdit.Normal
default = "<your name here>"

text, ok = QInputDialog.getText(qid, title, label, mode, default)
print text
